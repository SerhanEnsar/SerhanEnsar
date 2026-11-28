#!/usr/bin/env python3
"""Renders the last 31 days of GitHub contributions as an animated SVG.

Replaces the (now disabled) github-readme-activity-graph service.
Runs in the snake workflow:  GITHUB_TOKEN=... python3 scripts/activity_graph.py USER OUT.svg
"""
import json
import os
import sys
import urllib.request
from datetime import date, timedelta

BG1, LINE, CYAN, ORANGE, TEXT, DIM = "#0B1226", "#22304F", "#5EEAD4", "#FF7A45", "#E6EDF3", "#8B96AD"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Menlo,Consolas,'Liberation Mono',monospace"
DAYS = 31

QUERY = """query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){
contributionsCollection(from:$from,to:$to){contributionCalendar{weeks{contributionDays{date contributionCount}}}}}}"""


def fetch(user: str) -> list[tuple[str, int]]:
    to = date.today()
    frm = to - timedelta(days=DAYS - 1)
    body = json.dumps({"query": QUERY, "variables": {
        "login": user, "from": f"{frm}T00:00:00Z", "to": f"{to}T23:59:59Z"}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"})
    data = json.load(urllib.request.urlopen(req, timeout=30))
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [(d["date"], d["contributionCount"]) for w in weeks for d in w["contributionDays"]]
    return days[-DAYS:]


def render(days: list[tuple[str, int]]) -> str:
    W, H = 1000, 320
    L, R, T, B = 60, 30, 70, 50
    pw, ph = W - L - R, H - T - B
    peak = max(c for _, c in days) or 1
    step = max(1, -(-peak // 4))           # ceil(peak/4): 4 gridlines
    top = step * 4
    n = len(days)
    pts = [(L + i * pw / (n - 1), T + ph - c / top * ph) for i, (_, c) in enumerate(days)]

    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"M{L},{T + ph} L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f" L{L + pw},{T + ph} Z"
    total = sum(c for _, c in days)

    grid = []
    for k in range(5):
        y = T + ph - k * ph / 4
        grid.append(f'<line x1="{L}" y1="{y:.1f}" x2="{L + pw}" y2="{y:.1f}" stroke="{LINE}" stroke-dasharray="3 5"/>')
        grid.append(f'<text x="{L - 12}" y="{y + 4:.1f}" text-anchor="end" class="mono ax">{k * step}</text>')
    for i, (d, _) in enumerate(days):
        if i % 5 == 0 or i == n - 1:
            grid.append(f'<text x="{pts[i][0]:.1f}" y="{T + ph + 24}" text-anchor="middle" class="mono ax">{d[8:10]}.{d[5:7]}</text>')

    dots = "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{ORANGE}" class="dot" style="animation-delay:{1.2 + i * 0.03:.2f}s"/>'
        for i, (x, y) in enumerate(pts))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<style>
  .sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
  .ax{{font-size:11px;fill:{DIM}}}
  .ln{{stroke-dasharray:4000;stroke-dashoffset:4000;animation:draw 2s ease-out forwards}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  .ar{{opacity:0;animation:fade 1.2s ease-out .8s forwards}}
  .dot{{opacity:0;animation:fade .4s ease-out forwards}}
  @keyframes fade{{to{{opacity:1}}}}
  @media (prefers-reduced-motion:reduce){{.ln,.ar,.dot{{animation:none;opacity:1;stroke-dashoffset:0}}}}
</style>
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="{CYAN}" stop-opacity=".35"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
</linearGradient></defs>
<rect width="{W}" height="{H}" rx="18" fill="{BG1}"/>
<text x="{L}" y="40" class="sans" font-size="20" font-weight="600" fill="{TEXT}">Contribution trajectory</text>
<text x="{W - R}" y="40" text-anchor="end" class="mono" font-size="12" fill="{DIM}">last {n} days · <tspan fill="{CYAN}">{total}</tspan> contributions</text>
{''.join(grid)}
<path d="{area}" fill="url(#g)" class="ar"/>
<polyline points="{line}" fill="none" stroke="{CYAN}" stroke-width="2.5" stroke-linejoin="round" class="ln"/>
{dots}
</svg>
"""


if __name__ == "__main__":
    user, out = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        f.write(render(fetch(user)))
    print(f"wrote {out}")
