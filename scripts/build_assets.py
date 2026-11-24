#!/usr/bin/env python3
"""Generates the profile's SVG assets into ../assets.

Edit the DATA section below and re-run:  python3 scripts/build_assets.py
"""
from pathlib import Path
import random
from xml.sax.saxutils import escape as esc

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

# ───────────────────────── DATA ─────────────────────────
NAME = "Serhan Ensar Büdün"
MISSION_TAG = "MISSION LOG // SEB-2026 · JOURNEY TO THE MOON"
ROLES = [
    "computer vision engineer",
    "embedded systems developer",
    "TEKNOFEST team captain ×2",
    "builds it end to end",
]
SUBLINE = "Computer Engineering @ Ege University  ·  IEEE CS Chair  ·  İzmir, TR"
COORDS = "LAT 38.4237° N    LON 27.1428° E"

TELEMETRY = [
    ("4", "TEKNOFEST teams", "2 as captain"),
    ("0.655", "mAP@50", "LAÇİN aerial detection"),
    ("116K", "labelled images", "trained & shipped"),
    ("6", "IEEE sub-teams", "led as CS Chair"),
]

SECTIONS = {
    "about": ("01", "ABOUT", "who's at the console"),
    "now": ("02", "CURRENT STATUS", "what's running right now"),
    "missions": ("03", "MISSIONS", "selected projects"),
    "toolkit": ("04", "TOOLKIT", "what I build with"),
    "signal": ("05", "SIGNAL", "live github telemetry"),
}

# ───────────────────────── THEME ─────────────────────────
BG0, BG1, BG2 = "#05070F", "#0B1226", "#121B36"
CYAN, ORANGE, TEXT, DIM, LINE = "#5EEAD4", "#FF7A45", "#E6EDF3", "#8B96AD", "#22304F"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Menlo,Consolas,'Liberation Mono',monospace"

BASE_STYLE = f"""
  .sans{{font-family:{SANS}}}
  .mono{{font-family:{MONO}}}
  .tw{{animation:tw 3.2s ease-in-out infinite}}
  @keyframes tw{{0%,100%{{opacity:.15}}50%{{opacity:1}}}}
  .blink{{animation:blink 1s steps(1) infinite}}
  @keyframes blink{{50%{{opacity:0}}}}
  .pulse{{animation:pulse 1.6s ease-in-out infinite}}
  @keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""


def corners(w, h, pad=18, size=22, color=CYAN, op=0.7):
    p, s = pad, size
    d = (f"M{p},{p+s} V{p} H{p+s} M{w-p-s},{p} H{w-p} V{p+s} "
         f"M{w-p},{h-p-s} V{h-p} H{w-p-s} M{p+s},{h-p} H{p} V{h-p-s}")
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2" opacity="{op}"/>'


def stars(w, h, n, seed, avoid=None):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        r = rnd.choice([0.6, 0.8, 1, 1, 1.3, 1.7])
        d = rnd.uniform(0, 3.2)
        out.append(f'<circle class="tw" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" '
                   f'style="animation-delay:{d:.2f}s"/>')
    return "\n    ".join(out)


def frame(w, h, body, extra_style="", defs=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{BG0}"/><stop offset=".55" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="#7DD3FC"/>
    </linearGradient>
    <clipPath id="card"><rect width="{w}" height="{h}" rx="22"/></clipPath>
    {defs}
  </defs>
  <style>{BASE_STYLE}{extra_style}</style>
  <g clip-path="url(#card)">
    <rect width="{w}" height="{h}" fill="url(#bg)"/>
    {body}
  </g>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="21" fill="none" stroke="{LINE}" stroke-width="2"/>
</svg>
"""


