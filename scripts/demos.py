"""Animated mini-demo cards for each mission (600×300), in the profile palette.

Each demo is a stylised illustration of what the project does, not real output.
"""
import random
from build_assets import frame, CYAN, ORANGE, TEXT, DIM, LINE, BG0, BG1, esc

W, H = 600, 300


def head(title, status="LIVE"):
    return (f'<text class="mono" x="26" y="36" font-size="12" letter-spacing="1.5" fill="{CYAN}">// {esc(title)}</text>'
            f'<text class="mono" x="{W-26}" y="36" font-size="11" text-anchor="end" fill="{DIM}">'
            f'<tspan class="pulse" fill="{ORANGE}">●</tspan> {esc(status)}</text>')


def card(title, body, style="", status="LIVE", defs=""):
    return frame(W, H, head(title, status) + body, style, defs)


# ─────────────── PhyDose-CT ───────────────
def phydose():
    rnd = random.Random(3)
    noise = "".join(
        f'<circle class="tw" cx="{150+rnd.uniform(-70,70):.0f}" cy="{150+rnd.uniform(-70,70):.0f}" r="1.3" '
        f'fill="{TEXT}" style="animation-delay:{rnd.uniform(0,3):.2f}s;animation-duration:.9s"/>'
        for _ in range(140))
    style = ".ci{animation:ci 5s ease-in-out infinite;transform-origin:300px 0}@keyframes ci{0%{transform:scaleX(2.2)}45%,100%{transform:scaleX(1)}}"
    body = f"""
    <defs><clipPath id="ctl"><circle cx="150" cy="150" r="82"/></clipPath><clipPath id="ctr"><circle cx="450" cy="150" r="82"/></clipPath></defs>
    <circle cx="150" cy="150" r="82" fill="#1A2440" stroke="{LINE}" stroke-width="2"/>
    <g clip-path="url(#ctl)">{noise}</g>
    <ellipse cx="128" cy="150" rx="28" ry="46" fill="none" stroke="{DIM}" opacity=".5"/><ellipse cx="172" cy="150" rx="28" ry="46" fill="none" stroke="{DIM}" opacity=".5"/>
    <circle cx="140" cy="130" r="7" fill="{TEXT}" opacity=".7"/>
    <circle cx="450" cy="150" r="82" fill="#1A2440" stroke="{LINE}" stroke-width="2"/>
    <ellipse cx="428" cy="150" rx="28" ry="46" fill="#24325A" stroke="{DIM}" opacity=".8"/><ellipse cx="472" cy="150" rx="28" ry="46" fill="#24325A" stroke="{DIM}" opacity=".8"/>
    <circle cx="440" cy="130" r="7" fill="{TEXT}"/>
    <circle class="pulse" cx="440" cy="130" r="13" fill="none" stroke="{CYAN}" stroke-width="1.5"/>
    <text class="mono" x="150" y="252" font-size="11" text-anchor="middle" fill="{DIM}">low-dose input</text>
    <text class="mono" x="450" y="252" font-size="11" text-anchor="middle" fill="{DIM}">physics-informed output</text>
    <path d="M250,150 H350" stroke="{CYAN}" stroke-width="2" stroke-dasharray="4 5"><animate attributeName="stroke-dashoffset" from="18" to="0" dur="1s" repeatCount="indefinite"/></path>
    <path d="M343,144 l8,6 -8,6" fill="none" stroke="{CYAN}" stroke-width="2"/>
    <line x1="210" y1="278" x2="390" y2="278" stroke="{LINE}" stroke-width="2"/>
    <rect class="ci" x="270" y="273" width="60" height="10" rx="5" fill="{CYAN}" opacity=".85"/>
    <line x1="352" y1="266" x2="352" y2="290" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="3 3"/>
    <text class="mono" x="400" y="282" font-size="10" fill="{DIM}">volume CI vs threshold</text>"""
    return card("PHYDOSE-CT · VERIFY THE VOLUME", body, style, "UNDER REVIEW")


