# Start here

## What exists (31 October 2026)

- **Brand book** — `01-Strategy-and-Voice/brand-book.md`: content fundamentals, identity, color, typography, spacing, imagery, motion, departments, accessibility.
- **Brand handoff** — `01-Strategy-and-Voice/AMA_SOLUTIONS_CORPORATE_BRAND_HANDOFF.md` (v1.0, 29 October 2026).
- **Governance** — `governance.md`: statuses, naming, approval gates, owner inputs, checklist.
- **Logos** — three approved rasters (badge 1024×1024, monogram 788×580, horizontal lockup) plus the five founder-supplied originals. Interim website SVG mark.
- **Tokens** — 26 colors (website + provisional brand + status), 4 spacing, 5 radii, 3 shadows, website and proposed document type styles. `tokens.css` is generated from `tokens.json`.
- **Website components** — Badge, Button, Card, Cover, Nav, NewsletterSignup, Wordmark: guidelines and static HTML previews styled by `bundle.css`. The previews are fragments made for the Design System viewer; to view one standalone, load `03-Color-and-Type/tokens.css` and `06-Website-and-Product/components/bundle.css` first.
- **Imagery** — HAMAL campus concept render and the twelve Mob images from the website (label the campus as concept).

## What is still missing

1. **Vector master of the badge, monogram and lockup** (SVG + print PDF), approved by the founder. Blocks favicons, one-color, small sizes, embossing, print and the lapel pin.
2. Transparent cut-outs of the badge for dark grounds.
3. Color values sampled from the badge (HEX, RGB, CMYK; Pantone/metallic after proofing).
4. Font approval (proposed: Source Serif 4, IBM Plex Sans, JetBrains Mono).
5. Templates: letterhead, cards, email signature, memo, briefing, proposal/SOW, invoice and receipt, forms, onboarding, delivery reports, logs, contract shells.
6. Social and deck templates; icon family; pin production sheet.
7. Owner inputs listed in `governance.md` (legal entity, addresses, payment details, titles, catalog).

## Origin of each file

`design-system-source/project/` is the untouched export. The numbered folders reorganize the same files into the library structure from the brand handoff; the only edits are relative image paths in two component previews and the generated `tokens.css`.
