"""Reduce the console's screenshots in brand/media/console/ to 256 colors.

    python3 brand/tools/quantize_stills.py

video/console/stills.mjs writes them in full color; the README and the guide
carry them as 256-color PNGs, which are far smaller and look the same at the
size they are shown. Needs Pillow (tools/requirements.txt).
"""

from pathlib import Path

from PIL import Image

DIR = Path(__file__).resolve().parent.parent / "media" / "console"


def main() -> None:
    for f in sorted(DIR.glob("*.png")):
        before = f.stat().st_size
        im = Image.open(f).convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        im.save(f, optimize=True)
        print(f"{f.name}: {before} -> {f.stat().st_size} bytes")


if __name__ == "__main__":
    main()
