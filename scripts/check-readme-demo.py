from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageSequence


PATH = Path("assets/animated-showcase-ui-demo.gif")
MIN_SIZE = (1200, 675)
MIN_FRAMES = 48
MAX_BYTES = 4_000_000


def fail(message: str) -> None:
    raise SystemExit(f"README demo check failed: {message}")


def main() -> None:
    if not PATH.exists():
        fail(f"missing {PATH}")

    byte_size = PATH.stat().st_size
    if byte_size > MAX_BYTES:
        fail(f"{PATH} is too large: {byte_size} bytes > {MAX_BYTES}")

    with Image.open(PATH) as img:
        width, height = img.size
        if width < MIN_SIZE[0] or height < MIN_SIZE[1]:
            fail(f"image too small: {width}x{height}; expected at least {MIN_SIZE[0]}x{MIN_SIZE[1]}")

        frame_count = sum(1 for _ in ImageSequence.Iterator(img))
        if frame_count < MIN_FRAMES:
            fail(f"not enough frames: {frame_count}; expected at least {MIN_FRAMES}")

        img.seek(0)
        first = img.convert("RGB")
        sample_points = [
            first.getpixel((width // 2, height // 2)),
            first.getpixel((80, 80)),
            first.getpixel((width - 80, height - 80)),
        ]
        if len(set(sample_points)) == 1:
            fail("first frame appears visually flat")

    print(f"README demo check passed: {PATH} {width}x{height}, {frame_count} frames, {byte_size} bytes")


if __name__ == "__main__":
    main()
