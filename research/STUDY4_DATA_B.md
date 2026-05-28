# Study 4 Data — Group B: Handoff Chain
Project: Portfolio website vibe coding (6 sessions)

---

## Handoff1 — T1 Test Context (after S1)

# Handoff - portfolio-site - Session 1: Foundation

## Current Goal
Built the full HTML skeleton and CSS foundation; color system is locked. Next session: finish the nav hover flicker and build out hero and about section content.

## Key Decisions
- Dropped Bootstrap mid-session → it caused immediate specificity conflicts on `.container` padding that couldn't be cleanly overridden; the CSS variable system required cascading workarounds the user didn't want
- Accent color settled as `#e94560` (coral red) → burnt orange tried first, rejected as "sports team logo feel"; bright orange rejected as aggressive; terra cotta rejected as "real estate brand"
- Nav: 3 links only (About, Work, Contact), no hamburger collapse → 3 short words fit on any reasonable phone screen; hamburger is only needed for 6+ items

## In Progress
- Nav hover flicker — partially fixed but not fully resolved; a very faint one-frame flash may still appear on first hover in some browsers

## Completed This Session
- Full HTML skeleton: nav, hero, about, projects, contact, footer sections
- CSS written from scratch — no framework, ~60 lines, every rule explicit
- Color system locked in `:root` variables: `--color-bg #1a1a2e`, `--color-nav #16213e`, `--color-accent #e94560`, `--color-text #e0e0e0`, `--color-text-muted #8892b0`
- Nav: fixed position, `z-index: 100`, brand in accent color, links uppercase with letter-spacing
- Hero: name + placeholder tagline + coral-red CTA button linking to `#projects`
- About: two-column grid (280px photo + 1fr text), skill tags with accent tint, section heading with `::after` accent bar (50px wide, 3px tall)
- Section layout: `padding: 5rem 2rem`, `max-width: 1100px`, `margin: 0 auto`, footer reuses `--color-nav` background
- Photo placeholder via placeholder service using site colors

## Safety Rules
- Do not add Bootstrap back — the specificity wall on its variable system was the reason it was dropped; plain CSS is intentional
- Do not use orange as accent color — all three variants were tried and rejected with specific reasons tied to unwanted brand associations
- The `a { color: inherit; }` reset line is intentional — it neutralizes the browser UA stylesheet default link color; without it, nav hover flicker returns

## Last Actions
- Added `a { color: inherit; }` to global reset to fix nav hover flicker root cause
- Added placeholder image via placeholder.com service in matching site colors
- Confirmed nav hover contrast (muted grey → full white) is satisfying and sufficient

## Next Actions
- Verify nav hover flicker is fully gone across multiple hover cycles
- Begin hero content: settle on the actual tagline copy
- Build about section content (two-column grid is scaffolded, needs photo circle treatment and responsive stacking)

## Recon Notes
- Bootstrap dropped after user directly hit specificity wall trying `padding: 0` on `.container` — didn't work, Claude explained why, user made the call immediately
- Orange rejected after seeing all three variants on screen — "sports team," "aggressive," "real estate" were user's own words in sequence
- Nav hover flicker was traced through two root causes in S1: global `a { color: white }` rule (removed) and UA stylesheet default (patched with `color: inherit`) — may need one more check

## Background
→ read ~/Desktop/context-relay/research/STUDY4_CONTENT.md for full session logs

---

## Handoff2 — T2 Test Context (after S2)

# Handoff - portfolio-site - Session 2: Hero + About

## Current Goal
Hero and about section are complete. Next session: build the projects/work card grid with filtering.

## Key Decisions
- Nav hover flicker fully resolved → two overlapping root causes found: stale `.site-nav a { color: var(--color-text) }` rule (created ambiguity in cascade starting-state calculation) plus missing `color: inherit` on the `a` reset; fix was removing the stale rule AND adding `color: inherit` — no new transition classes added
- Hero tagline locked: "Frontend engineer. The details are the whole point." → started from option 2 with "obsess" framing, rejected as cliché; iterated to this version which the user immediately confirmed
- Hero animation removed → CSS `fadeInUp` keyframes tried with staggered delays; caused layout shift on iOS (translateY + animation-fill-mode: both triggers layout recalculation between painted position and end state); user decided to remove rather than patch
- Circular photo uses container approach → `border-radius: 50%` and `overflow: hidden` go on `.about-photo` (not the image); explicit `width: 280px; height: 280px` on container required because grid stretches container vertically otherwise

