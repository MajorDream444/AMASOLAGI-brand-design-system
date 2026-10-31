# Card
The 32px-radius `surface` panel with a `border` hairline that holds every value prop, Mob and step on the site.

- Consumer supplies: a container with class `card` (add `card-gold` for gold hover), and its content: typically a 40px `gold-glow` icon tile, a `display-sm` title and `body-mono` copy in `text-secondary`.
- Padding is `spacing-card`. At rest: border only. Hover: `border-light` + `shadow-card-hover` + 2px lift; `card-gold` swaps to `gold-dim` and `shadow-card-gold-hover`.
- Static rendition of `.card` / `.card-gold` in `src/app/globals.css`.
