# Interactive Advisory Storefront — Research Brief (Draft)

Oct 28, 2026 · @Major Dream Williams

**Status: research draft for Major and Claude Code — not reviewed, not client-ready.** No code was changed, nothing was deployed, purchased or configured, and no test described here has been run. Every latency, cost and conversion figure is a vendor claim or a hypothesis until the proof-of-concept test plan below is executed.

Inspected: `amasolagi-site` main at commit `4ee9f8b` (2026-09-25 merge, Next.js 16.3.6, no API routes, contact form not connected), the live amasolagi.com homepage, `MajorDream444/open-notebook` at commit `d39af07` (v1.9.0, MIT, with Esperanto 2.22.0 and podcast-creator 0.13.1 packages unpacked), and the commerce handover dated 28 Oct 2026.

**Revision 2 (28 Oct 2026, after Major's review).** The build foundation is Major's local `697a62a` snapshot, where the storefront already exists. That commit is not on GitHub and this desk has **not inspected it**; statements about current site files below describe older `main` and must be re-checked against `697a62a`. This revision makes providers configurable, shortens the voice script to 35–60 words, separates availability from relevance, replaces blanket declines of build requests with a clarifying question, hardens voice authorization, and adds Major's mindset pack, the Google data flow and the one-shot build prompt.

## Executive recommendation

**Build a text-first advisor inside the existing storefront, with Major's cloned voice as a click-to-play extra, and keep Open Notebook behind the counter for research and paid production.** The smallest workable version is one advisor component, two server routes, the storefront's own catalog, a small approved collection of how Major thinks, and configurable model and voice providers. Current candidates are a fast Claude model and an ElevenLabs Instant Voice Clone; their names, prices and retirement dates are re-verified at build time and do not shape the design.

**What the visitor gets:** one useful observation before any selling — a 35–60-word insight framed the way Major frames problems; one best-fit AMA product or consulting session with a one-line reason and its honest availability state (purchasable, opening soon, or by inquiry); at most one follow-up question; and a "Hear it from Major" button that speaks the same words in his disclosed AI voice.

&#91;embedded content: advisor request flow · 2 routes, 2 outside services\]

The browser never holds a key, prices and links come only from the catalog, and the voice route speaks only text the server produced.

**Why this path:**

- **It reuses what exists.** The `697a62a` storefront already has the brand, catalog and product pages; the advisor adds a component and two route handlers, not a second site.
- **The mindset pack makes it sound like AMA before the voice plays.** Product descriptions say what AMA sells; Major's approved framing, questions, accepted and rejected advice, and Map → Poke → Scale → Pressure-Proof teach how AMA thinks.
- **Open Notebook is the wrong engine for visitors.** It is a single-password, unrate-limited research app whose podcast pipeline runs minutes-long jobs. It is the right tool for research and paid deliverables in the same cloned voice — with client material kept in private per-client workspaces, never a shared notebook.
- **Voice is cheap if gated.** At list prices checked on 28 Oct 2026 a voiced preview costs about $0.01 and a text preview well under $0.001. Audio on click, per-IP limits, a daily cap and expiring single-use audio tokens bound cost and misuse.
- **It protects Major's time.** Standard problems route to asynchronous products; decision and architecture problems route to his paid sessions ($350 / $1,250); only out-of-scope or regulated requests get no product.

**Material tradeoffs:**

| Choice | Gain | Cost or risk |
| --- | --- | --- |
| Instant clone now, Professional later | Ready in a day from 1–2 min of audio | Lower likeness than a 30-minute Professional clone; settled by the listening test |
| Catalog and examples in the prompt, no live retrieval | Fast, simple, predictable | Insights draw on general knowledge plus AMA's catalog, not Major's private notes |
| Audio on click, not autoplay | Accessible, cheap, no surprise sound | Fewer visitors hear the voice |
| One follow-up question maximum | Short path to a recommendation | Some visitors get a consulting route instead of a perfect product match |
| Decline regulated or guarantee requests | Trust and liability protection | Some leads are turned away from the storefront |

**Smallest useful test:** before touching the site, clone the voice, run the ten journeys through the routing prompt three times each, have Major approve the insights and the voice blind, and time 20 calls. Pass = 9/10 correct routes with no invented prices, Major's sign-off on words and voice, and latency recorded. If voice fails, ship text-only; routing is the commercial core.

**Owner actions, in parallel with the interface build:** supply and approve the mindset pack; approve the voice and model provider accounts and a rate-limit store; sign a short voice-use authorization; confirm disclosure wording, what preview data AMA keeps, and the Google destinations for inquiries and orders. The interface can be built and tested with providers switched off. Every latency, quality and demand claim stays a hypothesis until the test runs.

## Capability and evidence matrix

Nothing in this matrix has been tested by AMA; "documented" means a primary source or the inspected code states it. All sources accessed 28 Oct 2026.

| Capability | Status | Evidence | Remaining uncertainty |
| --- | --- | --- | --- |
| Site can host server routes for the advisor | Documented | Next.js route handlers support POST and streamed `Response` bodies ([Next.js route.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)); repo has no API routes yet | Installed Next 16.3.6 docs in `node_modules` not yet read (AGENTS.md requires it) |
| Function time limit is sufficient | Documented | Vercel default 300 s with Fluid compute; set via `maxDuration` ([Vercel duration](https://vercel.com/docs/functions/configuring-functions/duration)) | Which Vercel plan and project the site deploys to is unverified |
| Structured JSON routing output | Documented | Claude API `output_config.format` with JSON schema, GA, Haiku 5.5 supported ([structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)) | Routing accuracy is a hypothesis until the 10-journey eval runs |
| Text cost per preview ≈ $0.0005 | Calculated | Haiku 5.5 $0.10 / $0.50 per MTok under 100K-token prompts ([Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing)) | Token counts are estimates |
| Self-serve clone of Major's voice | Documented | Instant clone needs ≥10 s total audio, 1–2 min recommended, consent checkbox ([ElevenLabs IVC](https://elevenlabs.io/docs/product-guides/voices/voice-cloning/instant-voice-cloning)); Starter $6/mo includes clone and commercial licence ([ElevenLabs pricing](https://elevenlabs.io/pricing)) | Clone quality for Major's voice untested; full use-policy text did not load |
| Streaming TTS | Documented | `POST /v1/text-to-speech/{voice_id}/stream` ([ElevenLabs stream](https://elevenlabs.io/docs/api-reference/text-to-speech/stream)) | Real first-audio time from Vercel region to Bali/US/EU untested |
| TTS cost per 60-word clip ≈ $0.015 | Calculated | Flash $0.04, Multilingual v2/v3 $0.08 per 1K characters, same on every plan ([ElevenLabs API pricing](https://elevenlabs.io/pricing/api)) | Character count per clip is an estimate |
| Commercial use of cloned output | Documented | Paid users may use output commercially; own or authorised voice only ([ElevenLabs terms](https://elevenlabs.io/terms-of-use), updated 9 Oct 2026) | ElevenLabs takes a broad licence to uploaded content (§4(d)); Major should read it |
| Alternative provider | Documented | Cartesia Pro $5/mo with instant clone; under-90 ms claim ([Cartesia pricing](https://cartesia.ai/pricing), [Sonic](https://cartesia.ai/sonic)) | Cartesia full terms did not load |
| OpenAI / Google custom voices | Documented as gated | Sales-only custom voices and 6 Jan 2027 shutdown of current TTS models ([OpenAI TTS](https://developers.openai.com/api/docs/guides/text-to-speech), [OpenAI custom voices](https://developers.openai.com/api/docs/guides/custom-voices)); allow-list ([Google ICV](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice)) | Not pursued |
| AI-voice disclosure duty | Documented | OpenAI terms require disclosure; EU Art. 50 transparency obligations apply from 2 Aug 2026 ([European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content)); FTC has no general disclosure rule but enforces impersonation ([FTC](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/04/approaches-address-ai-enabled-voice-cloning)) | Official EUR-Lex text not read; not legal advice |
| Per-IP rate limiting | Documented | `@upstash/ratelimit` sliding window with IP identifier ([Upstash](https://upstash.com/docs/redis/sdks/ratelimit-ts/gettingstarted)) | Requires a new Redis account (owner decision) |
| Open Notebook in the live path | Documented as unsuitable | Single shared password, CORS `*` default, no rate limiting, podcast jobs of 3–20 segments (inspected code, v1.9.0) | — |
| Open Notebook reuses the cloned voice | Documented in code, untested | Esperanto ElevenLabs provider passes any `voice_id` to the non-streaming endpoint | Must test with Major's actual clone ID |
| Visitors want an AI-voice reply | **Hypothesis** | No visitor data exists; the live site has no advisor | Measured only by the PoC funnel |
| Insight drives product purchase | **Hypothesis** | No data | Measured only after Payment Links are live |

## A. Open Notebook: useful for fulfillment, wrong for the live request path

Open Notebook v1.9.0 can do most of the *back-office* work (sources, RAG Q&A, transformations, long-form podcasts with a cloned voice ID), but it is a single-tenant, password-protected research app with no rate limiting and no streaming TTS. Do not expose it to website visitors in v1.

| Capability | What the code shows | Evidence level | Fit for 15–30 s visitor preview |
| --- | --- | --- | --- |
| Research / Q&A | `POST /search/ask/simple` runs a 3-model graph (strategy, answer, final answer) over embedded notebook sources; needs an embedding model | Documented in code | Poor: several sequential LLM calls; latency unmeasured (hypothesis: too slow) |
| Transformations | `POST /transformations/execute` = one prompt-template LLM call on `input_text`, synchronous | Documented in code | Possible, but a direct LLM call from the site does the same with less infrastructure |
| Podcast generation | `POST /podcasts/generate` queues a background job: outline → transcript → per-segment TTS → merged file; `num_segments` must be 3–20; docs cite 10+ min for a 30-min episode | Documented in code and docs | No: job-based, multi-segment, minutes not seconds |
| Speaker profiles | 1–4 speakers, each needs `name`, `voice_id`, `backstory`, `personality`; `voice_model` points at a registered TTS model | Documented in code | Yes for fulfillment: a profile can hold Major's cloned `voice_id` |
| Custom voice provider | Esperanto 2.22.0 TTS providers: ElevenLabs, OpenAI, OpenAI-compatible, Google, Vertex, Azure, Deepgram, Mistral, xAI. ElevenLabs passes any `voice_id` to `/v1/text-to-speech/{voice}` (default model `eleven_multilingual_v2`, mp3 44.1 kHz/128 kbps) | Documented in code; **untested** with a cloned ID | Uses the non-streaming endpoint, so no early playback |
| Voice cloning | None: no endpoint creates or verifies a voice; that happens in the provider's console | Absent | Gap |
| Auth / exposure | One shared bearer password for every API route; CORS defaults to `*` (startup warning); security review lists rate limiting as not implemented | Documented in code and docs | Must stay private |
| Licence | MIT, © 2024 Luis Novo; fork remote is `MajorDream444/open-notebook` | Documented | Internal use is fine; keep the MIT notice with any redistributed copy |

**Missing for this experience:** a public, rate-limited endpoint; a short single-voice clip mode; streaming audio; caching of repeated answers; a product catalog and routing schema; consent and disclosure records for the cloned voice; usage logging per visitor.

**Role it should play:** (1) the internal notebook where AMA keeps the approved routing rules, product scopes and example answers that feed the website prompt; (2) the production tool for paid deliverables such as Walk In Ready's listening overview, using a speaker profile with Major's cloned voice once that is verified. One small inconsistency to note for whoever operates it: the auth middleware docstring says a default password is always active, while the code skips auth when `OPEN_NOTEBOOK_PASSWORD` is unset — confirm the password is set on any reachable instance.

## B. Preview experience: text first, voice on request

Show the text insight and product card first; generate Major's voice only when the visitor presses play. That keeps the page useful when audio fails and spends TTS money only on engaged visitors.

**Providers are configuration, not design.** The advisor calls a small `ModelProvider` and `VoiceProvider` interface selected by environment variables, so a model or vendor can change without touching the interface. Current candidate for voice: an ElevenLabs Instant Voice Clone with a low-latency model over HTTP streaming, because on 28 Oct 2026 it was the only checked option combining a self-serve clone, commercial use on an entry plan, a stream endpoint and a voice ID Open Notebook can reuse. Cartesia is the alternate. Model names, prices and retirement dates in this brief (for example OpenAI's stated 6 Jan 2027 shutdown of its current TTS models) must be re-checked against current documentation at build time.

| Decision | Recommendation | Basis |
| --- | --- | --- |
| Clone type | Instant clone from 1–2 min of clean audio first; upgrade to Professional (30+ min, spoken verification, Creator $22/mo) only if the listening test fails | ElevenLabs docs; quality need is a hypothesis |
| Clip length | 35–60 words, the same words shown on screen; measure each recording and trim the target if clips run past 30 s | Brief requirement |
| Format | `mp3_44100_128` streamed to an `<audio>` element | ElevenLabs output formats |
| Disclosure | Next to the player: "AI-generated voice of Major Dream Williams, used with his permission. Text above is the full transcript." | OpenAI and Mistral terms require AI-voice disclosure; EU AI Act Art. 50 transparency obligations apply from 2 Aug 2026 |
| Consent record | Major signs a short internal voice-use authorization: scope (website previews, named deliverables), revocation, who may trigger generation | ElevenLabs terms §4(b): own or authorised voice only |

**Visual treatment.** Reuse the site's dark surface, gold accent and dot-grid language. While text streams, show a slow gold pulse on the AMA mark; while audio plays, draw a simple gold level meter from the Web Audio `AnalyserNode`. Check `prefers-reduced-motion` in JavaScript as well as CSS: the existing `HeroCanvas` animates through `requestAnimationFrame`, which the CSS reduced-motion rule does not stop, so new animation must not copy that pattern. No photo or video avatar in v1.

**Latency targets (hypotheses to measure, not claims):**

| Step | Target p50 | Target p95 |
| --- | --- | --- |
| Insight text, first characters on screen | ≤ 1.5 s | ≤ 3 s |
| Insight and product card complete | ≤ 4 s | ≤ 8 s |
| Press play → first audio | ≤ 1.5 s | ≤ 3 s |

Vendor claims for context only: ElevenLabs Flash about 75 ms model time and 100–150 ms time-to-first-byte; Vercel functions default to a 300 s limit, far above this workload.

**Cost per preview (calculated from list prices on 28 Oct 2026, not measured):** a 50-word clip is about 300 characters, so a voice model at $0.04 per 1K characters costs about $0.012. A small model at $0.10 / $0.50 per million input/output tokens costs about $0.0005 for a \~3,000-token prompt and \~300-token reply; the mindset pack may double the prompt. Audio dominates either way.

**Cost and abuse controls:**

- Per-IP limits (for example `@upstash/ratelimit`): 5 previews per hour as a starting value to tune.
- A global daily audio cap (for example 200 clips ≈ $2.40/day) and an `ADVISOR_AUDIO_ENABLED` kill switch; above the cap the player hides and text continues.
- Input capped at 1,000 characters; output tokens capped; replies that fail schema validation are discarded.
- Pre-rendered clips for the example journeys, served as static files.

**Voice misuse controls — speaking only model-generated text is not enough on its own:**

- **Validate the text before synthesis:** 35–60 words; no URLs, emails, phone numbers or prices; no first-person promises, endorsements or claims of having reviewed the visitor's materials; no names of other real people; no quoted visitor text longer than a few words. Failing text plays no audio.
- **Reject impersonation attempts upstream:** if the visitor asks the advisor to say something "as Major", make a statement for them, or read their text aloud, the reply is text-only and the audio button does not appear.
- **Authorize each clip:** the advise route stores the validated text under a random ID with a 5-minute expiry and returns a signed token bound to that ID and the requester's IP; the voice route accepts each token once (a used or expired token returns 403) and synthesises only the stored text, never text sent by the browser.
- **Log** token issue, use and refusal counts (not visitor text) so misuse shows up.

**Fallbacks:**

1. Audio fails or cap reached → text stays; player shows "Audio isn't available right now."
2. Model fails, times out (8 s) or returns an invalid product → a static picker of the problem categories in section C, linking to products and consulting.
3. Rate limit reached → same picker plus the contact route.
4. Visitor pastes what looks like confidential material → short reply asking them to remove it; no audio.

**Privacy.** Visitor text goes to Anthropic for the insight and, when played, the insight text goes to ElevenLabs. The privacy page must name both processors, say what is logged (proposal: category, product routed, timings and an anonymous counter; not the visitor's full text) and how long. Do not place visitor text in analytics events or URLs.

## C. Commercial routing: recommend, ask once, consult, or decline

The router gives one useful observation first, then picks exactly one of four actions, and asks at most one follow-up question per visit. It recommends the best-fit offer whatever its sale state; availability is shown honestly beside it and never changes relevance. Prices, links and availability come from the storefront catalog, never from the model.

**Action rules (in priority order)**

1. **Decline — AMA cannot help this visitor.** Legal, tax, investment, medical or compliance judgment; guarantees of demand, sales, compliance or counterparty authenticity; requests to impersonate someone; anything unrelated to AMA's work. Give a short general observation, say plainly what AMA doesn't do, offer the contact route, and show **no product**.
2. **Ask once — the help wanted is unclear.** Two offers fit and one fact separates them (see table), or the visitor asks AMA to build something. A build request is not declined: ask whether they want a decision on approach (consulting), a build-ready spec (Idea to MVP Brief), or an implementation quote (inquiry; implementation is scoped separately and is outside the fixed-price products). The next turn must recommend, route to consulting, or route to inquiry.
3. **Recommend consulting.** A decision about tools, architecture or approach rather than a deliverable (AI Choice Session, $350); a whole workflow to map, challenge and pilot (Map → Poke → Scale → Pressure-Proof Workshop, $1,250); or two offers still fit after the follow-up.
4. **Recommend one product.** The signals match one row and the visitor has, or can get, the sources it needs. Monthly packages only when the visitor states a recurring cadence.

"Outside the products' scope" (for example, writing the app's code) is different from "cannot help": the first still gets the nearest useful offer or an inquiry route; only the second gets no product.

**Problem-to-product map**

| Visitor signal | Product (USD) | The one question that separates it |
| --- | --- | --- |
| Big meeting soon, wants to arrive prepared | Walk In Ready ($250) | — |
| Offer is hard to explain to buyers | Make It Make Sense Kit ($495) | "Do buyers mostly need one clear story, or answers to repeated objections?" → Customer Question Kit |
| Same objections and questions keep coming up | Customer Question Kit ($395) | (same as above) |
| Unsure what customers struggle with; no interviews yet | Find the Friction ($595) | "Do you already have interview notes or recordings?" → Voice of Customer |
| Has interviews, needs themes and evidence | Voice of Customer Brief ($795) | (same as above) |
| Unclear how to stand out from competitors | Find Your Opening ($795) | — |
| Nontechnical founder with an app idea, needs a build-ready spec | Idea to MVP Brief ($995) | — (building the app is out of scope) |
| Has an RFP to answer | RFP Response Starter ($895) | — |
| Vendor contract vs internal policy | Policy Gap Review ($795) | — (preliminary discrepancy list, not compliance sign-off) |
| Project updates conflict, nobody knows what was decided | Project Clarity Brief ($395) | — |
| New hire starting, onboarding is ad hoc | First Week Ready ($795) | "One role, or recurring onboarding?" → Team Learning Monthly |
| Choosing between up to 3 providers | Vendor Choice Brief ($895) | "Is this one decision or a recurring one?" → Decision Desk Monthly |
| Recurring: customer education content | Explain It Monthly ($1,250/mo) or Customer Education Monthly ($2,250/mo) | "Explainer videos and FAQs, or full bundles with decks and infographics?" |
| Recurring: weekly reading packs for a founder | Executive Listening Desk ($995/mo) | — |
| Recurring: internal knowledge keeps changing | Knowledge Continuity Monthly ($1,500/mo) | — |
| "Which AI tool should we use?" / approach unclear | AI Choice Session ($350) | — |
| Whole workflow to redesign, wants a staged pilot | Pressure-Proof Workshop ($1,250) | — |

**Guardrails on the insight:** 35–60 words; restate the problem in the visitor's terms; one concrete next step they can take without buying; no fabricated statistics, client results or tool claims; no promised outcomes; no mention of NotebookLM or Open Notebook. If the visitor pastes confidential material, the reply asks them not to and nothing is retained.

## Major's mindset pack (the missing ingredient)

The catalog tells the advisor what AMA sells; the mindset pack teaches it how Major thinks. It is a small, versioned set of files that Major writes or approves — this desk has **not** written any of its content, because inventing his judgment would defeat the purpose.

| File | Holds | Suggested size |
| --- | --- | --- |
| `framing.md` | How Major restates a problem before answering: what he looks for first, what he ignores | 5–10 principles |
| `questions.md` | Questions he asks before recommending tools or products, ranked by how often they change the answer | 10–15 questions |
| `advice-given.md` | Short examples of advice he would give, each with the problem it answered | 10–20 pairs |
| `advice-rejected.md` | Advice he would reject (for example, tool-first answers) and why | 10 pairs |
| `mpsp.md` | Map → Poke → Scale → Pressure-Proof: one paragraph per stage, with what each stage produces | 1 page |
| `voice-and-tone.md` | Words he uses and avoids; how blunt to be | half a page |

Rules: only approved files ship (each carries an approval date and version); the prompt cites them as AMA's approach, not as quotes from Major; the evaluation set checks that insights follow the framing and never produce a rejected pattern. Major can draft by voice memo; Open Notebook can transcribe and organize it internally, and he approves the final text.

## Google data flow: three stages, no automatic mixing

Data moves forward only on an explicit event, and client material never enters a shared research notebook automatically.

| Stage | Created when | What is stored | Where (to confirm) | Retention |
| --- | --- | --- | --- | --- |
| Anonymous preview | Visitor uses the advisor | Problem category, action, product slug, timings, availability shown, anonymous counter; **not** the visitor's text | Aggregate log or analytics events | Short, owner-set |
| Inquiry record | Visitor submits the contact form (opt-in) | Name, email, message, the preview's category and recommended product if the visitor chooses to attach it | Google Workspace inquiry sheet or form responses | Per privacy policy |
| Order + private workspace | Payment verified against a Stripe session or order reference (never a redirect) | Order reference linked to the inquiry; a restricted Drive folder per client for sources and deliverables | Restricted Google Drive folder shared with the buyer only | Per service terms |

Research use: a client's material may be copied into an Open Notebook notebook only for that client's paid work, in a notebook dedicated to that client, by a human operator. Shared AMA research notebooks hold only public sources and approved AMA material such as the mindset pack. The exact Google destinations (Sheet, Form, Drive parent folder) and who can access them are owner decisions not yet given to this desk.

## Ten example visitor journeys

These are illustrative test cases written for this brief, not real visitor messages or evidence of demand. They double as the proof-of-concept evaluation set: five recommend (one monthly), three ask once, one routes to consulting, one declines. Each "Routes to" cell names the best fit regardless of whether checkout is live; the product card then shows its real availability. Insights in this table predate the mindset pack and must be rewritten against it before the evaluation.

| # | Visitor says | Action | Proposed insight (draft) | Routes to |
| --- | --- | --- | --- | --- |
| 1 | "I pitch a hospital procurement board Thursday and I've only skimmed their annual report." | Recommend | Boards remember the presenter who asks about their stated priorities. Pull the three goals they repeat most in the report and open with one question on each. | Walk In Ready ($250): a two-page brief and ten questions built from up to 3 sources, in 3 business days. |
| 2 | "People love our product once they get it, but nobody understands the homepage." | Ask once | When people "get it" only after a demo, the gap is usually one missing sentence: who it is for and what changes for them. Write that sentence before redesigning anything. *Question: do buyers mostly need one clear story, or answers to the same objections?* | Story → Make It Make Sense Kit ($495); objections → Customer Question Kit ($395) |
| 3 | "We have 14 recorded customer calls and no time to listen to them." | Recommend | Recorded calls are your strongest evidence because the words are the customer's. Start by tagging the moments people describe a workaround; those usually point to the real pain. | Voice of Customer Brief ($795): themes, attributable quotes, one infographic. Note 14 calls may exceed 8 source units at 30 minutes each. |
| 4 | "I think small gyms need better scheduling, but I haven't talked to any yet." | Recommend | Before building, find where gym owners already complain in public, in their words. That tells you whether scheduling is the pain or a symptom. Public posts are signals, not proof of demand. | Find the Friction ($595): up to 15 accessible sources, a pain-point evidence table and interview questions. |
| 5 | "Three competitors all claim 'AI-powered'. How do we stand out?" | Recommend | When every competitor claims the same feature, compare what each one proves on its pricing and feature pages. The opening is often the buyer they ignore, not the feature they share. | Find Your Opening ($795): three-competitor comparison with dated evidence and positioning hypotheses. |
| 6 | "Every week I get a stack of board packs and market reports I never read." | Recommend (monthly) | A weekly stack is a cadence problem, not a reading problem. Decide which two decisions each pack must inform, then read only for those. | Executive Listening Desk ($995/month): four audio briefings and four one-page takeaways. |
| 7 | "Should we use ChatGPT, Claude or build our own agent for customer support?" | Consult | The right choice depends on your ticket volume, data sensitivity and who maintains it, more than on the model. List your top three ticket types before comparing tools. | AI Choice Session ($350): 60 minutes with Major on one question, plus a one-page recommendation. |
| 8 | "We're choosing between two payroll providers." | Ask once | Compare providers on the criteria that would hurt most if they failed, such as filing errors or support response, before price. *Question: is this a one-time choice or a decision you make regularly?* | One-time → Vendor Choice Brief ($895); recurring → Decision Desk Monthly ($2,500/month) |
| 9 | "Is this gold deal from a West African seller legitimate? Should I wire the deposit?" | Decline | AMA can't verify a counterparty or advise on whether to send funds; that needs legal and financial professionals. Don't wire anything until independent verification is complete. | No product. Contact link only. |
| 10 | "Can you build our app for us?" | Ask once | Most app builds go wrong before the first line of code, when nobody has written down who it's for and what "done" means. Question: do you need help choosing the approach, a build-ready spec, or a quote to build it? | Approach → AI Choice Session ($350); spec → Idea to MVP Brief ($995); build quote → inquiry (implementation scoped separately) |

Journey 3 shows a case the router must flag rather than hide: the visitor's material may exceed the product's source allowance, so the reply names the limit and lets AMA quote extra scope after purchase review. Journey 9 is the only true decline; journey 10 shows that a build request gets a clarifying question, not a refusal.

## Minimal proof-of-concept test plan

The smallest useful test is offline and costs under $10: one voice clone, one routing prompt, the ten journeys, and a timing script — running in parallel with the interface build. Owner approval is needed for the two accounts (ElevenLabs Starter, Anthropic API key) since this research task purchased nothing.

| Step | What to do | Pass criterion | Owner |
| --- | --- | --- | --- |
| 1. Consent | Major signs the voice-use authorization (scope, revocation) | Signed note filed internally | Major |
| 2. Clone | Record 1–2 min of clean speech; create an Instant clone | Clone ID exists | Major |
| 3. Routing eval | Run the 10 journeys through the draft prompt and JSON schema with the candidate model and the approved mindset pack, 3 runs each | ≥ 9/10 journeys route to the expected action and product in all runs; 0 invented prices, products or outcomes; both declines decline | Claude Code |
| 4. Insight review | Major reads the 10 insights | ≥ 8/10 he would sign his name to without edits | Major |
| 5. Voice listening test | Synthesise the 10 insights with Flash v2.5 and Multilingual v2; Major plus two people who know his voice listen blind | Major approves the voice; listeners call it recognisably his and not embarrassing; pick the model | Major |
| 6. Timing | Script calls both APIs 20 times from a Vercel preview function (or local, labelled as such) and records time to first text, full text, first audio byte | Results recorded against the latency targets; p95 reported honestly | Claude Code |
| 7. Cost check | Compare provider dashboard usage with the $0.015 and $0.0005 estimates | Actual within 2× of estimate | Claude Code |
| 8. Open Notebook reuse | Add the clone ID to a speaker profile and generate one short Walk In Ready listening overview internally | Audio produced with the cloned voice, or failure documented | Claude Code / operator |

**Stop rule:** if step 3 or step 5 fails twice after prompt or recording fixes, ship the text-only advisor and keep voice in the backlog. Text plus routing is the commercial core; voice is an enhancement.

**After launch (only once live):** count previews, audio plays, product-card clicks and checkout starts per week. No conversion claim until real data exists.

## Claude Code implementation brief

Build the advisor as one component and two route handlers inside the existing storefront in Major's `697a62a` snapshot. It reads that storefront's catalog and availability states; it adds no new site, framework or design system.

**Sequence and placement**

1. Start from the `697a62a` snapshot. Inspect its catalog, product pages, availability states, contact flow and design tokens before changing anything; preserve uncommitted work.
2. Read `AGENTS.md` and the installed Next.js guides in `node_modules/next/dist/docs/` on route handlers and streaming before writing code.
3. Add the advisor component where the storefront's "Make It Make Sense" entry points already are (products index and homepage section), reusing existing components and styles.
4. Add an advise route (POST, Node runtime): validate input → rate-limit → `ModelProvider` with JSON schema, catalog summary and mindset pack → server check that any slug exists in the catalog → attach title, price, link and availability from the catalog → issue a single-use audio token when the text passes validation.
5. Add a voice route (POST): accept only a valid, unexpired, unused token; check the daily cap and kill switch; synthesise the stored text through `VoiceProvider`; stream audio back.
6. Keep the system prompt, schema, routing table, mindset pack and example journeys as versioned files under one advisor folder; only files marked approved are loaded.
7. Contact form: when a visitor chooses to attach their preview, send its category and recommended product with the inquiry. Preview text is never stored.
8. Update the privacy page and setup checklist: name the model and voice processors, the preview data kept, and the inquiry/order stages.

**Dependencies (owner approval needed for accounts and keys)**

| Item | Purpose | Notes |
| --- | --- | --- |
| Model provider adapter | Insight + routing | `ADVISOR_MODEL_PROVIDER`, `ADVISOR_MODEL_ID`, provider API key; server-only; candidate: a fast Claude model via `@anthropic-ai/sdk` |
| Voice provider adapter | Voice | `ADVISOR_VOICE_PROVIDER`, `ADVISOR_VOICE_ID`, `ADVISOR_VOICE_MODEL_ID`, provider key; candidate: ElevenLabs REST via `fetch` |
| Rate-limit and token store | Per-IP limits, daily cap, single-use tokens | Candidate: `@upstash/ratelimit` + `@upstash/redis` (`UPSTASH_REDIS_REST_URL`, `UPSTASH_REDIS_REST_TOKEN`) |
| Flags | Safety | `ADVISOR_ENABLED`, `ADVISOR_AUDIO_ENABLED`, `ADVISOR_AUDIO_DAILY_CAP`, `ADVISOR_SIGNING_SECRET` |

All secrets in ignored local env or Vercel environment variables; none in client components or `NEXT_PUBLIC_*`.

**Acceptance criteria**

- With `ADVISOR_ENABLED` off or keys missing, the component renders a static problem picker; `npm run lint` and `npm run build` pass.
- A fixture test runs the example journeys against mocked model output: unknown slug → picker; decline → no product; ask-once → exactly one question, then a product, consulting or inquiry route; a build request is never declined.
- The best-fit product is shown whatever its sale state, with the catalog's availability label; no fake checkout.
- No price, product name, link or availability in a reply comes from model text.
- Audio plays only after a click, speaks exactly the validated on-screen text, shows the AI-voice disclosure; a forged, reused or expired token returns 403; text failing validation shows no audio button.
- Switching provider IDs in env changes provider without code changes (tested with a mock provider).
- Rate limit and cap return a friendly state; the kill switch hides the player within one request.
- No visitor text in analytics, URLs or long-term logs; client material never written to a shared notebook or shared folder.
- Keyboard operable, visible focus, `aria-live="polite"` on the insight, animation stops under `prefers-reduced-motion` checked in JS.
- No public mention of NotebookLM or Open Notebook; no proprietary-model claims; no promised outcomes.

**Unresolved decisions for Major**

- [ ] Write or approve the mindset pack (six files above).
- [ ] Choose providers after the listening test; approve their accounts and a rate-limit store.
- [ ] Sign the voice-use authorization and choose the disclosure wording.
- [ ] Set the daily audio budget (proposed cap 200 clips ≈ $2.40/day).
- [ ] Confirm preview data retention and the Google destinations for inquiries and the per-client order folders, and who can access them.
- [ ] Confirm English-only replies for v1.

## One-shot build prompt (draft)

Paste this with the `697a62a` ZIP attached. It is written so the builder inspects the snapshot rather than trusting this desk's view of older `main`; replace the bracketed items once Major supplies them.

```markdown
You are extending the existing AMA Solutions website in the attached 697a62a snapshot. The storefront (catalog, product pages, consulting offers, availability states) already exists. Do not rebuild it, replace the framework, or create a second site. Preserve existing work, brand and the dark-and-gold visual language.

First inspect: AGENTS.md, CLAUDE.md, README and docs/; the catalog file and its availability states; product and consulting pages; the contact flow; design tokens and shared components; installed Next.js docs in node_modules/next/dist/docs/ for route handlers and streaming. Summarize what you found before coding.

Build the "Make It Make Sense" advisor:

1. Component on the existing products index and homepage entry points. Visitor describes a business problem (max 1,000 characters).
2. Advise route (server only). Order: validate → per-IP rate limit → call ModelProvider with a JSON schema → verify any product slug against the catalog → attach title, price, link and availability from the catalog → return. The model never supplies prices, links or availability.
3. Response = one useful observation first (35–60 words, plain language, one next step the visitor can take without buying), then exactly one action:
   - recommend: the best-fit product, shown with its honest availability (purchasable, opening soon, or by inquiry) even if checkout is not live;
   - ask_once: one question when two offers fit, or when the visitor asks AMA to build something (approach → AI Choice Session; spec → Idea to MVP Brief; build quote → inquiry). Never more than one question per visit;
   - consult: AI Choice Session or Map → Poke → Scale → Pressure-Proof Workshop for decisions about tools, architecture or a whole workflow;
   - decline: only when AMA cannot help (legal, tax, investment, medical or compliance judgment; guarantees; impersonation; unrelated requests). No product; offer the contact route.
4. Load the approved mindset pack (advisor/mindset/*.md, only files marked approved) into the system prompt as AMA's approach: how Major frames problems, the questions he asks before recommending tools, advice he gives and rejects, and Map → Poke → Scale → Pressure-Proof. [Major to supply the six files.]
5. Voice (click to play only). Validate the insight text before synthesis (35–60 words; no URLs, contact details, prices, promises, other people's names or quoted visitor text). If the visitor asks the advisor to speak for or as Major, return text only. Store validated text under a random ID for 5 minutes; issue a signed token bound to that ID and requester IP; the voice route accepts each token once, checks a daily cap and kill switch, synthesises only the stored text through VoiceProvider, and streams audio. Show: "AI-generated voice of Major Dream Williams, used with his permission. The text above is the full transcript."
6. Providers are configurable adapters (ModelProvider, VoiceProvider) chosen by environment variables, with a mock provider for tests. Do not hard-code model names or prices; check current provider documentation before choosing defaults. Secrets stay server-side, never in client code or NEXT_PUBLIC_ variables or git.
7. Fallbacks: missing keys, ADVISOR_ENABLED off, timeout (8 s), invalid output or rate limit → a static problem picker linking to products, consulting and contact. Audio failure → text stays, player shows a short notice.
8. Data flow: anonymous previews store only category, action, product slug, availability shown and timings — never the visitor's text. Contact submission creates an inquiry record [Google destination to confirm] and may attach the preview's category and product if the visitor opts in. Only a verified payment (session/order reference, never a redirect or query string) links an inquiry to an order and a restricted per-client Google Drive folder [parent folder to confirm]. Client material never enters a shared research notebook or folder automatically.
9. Visual: reuse site tokens; gold pulse while text streams; simple gold level meter from Web Audio while audio plays; stop all animation when prefers-reduced-motion is set, checked in JavaScript. Keyboard operable, visible focus, aria-live="polite" on the insight.
10. Public copy says AMA Solutions only. No mention of NotebookLM or Open Notebook, no proprietary-model claims, no promised outcomes.
11. Update the privacy page (model and voice processors, preview data kept, inquiry and order stages) and the setup checklist.

Tests: lint and build pass with providers off; fixture tests for the example journeys with a mock provider (unknown slug → picker; decline → no product; build request → ask_once, never decline; single question then route); forged, reused or expired audio token → 403; provider swap via env only. Report what is implemented, mocked, configured, tested live and still blocked. Do not deploy, purchase services or change accounts.
```

## Backlog (not needed for the first build)

- Talking-head or lip-synced video avatar of Major (higher cost, consent and uncanny-valley risk; revisit after audio is measured).
- Retrieval over AMA's own notebook at request time via Open Notebook or a vector store; v1 puts the approved catalog and examples in the prompt instead.
- Multi-turn chat beyond one follow-up question.
- Non-English replies and voice.
- Webhook-driven fulfillment and order state (the handover already defers this).
- Competitor scan of AI-advisor storefronts and pricing benchmarks.
- Server-side analytics funnel (insight → product view → checkout) beyond Vercel Analytics page events.
- Open Notebook hardening for any shared use: rate limiting, scoped tokens, restricted CORS.

## Sources (accessed 28 Oct 2026)

Repositories and internal documents: [amasolagi-site](https://github.com/MajorDream444/amasolagi-site) at `4ee9f8b`; [open-notebook](https://github.com/MajorDream444/open-notebook) at `d39af07` (v1.9.0); Esperanto 2.22.0 and podcast-creator 0.13.1 packages from PyPI; [amasolagi.com](https://amasolagi.com) homepage; AMA Commerce Handover (28 Oct 2026, project document).

Vendor and official pages (paraphrased; latency figures are vendor claims). Pages marked † were opened directly by this desk; the rest were opened by a delegated research task and reconciled here.

- [Next.js route.js reference](https://nextjs.org/docs/app/api-reference/file-conventions/route) †
- [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing) †
- [Claude structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) †
- [ElevenLabs API pricing](https://elevenlabs.io/pricing/api) †
- [OpenAI text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech) †
- [ElevenLabs Instant Voice Cloning](https://elevenlabs.io/docs/product-guides/voices/voice-cloning/instant-voice-cloning), [Professional Voice Cloning](https://elevenlabs.io/docs/product-guides/voices/voice-cloning/professional-voice-cloning), [pricing](https://elevenlabs.io/pricing), [terms of use](https://elevenlabs.io/terms-of-use) (updated 9 Oct 2026), [stream endpoint](https://elevenlabs.io/docs/api-reference/text-to-speech/stream), [models](https://elevenlabs.io/docs/models), [latency optimization](https://elevenlabs.io/docs/developers/best-practices/latency-optimization)
- [OpenAI custom voices](https://developers.openai.com/api/docs/guides/custom-voices)
- [Cartesia pricing](https://cartesia.ai/pricing), [Sonic](https://cartesia.ai/sonic), [voice cloning](https://docs.cartesia.ai/build-with-cartesia/capability-guides/clone-voices), [acceptable use](https://cartesia.ai/legal/acceptable-use)
- [Google Chirp 3 Instant Custom Voice](https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice), [Google TTS pricing](https://cloud.google.com/text-to-speech/pricing)
- [Deepgram pricing](https://deepgram.com/pricing); [Mistral voice cloning](https://docs.mistral.ai/studio/audio/text-to-speech/voice-cloning)
- [Vercel function duration](https://vercel.com/docs/functions/configuring-functions/duration), [Vercel streaming functions](https://vercel.com/docs/functions/streaming-functions)
- [Upstash Ratelimit getting started](https://upstash.com/docs/redis/sdks/ratelimit-ts/gettingstarted)
- [European Commission: code of practice on marking AI-generated content](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content); [FTC on AI voice cloning](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/04/approaches-address-ai-enabled-voice-cloning)

**Not confirmed:** full text of ElevenLabs' use policy on impersonation and AI transparency; Cartesia's full terms; the official EUR-Lex text of EU AI Act Article 50. Mistral's own pages give conflicting prices and clone minimums, so Mistral was not shortlisted.
