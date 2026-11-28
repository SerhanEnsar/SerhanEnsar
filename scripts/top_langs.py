#!/usr/bin/env python3
"""Renders a "Most used languages" card as an SVG.

Replaces the public github-readme-stats top-langs card.
Runs in the snake workflow:  GITHUB_TOKEN=... python3 scripts/top_langs.py USER OUT.svg
"""
import json
import os
import sys
import urllib.request
from xml.sax.saxutils import escape as esc

BG1, LINE, CYAN, TEXT, DIM = "#0B1226", "#22304F", "#5EEAD4", "#E6EDF3", "#8B96AD"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Menlo,Consolas,'Liberation Mono',monospace"
HIDE = {"html", "jupyter notebook", "shell"}
COUNT = 8

QUERY = """query($login:String!,$cursor:String){user(login:$login){
repositories(ownerAffiliations:OWNER,isFork:false,privacy:PUBLIC,first:100,after:$cursor){
pageInfo{hasNextPage endCursor}
nodes{languages(first:20,orderBy:{field:SIZE,direction:DESC}){edges{size node{name color}}}}}}}"""


def gql(variables: dict) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"})
    data = json.load(urllib.request.urlopen(req, timeout=30))
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]["repositories"]


def fetch(user: str) -> list[tuple[str, str, int]]:
    sizes: dict[str, int] = {}
    colors: dict[str, str] = {}
    cursor = None
    while True:
        page = gql({"login": user, "cursor": cursor})
        for repo in page["nodes"]:
            for e in repo["languages"]["edges"]:
                name = e["node"]["name"]
                if name.lower() in HIDE:
                    continue
                sizes[name] = sizes.get(name, 0) + e["size"]
                colors[name] = e["node"]["color"] or DIM
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    if not sizes:
        sys.exit("no language data")
    top = sorted(sizes.items(), key=lambda kv: -kv[1])[:COUNT]
    return [(n, colors[n], s) for n, s in top]


def render(langs: list[tuple[str, str, int]]) -> str:
    W, H, P = 400, 195, 25
    total = sum(s for *_, s in langs)
    bw = W - 2 * P

    # stacked bar, clipped to a rounded rect
    bar, x = [], P
    for i, (n, c, s) in enumerate(langs):
        w = bw * s / total
        bar.append(f'<rect x="{x:.2f}" y="62" width="{w + 0.5:.2f}" height="8" fill="{c}" class="seg" '
                   f'style="animation-delay:{i * 0.08:.2f}s"/>')
        x += w

    rows = []
    for i, (n, c, s) in enumerate(langs):
        col, row = i % 2, i // 2
        lx, ly = P + col * (bw / 2), 100 + row * 24
        rows.append(
            f'<g class="row" style="animation-delay:{0.4 + i * 0.08:.2f}s">'
            f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{c}"/>'
            f'<text x="{lx + 16}" y="{ly}" class="sans" font-size="12" fill="{TEXT}">{esc(n)}</text>'
            f'<text x="{lx + bw / 2 - 14}" y="{ly}" text-anchor="end" class="mono" font-size="11" fill="{DIM}">'
            f'{100 * s / total:.1f}%</text></g>')

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<style>
  .sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
  .seg{{transform-box:fill-box;transform-origin:left;transform:scaleX(0);animation:grow .6s ease-out forwards}}
  @keyframes grow{{to{{transform:scaleX(1)}}}}
  .row{{opacity:0;animation:fade .5s ease-out forwards}}
  @keyframes fade{{to{{opacity:1}}}}
  @media (prefers-reduced-motion:reduce){{.seg,.row{{animation:none;opacity:1;transform:none}}}}
</style>
<defs><clipPath id="bar"><rect x="{P}" y="62" width="{bw}" height="8" rx="4"/></clipPath></defs>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{BG1}" stroke="{LINE}"/>
<text x="{P}" y="40" class="sans" font-size="18" font-weight="600" fill="{CYAN}">Most Used Languages</text>
<g clip-path="url(#bar)">{''.join(bar)}</g>
{''.join(rows)}
</svg>
"""


if __name__ == "__main__":
    user, out = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        f.write(render(fetch(user)))
    print(f"wrote {out}")