# ─────────────── NISAR Time Machine ───────────────
def nisar():
    style = ".bar{animation:drop 6s ease-in-out infinite;transform-origin:0 250px}@keyframes drop{0%,30%{transform:scaleY(1)}55%,100%{transform:scaleY(.62)}}"
    body = f"""
    <defs><clipPath id="g"><circle cx="170" cy="160" r="95"/></clipPath>
    <radialGradient id="gl" cx=".35" cy=".35"><stop offset="0" stop-color="#1E3A5F"/><stop offset="1" stop-color="{BG0}"/></radialGradient>
    <path id="orb" d="M60,200 A120,40 -20 1,1 280,120 A120,40 -20 1,1 60,200"/></defs>
    <circle cx="170" cy="160" r="95" fill="url(#gl)" stroke="{LINE}" stroke-width="2"/>
    <g clip-path="url(#g)" fill="none" stroke="{CYAN}" stroke-opacity=".25">
      <ellipse cx="170" cy="160" rx="95" ry="30"/><ellipse cx="170" cy="160" rx="95" ry="65"/>
      <ellipse cx="170" cy="160" rx="30" ry="95"><animate attributeName="rx" values="0;95;0" dur="8s" repeatCount="indefinite"/></ellipse>
      <ellipse cx="170" cy="160" rx="65" ry="95"/><line x1="75" y1="160" x2="265" y2="160"/>
    </g>
    <circle cx="200" cy="135" r="6" fill="{ORANGE}"/><circle class="pulse" cx="200" cy="135" r="14" fill="none" stroke="{ORANGE}"/>
    <use href="#orb" fill="none" stroke="{TEXT}" stroke-opacity=".25" stroke-dasharray="3 6"/>
    <g><rect x="-6" y="-3" width="12" height="6" fill="{TEXT}"/><rect x="-16" y="-1.5" width="8" height="3" fill="{CYAN}"/><rect x="8" y="-1.5" width="8" height="3" fill="{CYAN}"/>
      <animateMotion dur="9s" repeatCount="indefinite"><mpath href="#orb"/></animateMotion></g>
    <text class="mono" x="340" y="78" font-size="11" fill="{DIM}">HV backscatter · burned forest</text>
    <line x1="340" y1="250" x2="560" y2="250" stroke="{LINE}" stroke-width="2"/>
    <rect x="360" y="110" width="50" height="140" rx="4" fill="{DIM}" opacity=".5"/>
    <rect class="bar" x="450" y="110" width="50" height="140" rx="4" fill="{CYAN}"/>
    <text class="mono" x="385" y="270" font-size="11" text-anchor="middle" fill="{DIM}">before</text>
    <text class="mono" x="475" y="270" font-size="11" text-anchor="middle" fill="{CYAN}">after</text>
    <text class="sans" x="475" y="100" font-size="14" font-weight="700" text-anchor="middle" fill="{TEXT}">≈ −5 dB</text>"""
    return card("NISAR · RADAR TIME MACHINE", body, style, "GLOBAL NOMINEE")


# ─────────────── TUYGUN / LAÇİN ───────────────
def tuygun():
    boxes = [(70, 90, 46, 30, "vehicle"), (190, 170, 22, 34, "person"), (110, 200, 50, 32, "vehicle"), (230, 80, 40, 40, "UAP")]
    b = "".join(
        f'<g class="bb" style="animation-delay:{i*.7:.1f}s"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{ORANGE if l=="UAP" else CYAN}" stroke-width="2"/>'
        f'<rect x="{x}" y="{y-14}" width="{len(l)*7+8}" height="13" fill="{ORANGE if l=="UAP" else CYAN}"/>'
        f'<text class="mono" x="{x+4}" y="{y-4}" font-size="10" fill="{BG0}">{l}</text></g>'
        for i, (x, y, w, h, l) in enumerate(boxes))
    style = (".bb{opacity:0;animation:bb 6s infinite}@keyframes bb{0%{opacity:0}8%,80%{opacity:1}90%,100%{opacity:0}}"
             ".vo{stroke-dasharray:420;animation:draw 6s linear infinite}@keyframes draw{from{stroke-dashoffset:420}to{stroke-dashoffset:0}}"
             "@media (prefers-reduced-motion:reduce){.bb{opacity:1}}")
    body = f"""
    <rect x="30" y="56" width="290" height="220" rx="10" fill="#101A33" stroke="{LINE}"/>
    <path d="M30,140 H320 M150,56 V276" stroke="#22304F" stroke-width="14"/>
    <rect x="76" y="96" width="34" height="18" rx="3" fill="{DIM}" opacity=".6"/><rect x="116" y="206" width="38" height="20" rx="3" fill="{DIM}" opacity=".6"/>
    <circle cx="201" cy="186" r="6" fill="{DIM}" opacity=".7"/><circle cx="250" cy="100" r="14" fill="none" stroke="{DIM}" stroke-width="3" opacity=".7"/>
    {b}
    <text class="mono" x="350" y="70" font-size="11" fill="{DIM}">visual odometry · GPS lost</text>
    <rect x="350" y="80" width="220" height="196" rx="10" fill="#101A33" stroke="{LINE}"/>
    <path d="M370,250 C410,200 430,230 470,170 S540,120 550,100" fill="none" stroke="{DIM}" stroke-width="2" stroke-dasharray="4 5"/>
    <path class="vo" d="M370,250 C412,204 428,226 472,174 S536,118 548,104" fill="none" stroke="{CYAN}" stroke-width="2.5"/>
    <text class="mono" x="365" y="100" font-size="10" fill="{DIM}">--- ground truth</text><text class="mono" x="470" y="100" font-size="10" fill="{CYAN}">— estimate</text>"""
    return card("TUYGUN & LAÇİN · AERIAL AI", body, style, "TEKNOFEST 2026")


