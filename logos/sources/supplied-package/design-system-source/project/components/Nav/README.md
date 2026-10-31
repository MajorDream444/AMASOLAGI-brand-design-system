# Nav
Fixed 64px top bar: wordmark left, pill links center, compact gold CTA right, over a blurred 85% `bg` scrim with a `border` bottom edge.

- Consumer supplies: the link list (How It Works, The Mobs, Foundry OS, Founder, Partner), the current path for the active state, and the CTA target (/contact).
- Links: `nav-link` style in `text-secondary`; active link `gold-light`, 600, on `gold-glow-sm` with a 20% gold border, `radius-pill`.
- Under 768px the links collapse into a hamburger (`radius-sm` outline button) that opens a full-width drawer with 13px links and a full-width primary CTA.
- Static rendition of `src/components/Nav.tsx` (desktop state).