## In Progress
- No active blockers; projects and contact sections are still empty skeletons
- Placeholder photo and bio text in about section — user will write own copy later
- No hamburger nav for mobile — noted for later, not urgent with 3 links

## Completed This Session
- Nav hover flicker closed for real — all hover cycles clean across all three links
- Hero: name + "Frontend engineer. The details are the whole point." + CTA button; statically rendered, no animation
- About section: circular photo (container-clips approach), bio placeholder, skill tags, responsive 768px breakpoint (single column, photo 200px centered)
- `prefers-reduced-motion` noted: since animation was removed, no need for this media query

## Safety Rules
- Do not add any CSS animation to the hero — it caused iOS layout shift; the decision to remove it was explicit and the user confirmed "it actually feels more confident without the animation"
- Do not add new transition classes to fix the nav hover — the fix was cascade cleanup, not transition modification; nav transition was correct the whole time
- `.about-photo` must have explicit `width` AND `height` set to the same value — removing either makes the circle become oval due to grid row height stretching the container
- The 4rem gap on `.about-grid` is intentional — user tried 3rem, disliked it, reverted to 4rem

## Last Actions
- Added `@media (max-width: 768px)` collapsing about grid to single column, photo to 200px centered
- Confirmed responsive nav is not overflowing on mobile (3 links fit on one line)
- Confirmed `clamp()` font sizes on hero name and tagline behave correctly on mobile

## Next Actions
- Build project card grid: six text-only cards, three categories (Frontend, Backend, Design), filter buttons above the grid
- Decide card hover effect
- Add responsive breakpoints for the card grid

## Recon Notes
- Stale `.site-nav a` rule was found by asking user to grep for all `a`-targeting rules — user found it themselves during the search
- Animation mobile problem discovered when user specifically tested on phone after applying the CSS keyframes — layout jump appeared immediately on load
- Oval photo problem traced: `aspect-ratio: 1` on the image failed because grid was assigning the container a non-square height; explicit container height was the fix

## Background
→ read ~/Desktop/context-relay/research/STUDY4_CONTENT.md for full session logs

---

## Handoff3 — T3 Test Context (after S3)

# Handoff - portfolio-site - Session 3: Project Gallery

## Current Goal
Work section (project gallery) is complete. Next session: build the contact form.

## Key Decisions
- Section renamed "Projects" → "Work" everywhere → user said "Work sounds more like a designer would say it, more intentional than developer-resume energy"; rename touched 5 locations (section id, nav link text+href, hero CTA href, CSS selector)
- Card hover: border-left accent line → box-shadow tried in 3 configurations (ring+shadow, shadow-only, radial halo) and rejected each time — "too UI-y like a form input," "too corporate/enterprise dashboard"; border-left is more editorial
- Text-only cards → no images for now, placeholder cards have equal height which makes grid look intentional
- Filter JS uses exact string match `===` on `data-tags` → single-category cards only; multi-tag support would require `split(' ').includes()` but not needed now
- Footer CSS moved to end of file in labelled comment block → it was accidentally displaced during the rename edits; physically isolating it from the section-editing zone prevents future proximity casualties

## In Progress
- Contact section is still an empty skeleton
- About section still has placeholder photo and bio
- "View Project →" links all point to `#` (placeholder) — clicking them scrolls to top; will be replaced with real URLs when content is ready

## Completed This Session
- Six-card CSS grid, `repeat(3, 1fr)`, responsive: 2 columns at ≤768px, 1 column at ≤480px; filter bar wraps at ≤480px
- Filter system: JS `data-filter` / `data-tags` matching, `display: block/none` toggling, `.active` class moves between buttons
- Card hover: `border-left: 3px solid transparent` base state (space pre-reserved), `border-left-color: var(--color-accent)` on hover, `transition: border-color 0.2s ease`
- "Work" nav link confirmed scrolling correctly; "About" and "Contact" nav links unaffected
- Footer spacing (`margin-top: 4rem`) restored after being accidentally dropped during rename edits

## Safety Rules
- Box shadow on cards is off the table — tried in 3 configurations, all rejected as too heavy/corporate on the dark background; do not revisit
- The card hover requires BOTH rules coexisting: `border-left: 3px solid transparent` in base AND `border-left-color: var(--color-accent)` in hover — removing either silently breaks the hover (base removal causes 3px card shift on hover; hover removal means nothing happens)
- Footer CSS lives at the end of style.css in a labelled comment block — this is intentional; do not move it back into the middle of the file near the section rules
- The email regex (coming in S4) intentionally rejects `+` addresses — do not "fix" this

