# Component specifications · v0.2.0 · in_review

Tokens: `tokens/ama-tokens-v0.2.0.css`. Live reference: `AMA Components.dc.html`. All states use `--ease` with 150ms (controls) / 250ms (cards). Reduced motion collapses durations and removes lifts.

## Global rules
- Focus: 2px solid `--gold`, 3px offset, on every interactive element. Never removed.
- Min control height 44px; touch targets 44×44.
- Status = icon/shape + word (+ optional owner/timestamp). Shapes: ● complete, ◐ in progress, ○ awaiting, ▲ warning/to confirm, ■ blocked/error, ◇ draft.
- One primary button per view. Labels are verbs ("Send inquiry", "Review and approve").

## Buttons
| Variant | Default | Hover | Active | Disabled | Loading |
|---|---|---|---|---|---|
| Primary | bg gold, ink #080808 | gold-light, −1px, glow | gold-dim, white ink | surface-3, text-dim, dashed border-light | spinner + present-tense verb, `role=status` |
| Secondary | 1px text-dim border, white | border text-secondary, surface-2 | surface-3 | dashed border-light | spinner |
| Text | gold-light underline | white | gold | text-dim | n/a |
| Destructive | 1px danger-ink border + text | 12% danger wash | 20% wash | dashed | spinner; always behind a confirm dialog |
Type: JetBrains Mono 13/600, 0.04em, uppercase. Radius pill. Padding 12×24.

## Form fields
Anatomy: label (13/600, always visible) → help text (12, text-secondary, `aria-describedby`) → control (bg #080808, 1px `--input-border`, radius 8, 44px) → error (12, danger-ink, ■ prefix).
States: hover border text-secondary · focus border gold + focus ring · error 2px danger-ink + `aria-invalid` · disabled dashed border-light, surface bg · success border success-ink + "● Verified".
Error summary: top of form, `role=alert`, receives focus on submit, links to each field.
Receipt: `role=status`, reference ID, what happens next, explicitly what has NOT happened (no booking, no payment).
Checkbox/radio: 20px, `accent-color: gold`, whole row is the label, row ≥44px.

## Navigation
Desktop: 64px bar, name in Inter 600 15px, pill links (mono 12), active = gold-light on gold-glow-sm + 20% gold border + `aria-current=page`. One primary CTA.
Mobile (<720): 44px menu button with `aria-expanded`/`aria-controls`; panel moves focus to first link; Esc closes and returns focus to the button.
Tabs: `role=tablist/tab/tabpanel`, roving tabindex, ←/→ move, 2px gold underline on selected.
Breadcrumbs: `nav[aria-label=Breadcrumb] > ol`, current item `aria-current=page`.

## Cards, tables, lists, accordions, dialogs
Card: surface, 1px border, radius 32, padding 24; hover border gold-dim + gold shadow + 2px lift (interactive cards only).
Table: caption, `th[scope]`, header 11px caps text-secondary, rows 1px border. Horizontal scroll container on mobile.
Accordion: heading > button with `aria-expanded`/`aria-controls`, +/− glyph, 48px row.
Dialog: `role=dialog aria-modal`, labelled + described, focus to the safe action, Esc and backdrop close, focus returns to trigger.

## Alerts and notifications
Info (border-light), success (success-ink), warning (dashed warning-ink), error (danger-ink). 6% tinted wash, radius 16, icon column 24px. Errors use `role=alert`; others `role=status`. Toast: surface-2, shadow, dismiss button 32px with label.

## Progress
Bar: 8px, surface-3 track, gold fill, `role=progressbar` with value text ("4 of 7"). Stepper: ✓ filled gold, current = 2px gold ring + `aria-current=step`, future = dashed.

## Empty / loading / success / error
Empty: dashed border, ○, one sentence, one next action. Loading: skeleton bars pulsing (disabled under reduced motion) + text "Loading…", `aria-busy`. Success: ●, what was recorded, who, when (with timezone). Error: ■, reassurance ("nothing was charged / your work is saved"), retry action.

## Business components
**Product card** fields: kind label · version/status · name · practical outcome · For · You get (deliverables+format) · You bring (inputs) · Delivery/access · Support/eligibility · price or "Price to confirm" · availability · CTA. No live checkout CTA until an integration is verified; show "Checkout not connected".
**Bundle card**: gold-dim border; named included IDs; overlap disclosure; bundle price shown only when confirmed.
**Consulting journey**: Inquiry → Fit review → Scoped proposal → Acceptance → Payment → Confirmed booking → Onboarding. Each stage its own state (done/now/next). Copy never merges stages.
**Slot picker**: duration, format, explicit timezone with change link, `role=radiogroup`, taken slots struck-through + dashed + `aria-disabled`; selected slot shows "Held · not confirmed" with hold window.
**Next action (workspace)**: 2px gold border, title verb, owner, due date, what it blocks, primary + secondary action. Exactly one per workspace.