# ─────────────── EGE ODBARS ───────────────
def odbars():
    wheels = "".join(f'<circle cx="{x}" cy="18" r="9" fill="{BG0}" stroke="{TEXT}" stroke-width="2.5"/>' for x in (-38, 0, 38))
    body = f"""
    <defs><path id="ter" d="M30,236 C40,236 60,214 120,218 S210,244 270,230 S360,206 420,222 S520,240 640,228"/></defs>
    <path d="M0,236 C40,236 60,214 120,218 S210,244 270,230 S360,206 420,222 S520,240 600,228 V300 H0 Z" fill="#162244"/>
    <use href="#ter" fill="none" stroke="{DIM}" stroke-width="2"/>
    <g transform="translate(470,170)"><path d="M0,0 L-14,44 H14 Z" fill="{ORANGE}" opacity=".9"/><rect x="-26" y="-12" width="52" height="66" fill="none" stroke="{CYAN}" stroke-width="2" class="pulse"/>
      <text class="mono" x="-26" y="-18" font-size="10" fill="{CYAN}">cone</text></g>
    <g><g transform="translate(0,-34)">
      <path d="M-38,18 L-19,0 L0,18 M-19,0 L19,-4 L38,18" fill="none" stroke="{CYAN}" stroke-width="3"/>
      <rect x="-30" y="-24" width="60" height="18" rx="4" fill="{BG1}" stroke="{CYAN}" stroke-width="2"/>
      <path d="M30,-18 l40,-14 v28 z" fill="{CYAN}" opacity=".12"/>{wheels}</g>
      <animateMotion dur="9s" repeatCount="indefinite" rotate="auto"><mpath href="#ter"/></animateMotion></g>
    <text class="mono" x="26" y="70" font-size="11" fill="{DIM}">6×4 rocker-bogie · YOLOv8 + ByteTrack</text>"""
    return card("EGE ODBARS · AUTONOMOUS UGV", body, "", "TEKNOFEST 2026")


# ─────────────── EGENODE ───────────────
def egenode():
    tags = [(120, 110), (300, 110), (480, 110), (480, 240), (300, 240)]
    t = "".join(f'<rect x="{x-9}" y="{y-9}" width="18" height="18" rx="3" fill="none" stroke="{CYAN}" stroke-width="2"/>'
                f'<rect x="{x-5}" y="{y-5}" width="10" height="10" fill="{CYAN}" opacity="0">'
                f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;.05;.4" dur="10s" begin="{i*2}s" repeatCount="indefinite"/></rect>'
                for i, (x, y) in enumerate(tags))
    grid = "".join(f'<line x1="{x}" y1="56" x2="{x}" y2="280" stroke="#1A2545"/>' for x in range(40, 600, 40))
    grid += "".join(f'<line x1="20" y1="{y}" x2="580" y2="{y}" stroke="#1A2545"/>' for y in range(60, 300, 40))
    body = f"""
    {grid}
    <path id="route" d="M120,110 H300 H480 V240 H300 H120 V110" fill="none" stroke="{DIM}" stroke-dasharray="3 6"/>
    {t}
    <g><rect x="-16" y="-16" width="32" height="32" rx="6" fill="{BG1}" stroke="{ORANGE}" stroke-width="2.5"/>
      <path d="M0,-6 L10,-16 L14,-10" fill="none" stroke="{TEXT}" stroke-width="2"/><circle r="3" fill="{ORANGE}"/>
      <animateMotion dur="10s" repeatCount="indefinite" path="M120,110 H300 H480 V240 H300 H120 V110"/></g>
    <text class="mono" x="26" y="290" font-size="11" fill="{DIM}">RFID · IMU · 4-DOF arm on one ESP32</text>"""
    return card("EGENODE · LOGISTICS ROBOT", body, "", "TEKNOFEST 2026")


# ─────────────── AkıllıTepsi ───────────────
def tray():
    cells = [(70, 70, 210, 100, CYAN, 0), (300, 70, 230, 100, ORANGE, 1), (70, 190, 140, 80, CYAN, 2), (230, 190, 140, 80, CYAN, 3), (390, 190, 140, 80, ORANGE, 4)]
    c = "".join(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#1A2440" stroke="{LINE}" stroke-width="2"/>'
        f'<ellipse class="m" cx="{x+w/2}" cy="{y+h/2}" rx="{w*.3}" ry="{h*.28}" fill="{col}" fill-opacity=".35" stroke="{col}" stroke-width="2" style="animation-delay:{d*.6}s"/>'
        for x, y, w, h, col, d in cells)
    style = (".m{opacity:0;animation:m 6s infinite}@keyframes m{0%{opacity:0}10%,80%{opacity:1}90%,100%{opacity:0}}"
             ".scan{animation:scan 3s linear infinite}@keyframes scan{from{transform:translateY(0)}to{transform:translateY(210px)}}"
             "@media (prefers-reduced-motion:reduce){.m{opacity:1}}")
    body = f"""
    <rect x="50" y="56" width="500" height="228" rx="22" fill="none" stroke="{DIM}" stroke-width="2"/>
    {c}
    <rect class="scan" x="50" y="60" width="500" height="2" fill="{CYAN}" opacity=".6"/>
    <text class="mono" x="{W-26}" y="292" font-size="10" text-anchor="end" fill="{DIM}">segmenting leftovers per compartment</text>"""
    return card("AKILLITEPSI · FOOD WASTE AI", body, style, "TOP 100")


