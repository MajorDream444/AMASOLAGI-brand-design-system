# Brief · AMA badge and monogram clean vector redraw
Version 1.0 · 31 Oct 2026 · Owner: Major Dream Williams (final approver) · For: external designer and internal (Claude) use

## Goal
Produce faithful, editable vector masters of the approved AMA badge and standalone monogram, plus a flat master and compact family, so the identity can be used at small sizes, in one colour, in print and on dark grounds. This is a redraw, not a redesign.

## Reference (do not modify)
- `logos/approved/ama-badge.png` (1024×1024, RGB, cream ground)
- `logos/approved/ama-monogram.png` (788×580)
- `logos/approved/ama-lockup-horizontal.png` (1024×1024)
- Founder originals in `logos/sources/supplied-package/02-Logo-Masters/founder-originals/`
- Known-faulty attempt for comparison only: v002 vector (see `uploads/check_side-by-side_v002.png`)

## What to preserve
- Three interlocking triangular forms; the centre apex rises above the two outer peaks.
- Sculptural ribbon folds: each stroke turns over itself at the inner corners. Overlap order must match the reference at every crossing.
- Node fields: diamond cluster in the centre, two triangular clusters left and right. Even rhythm; dot sizes graded largest at the centre line. Count and positions follow the reference; do not add, remove or regularise into a grid.
- Badge: dark field, double gold rim with a thin inner shadow line.
- Proportions: overall monogram width to height and the gap between monogram base and rim as in the reference.

## Faults to avoid (seen in v002)
- Torn or jagged edges at the lower inner folds of the left and right triangles.
- Broken overlap at the centre base, where the middle strokes cross.
- Highlight shapes cut through ribbon edges.
- Rim flattened to a single ring; lost inner shadow line.
- Embedded raster inside an SVG. Deliverables must contain paths only.

## Deliverables (all start as in_review)
1. **Dimensional master** (badge, monogram): layered vector with gradients reproducing the metallic look. AI + SVG. Named layers: rim-outer, rim-inner, field, ribbon-{left,centre,right}, folds, nodes, highlights.
2. **Flat master**: same geometry, solid fills, no gradients. Two-tone (gold #C9A227 on #0A0A0A) and one-colour (black, white, gold).
3. **Compact mark** for 16–48px: proposed simplification (fewer, larger nodes or nodes removed), shown beside the full mark at 16, 24, 32, 48 px. Clearly labelled as a proposal; founder decides.
4. **Dark-ground lockup** proposal: badge + "AMA / SOLUTIONS" legible on #080808. Wordmark construction must be documented (font name, version, licence) or drawn as custom outlines with source notes.
5. **Comparison sheet**: reference vs redraw at 1024px, 256px, 64px, plus 4× crops of every fold and crossing.
6. **Exports**: SVG (paths only, viewBox set, no `<image>`), PDF, PNG at 16/32/48/64/128/180/192/512/1024, ICO.

## Technical requirements
- SVG: no embedded rasters, no live text, no filters for the flat master. Validate by searching for `<image` and `<text` (must be zero).
- Even node spacing checked with an overlay grid; tolerances noted.
- Colour values for the flat master use website tokens; print colours (CMYK/Pantone/foil) are out of scope until a vendor proof.
- File naming: `AMA_{Badge|Monogram|Lockup}_{variant}_{size}_EN_v003_REVIEW.{ext}`.

## Process
1. Designer delivers comparison sheet first; founder reviews geometry before any family work.
2. On acceptance, flat and compact variants follow.
3. Every file is registered in `brand/ASSET_REGISTER.csv` as in_review. Only Major Dream Williams moves files to `logos/approved/`, with date and evidence recorded.

## Rights
Designer confirms original work and assigns rights in the redraw to AMA Solutions Inc. (counsel to supply the agreement). No font outlines without a verified licence.

## For internal (Claude) use
Claude can build the comparison sheet, overlay grids and export checks, and can test small-size candidates, but should not claim a traced or AI-generated path is a faithful master. Any internally produced geometry is a study, labelled in_review, and goes to the external designer as reference.