# ───────────────────────── BANNER ─────────────────────────
def banner():
    w, h = 1200, 400
    mx, my, mr = 965, 190, 112
    n = len(ROLES)
    cycle = 3.5 * n
    on = 100 / n
    role_style = (f".role{{opacity:0;animation:roles {cycle}s infinite}}"
                  f"@keyframes roles{{0%{{opacity:0}}2%{{opacity:1}}{on-3:.1f}%{{opacity:1}}"
                  f"{on-1:.1f}%,100%{{opacity:0}}}}"
                  "@media (prefers-reduced-motion:reduce){.r0{opacity:1}}")
    roles = "\n    ".join(
        f'<text class="role r{i} mono" x="80" y="222" font-size="23" fill="{TEXT}" '
        f'style="animation-delay:{i*3.5}s" data-i="{i}"><tspan fill="{CYAN}">$ </tspan>{esc(r)}'
        f'<tspan class="blink" fill="{CYAN}"> ▍</tspan></text>'
        for i, r in enumerate(ROLES))
    craters = "".join(
        f'<circle cx="{mx+dx}" cy="{my+dy}" r="{r}" fill="#6B7489" opacity="{o}"/>'
        for dx, dy, r, o in [(-38, -30, 20, .35), (30, 22, 26, .3), (-10, 52, 12, .35),
                             (48, -48, 11, .3), (-62, 24, 9, .3), (12, -8, 7, .25), (-30, 80, 6, .3)])
    orbit = f"M{mx-215},{my} a215,62 0 1,0 430,0 a215,62 0 1,0 -430,0"
    traj = f"M470,392 C640,380 760,330 {mx-mr-8},{my+40}"
    defs = f"""
    <radialGradient id="moon" cx=".35" cy=".35" r=".75">
      <stop offset="0" stop-color="#F4F6FB"/><stop offset=".6" stop-color="#C3CAD8"/><stop offset="1" stop-color="#7E879B"/>
    </radialGradient>
    <radialGradient id="glow"><stop offset="0" stop-color="{CYAN}" stop-opacity=".22"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
    <linearGradient id="fadeL" x1="0" x2="1"><stop offset="0" stop-color="{BG0}" stop-opacity=".85"/><stop offset=".6" stop-color="{BG0}" stop-opacity="0"/></linearGradient>
    <path id="orbit" d="{orbit}" transform="rotate(-14 {mx} {my})"/>
    <path id="traj" d="{traj}"/>"""
    body = f"""
    {stars(w, h, 120, 7)}
    <circle cx="{mx}" cy="{my}" r="230" fill="url(#glow)"/>
    <circle cx="{mx}" cy="{my}" r="{mr}" fill="url(#moon)"/>
    {craters}
    <use href="#orbit" fill="none" stroke="{CYAN}" stroke-opacity=".45" stroke-dasharray="4 7"/>
    <g>
      <rect x="-5" y="-4" width="10" height="8" rx="1.5" fill="{TEXT}"/>
      <rect x="-19" y="-2.5" width="12" height="5" fill="{CYAN}"/><rect x="7" y="-2.5" width="12" height="5" fill="{CYAN}"/>
      <animateMotion dur="14s" repeatCount="indefinite" rotate="auto"><mpath href="#orbit"/></animateMotion>
    </g>
    <use href="#traj" fill="none" stroke="{ORANGE}" stroke-opacity=".55" stroke-width="1.5" stroke-dasharray="2 8"/>
    <circle r="4" fill="{ORANGE}">
      <animateMotion dur="6s" repeatCount="indefinite" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".4 0 .2 1"><mpath href="#traj"/></animateMotion>
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" dur="6s" repeatCount="indefinite"/>
    </circle>
    <rect width="760" height="{h}" fill="url(#fadeL)"/>
    {corners(w, h)}
    <text class="mono" x="80" y="98" font-size="14" letter-spacing="2" fill="{CYAN}" opacity=".9">&gt; {esc(MISSION_TAG)}</text>
    <text class="sans" x="78" y="168" font-size="58" font-weight="800" fill="{TEXT}" letter-spacing="-1">{esc(NAME)}</text>
    {roles}
    <rect x="80" y="252" width="64" height="3" rx="1.5" fill="url(#accent)"/>
    <text class="sans" x="80" y="292" font-size="18" fill="{DIM}">{esc(SUBLINE)}</text>
    <text class="mono" x="80" y="356" font-size="13" letter-spacing="1.5" fill="{DIM}" opacity=".8">{esc(COORDS)}    STATUS <tspan class="pulse" fill="#4ADE80">●</tspan> ONLINE</text>"""
    return frame(w, h, body, role_style, defs)