# ─────────────── UniLate ───────────────
def unilate():
    rows = [("Signals", .45, CYAN), ("Physics II", .9, ORANGE), ("Algorithms", .3, CYAN), ("Calculus", .6, CYAN)]
    r = "".join(
        f'<text class="sans" x="232" y="{112+i*42}" font-size="12" fill="{TEXT}">{n}</text>'
        f'<rect x="232" y="{120+i*42}" width="136" height="6" rx="3" fill="#22304F"/>'
        f'<rect x="232" y="{120+i*42}" width="0" height="6" rx="3" fill="{col}"><animate attributeName="width" values="0;{136*v:.0f};{136*v:.0f}" keyTimes="0;.4;1" dur="5s" begin="{i*.3}s" repeatCount="indefinite"/></rect>'
        for i, (n, v, col) in enumerate(rows))
    body = f"""
    <rect x="210" y="52" width="180" height="240" rx="26" fill="{BG0}" stroke="{TEXT}" stroke-opacity=".6" stroke-width="2.5"/>
    <rect x="275" y="60" width="50" height="6" rx="3" fill="{DIM}" opacity=".5"/>
    <text class="sans" x="232" y="88" font-size="13" font-weight="800" fill="{CYAN}">Absence room</text>
    {r}
    <text class="mono" x="40" y="140" font-size="11" fill="{DIM}">offline-first</text>
    <text class="mono" x="40" y="160" font-size="11" fill="{DIM}">no account</text>
    <text class="mono" x="40" y="180" font-size="11" fill="{DIM}">no backend</text>
    <text class="mono" x="560" y="160" font-size="11" text-anchor="end" fill="{ORANGE}">⚠ near limit</text>"""
    return card("UNILATE · STUDENT CO-PILOT", body, "", "CLOSED BETA")


# ─────────────── TrackpadProMax ───────────────
def trackpad():
    style = ".rip{animation:rip 2.4s ease-out infinite;transform-origin:250px 170px}@keyframes rip{from{transform:scale(.2);opacity:1}to{transform:scale(2.6);opacity:0}}"
    body = f"""
    <rect x="70" y="70" width="360" height="200" rx="18" fill="#1A2440" stroke="{LINE}" stroke-width="2"/>
    <circle class="rip" cx="250" cy="170" r="22" fill="none" stroke="{CYAN}" stroke-width="2"/>
    <circle class="rip" cx="250" cy="170" r="22" fill="none" stroke="{CYAN}" stroke-width="2" style="animation-delay:.8s"/>
    <circle cx="250" cy="170" r="16" fill="{CYAN}" opacity=".9"><animate attributeName="r" values="12;18;12" dur="2.4s" repeatCount="indefinite"/></circle>
    <text class="mono" x="470" y="82" font-size="11" fill="{DIM}">force</text>
    <rect x="476" y="92" width="22" height="170" rx="11" fill="#22304F"/>
    <rect x="476" y="92" width="22" height="170" rx="11" fill="{ORANGE}"><animate attributeName="height" values="20;170;20" dur="2.4s" repeatCount="indefinite"/><animate attributeName="y" values="242;92;242" dur="2.4s" repeatCount="indefinite"/></rect>
    <text class="mono" x="512" y="100" font-size="10" fill="{ORANGE}">deep</text><text class="mono" x="512" y="260" font-size="10" fill="{DIM}">light</text>
    <text class="mono" x="70" y="292" font-size="10" fill="{DIM}">pressure gestures · custom taps · haptics</text>"""
    return card("TRACKPADPROMAX · FORCE TOUCH", body, style, "macOS")


# ─────────────── ecosystem-connector ───────────────
def ecosystem():
    mac, win, phone = (150, 130), (450, 130), (300, 240)
    links = [(mac, win), (win, phone), (phone, mac)]
    l = ""
    for i, ((x1, y1), (x2, y2)) in enumerate(links):
        p = f"M{x1},{y1} L{x2},{y2}"
        l += (f'<path d="{p}" stroke="{LINE}" stroke-width="2"/>'
              f'<circle r="5" fill="{CYAN if i != 1 else ORANGE}"><animateMotion dur="2.6s" begin="{i*.8}s" repeatCount="indefinite" path="{p}"/></circle>')
    body = f"""
    {l}
    <g transform="translate(150,130)"><rect x="-46" y="-32" width="92" height="58" rx="6" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/><rect x="-58" y="26" width="116" height="8" rx="3" fill="{TEXT}" opacity=".7"/></g>
    <g transform="translate(450,130)"><rect x="-50" y="-34" width="100" height="62" rx="5" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/><rect x="-6" y="28" width="12" height="12" fill="{TEXT}" opacity=".7"/><rect x="-24" y="40" width="48" height="5" rx="2" fill="{TEXT}" opacity=".7"/></g>
    <g transform="translate(300,240)"><rect x="-17" y="-32" width="34" height="62" rx="7" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/></g>
    <text class="mono" x="150" y="192" font-size="11" text-anchor="middle" fill="{DIM}">macOS</text>
    <text class="mono" x="450" y="196" font-size="11" text-anchor="middle" fill="{DIM}">Windows</text>
    <text class="mono" x="352" y="244" font-size="11" fill="{DIM}">Android</text>
    <text class="mono" x="26" y="290" font-size="10" fill="{DIM}">files · clipboard · handoff over LAN</text>"""
    return card("ECOSYSTEM-CONNECTOR · ONE MESH", body, "", "RUST")


