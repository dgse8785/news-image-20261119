#!/usr/bin/env python3
"""Build entry.png: a 1024x1024 news poster summing up 19 November 2026.

Deterministic: pure Pillow drawing, no randomness, no network, no clock.
Run: python3 build_poster.py  (writes entry.png next to this script)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W = H = 1024
BG = (10, 25, 41)          # dark navy
RED = (217, 38, 56)
GOLD = (255, 201, 77)
WHITE = (255, 255, 255)
LEAD_FILL = (19, 42, 66)
CARD_FILL = (16, 34, 54)
LEAD_SUB = (196, 208, 220)
CARD_SUB = (158, 172, 188)
DIVIDER = (70, 92, 118)
MARGIN = 46
RIGHT = W - MARGIN


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap using real glyph widths."""
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_width, leading):
    """Draw wrapped text, return y just past the block."""
    for line in wrap(draw, text, fnt, max_width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def panel(draw, box, fill, bar_color, radius=14, bar_w=8):
    draw.rounded_rectangle(box, radius=radius, fill=fill)
    x0, y0, x1, y1 = box
    draw.rounded_rectangle([x0, y0, x0 + bar_w, y1], radius=radius, fill=bar_color)
    draw.rectangle([x0 + bar_w - radius, y0, x0 + bar_w, y1], fill=bar_color)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Red top bar
    d.rectangle([0, 0, W, 16], fill=RED)

    # Masthead
    f_title = font(BOLD, 56)
    f_date = font(BOLD, 27)
    d.text((MARGIN, 42), "THE WORLD IN ONE IMAGE", font=f_title, fill=WHITE)
    d.text((MARGIN, 116), "THURSDAY \u00b7 19 NOVEMBER 2026", font=f_date, fill=GOLD)
    d.line([MARGIN, 162, RIGHT, 162], fill=DIVIDER, width=2)

    # ---- Lead story panel: Shenzhen trilateral summit ----
    lead = [MARGIN, 180, RIGHT, 418]
    panel(d, lead, LEAD_FILL, GOLD)
    tx = MARGIN + 36
    tw = RIGHT - 28 - tx
    y = 180 + 24
    d.text((tx, y), "LEAD STORY \u2014 SHENZHEN, CHINA", font=font(BOLD, 22), fill=RED)
    y += 36
    y = text_block(
        d, tx, y,
        "Trump, Xi & Putin Hold First-Ever Trilateral Summit",
        font(BOLD, 43), WHITE, tw, 54,
    )
    y += 6
    text_block(
        d, tx, y,
        "Nuclear arms and two wars on the table as the three leaders meet "
        "face to face. Kyiv urges the trio to press Putin to end the war.",
        font(REG, 24), LEAD_SUB, tw, 31,
    )

    # ---- 2x2 card grid ----
    cards = [
        ("MIDDLE EAST", (255, 138, 61),
         "Tankers Ablaze After Mine Strikes Near Hormuz",
         "Gulf states repel Iranian drone attacks; US reissues security warnings"),
        ("WORLD COURT", (62, 198, 184),
         "World Court Rules on Myanmar Rohingya Genocide Case",
         "A historic verdict day at The Hague"),
        ("GAMING", (183, 140, 255),
         "GTA VI Launches Worldwide to Rave Reviews",
         "Gamers return to Vice City after a 13-year wait"),
        ("ART MARKET", GOLD,
         "Van Gogh Sells for Record $190.4 Million",
         "Record price after a row over its Nazi-era past"),
    ]
    gap = 18
    card_w = (RIGHT - MARGIN - gap) // 2
    card_h = 178
    grid_y = 438
    f_tag = font(BOLD, 20)
    f_head = font(BOLD, 26)
    f_sub = font(REG, 20)
    for i, (tag, color, head, sub) in enumerate(cards):
        cx = MARGIN + (i % 2) * (card_w + gap)
        cy = grid_y + (i // 2) * (card_h + gap)
        panel(d, [cx, cy, cx + card_w, cy + card_h], CARD_FILL, color)
        tx = cx + 30
        tw = card_w - 30 - 16
        y = cy + 16
        d.text((tx, y), tag, font=f_tag, fill=color)
        y += 30
        y = text_block(d, tx, y, head, f_head, WHITE, tw, 32)
        y += 4
        text_block(d, tx, y, sub, f_sub, CARD_SUB, tw, 25)

    # ---- Space card (full width) ----
    sy = grid_y + 2 * card_h + gap + 20  # 842
    panel(d, [MARGIN, sy, RIGHT, sy + 104], CARD_FILL, (94, 168, 255))
    tx = MARGIN + 36
    tw = RIGHT - 28 - tx
    y = sy + 13
    d.text((tx, y), "SPACE", font=font(BOLD, 20), fill=(94, 168, 255))
    d.text((tx + 96, y - 4), "Voyager 1 Is Now One Light-Day From Earth",
           font=font(BOLD, 27), fill=WHITE)
    y += 34
    text_block(
        d, tx, y,
        "NASA's farthest probe, launched in 1977, crosses a new milestone",
        font(REG, 20), CARD_SUB, tw, 25,
    )

    # ---- ALSO TODAY strip ----
    by = sy + 104 + 18
    text_block(
        d, MARGIN, by,
        "ALSO TODAY:  Pew: Muslims to outnumber Christians by 2035  \u00b7  "
        "M5.7 quake hits Kumamoto, Japan  \u00b7  Anthropic eyes a $1.4tn debut",
        font(REG, 20), CARD_SUB, RIGHT - MARGIN, 26,
    )

    img.save(OUT, format="PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
