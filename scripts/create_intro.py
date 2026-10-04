"""Regenerate the original looping banner. Requires Pillow; optional local tool."""
from pathlib import Path
import math
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path(os.environ.get("PROFILE_FONT_DIR", "C:/Windows/Fonts"))


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_DIR / ("segoeuib.ttf" if bold else "segoeui.ttf")), size)


def main():
    width, height = 1000, 320
    base = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(base)
    for y in range(height):
        t = y / height
        draw.line((0, y, width, y), fill=(int(11 + 5*t), int(18 + 19*t), int(32 + 15*t)))
    for x in range(640, width, 28):
        draw.line((x, 0, x, height), fill=(26, 45, 58))
    for y in range(0, height, 28):
        draw.line((640, y, width, y), fill=(26, 45, 58))
    draw.text((48, 32), "LEARNING IN PUBLIC", font=font(13), fill="#57e2c0")
    draw.text((44, 71), "Hi, I'm YZC0219.", font=font(55, True), fill="#eff7fc")
    draw.text((48, 150), "Turning data into understanding.", font=font(23), fill="#bfd0dc")
    draw.text((48, 196), "DATA ENGINEERING  /  ANALYTICS  /  VISUALIZATION", font=font(12), fill="#8da5b5")
    for x, number, name in [(680, "01", "RAW"), (787, "02", "MODEL"), (894, "03", "INSIGHT")]:
        draw.rounded_rectangle((x, 102, x+70, 174), radius=12, fill="#101d2a", outline="#365160", width=1)
        draw.text((x+22, 119), number, font=font(23, True), fill="#9bb5c5")
        draw.text((x+3, 188), name, font=font(11), fill="#91aab9")
    draw.line((715, 250, 929, 250), fill="#365160", width=2)
    draw.text((48, 272), "BUILD. VERIFY. EXPLAIN.", font=font(13), fill="#57e2c0")
    frames = []
    for frame in range(90):
        image = base.copy()
        d = ImageDraw.Draw(image)
        t = frame / 90
        for x in (754, 861):
            d.line((x, 138, x+29, 138), fill="#365160", width=2)
            px = x + int(29 * ((t*2) % 1))
            d.ellipse((px-3, 135, px+3, 141), fill="#57e2c0")
        points = [(660+i*5, 57-int(12*math.sin(i*.28+t*math.tau))) for i in range(62)]
        d.line(points, fill="#57e2c0", width=2)
        px = 715 + int(214*t)
        d.ellipse((px-4, 246, px+4, 254), fill="#57e2c0")
        pulse = int(110 + 90*(.5+.5*math.sin(t*math.tau)))
        d.ellipse((950, 272, 958, 280), fill=(87, pulse, 192))
        frames.append(image.quantize(colors=96))
    frames[0].save(ROOT / "assets/intro.gif", save_all=True, append_images=frames[1:], duration=70, loop=0, optimize=True, disposal=2)
    (ROOT / "preview").mkdir(exist_ok=True)
    base.save(ROOT / "preview/intro.png")
    print("Created 90-frame looping intro")


if __name__ == "__main__":
    main()
