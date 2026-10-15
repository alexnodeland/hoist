#!/usr/bin/env python3
"""Write the README's animated SVGs to brand/readme/.

usage: python3 brand/tools/readme_svgs.py

Every number on a card comes from docs/results/claims.md or the paper, with its
scope; change one there first. Colours are brand/tokens.css's, light by default
and dark under prefers-color-scheme; each image carries its own background, so
it reads on either page theme. The animations are CSS only (GitHub strips
scripts) and stop under prefers-reduced-motion.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "readme"

STYLE = """
:root{--bg:#f8fbfb;--surface:#ffffff;--well:#eff3f4;--line:#dae1e3;--strong:#7e888b;--text:#141c1e;--muted:#4a5557;--subtle:#646e70;--accent:#02767b;--gfx:#039298;--soft:#e0f5f6;--ink:#141c1e;--onink:#f8fbfb}
@media (prefers-color-scheme:dark){:root{--bg:#0b0f11;--surface:#121719;--well:#191f21;--line:#272f32;--strong:#606b6f;--text:#eceff0;--muted:#b3bcbf;--subtle:#909a9d;--accent:#5dd2d8;--gfx:#33c0c7;--soft:#0b292c;--ink:#eceff0;--onink:#0b0f11}}
text{font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;fill:var(--text)}
.m{font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace}
.bg{fill:var(--bg);stroke:var(--line)}.card{fill:var(--surface);stroke:var(--line)}.well{fill:var(--well)}
.muted{fill:var(--muted)}.subtle{fill:var(--subtle)}.acc{fill:var(--accent)}.gfx{fill:var(--gfx)}.soft{fill:var(--soft)}
.turn{fill:var(--surface);stroke:var(--text);stroke-width:1.5}.chip{fill:var(--well);stroke:var(--strong);stroke-width:1.2}
.read{fill:var(--gfx)}.onread{fill:var(--onink)}.ghost{fill:none;stroke:var(--strong);stroke-width:1.5;stroke-dasharray:5 4}
.ink{fill:var(--ink)}.onink{fill:var(--onink)}.ln{stroke:var(--line);stroke-width:1}.lnS{stroke:var(--strong);stroke-width:1.5;fill:none}
.lnA{stroke:var(--gfx);stroke-width:2;fill:none}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
"""


def svg(w, h, title, desc, body, extra_css=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-labelledby="t d"><title id="t">{escape(title)}</title>'
        f'<desc id="d">{escape(desc)}</desc><style>{STYLE}{extra_css}</style>'
        f'<rect class="bg" x=".5" y=".5" width="{w-1}" height="{h-1}" rx="14"/>{body}</svg>\n'
    )


def keyframes(name, on, off, loop):
    """Hidden until `on` seconds, shown to `off`, then reset at the loop's end."""
    p = lambda s: f"{100*s/loop:.2f}%"
    return (f"@keyframes {name}{{0%,{p(on)}{{opacity:0}}{p(on+0.35)},{p(off)}{{opacity:1}}100%{{opacity:0}}}}"
            f".{name}{{animation:{name} {loop}s ease-out infinite}}")


# ---------------------------------------------------------------- hero
def hero():
    L = 11.0  # loop seconds
    x0, T, C, G = 176, 118, 86, 4
    css, body = [], []
    n = 0

    def at(x):  # seconds at which a segment starting at x appears
        return 0.5 + (x - x0) / (712 - x0) * 4.2

    def seg(x, y, w, kind, label, sub=None, cls=None):
        nonlocal n
        n += 1
        name = f"h{n}"
        css.append(keyframes(name, at(x), L - 1.2, L))
        h = 44
        if kind == "turn":
            g = (f'<rect class="turn" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>'
                 f'<text x="{x+w/2}" y="{y+19}" text-anchor="middle" font-size="12" font-weight="600">{label}</text>'
                 f'<text x="{x+w/2}" y="{y+34}" text-anchor="middle" font-size="11" class="subtle">{sub}</text>')
        elif kind == "call":
            g = (f'<rect class="chip" x="{x}" y="{y+6}" width="{w}" height="{h-12}" rx="6"/>'
                 f'<text class="m" x="{x+w/2}" y="{y+27}" text-anchor="middle" font-size="11">{label}</text>')
        else:  # call with the read-ahead riding along
            hw = w / 2
            g = (f'<rect class="chip" x="{x}" y="{y+6}" width="{hw}" height="{h-12}" rx="6"/>'
                 f'<rect class="read" x="{x+hw}" y="{y+6}" width="{hw}" height="{h-12}" rx="6"/>'
                 f'<text class="m" x="{x+hw/2}" y="{y+27}" text-anchor="middle" font-size="11">{label}</text>'
                 f'<text class="m onread" x="{x+hw*1.5}" y="{y+27}" text-anchor="middle" font-size="11">{sub}</text>')
        body.append(f'<g class="{name}">{g}</g>')

    ya, yb = 54, 156
    # lane labels
    body.append('<text x="28" y="34" font-size="13" font-weight="700" class="muted">WITHOUT HOIST</text>')
    body.append(f'<text x="28" y="{ya+20}" font-size="12" class="subtle">the agent asks,</text><text x="28" y="{ya+35}" font-size="12" class="subtle">one read per turn</text>')
    body.append(f'<text x="28" y="{yb+20}" font-size="12" class="acc" font-weight="600">Hoist reads ahead,</text><text x="28" y="{yb+35}" font-size="12" class="acc" font-weight="600">in the same result</text>')
    body.append(f'<line class="ln" x1="24" x2="856" y1="116" y2="116"/>')
    body.append('<text x="28" y="136" font-size="13" font-weight="700" class="acc">WITH HOIST</text>')
    # lane A
    x = x0
    seg(x, ya, T, "turn", "LLM turn 1", "asks for the user"); x += T + G
    seg(x, ya, C, "call", "get_user"); x += C + G
    seg(x, ya, T, "turn", "LLM turn 2", "asks for the order"); x += T + G
    seg(x, ya, C, "call", "get_order"); x += C + G
    seg(x, ya, T, "turn", "LLM turn 3", "replies"); xa_end = x + T
    # lane B
    x = x0
    seg(x, yb, T, "turn", "LLM turn 1", "asks for the user"); x += T + G
    seg(x, yb, C * 2 - 20, "pair", "get_user", "get_order"); x += C * 2 - 20 + G
    seg(x, yb, T, "turn", "LLM turn 2", "replies"); xb_end = x + T
    # the turn spared
    n += 1
    css.append(keyframes(f"h{n}", at(xb_end) + 0.4, L - 1.2, L))
    body.append(f'<g class="h{n}"><rect class="ghost" x="{xb_end+G}" y="{yb}" width="{xa_end-xb_end-G}" height="44" rx="8"/>'
                f'<text x="{(xb_end+xa_end)/2+G/2}" y="{yb+19}" text-anchor="middle" font-size="12" font-weight="700" class="acc">1 LLM turn</text>'
                f'<text x="{(xb_end+xa_end)/2+G/2}" y="{yb+34}" text-anchor="middle" font-size="11" class="acc">spared</text></g>')
    # time axis
    body.append(f'<line class="lnS" x1="{x0}" x2="{xa_end+8}" y1="224" y2="224"/>'
                f'<path class="lnS" d="M{xa_end+2} 219l8 5-8 5"/>'
                f'<text x="{x0}" y="243" font-size="11" class="subtle">time</text>'
                f'<text x="856" y="243" text-anchor="end" font-size="11" class="subtle">Illustrative: a lookup of the order the user names, read from the first result.</text>')
    return svg(880, 258, "A lookup spares an LLM turn",
               "Without Hoist the agent reads the user, then the order, then replies, in three LLM turns. "
               "With Hoist the order is read ahead and returned in the same tool result, and the agent replies in its second turn.",
               "".join(body), "".join(css))


# ---------------------------------------------------------------- numbers
def numbers():
    cols = [
        ("LIVE", "20.5% · 22.4%", "fewer LLM turns", "Claude Sonnet 5 · Claude Haiku 4.5", "τ²-bench, 28 tasks, 3 trials, pre-registered"),
        ("REPLAY", "86.4%", "of retail’s read-only ceiling", "nine agents it never saw", "10.2 points over a next-step speculator"),
        ("PROCEDURE", "39 of 40", "held-out tasks passed", "0.48 LLM turns per ticket", "τ²-bench solo telecom; 15.9 for the model alone"),
    ]
    W, H, cw = 880, 150, 277
    body, css = [], []
    for i, (kind, big, unit, l1, l2) in enumerate(cols):
        x = 24 + i * cw
        css.append(f"@keyframes n{i}{{0%{{opacity:0}}100%{{opacity:1}}}}.n{i}{{animation:n{i} .8s ease-out {0.2*i:.1f}s backwards}}")
        g = (f'<text class="acc m" x="{x}" y="34" font-size="11" font-weight="700">{kind}</text>'
             f'<text x="{x}" y="78" font-size="34" font-weight="700" letter-spacing="-1">{big}</text>'
             f'<text x="{x}" y="98" font-size="13" class="muted">{unit}</text>'
             f'<text x="{x}" y="120" font-size="12" font-weight="600">{l1}</text>'
             f'<text x="{x}" y="136" font-size="11" class="subtle">{l2}</text>')
        body.append(f'<g class="n{i}">{g}</g>')
        if i:
            body.append(f'<line class="ln" x1="{x-16}" x2="{x-16}" y1="24" y2="{H-16}"/>')
    return svg(W, H, "Hoist's headline results, each with its scope",
               "Live on 28 τ²-bench retail and airline tasks, three trials, pre-registered: Claude Sonnet 5 took 20.5% fewer LLM turns and Claude Haiku 4.5 22.4% fewer. "
               "Replay of nine agents it never saw: 86.4% of retail's read-only ceiling, 10.2 points more than a next-step speculator. "
               "A procedure compiled once passes 39 of 40 held-out solo telecom tasks at 0.48 LLM turns per ticket against 15.9 for the model alone.",
               "".join(body), "".join(css))


# ---------------------------------------------------------------- how it works
def how():
    steps = [
        ("1", "Record", "hoist-mcp", "Run your MCP server behind the proxy. It forwards every message and logs each session.", "rec"),
        ("2", "Learn", "hoist learn", "Count which reads follow which calls, and where each argument came from. Out comes a flow.", "learn"),
        ("3", "Review", "hoist flow-show", "Read the flow, run it in shadow, then promote the lookups that paid.", "review"),
        ("4", "Serve", "hoist-mcp --flow", "After each call, the flow’s lookups ride in the same tool result.", "serve"),
    ]
    W, H = 880, 284
    cw, gx, px = 190, 24, 24
    body, css = [], []
    y0 = 56
    # the track the packet runs along
    tx0, tx1, ty = px + cw / 2, px + 3 * (cw + gx) + cw / 2, y0 + 36
    body.append(f'<line class="lnS" x1="{tx0}" x2="{tx1}" y1="{ty}" y2="{ty}" stroke-dasharray="2 5"/>')
    for i, (n, name, cmd, text, icon) in enumerate(steps):
        x = px + i * (cw + gx)
        body.append(f'<rect class="card" x="{x}" y="{y0}" width="{cw}" height="202" rx="10"/>')
        cx = x + cw / 2
        body.append(f'<circle cx="{cx}" cy="{ty}" r="22" class="soft" stroke="var(--gfx)" stroke-width="1.5"/>')
        # icons, drawn in 24x24 around (cx, ty)
        s = lambda d: f'<g transform="translate({cx-12},{ty-12})" class="lnA" stroke-linecap="round" stroke-linejoin="round">{d}</g>'
        body.append(s({
            "rec": '<circle cx="12" cy="12" r="6" fill="var(--gfx)" stroke="none"/><circle cx="12" cy="12" r="10"/>',
            "learn": '<path d="M4 20V13M10 20V6M16 20V10M22 20H2"/>',
            "review": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
            "serve": '<path d="M3 12h14M12 6l6 6-6 6"/><path d="M21 6v12"/>',
        }[icon]))
        body.append(f'<text x="{x+16}" y="{y0+82}" font-size="11" font-weight="700" class="acc m">STEP {n}</text>')
        body.append(f'<text x="{x+16}" y="{y0+104}" font-size="18" font-weight="700">{name}</text>')
        body.append(f'<rect class="well" x="{x+16}" y="{y0+114}" width="{cw-32}" height="22" rx="5"/>'
                    f'<text class="m" x="{x+24}" y="{y0+129}" font-size="11.5">{cmd}</text>')
        # wrap text at ~30 chars
        words, lines, cur = text.split(), [], ""
        for w in words:
            if len(cur) + len(w) + 1 > 27:
                lines.append(cur); cur = w
            else:
                cur = (cur + " " + w).strip()
        lines.append(cur)
        for k, ln in enumerate(lines):
            body.append(f'<text x="{x+16}" y="{y0+154+k*14}" font-size="11.5" class="muted">{escape(ln)}</text>')
    # the packet: a read riding along
    css.append(f"@keyframes pk{{0%{{transform:translateX(0);opacity:0}}6%{{opacity:1}}88%{{opacity:1}}100%{{transform:translateX({tx1-tx0}px);opacity:0}}}}"
               ".pk{animation:pk 5.5s ease-in-out infinite}")
    body.insert(1, f'<g class="pk"><circle cx="{tx0}" cy="{ty}" r="6" class="read"/></g>')
    body.append(f'<text x="24" y="30" font-size="13" font-weight="700" class="muted">THE LOOP</text>'
                f'<text x="856" y="30" text-anchor="end" font-size="11.5" class="subtle">sessions keep arriving: hoist stage learns the next version beside the served one; hoist flow-commit serves it</text>')
    return svg(W, H, "How Hoist works: record, learn, review, serve",
               "Record sessions behind hoist-mcp. Learn a flow with hoist learn. Review it with hoist flow-show, in shadow, then promote the lookups that paid. "
               "Serve it: after each call, the flow's lookups ride in the same tool result.",
               "".join(body), "".join(css))


# ---------------------------------------------------------------- ceiling
def ceiling():
    rows = [
        ("AgentDojo, travel suite", 47.1, "a city’s listing names every later lookup"),
        ("τ²-bench", 29.0, "the user names themselves; the agent walks the records"),
        ("τ-bench", 28.4, "the same walk, with agents a year older"),
        ("AgentDojo, 4 suites", 22.1, ""),
        ("BFCL multi-turn", 13.2, ""),
        ("DTap-Bench, 6 domains", 10.7, ""),
        ("MCPMark", 7.0, "agents write their own SQL and pick the files"),
        ("WorkBench", 3.5, "each request names what to read"),
    ]
    W, rh, y0 = 880, 30, 78
    H = y0 + len(rows) * rh + 66
    lx, bx, bw = 24, 190, 330
    body = [f'<text x="24" y="30" font-size="13" font-weight="700" class="muted">WHERE A READ-ONLY SPECULATOR HAS ROOM</text>',
            f'<text x="24" y="50" font-size="12" class="subtle">The read-only ceiling: the most LLM turns a speculator that binds arguments from tool results could save. The domain sets it.</text>']
    css = []
    for i, (name, v, note) in enumerate(rows):
        y = y0 + i * rh
        nm = f"c{i}"
        css.append(f"@keyframes {nm}{{0%{{transform:scaleX(0)}}100%{{transform:scaleX(1)}}}}"
                   f".{nm}{{transform-box:fill-box;transform-origin:left;animation:{nm} .9s cubic-bezier(.2,.7,.2,1) {0.08*i:.2f}s backwards}}")
        body.append(f'<text x="{lx}" y="{y+17}" font-size="12.5" {"font-weight=\"700\"" if name=="τ²-bench" else ""}>{name}</text>')
        body.append(f'<rect class="well" x="{bx}" y="{y+5}" width="{bw}" height="16" rx="4"/>')
        w = bw * v / 55
        cls = "read" if v >= 20 else "ink"
        body.append(f'<rect class="{cls} {nm}" x="{bx}" y="{y+5}" width="{w:.1f}" height="16" rx="4"/>')
        body.append(f'<text class="m" x="{bx+w+8:.1f}" y="{y+18}" font-size="12" font-weight="700">{v}%</text>')
        if note:
            body.append(f'<text x="{bx+bw+18}" y="{y+17}" font-size="11" class="subtle">{note}</text>')
    body.append(f'<text x="24" y="{H-30}" font-size="11" class="subtle">Share of LLM turns, replayed from the agents’ published trajectories (the paper’s Tables 1 and 1b).</text>')
    body.append(f'<text x="24" y="{H-16}" font-size="11" class="subtle">In WorkBench, the lowest, the speculator makes no lookup at all.</text>')
    return svg(W, H, "The read-only ceiling by benchmark",
               "The most LLM turns a read-only speculator could save, as a share of turns: AgentDojo travel suite 47.1%, τ²-bench 29.0%, τ-bench 28.4%, "
               "AgentDojo four suites 22.1%, BFCL multi-turn 13.2%, DTap-Bench 10.7%, MCPMark 7.0%, WorkBench 3.5%.",
               "".join(body), "".join(css))


# ---------------------------------------------------------------- pillars
def pillars():
    items = [
        ("Any agent, any server", "Wraps a command or an HTTP server. Nothing else changes.",
         '<rect x="3" y="4" width="7" height="7" rx="1.5"/><rect x="14" y="4" width="7" height="7" rx="1.5"/><rect x="8.5" y="14" width="7" height="7" rx="1.5"/>'),
        ("Reads only", "Its worst case is a detour: a lookup nobody used. No state changes.",
         '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>'),
        ("No model of its own", "The reach decider counts. No key; a decision takes under a millisecond.",
         '<path d="M4 20V13M10 20V6M16 20V10M22 20H2"/>'),
        ("Reviewable", "A flow is a JSON file of counts. Diff it, shadow it, promote it.",
         '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h7"/>'),
    ]
    W, H, cw, gx, px = 880, 160, 196, 16, 24
    body = []
    css = []
    for i, (h, t, icon) in enumerate(items):
        x = px + i * (cw + gx)
        css.append(f"@keyframes p{i}{{0%{{opacity:0;transform:translateY(6px)}}100%{{opacity:1;transform:none}}}}.p{i}{{animation:p{i} .7s ease-out {0.12*i:.2f}s backwards}}")
        words, lines, cur = t.split(), [], ""
        for w in words:
            if len(cur) + len(w) + 1 > 26:
                lines.append(cur); cur = w
            else:
                cur = (cur + " " + w).strip()
        lines.append(cur)
        g = (f'<rect class="card" x="{x}" y="14" width="{cw}" height="132" rx="10"/>'
             f'<g transform="translate({x+16},28)" class="lnA" stroke-linecap="round" stroke-linejoin="round">{icon}</g>'
             f'<text x="{x+16}" y="74" font-size="14" font-weight="700">{h}</text>'
             + "".join(f'<text x="{x+16}" y="{92+k*14}" font-size="11.5" class="muted">{escape(l)}</text>' for k, l in enumerate(lines)))
        body.append(f'<g class="p{i}">{g}</g>')
    return svg(W, H, "What Hoist is",
               "Any agent, any MCP server. Reads only. No model of its own. Reviewable: a flow is a JSON file.",
               "".join(body), "".join(css)).replace('<rect class="bg"', '<rect fill="none" stroke="none"', 1)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, fn in [("hero", hero), ("numbers", numbers), ("how", how), ("ceiling", ceiling), ("pillars", pillars)]:
        (OUT / f"{name}.svg").write_text(fn())
        print("wrote", OUT / f"{name}.svg")