# ───────────────────────── TELEMETRY ─────────────────────────
def telemetry():
    w, h = 1200, 200
    tile_w, gap, x0 = 252, 24, 60
    tiles = []
    for i, (big, label, sub) in enumerate(TELEMETRY):
        x = x0 + i * (tile_w + gap)
        d = 0.15 * i
        tiles.append(f"""
    <g class="tile" style="animation-delay:{d:.2f}s">
      <rect x="{x}" y="56" width="{tile_w}" height="112" rx="14" fill="{BG0}" fill-opacity=".92" stroke="{LINE}"/>
      <text class="sans" x="{x+22}" y="112" font-size="40" font-weight="800" fill="url(#accent)">{esc(big)}</text>
      <text class="sans" x="{x+22}" y="138" font-size="15" font-weight="600" fill="{TEXT}">{esc(label)}</text>
      <text class="mono" x="{x+22}" y="156" font-size="11.5" fill="{DIM}">{esc(sub)}</text>
      <rect x="{x+22}" y="72" width="0" height="2" rx="1" fill="{ORANGE}">
        <animate attributeName="width" from="0" to="{tile_w-44}" dur="1.4s" begin="{0.3+d:.2f}s" fill="freeze"/>
      </rect>
    </g>""")
    style = (".tile{animation:in .8s ease-out backwards}"
             "@keyframes in{from{opacity:0}}")
    body = f"""
    {stars(w, h, 40, 11)}
    <text class="mono" x="60" y="38" font-size="13" letter-spacing="2" fill="{CYAN}">// TELEMETRY</text>
    <text class="mono" x="{w-60}" y="38" font-size="12" text-anchor="end" fill="{DIM}">source: serhanensar.me</text>
    {''.join(tiles)}"""
    return frame(w, h, body, style)


# ───────────────────────── SECTION HEADERS ─────────────────────────
def header(num, title, sub):
    w, h = 1200, 70
    body = f"""
    <text class="mono" x="34" y="44" font-size="15" fill="{ORANGE}">{num}</text>
    <text class="sans" x="70" y="45" font-size="22" font-weight="800" letter-spacing="3" fill="{TEXT}">{esc(title)}</text>
    <text class="mono" x="{70 + len(title)*17 + 20}" y="44" font-size="13" fill="{DIM}">— {esc(sub)}</text>
    <rect x="{w-250}" y="34" width="210" height="2" rx="1" fill="url(#accent)" opacity=".7"/>
    <circle class="pulse" cx="{w-34}" cy="35" r="4" fill="{CYAN}"/>"""
    return frame(w, h, body)


# ───────────────────────── FOOTER ─────────────────────────
def footer():
    w, h = 1200, 170
    body = f"""
    {stars(w, h, 60, 23)}
    <path d="M0,{h} Q{w/2},{h-90} {w},{h} Z" fill="#C3CAD8" opacity=".14"/>
    <path d="M0,{h} Q{w/2},{h-70} {w},{h} Z" fill="#C3CAD8" opacity=".12"/>
    <text class="sans" x="{w/2}" y="74" font-size="30" font-weight="800" text-anchor="middle" fill="{TEXT}">Let's build something.</text>
    <text class="mono" x="{w/2}" y="106" font-size="14" text-anchor="middle" fill="{DIM}">transmission ends · always reading messages<tspan class="blink" fill="{CYAN}"> ▍</tspan></text>"""
    return frame(w, h, body)


def main():
    files = {"banner.svg": banner(), "telemetry.svg": telemetry(), "footer.svg": footer()}
    for key, (num, title, sub) in SECTIONS.items():
        files[f"h-{key}.svg"] = header(num, title, sub)
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8")
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()
