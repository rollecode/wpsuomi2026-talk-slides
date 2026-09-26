"""Editable code panel: plain panel PNG plus one Geist Mono text item with syntax-coloured runs."""
import html, re, subprocess, sys
sys.path.insert(0, "/Users/rolle/Projects/keynote-base")
import deck, newsection as ns
K = "/Users/rolle/Projects/keynote-base/talks/wpsuomi-2026/keyassets"
LS = " "  # line separator: no paragraph spacing; sized 34 for ~40px lines at 26pt


def rgb(h):
    return "{" + ", ".join(str(int(h[i:i+2], 16) * 257) for i in (1, 3, 5)) + "}"


def runs(code, lang):
    out, text = [], ""
    for m in re.finditer(r'<span class="t-(\w+)">(.*?)</span>|([^<]+)', deck.highlight(code, lang), re.S):
        kind, seg = (m.group(1), m.group(2)) if m.group(1) else (None, m.group(3))
        seg = html.unescape(seg).replace("\n", LS)
        a = len(text) + 1
        text += seg
        if kind:
            out.append((a, len(text), deck.CODE_THEME[kind]))
    return text + LS, out


def panel(w, h):
    f = f"{K}/panel-{w}x{h}.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c=0x1B0B38:s={w*2}x{h*2}", "-frames:v", "1", f], check=True)
    return f


def add(slide, code, lang, x, y, w, pad=28):
    lines = code.count("\n") + 1
    h = pad * 2 + 40 * lines
    text, rs = runs(code, lang)
    sc = [f'tell application "Keynote" to tell slide {slide} of document {ns.q(ns.DOC)}',
          f'make new image with properties {{file:(POSIX file "{panel(w, h)}"), position:{{{x}, {y}}}, width:{w}, height:{h}}}',
          f'set t to make new text item with properties {{object text:{ns.q(text)}}}',
          f'tell object text of t\nset its font to "GeistMono-Regular"\nset its size to 26\nset its color to {rgb(deck.CODE_THEME["text"])}\nend tell']
    for a, b, c in rs:
        sc.append(f'tell characters {a} thru {b} of object text of t to set its color to {rgb(c)}')
    for i, ch in enumerate(text, 1):
        if ch == LS:
            sc.append(f'set size of character {i} of object text of t to 34')
    sc += [f'set width of t to {w - pad * 2 + 16}', f'set position of t to {{{x + pad - 4}, {y + pad - 8}}}', 'end tell']
    ns.osa("\n".join(sc))
    return h
