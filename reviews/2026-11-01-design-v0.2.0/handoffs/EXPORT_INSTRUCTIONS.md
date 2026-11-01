# Export instructions and dependencies · v0.2.0 · in_review

## Files
- `AMA Foundations.dc.html` · `AMA Components.dc.html` · `AMA Applications.dc.html` · `AMA Communications.dc.html` — open directly in a browser (require `support.js` alongside).
- Tokens: `tokens/ama-tokens-v0.2.0.css|json`. Supplied tokens kept unchanged in `tokens/supplied-tokens.*`.

## Asset dependencies
| Asset | Status | Used in |
|---|---|---|
| logos/approved/ama-badge.png (1024², RGB, cream ground) | approved reference | foundations, scope page, portrait post |
| logos/approved/ama-monogram.png (788×580) | approved reference | foundations |
| logos/approved/ama-lockup-horizontal.png (1024²) | approved reference | foundations only (margins too large for nav) |
| logos/review/AMA_Badge_512x512_EN_v001_REVIEW.png | in_review cut-out | dark covers, proposal header |
| logos/review/AMA_Logo_monogram_695x527_EN_v001_REVIEW.png | in_review cut-out | LinkedIn banner |
| logos/review/AMA_Badge_{16,32,64}…REVIEW.png | in_review, do not ship | small-size test |
Fonts load from Google Fonts at runtime: Inter, JetBrains Mono, Source Serif 4, IBM Plex Sans. No font files are bundled; obtain licence texts before packaging.

## Artboard sizes (confirm with platform before publishing)
- Slides 1920×1080 · Documents US Letter 816×1056 px @96dpi (A4 794×1123) · LinkedIn banner 1584×396 (profile photo overlap bottom-left, ~440×230 guide) · Square 1080×1080 · Portrait 1080×1350.

## How to export
1. Turn off guides: Communications → Tweaks → "Show guides" off.
2. PNG: ask Claude Design to snapshot each `[data-screen-label]` artboard at 1× or 2×. Never upscale raster logos beyond native size; the 512px badge cut-out must not exceed 512px on the exported artboard.
3. PDF (slides/documents): request a print export; documents are visual proofs, not tagged PDFs.
4. PPTX: request an editable PPTX export of the three slides.
5. Before release, inspect cut-out rims at 100% on dark grounds for cream fringe.

## Importing to GitHub
Claude Design does not sync automatically. Download the project, then follow `handoffs/IMPORT_INSTRUCTIONS.md`: copy into a new branch `review/ama-design-system-v0.2.0`, reconcile `brand/ASSET_REGISTER.csv` rows AMA-0123–AMA-0131 by path, open a draft PR. Do not merge as approval. Nothing in this package goes into `logos/approved/`.
