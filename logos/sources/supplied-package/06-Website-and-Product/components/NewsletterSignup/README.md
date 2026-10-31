# NewsletterSignup
The footer opt-in form: gold eyebrow, a plain-language explainer, email field, explicit consent checkbox and a secondary Subscribe button.

- Consumer supplies: the submit handler (POSTs `{email, consent, website}` to `/api/subscribe`), and a polite live region for the status message.
- Consent is required and unticked by default; the copy states the emails are occasional and unsubscribable. Keep a hidden honeypot `website` field.
- Input: `surface` fill, `border` hairline, 10px radius, 12px × 14px padding, `text` value. Labels in `label-mono`, `text-dim`.
- Max width 360px. Static rendition of `src/components/NewsletterSignup.tsx`.