# ─────────────── HomeAgent ───────────────
def homeagent():
    hub = (300, 165)
    clients = [((110, 95), "web"), ((490, 95), "telegram"), ((110, 240), "ESP32-S3"), ((490, 240), "Wear OS")]
    s = ""
    for i, ((x, y), name) in enumerate(clients):
        p = f"M{hub[0]},{hub[1]} L{x},{y}"
        s += (f'<path d="{p}" stroke="{LINE}" stroke-width="2"/>'
              f'<circle r="4" fill="{CYAN}"><animateMotion dur="2s" begin="{i*.5}s" repeatCount="indefinite" path="{p}"/></circle>'
              f'<rect x="{x-48}" y="{y-18}" width="96" height="36" rx="10" fill="{BG1}" stroke="{CYAN}" stroke-opacity=".7"/>'
              f'<text class="mono" x="{x}" y="{y+4}" font-size="11" text-anchor="middle" fill="{TEXT}">{name}</text>')
    body = f"""
    {s}
    <rect x="250" y="130" width="100" height="70" rx="12" fill="{BG0}" stroke="{ORANGE}" stroke-width="2.5"/>
    <text class="sans" x="300" y="162" font-size="14" font-weight="800" text-anchor="middle" fill="{TEXT}">Pi 5 hub</text>
    <text class="mono" x="300" y="182" font-size="10" text-anchor="middle" fill="{DIM}">FastAPI · Gemini</text>"""
    return card("HOMEAGENT · ONE HUB, FOUR SCREENS", body, "", "SELF-HOSTED")


# ─────────────── Eye2S ───────────────
def eye2s():
    frames = "".join(
        f'<rect x="{40+i*42}" y="80" width="34" height="26" rx="4" fill="#1A2440" stroke="{LINE}"/>'
        f'<rect x="{40+i*42}" y="80" width="34" height="26" rx="4" fill="{CYAN}" opacity="0"><animate attributeName="opacity" values="0;0;.8;.8;0" keyTimes="0;{i*.08:.2f};{i*.08+.02:.2f};.85;1" dur="6s" repeatCount="indefinite"/></rect>'
        for i in range(6))
    style = (".lock{opacity:0;animation:lock 6s infinite}@keyframes lock{0%,55%{opacity:0}60%,90%{opacity:1}100%{opacity:0}}"
             "@media (prefers-reduced-motion:reduce){.lock{opacity:1}}")
    body = f"""
    <text class="mono" x="40" y="72" font-size="11" fill="{DIM}">few-shot: 6 frames</text>
    {frames}
    <rect x="40" y="124" width="250" height="150" rx="10" fill="#101A33" stroke="{LINE}"/>
    <rect x="140" y="178" width="46" height="54" rx="6" fill="{DIM}" opacity=".6"/><path d="M186,190 h10 a12,12 0 0 1 0,24 h-10" fill="none" stroke="{DIM}" stroke-width="5" opacity=".6"/>
    <g class="lock"><path d="M118,160 h14 M118,160 v14 M212,160 h-14 M212,160 v14 M118,242 h14 M118,242 v-14 M212,242 h-14 M212,242 v-14" stroke="{ORANGE}" stroke-width="2.5" fill="none"/>
      <text class="mono" x="118" y="152" font-size="10" fill="{ORANGE}">learned: mug</text></g>
    <g transform="translate(440,190)" fill="none" stroke="{CYAN}" stroke-width="2.5" stroke-linecap="round">
      <path d="M-20,30 v-50 M-6,30 v-62 M8,30 v-56 M22,30 v-40 M-34,40 q-6,-24 14,-10"/>
      <circle cx="-6" cy="-32" r="4" fill="{CYAN}" class="pulse"/></g>
    <text class="mono" x="440" y="262" font-size="11" text-anchor="middle" fill="{DIM}">hand tracking</text>"""
    return card("EYE2S · AR PERCEPTION", body, style, "SOLO")


# ─────────────── Portfolio ───────────────
def portfolio():
    style = (".scene{animation:sc 8s ease-in-out infinite}@keyframes sc{0%,10%{transform:translateY(0)}45%,55%{transform:translateY(-120px)}90%,100%{transform:translateY(0)}}"
             ".thumb{animation:th 8s ease-in-out infinite}@keyframes th{0%,10%{transform:translateY(0)}45%,55%{transform:translateY(110px)}90%,100%{transform:translateY(0)}}")
    body = f"""
    <defs><clipPath id="win"><rect x="60" y="78" width="480" height="196"/></clipPath></defs>
    <rect x="60" y="56" width="480" height="218" rx="10" fill="{BG0}" stroke="{LINE}" stroke-width="2"/>
    <circle cx="78" cy="67" r="4" fill="{ORANGE}"/><circle cx="92" cy="67" r="4" fill="{DIM}"/><circle cx="106" cy="67" r="4" fill="{DIM}"/>
    <text class="mono" x="300" y="71" font-size="10" text-anchor="middle" fill="{DIM}">serhanensar.me</text>
    <g clip-path="url(#win)"><g class="scene">
      <circle cx="400" cy="160" r="48" fill="#C3CAD8"/><circle cx="385" cy="148" r="9" fill="#8B96AD" opacity=".5"/>
      <text class="sans" x="90" y="150" font-size="24" font-weight="800" fill="{TEXT}">Journey to</text>
      <text class="sans" x="90" y="180" font-size="24" font-weight="800" fill="{CYAN}">the Moon</text>
      <rect x="90" y="270" width="180" height="90" rx="8" fill="#1A2440" stroke="{CYAN}" stroke-opacity=".6"/>
      <rect x="110" y="290" width="50" height="34" fill="none" stroke="{ORANGE}" stroke-width="2"/>
      <text class="mono" x="300" y="300" font-size="11" fill="{DIM}">live ONNX detection</text>
      <text class="mono" x="300" y="320" font-size="11" fill="{DIM}">in your browser</text>
    </g></g>
    <rect x="528" y="84" width="4" height="184" rx="2" fill="#22304F"/>
    <rect class="thumb" x="528" y="84" width="4" height="60" rx="2" fill="{CYAN}"/>"""
    return card("SERHANENSAR.ME · SCROLL ENGINE", body, style, "NEXT.JS")