## Last Actions
- Restored `.footer-inner p` rule (small + muted copyright text) which was dropped during the rename edits
- Moved both footer rules to end of file inside "Footer" comment block
- Verified all three nav links and hero CTA scroll correctly after rename

## Next Actions
- Build contact form: name, email, message fields, submit button
- Add blur-triggered field validation (user prefers blur over submit-only)
- Add Safari smooth scroll polyfill

## Recon Notes
- Box shadow was rejected progressively — ring version first ("looks like a focused form input"), then shadow-only ("corporate enterprise dashboard"), then radial halo ("still not right") — three tries before user said "the glowing thing doesn't fit this design"
- "Work" rename was user's idea mid-session after noticing inconsistency with "See My Work" button already in the hero
- Footer `margin-top` loss was a proximity casualty — not caused by the rename logic itself, just lost during adjacent CSS edits

## Background
→ read ~/Desktop/context-relay/research/STUDY4_CONTENT.md for full session logs

---

## Handoff4 — T4 Test Context (after S4)

# Handoff - portfolio-site - Session 4: Contact Form + JS

## Current Goal
Contact form is complete with blur validation and Safari smooth scroll. Next session: polish and performance work.

## Key Decisions
- Blur-triggered validation chosen over submit-only or live → user's preference; "feels like the form is paying attention to you as you fill it out"
- Email regex intentionally rejects `name+work@gmail.com` style addresses → user was offered the fix, explicitly declined: "my clients won't use plus addresses, it's a contact form not a mission-critical system" — this is a product decision, not a bug
- Safari smooth scroll: JS polyfill using `querySelectorAll('a[href^="#"]').forEach()` + `scrollIntoView({ behavior: 'smooth' })` → CSS `scroll-behavior: smooth` alone doesn't work on older Safari (added only in Safari 15.4); polyfill has better coverage from Safari 14
- `scroll-margin-top: 70px` on all sections → prevents fixed nav from covering headings when JS scrollIntoView fires
- 3-second `setTimeout` for success message → user tested and confirmed "quick enough but enough time to read it"
- Form resets immediately on valid submit → `e.target.reset()` fires at same time as success message display; user confirmed "the form is done, clear it right away"

## In Progress
- Smooth scroll polyfill uses per-element event listeners via `forEach` — flagged as memory-leak-adjacent; should be refactored to event delegation before deployment
- No backend on the form — success message is cosmetic only, no data transmitted
- About section still has placeholder photo and bio

## Completed This Session
- Contact form: name, email, message, submit; `novalidate` disables browser-native validation popups
- Blur validation: `validateField()` + `showFieldError()` functions; errors appear and clear reactively per field; submit handler runs all validations as final gate
- Form success: `#form-success` div shows for 3s then hides, form resets immediately
- Safari smooth scroll polyfill (per-element version — to be improved in S6)
- `scroll-margin-top: 70px` on section rule
- `.section-heading::after` accent bar confirmed working on Contact heading after a duplicate rule with `background-color: transparent` was found and deleted

## Safety Rules
- Email regex (`/^[a-zA-Z0-9._%\-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/`) rejects `+` addresses — this is intentional product behavior confirmed by the user; do not update it
- Do not add hero animation — this was removed in S2 because it caused iOS layout shift; the decision is final
- Card hover border-left requires BOTH base rule (transparent border) and hover rule — removing either silently breaks the effect
- Footer CSS is at the end of style.css in a labelled block — do not move it

## Last Actions
- Fixed `.field-error` CSS to use `var(--color-accent)` instead of hardcoded `#e94560` (caught by user during review)
- Added `scroll-margin-top: 70px` after user discovered nav was clipping section headings on Safari scroll
- Verified smooth scroll and nav offset working in Safari

## Next Actions
- Refactor smooth scroll polyfill to delegated document listener (pre-deployment cleanup)
- IntersectionObserver for sticky nav behavior
- Consider dark mode toggle and CSS variable cleanup

## Recon Notes
- Plus-sign email rejection discovered when user tested with their own work email `name+work@gmail.com` — saw the error, Claude offered fix, user explicitly declined after thinking about the audience
- Safari heading-clip issue discovered after user tested Safari smooth scroll and noticed headings disappearing under nav — led directly to `scroll-margin-top`
- Duplicate `.section-heading::after` rule found via DevTools — pseudo-element was present but transparent because a second rule at end of CSS was overriding the color

