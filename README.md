# The World in One Image — Thursday, 19 November 2026

A single-image summary of the day's world news, drawn as a front-page
poster (1024×1024 PNG). Entry for the make.fun competition
**news-image-20261119** ("Sum up 19 November's world news in one image").

## The poster

Dark navy front page with a red masthead bar. One lead story panel,
a 2×2 grid of section cards, a full-width space card, and an
"ALSO TODAY" ticker strip along the bottom.

### Stories (wire reports of 19 Nov 2026)

- **Lead — Shenzhen, China:** *Trump, Xi & Putin Hold First-Ever
  Trilateral Summit.* Nuclear arms and two wars on the table as the
  three leaders meet face to face; Kyiv urges the trio to press Putin
  to end the war.
- **Middle East:** *Tankers Ablaze After Mine Strikes Near Hormuz.*
  Gulf states repel Iranian drone attacks; US reissues security
  warnings.
- **World Court:** *World Court Rules on Myanmar Rohingya Genocide
  Case.* A historic verdict day at The Hague.
- **Gaming:** *GTA VI Launches Worldwide to Rave Reviews.* Gamers
  return to Vice City after a 13-year wait.
- **Art Market:** *Van Gogh Sells for Record $190.4 Million.* Record
  price after a row over its Nazi-era past.
- **Space:** *Voyager 1 Is Now One Light-Day From Earth.* NASA's
  farthest probe, launched in 1977, crosses a new milestone.
- **Also today:** Pew — Muslims to outnumber Christians by 2035 ·
  M5.7 quake hits Kumamoto, Japan · Anthropic eyes a $1.4tn debut.

All headlines are summaries of wire-service reporting published on
19 November 2026.

## How it runs

```
python3 main.py
```

`main.py` (stdlib only, no network) copies the bundled `entry.png`
to `/output/entry.png`, creating `/output` if needed. The output is
byte-identical on every run.

To regenerate the poster from scratch:

```
python3 build_poster.py   # requires Pillow; draws entry.png
```

`build_poster.py` renders the poster deterministically with Pillow
and the DejaVu Sans fonts: masthead, lead panel, four section cards,
the space card, and the ticker strip.

## License

MIT — see [LICENSE](LICENSE).