ALL = {
    "phydose": phydose, "nisar": nisar, "tuygun": tuygun, "odbars": odbars, "egenode": egenode,
    "tray": tray, "unilate": unilate, "trackpad": trackpad, "ecosystem": ecosystem,
    "homeagent": homeagent, "eye2s": eye2s, "portfolio": portfolio,
}


# ═══════════════ MINI CARDS (400×220) for "more from the hangar" ═══════════════
MW, MH = 400, 220


def mini(title, body, style=""):
    h = f'<text class="mono" x="20" y="30" font-size="11" letter-spacing="1.2" fill="{CYAN}">// {esc(title)}</text>'
    return frame(MW, MH, h + body, style)


def m_callbridge():
    return mini("CALLBRIDGE", f"""
    <rect x="50" y="70" width="110" height="80" rx="8" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/>
    <text class="mono" x="105" y="168" font-size="10" text-anchor="middle" fill="{DIM}">tablet · SIM</text>
    <rect x="270" y="58" width="56" height="104" rx="10" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/>
    <text class="sans" x="298" y="114" font-size="20" text-anchor="middle" fill="{CYAN}">☏</text>
    <circle cx="298" cy="108" r="20" fill="none" stroke="{CYAN}"><animate attributeName="r" values="18;40" dur="1.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0" dur="1.4s" repeatCount="indefinite"/></circle>
    <path d="M165,110 H262" stroke="{LINE}" stroke-width="2"/>
    <circle r="4" fill="{ORANGE}"><animateMotion dur="1.4s" repeatCount="indefinite" path="M165,110 H262"/></circle>
    <text class="mono" x="298" y="190" font-size="10" text-anchor="middle" fill="{DIM}">answer anywhere</text>""")


def m_hotspot():
    arcs = "".join(f'<path d="M{110-r},{110-r*.2} A{r},{r} 0 0 1 {110+r},{110-r*.2}" fill="none" stroke="{CYAN}" stroke-width="2.5" opacity="0">'
                   f'<animate attributeName="opacity" values="0;1;0" dur="1.8s" begin="{i*.3}s" repeatCount="indefinite"/></path>' for i, r in enumerate((16, 30, 44)))
    return mini("HOTSPOT TTL", f"""
    <rect x="92" y="110" width="36" height="66" rx="7" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/>{arcs}
    <rect x="230" y="96" width="110" height="68" rx="6" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/><rect x="218" y="164" width="134" height="7" rx="3" fill="{TEXT}" opacity=".7"/>
    <text class="mono" x="285" y="136" font-size="15" font-weight="700" text-anchor="middle" fill="{ORANGE}">TTL 65</text>
    <text class="mono" x="200" y="200" font-size="10" text-anchor="middle" fill="{DIM}">macOS · Windows · Linux · Android</text>""")


def m_telemetry():
    return mini("SMART TELEMETRY", f"""
    <circle cx="70" cy="115" r="30" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/><text class="mono" x="70" y="119" font-size="10" text-anchor="middle" fill="{CYAN}">WearOS</text>
    <rect x="165" y="95" width="70" height="40" rx="4" fill="{BG1}" stroke="{CYAN}" stroke-width="2"/><text class="mono" x="200" y="119" font-size="10" text-anchor="middle" fill="{TEXT}">ESP32</text>
    <rect x="285" y="88" width="90" height="56" rx="4" fill="{BG0}" stroke="{TEXT}" stroke-width="2"/>
    <text class="mono" x="330" y="122" font-size="16" text-anchor="middle" fill="{ORANGE}">72 <tspan font-size="9" fill="{DIM}">bpm</tspan></text>
    <path d="M100,115 H160 M240,115 H280" stroke="{LINE}" stroke-width="2"/>
    <circle r="4" fill="{CYAN}"><animateMotion dur="1s" repeatCount="indefinite" path="M100,115 H160 L240,115 H280"/></circle>
    <text class="mono" x="200" y="190" font-size="10" text-anchor="middle" fill="{DIM}">Nextion HMI · live at 1 Hz</text>""")


