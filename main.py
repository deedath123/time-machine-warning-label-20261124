"""Time-machine warning label entry for make.fun.

Writes the locked entry line to <output>/entry.txt, where <output> comes
from MAKEFUN_OUTPUT_DIR with /output as the fallback. No trailing newline.

Verified numbers: 96 chars / 96 bytes, one line.
"""

import os

LINE = "WARNING: Do not step on butterflies. One traveller did, and now his grandson is a parking meter."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
