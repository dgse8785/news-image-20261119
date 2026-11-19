#!/usr/bin/env python3
"""Entry point for news-image-20261119.

Copies the bundled poster (entry.png, next to this file) to
/output/entry.png. Stdlib only, no network, deterministic output:
two runs produce byte-identical files.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)


if __name__ == "__main__":
    main()