def m_nextion():
    style = (".l2{opacity:0;animation:l2 5s infinite}@keyframes l2{0%,45%{opacity:0}50%,100%{opacity:1}}"
             "@media (prefers-reduced-motion:reduce){.l2{opacity:1}}")
    return mini("NEXTION-EDITOR-LINUX", f"""
    <rect x="30" y="52" width="340" height="140" rx="8" fill="{BG0}" stroke="{LINE}" stroke-width="2"/>
    <circle cx="46" cy="66" r="4" fill="{ORANGE}"/><circle cx="60" cy="66" r="4" fill="{DIM}"/><circle cx="74" cy="66" r="4" fill="{DIM}"/>
    <text class="mono" x="46" y="104" font-size="13" fill="{TEXT}"><tspan fill="{CYAN}">$</tspan> ./install.sh<tspan class="blink" fill="{CYAN}">▍</tspan></text>
    <text class="mono l2" x="46" y="132" font-size="12" fill="{DIM}">wine prefix ready</text>
    <text class="mono l2" x="46" y="156" font-size="12" fill="{CYAN}" style="animation-delay:.6s">✓ Nextion Editor running on Ubuntu</text>""", style)


def m_labelforge():
    rows = "".join(f'<circle cx="262" cy="{86+i*24}" r="5" fill="{c}"/><text class="mono" x="274" y="{90+i*24}" font-size="11" fill="{TEXT}">{n}</text>'
                   for i, (n, c) in enumerate([("vehicle", CYAN), ("person", CYAN), ("UAP", ORANGE), ("UAI", ORANGE)]))
    return mini("LABELFORGE", f"""
    <rect x="30" y="56" width="200" height="140" rx="8" fill="#101A33" stroke="{LINE}"/>
    <rect x="70" y="96" width="0" height="0" fill="{CYAN}" fill-opacity=".15" stroke="{CYAN}" stroke-width="2">
      <animate attributeName="width" values="0;90;90" keyTimes="0;.5;1" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="height" values="0;60;60" keyTimes="0;.5;1" dur="3s" repeatCount="indefinite"/></rect>
    {rows}""")


def m_jsontoyolo():
    style = (".o{opacity:0;animation:o 4s infinite}@keyframes o{0%,40%{opacity:0}55%,100%{opacity:1}}"
             "@media (prefers-reduced-motion:reduce){.o{opacity:1}}")
    out = "".join(f'<text class="mono o" x="230" y="{100+i*22}" font-size="11" fill="{CYAN}" style="animation-delay:{i*.25}s">{t}</text>'
                  for i, t in enumerate(["0 0.512 0.418 0.120", "1 0.233 0.701 0.064", "2 0.804 0.297 0.151"]))
    return mini("JSONTOYOLO", f"""
    <text class="mono" x="30" y="96" font-size="11" fill="{DIM}">{{ "label": "car",</text>
    <text class="mono" x="40" y="118" font-size="11" fill="{DIM}">"points": [[412,</text>
    <text class="mono" x="40" y="140" font-size="11" fill="{DIM}">218], ...] }}</text>
    <path d="M180,118 H215" stroke="{ORANGE}" stroke-width="2"/><path d="M209,112 l7,6 -7,6" fill="none" stroke="{ORANGE}" stroke-width="2"/>
    {out}
    <text class="mono" x="200" y="196" font-size="10" text-anchor="middle" fill="{DIM}">Supervisely JSON → YOLOv8/v11 · GUI + CLI</text>""", style)


def m_stetoskop():
    style = ".car{animation:car 6s ease-in-out infinite}@keyframes car{0%,25%{transform:translateX(0)}35%,60%{transform:translateX(-90px)}70%,100%{transform:translateX(0)}}"
    cards = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{BG1}" stroke="{c}" stroke-width="2"/><circle cx="{x+w/2}" cy="{y+h*.38}" r="{w*.18}" fill="{DIM}" opacity=".6"/>'
                    for x, y, w, h, c in [(60, 78, 70, 96, LINE), (155, 64, 90, 124, CYAN), (270, 78, 70, 96, LINE), (365, 78, 70, 96, LINE)])
    return mini("STETOSKOP AKADEMİ", f"""<defs><clipPath id="cv"><rect x="20" y="50" width="360" height="150"/></clipPath></defs>
    <g clip-path="url(#cv)"><g class="car">{cards}</g></g>
    <text class="mono" x="200" y="206" font-size="10" text-anchor="middle" fill="{DIM}">zero dependencies · freelance · delivered</text>""", style)


def m_prextreme():
    return mini("PREXTREME", f"""
    <text class="mono" x="40" y="96" font-size="12" fill="{DIM}"><tspan fill="{ORANGE}">public class</tspan> Main {{</text>
    <text class="mono" x="60" y="118" font-size="12" fill="{DIM}">// greedy + next-pos table</text>
    <text class="mono" x="40" y="140" font-size="12" fill="{DIM}">}}</text>
    <text class="mono" x="270" y="92" font-size="11" fill="{DIM}">judge</text>
    <rect x="270" y="102" width="100" height="10" rx="5" fill="#22304F"/>
    <rect x="270" y="102" width="0" height="10" rx="5" fill="{CYAN}"><animate attributeName="width" values="0;100;100" keyTimes="0;.6;1" dur="3s" repeatCount="indefinite"/></rect>
    <text class="sans" x="370" y="140" font-size="18" font-weight="800" text-anchor="end" fill="{TEXT}">100</text>
    <text class="mono" x="200" y="196" font-size="10" text-anchor="middle" fill="{DIM}">IEEEXtreme-style problems in Java</text>""")