## Background
→ read ~/Desktop/context-relay/research/STUDY4_CONTENT.md for full session logs

---

## Handoff5 — T5 Test Context (after S5)

# Handoff - portfolio-site - Session 5: Polish + Performance

## Current Goal
Sticky nav and CSS variable system are complete. Dark mode toggle was added but is partial and known-broken. Next session: deployment prep — remove or finish dark mode, refactor smooth scroll, audit paths, add SEO tags.

## Key Decisions
- Sticky nav uses `IntersectionObserver` (not scroll event) → observes `#hero`; when hero exits viewport adds `.nav-scrolled` class with `background-color: rgba(22, 33, 62, 0.98)` and `box-shadow: 0 2px 20px rgba(0, 0, 0, 0.4)`; fires once per direction, not 60x/sec
- Dark mode: partial implementation, explicitly flagged as not production-ready → toggle changes body background and nav color only; project cards, form inputs, about section, skill tags all stay dark (hardcoded `background-color` values don't cascade from body); form inputs are unusable in light mode (dark bg + inherited dark text = invisible typed text); decision deferred to S6: finish properly or remove
- CSS variable sweep completed → all hardcoded hex values replaced with `var()` references; new variables added: `--color-card: #16213e`, `--color-border: rgba(136, 146, 176, 0.2)`; `rgba()` tinted accent values left as raw (CSS can't do `rgba(var(--color-accent), 0.15)` cleanly)
- Hero image: `loading="eager"` (not lazy) → user had mistakenly added `loading="lazy"` to all images including the hero; hero is above the fold and must load immediately; below-fold images use `loading="lazy"`
- System fonts: no web fonts, no Google Fonts CDN → intentional; zero external font loading overhead, no FOUT; Verdana on Linux is acceptable fallback

## In Progress
- Dark mode toggle exists in HTML/CSS/JS but is partial and known-broken — S6 decision: finish or remove
- Smooth scroll polyfill still uses per-element forEach listeners — flagged since S4, still needs delegation refactor
- About section still has placeholder photo and bio
- No SEO meta tags yet

## Completed This Session
- IntersectionObserver sticky nav fully working (threshold: 0.1 on hero)
- Dark mode toggle infrastructure: button in nav, `.light-mode` body class, `body.light-mode` CSS overrides for bg + nav
- CSS variable system completed: all hardcoded hex replaced with var() references
- Card hover rule silently broken during variable sweep (hover rule still had raw `#e94560`) — found and fixed; comment added to CSS explaining the coupled pair
- Hero image corrected from `loading="lazy"` to `loading="eager"`
- Debug `console.log` statements and commented `alert()` removed from main.js

## Safety Rules
- Do not add CSS animation to the hero — removed in S2 for iOS layout shift, decision is final
- Email regex rejects `+` addresses intentionally — user's explicit product decision from S4, do not change
- Card hover requires BOTH rules: `border-left: 3px solid transparent` (base) + `border-left-color: var(--color-accent)` (hover); they were silently broken once already during variable sweep
- Footer CSS is at end of style.css in labelled block — both `.site-footer` and `.footer-inner p` must be there together
- Hero image must be `loading="eager"` — user corrected this from an erroneous `lazy` this session

## Last Actions
- Added CSS comment to card rules explaining the coupled border-left pair
- Confirmed card hover working again after fixing missed `#e94560` in hover rule
- Removed debug code from main.js

## Next Actions
- Review dark mode in browser with fresh eyes → decide: finish completely (15-20 more CSS rules) or remove toggle entirely
- Refactor smooth scroll polyfill from forEach per-element to single delegated document listener
- Add SEO og: and twitter: meta tags
- Audit all src/href paths for absolute paths that will 404 on GitHub Pages subdirectory

## Recon Notes
- Dark mode incompleteness discovered when user switched to light mode and saw dark cards floating on light background — described it as "dark islands"; form inputs discovered to be unusable (typed text invisible) by actually clicking into a field in light mode
- Card hover breakage discovered when user tested hover after the variable sweep session — CSS had silently stopped working; missed `#e94560` was in the `:hover` rule
- Hero lazy loading mistake caught when Claude specifically asked about the hero image loading attribute

## Background
→ read ~/Desktop/context-relay/research/STUDY4_CONTENT.md for full session logs

---

## Handoff6 — T6 Test Context (after S6)

# Handoff - portfolio-site - Session 6: Deployment Prep

## Current Goal
Site is deployed to GitHub Pages. All pre-deploy issues resolved. Remaining items are post-launch content tasks.

## Key Decisions
- Dark mode removed entirely → reviewed in browser, user confirmed it "looks like someone broke the CSS and half the page forgot to update — not a feature, looks like a bug"; removed toggle button HTML, `.nav-right` wrapper, all `.theme-toggle` CSS, `body.light-mode` CSS blocks, JS handler; nav reverted to brand + ul.nav-links (no wrapper div)
- Smooth scroll polyfill refactored to event delegation → single `document.addEventListener('click', ...)` with `e.target.closest('a[href^="#"]')`; one listener instead of N; handles dynamically added anchor links; `closest()` supported from Safari 9
- Absolute paths fixed to relative → `href="/style.css"` → `href="style.css"` (critical: would have loaded completely unstyled on GitHub Pages); `src="/images/photo.jpg"` → `src="images/photo.jpg"`; og: meta tags correctly use full absolute URLs (required for social scrapers)
- SEO tags added → `og:title`, `og:description`, `og:image` (placeholder path, tag in place), `og:type`, `og:url`, and full Twitter Card equivalents; `og:image` will 404 until real file created but tag infrastructure is correct
- Footer `.footer-inner p` rule restored for third time → was missing again; both footer rules now confirmed in labelled comment block together

## In Progress
- `og:image` file doesn't exist yet — user must create `images/og-preview.jpg` (1200×630px, JPG, <300KB) before sharing URL publicly; tag is in HTML waiting for it
- About section still has placeholder photo (`images/photo.jpg`) and bio text
- Contact form submits cosmetically only — no backend; Formspree identified as lowest-friction path for GitHub Pages static site when ready
- Hero still shows placeholder name

## Completed This Session
- Smooth scroll polyfill refactored to delegated listener — memory pattern resolved
- SEO meta tags added (og + Twitter Card)
- Path audit: 2 absolute paths fixed to relative; og: tags correctly use absolute URLs
- Dark mode toggle fully removed: HTML, CSS, JS all cleaned up
- Footer `.footer-inner p` restored (third restoration)
- Verified Safari smooth scroll + nav heading offset on live deployed URL
- Email regex confirmed unchanged and intentional on final pre-ship check

## Safety Rules
- Email regex intentionally rejects `name+work@gmail.com` addresses — confirmed by user in S4 and again during final S6 review: "my clients won't use plus addresses"; do not change this
- Do not add hero animation — removed in S2 for iOS layout shift, decision has been standing for 4 sessions
- Card hover requires BOTH rules: base `border-left: 3px solid transparent` + hover `border-left-color: var(--color-accent)`; silently broken once already; both must stay in the file
- Footer CSS: BOTH `.site-footer` AND `.footer-inner p` must live together in the Footer comment block at the end of style.css — this rule has been lost 3 times; if either is missing, the footer text renders full-white and full-size
- All src/href in HTML body must be relative paths (no leading `/`) — GitHub Pages serves from a subdirectory; absolute paths 404
- og: meta tag content attributes must use full absolute URLs — social scrapers need these to be standalone HTTP-resolvable

## Last Actions
- Pushed to GitHub Pages; verified live URL loads with correct styles, smooth scroll, and footer styling
- Final pre-ship email regex check — user looked at it and confirmed intentional
- Confirmed Safari smooth scroll + `scroll-margin-top: 70px` nav offset working on live URL

## Next Actions
- Create `images/og-preview.jpg` (1200×630, dark navy bg, coral-red accent, name/title) before sharing URL publicly
- Replace placeholder photo with real photo; write real bio and hero name
- When ready for real email delivery: integrate Formspree (add `action` URL to form, optionally use `fetch` POST for no-page-reload UX)
- If dark mode wanted later: use `@media (prefers-color-scheme: light)` to redefine `:root` variables — CSS variable system is already in place; would be cascade-only, no per-component overrides needed

## Recon Notes
- Dark mode removal decided after user did a fresh visual review at start of S6 — first honest look at the partial state led immediately to "let's remove it"
- Absolute path bug found during Claude-prompted path audit; stylesheet path was critical (entire page would have loaded unstyled on GitHub Pages)
- Footer rule missing again discovered when Claude specifically asked user to look at footer copyright text before pushing
- Smooth scroll delegation change: `closest()` Safari compatibility verified explicitly because Safari was the original reason for the polyfill

## Background
→ read ~/Desktop/context-relay/research/STUDY4_CONTENT.md for full session logs
