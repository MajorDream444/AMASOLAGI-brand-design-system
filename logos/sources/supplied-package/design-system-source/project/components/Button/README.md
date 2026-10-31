# Button
Pill-shaped uppercase mono buttons: `btn-primary` (gold fill) for the one main action, `btn-secondary` (hairline outline) for everything beside it.

- Consumer supplies: an `<a>` or `<button>` with class `btn-primary` or `btn-secondary`, and a short uppercase-styled label ("Start a Conversation", "See how it works").
- One `btn-primary` per view region; pair it with a `btn-secondary` to its right.
- Text on the primary is always `bg` ink. Hover lifts 1px; primary shifts to `gold-light` with `shadow-btn-primary-hover`.
- The Nav's compact CTA overrides to 11px with 10px × 20px padding.
- Static rendition of `.btn-primary` / `.btn-secondary` in `src/app/globals.css`.
