from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


OUT = Path("assets/animated-showcase-ui-demo.gif")
W, H = 1280, 720
FRAMES = 64

BG = (6, 9, 16)
SURFACE = (14, 20, 33)
SURFACE_2 = (18, 27, 44)
SURFACE_3 = (21, 34, 54)
BORDER = (48, 68, 96)
BORDER_SOFT = (32, 49, 74)
TEXT = (237, 244, 251)
MUTED = (142, 158, 180)
BLUE = (93, 166, 255)
CYAN = (72, 229, 255)
MINT = (64, 236, 174)
VIOLET = (166, 128, 255)
AMBER = (255, 202, 98)
PINK = (255, 118, 150)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        f"C:/Windows/Fonts/{name}.ttf",
        f"C:/Windows/Fonts/{name}.ttc",
        "/System/Library/Fonts/SFNS.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            pass
    return ImageFont.load_default()


FONT_TITLE = font("segoeuib", 44)
FONT_H1 = font("segoeuib", 30)
FONT_H2 = font("segoeuib", 22)
FONT = font("segoeui", 20)
FONT_SM = font("segoeui", 16)
FONT_XS = font("segoeui", 13)
FONT_MONO = font("consola", 16)
FONT_MONO_SM = font("consola", 14)


def ease(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def rounded(draw: ImageDraw.ImageDraw, box, radius: int, fill, outline=None, width: int = 1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw: ImageDraw.ImageDraw, xy, value: str, fill=TEXT, font=FONT, anchor=None):
    draw.text(xy, value, fill=fill, font=font, anchor=anchor)


def pill(draw: ImageDraw.ImageDraw, box, label: str, color, fill=(12, 26, 41)):
    rounded(draw, box, 13, fill, (58, 91, 121), 1)
    text(draw, (box[0] + 14, box[1] + 6), label, color, FONT_XS)


def glow(img: Image.Image, xy, radius: int, color, alpha: int):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x, y = xy
    d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    layer = layer.filter(ImageFilter.GaussianBlur(radius // 2))
    img.alpha_composite(layer)


def draw_base(t: float) -> Image.Image:
    img = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(img)
    glow(img, (270 + 28 * math.sin(t * math.tau), 176), 230, BLUE, 50)
    glow(img, (900 + 20 * math.cos(t * math.tau), 170), 250, VIOLET, 42)
    glow(img, (745, 600), 260, MINT, 28)
    for x in range(-80, W + 120, 80):
        x2 = x + int((t * 80) % 80)
        d.line((x2, 0, x2 - 210, H), fill=(16, 42, 64, 95), width=1)
    for y in range(96, H, 96):
        d.line((0, y, W, y), fill=(16, 33, 51, 78), width=1)
    return img


def draw_window(d: ImageDraw.ImageDraw, box, title: str, live=True):
    x1, y1, x2, y2 = box
    rounded(d, box, 18, SURFACE, BORDER, 1)
    rounded(d, (x1 + 1, y1 + 1, x2 - 1, y1 + 42), 17, (18, 26, 42), None)
    d.line((x1, y1 + 43, x2, y1 + 43), fill=BORDER_SOFT, width=1)
    for i, c in enumerate([PINK, AMBER, MINT]):
        d.ellipse((x1 + 18 + i * 18, y1 + 17, x1 + 29 + i * 18, y1 + 28), fill=c)
    text(d, (x1 + 86, y1 + 13), title, MUTED, FONT_SM)
    if live:
        pill(d, (x2 - 96, y1 + 12, x2 - 20, y1 + 31), "live", MINT)


def draw_arrow(d: ImageDraw.ImageDraw, a, b, color):
    d.line((a, b), fill=color, width=3)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    size = 12
    p1 = (b[0] - size * math.cos(ang - math.pi / 6), b[1] - size * math.sin(ang - math.pi / 6))
    p2 = (b[0] - size * math.cos(ang + math.pi / 6), b[1] - size * math.sin(ang + math.pi / 6))
    d.polygon([b, p1, p2], fill=color)


def draw_readme_frame(i: int) -> Image.Image:
    t = i / (FRAMES - 1)
    img = draw_base(t)
    d = ImageDraw.Draw(img)

    # Header band
    rounded(d, (52, 38, 1228, 130), 24, (9, 15, 26, 225), (29, 46, 68), 1)
    text(d, (84, 55), "Animated Showcase UI Skill", TEXT, FONT_TITLE)
    text(d, (86, 106), "Vague prompt in. Premium animated product-demo direction out.", MUTED, FONT_SM)
    pill(d, (918, 68, 1108, 96), "creative direction", CYAN, (10, 27, 43))
    pill(d, (1120, 68, 1195, 96), "code", MINT, (10, 31, 38))

    # Left creative brief
    rounded(d, (58, 154, 356, 592), 20, (12, 18, 31, 238), BORDER, 1)
    text(d, (84, 184), "Prompt", BLUE, FONT_H2)
    rounded(d, (82, 222, 332, 286), 15, SURFACE_2, (49, 78, 110), 1)
    text(d, (104, 238), "modern cool", TEXT, FONT)
    text(d, (104, 263), "animated visuals", TEXT, FONT)
    text(d, (84, 326), "Skill chooses", VIOLET, FONT_H2)
    choices = [
        ("01", "terminal to product", MINT),
        ("02", "browser-use motion", CYAN),
        ("03", "dashboard proof", AMBER),
    ]
    for idx, (num, label, color) in enumerate(choices):
        y = 366 + idx * 58
        active = ease((t + 0.08 - idx * 0.12) / 0.28)
        rounded(d, (82, y, 332, y + 40), 12, (16, 27, 43), (45, 70, 99), 1)
        d.ellipse((102, y + 12, 116, y + 26), fill=color if active > 0.2 else (58, 72, 91))
        text(d, (128, y + 9), f"{num}  {label}", TEXT if active > 0.2 else MUTED, FONT_SM)

    # Main browser/device surface
    draw_window(d, (392, 154, 905, 594), "showcase canvas")
    rounded(d, (418, 222, 879, 270), 14, (13, 31, 47), (44, 73, 103), 1)
    text(d, (442, 234), "Agent launch dashboard", TEXT, FONT_H2)
    pill(d, (735, 231, 853, 256), "generated", MINT)
    # Chart card
    rounded(d, (418, 298, 628, 484), 16, SURFACE_2, (45, 70, 98), 1)
    text(d, (442, 322), "Run quality", TEXT, FONT_SM)
    d.line((446, 440, 600, 440), fill=(41, 61, 84), width=1)
    d.line((446, 350, 446, 440), fill=(41, 61, 84), width=1)
    points = [(452, 430), (485, 416), (520, 388), (555, 370), (598, 336)]
    upto = max(2, int(ease((t - 0.12) / 0.46) * (len(points) - 1)) + 1)
    for p, q in zip(points[:upto], points[1:upto]):
        d.line((p, q), fill=MINT, width=4)
    for p in points[:upto]:
        d.ellipse((p[0] - 5, p[1] - 5, p[0] + 5, p[1] + 5), fill=MINT)
    # Workflow card
    rounded(d, (656, 298, 879, 484), 16, SURFACE_2, (45, 70, 98), 1)
    text(d, (680, 322), "Motion plan", TEXT, FONT_SM)
    nodes = [(702, 386, "brief", BLUE), (770, 350, "scene", VIOLET), (834, 410, "proof", MINT)]
    for a, b in [(nodes[0], nodes[1]), (nodes[1], nodes[2])]:
        draw_arrow(d, (a[0] + 20, a[1]), (b[0] - 20, b[1]), (67, 101, 137))
    active_nodes = max(1, int(ease((t - 0.06) / 0.56) * 3.2))
    for idx, (x, y, label, color) in enumerate(nodes):
        fill = color if idx < active_nodes else (55, 71, 91)
        d.ellipse((x - 20, y - 20, x + 20, y + 20), fill=(13, 26, 42), outline=fill, width=3)
        text(d, (x, y + 30), label, TEXT if idx < active_nodes else MUTED, FONT_XS, anchor="mm")

    # Terminal overlay, intentionally short lines to avoid overflow
    rounded(d, (436, 506, 862, 570), 14, (7, 14, 24), (56, 82, 112), 1)
    terminal = [
        "$ choose-scene --creative",
        "selected: terminal -> browser -> proof",
        "visual QA: spacing, contrast, motion",
    ]
    reveal = min(len(terminal), int(ease((t - 0.2) / 0.55) * len(terminal)) + 1)
    for idx, line in enumerate(terminal[:reveal]):
        color = MINT if idx == reveal - 1 else (178, 192, 209)
        text(d, (458, 520 + idx * 16), line, color, FONT_MONO_SM)

    # Right QA panel
    rounded(d, (940, 154, 1222, 592), 20, (12, 18, 31, 238), BORDER, 1)
    text(d, (966, 184), "Quality gate", CYAN, FONT_H2)
    qa = [
        ("text fits", MINT),
        ("layout stable", BLUE),
        ("palette balanced", VIOLET),
        ("motion purposeful", AMBER),
        ("visual verified", MINT),
    ]
    for idx, (label, color) in enumerate(qa):
        y = 232 + idx * 58
        active = ease((t + 0.02 - idx * 0.09) / 0.26)
        rounded(d, (966, y, 1192, y + 40), 12, (16, 27, 43), (44, 68, 96), 1)
        if active > 0.15:
            d.line((986, y + 21, 996, y + 30, 1014, y + 12), fill=color, width=4)
        else:
            d.ellipse((988, y + 14, 1008, y + 34), outline=(61, 76, 97), width=2)
        text(d, (1030, y + 9), label, TEXT if active > 0.15 else MUTED, FONT_SM)

    # Cursor and click pulse
    ct = ease((t - 0.25) / 0.58)
    cx = int(716 + 140 * math.sin(ct * math.pi * 0.8))
    cy = int(442 - 88 * ct)
    if 0.18 < t < 0.92:
        if 0.48 < t < 0.58:
            d.ellipse((cx - 24, cy - 24, cx + 24, cy + 24), outline=(92, 219, 255, 180), width=3)
        d.polygon(
            [(cx, cy), (cx, cy + 30), (cx + 9, cy + 22), (cx + 22, cy + 45), (cx + 31, cy + 41), (cx + 18, cy + 19), (cx + 32, cy + 18)],
            fill=(250, 252, 255),
            outline=(29, 43, 62),
        )

    # Bottom proof rail
    rounded(d, (170, 628, 1110, 674), 20, (10, 17, 29, 230), (40, 64, 92), 1)
    steps = ["vague prompt", "creative choice", "animated scene", "quality pass"]
    for idx, label in enumerate(steps):
        x = 220 + idx * 230
        active = t + 0.04 > idx * 0.18
        d.ellipse((x, 644, x + 16, 660), fill=MINT if active else (61, 75, 95))
        text(d, (x + 28, 640), label, TEXT if active else MUTED, FONT_SM)

    return img


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames = []
    for i in range(FRAMES):
        frame = draw_readme_frame(i)
        frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=128))
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=70,
        loop=0,
        optimize=True,
    )
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