def m_n8n():
    nodes = [(60, "scrape"), (150, "parse"), (240, "LLM"), (330, "JSON")]
    n = "".join(f'<rect x="{x-34}" y="92" width="68" height="40" rx="10" fill="{BG1}" stroke="{ORANGE if t=="LLM" else CYAN}" stroke-width="2"/>'
                f'<text class="mono" x="{x}" y="116" font-size="11" text-anchor="middle" fill="{TEXT}">{t}</text>' for x, t in nodes)
    return mini("N8N DEEP SCRAPER", f"""
    <path d="M94,112 H116 M184,112 H206 M274,112 H296" stroke="{LINE}" stroke-width="2"/>
    {n}
    <circle r="4" fill="{CYAN}"><animateMotion dur="2.4s" repeatCount="indefinite" path="M60,150 H330"/></circle>
    <path d="M60,150 H330" stroke="{LINE}" stroke-dasharray="3 5"/>
    <text class="mono" x="200" y="192" font-size="10" text-anchor="middle" fill="{DIM}">paginated startup news → structured data</text>""")


def m_thumbnail():
    style = (".a{animation:a 6s infinite}.b{animation:a 6s infinite 3s;opacity:0}"
             "@keyframes a{0%,45%{opacity:1}50%,95%{opacity:0}100%{opacity:1}}")
    return mini("THUMBNAIL STUDIO", f"""
    <rect x="80" y="52" width="240" height="135" rx="8" fill="{BG0}" stroke="{LINE}" stroke-width="2"/>
    <g class="a"><circle cx="260" cy="125" r="34" fill="{DIM}" opacity=".7"/><rect x="100" y="80" width="110" height="18" rx="3" fill="{CYAN}"/><rect x="100" y="106" width="80" height="18" rx="3" fill="{ORANGE}"/></g>
    <g class="b"><circle cx="140" cy="125" r="34" fill="{DIM}" opacity=".7"/><rect x="195" y="88" width="105" height="22" rx="3" fill="{ORANGE}"/><rect x="195" y="118" width="70" height="14" rx="3" fill="{CYAN}"/></g>
    <text class="mono" x="200" y="206" font-size="10" text-anchor="middle" fill="{DIM}">style archetypes · consistent avatar</text>""", style)


def m_raspi():
    return mini("RASPI 5 TOOLKIT", f"""
    <rect x="40" y="70" width="120" height="84" rx="6" fill="{BG1}" stroke="{CYAN}" stroke-width="2"/>
    <rect x="60" y="90" width="34" height="34" fill="{BG0}"/><circle cx="130" cy="84" r="3" fill="{ORANGE}" class="pulse"/>
    <path d="M44,74 h112" stroke="{DIM}" stroke-dasharray="2 3"/>
    <rect x="240" y="70" width="130" height="84" rx="6" fill="{BG1}" stroke="{TEXT}" stroke-width="2"/>
    <text class="mono" x="305" y="117" font-size="11" text-anchor="middle" fill="{CYAN}">GNOME · RDP</text>
    <path d="M165,112 H235" stroke="{LINE}" stroke-width="2"/>
    <circle r="4" fill="{CYAN}"><animateMotion dur="1.6s" repeatCount="indefinite" path="M165,112 H235"/></circle>
    <text class="mono" x="200" y="196" font-size="10" text-anchor="middle" fill="{DIM}">headless setup · one-click Mac launcher</text>""")


def m_fretrum():
    strings = "".join(f'<line x1="40" y1="{80+i*14}" x2="250" y2="{80+i*14}" stroke="{DIM}" stroke-width="{1+i*.3:.1f}"/>' for i in range(6))
    frets = "".join(f'<line x1="{x}" y1="74" x2="{x}" y2="156" stroke="{LINE}" stroke-width="2"/>' for x in range(70, 250, 42))
    return mini("FRETRUM · IN PROGRESS", f"""
    {frets}{strings}
    <path stroke="{CYAN}" stroke-width="2" fill="none"><animate attributeName="d" values="M40,122 Q145,116 250,122;M40,122 Q145,128 250,122;M40,122 Q145,116 250,122" dur=".18s" repeatCount="indefinite"/></path>
    <circle cx="112" cy="108" r="6" fill="{ORANGE}"/>
    <path d="M290,150 A50,50 0 0 1 370,150" fill="none" stroke="{LINE}" stroke-width="2"/>
    <line x1="330" y1="150" x2="330" y2="112" stroke="{CYAN}" stroke-width="2.5"><animateTransform attributeName="transform" type="rotate" values="-25 330 150;8 330 150;-3 330 150;0 330 150" dur="3s" repeatCount="indefinite"/></line>
    <text class="mono" x="330" y="172" font-size="11" text-anchor="middle" fill="{CYAN}">E</text>
    <text class="mono" x="200" y="200" font-size="10" text-anchor="middle" fill="{DIM}">tuner · metronome · chords · tabs</text>""")


MINI = {
    "callbridge": m_callbridge, "hotspot": m_hotspot, "telemetry": m_telemetry, "nextion": m_nextion,
    "labelforge": m_labelforge, "jsontoyolo": m_jsontoyolo, "stetoskop": m_stetoskop, "prextreme": m_prextreme,
    "n8n": m_n8n, "thumbnail": m_thumbnail, "raspi": m_raspi, "fretrum": m_fretrum,
}
