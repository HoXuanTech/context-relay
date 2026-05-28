# Test Results: T6A (Auto-Compact, T6 — Architecture Overview)
Context: Summary6 | Question: Q51
---

**Q51** You've been building this portfolio website across 6 sessions. Describe what has been built: overall structure, technologies/approaches used, key decisions made, and current deployment state.

**Answer:**

The project is a single-page developer portfolio website built entirely in plain HTML, CSS, and vanilla JavaScript. There are no frameworks, no build step, no external font loading, and no server-side components — it deploys as static files directly to GitHub Pages.

**HTML Structure**

The page is a single HTML file with the following sections in order: a fixed navigation bar (`.site-nav`), hero, about (`#about`), work (`#work`), contact, and a footer. The nav contains a brand element and three anchor links (About, Work, Contact) inside a `.nav-inner` container. The `<script src="main.js">` tag uses a relative path and was already correct at deployment. The stylesheet is linked as `href="style.css"` (relative — a leading-slash bug was fixed in S6 before deployment). SEO meta tags were added in S6: `<meta name="description">`, Open Graph tags (`og:type`, `og:url`, `og:title`, `og:description`, `og:image`), and Twitter Card equivalents. OG/Twitter tags use absolute URLs because social scrapers fetch them without page context; all other paths in the HTML use relative paths. The `og:image` points to `images/og-preview.jpg` which does not yet exist — the tag is in place waiting for the file.

**CSS Approach**

CSS is hand-written from scratch. Bootstrap was started in S1 and abandoned when the user hit the specificity wall trying to override Bootstrap's CSS custom properties for container padding. The full Bootstrap CDN and JS bundle were removed and replaced with a custom reset.

The reset includes `box-sizing: border-box`, `margin: 0`, `padding: 0`, `scroll-behavior: smooth` on `html`, and `a { color: inherit; text-decoration: none }`. The `color: inherit` on the global `a` rule is critical — it neutralizes the browser's user-agent stylesheet default link color that was causing a nav hover flicker (fixed in S2).

Full CSS custom property system in `:root` with seven variables:
- `--color-bg: #1a1a2e` (dark navy background)
- `--color-nav: #16213e` (slightly lighter navy for nav)
- `--color-accent: #e94560` (coral-red accent — orange family was tried and rejected in S1 for looking like a sports team logo or lifestyle brand)
- `--color-text: #e0e0e0`
- `--color-text-muted: #8892b0`
- `--color-card: #16213e` (same value as `--color-nav` but kept semantically separate)
- `--color-border: rgba(136, 146, 176, 0.2)`

No hardcoded hex values remain after the full variable sweep in S5, with the exception of `rgba()` tinted accent values (skill tag backgrounds, `.form-success`) which cannot cleanly use CSS variables with hex-string values.

Section headings use a `.section-heading` class with a `::after` pseudo-element placing a 50px × 3px coral-red accent bar beneath each heading. All section content is constrained with `max-width: 1100px; margin: 0 auto`. All sections have `scroll-margin-top: 70px` to prevent the fixed nav from clipping section headings on anchor scroll.

No animations anywhere — a CSS `fadeInUp` entrance animation was tried in S2 and removed because it caused a layout shift on iOS (the `transform: translateY(20px)` combined with `animation-fill-mode: both` repositioned elements before the animation started).

**JavaScript Features (main.js — flat, no modules)**

1. **Project card filter:** Reads `data-filter` attribute on filter buttons and `data-tags` on cards; toggles `display: none/block` using exact string match (`===`). Filter state managed by `.active` class on buttons. "All" button has `.active` hardcoded in HTML for correct initial state.

2. **Contact form validation:** `validateField` and `showFieldError` functions. Each input field has its own `blur` listener — validation triggers on field exit, not on submit. Submit handler runs all validations as a final gate. On valid submit: shows `#form-success`, hides it after 3000ms via `setTimeout`, resets the form immediately with `e.target.reset()`. No double-submit guard (intentionally not added). No backend — the form does not transmit data anywhere. Contact form wiring to Formspree or similar is deferred as a future task.

3. **IntersectionObserver sticky nav:** Watches `#hero` with `{ threshold: 0.1 }`. When hero exits viewport, adds `.nav-scrolled` class to `.site-nav`, applying `background-color: rgba(22, 33, 62, 0.98)` and `box-shadow: 0 2px 20px rgba(0, 0, 0, 0.4)`. Transition on the nav animates the change. Fires at most twice per scroll direction change — not on every frame.

4. **Safari smooth scroll (delegated listener):** A single `document.addEventListener('click', ...)` handler using `e.target.closest('a[href^="#"]')` to handle anchor clicks. This replaced a per-element `querySelectorAll` + `forEach` + `addEventListener` pattern from S4 that was flagged as memory-leak-adjacent. The delegated approach has no per-element closures, handles dynamically added links automatically, and does not accumulate if run more than once. Uses `scrollIntoView({ behavior: 'smooth', block: 'start' })`.

**Sections**

- **Nav:** Fixed position, `z-index: 100`, dark navy background. Sticky opacity/shadow behavior via IntersectionObserver. Brand name + three links (About, Work, Contact) directly in `.nav-inner` as a `<ul>` — the `.nav-right` wrapper div and dark mode toggle button were added in S5 and fully removed in S6.
- **Hero:** Placeholder name, locked tagline ("Frontend engineer. The details are the whole point."), CTA button linking to `#work`. Left-aligned editorial layout, `max-width: 700px` on `.hero-content`. Hero image has `loading="eager"` (corrected from `loading="lazy"` in S5 — above-fold images must not be lazy loaded).
- **About:** Two-column CSS Grid — 280px photo column and `1fr` text column, `gap: 4rem`. Circular photo requires `.about-photo` container with both `width: 280px` AND `height: 280px` explicitly set (without height, CSS Grid stretches to match text column height, making the border-radius oval instead of circular). Responsive: single column at 768px, photo 200px centered. Skill tags as `<span>` elements with semi-transparent accent background and thin accent border. Bio and photo are still placeholders.
- **Work (formerly Projects):** CSS Grid `repeat(3, 1fr)` at desktop, 2 columns at 768px, 1 column at 480px. Six project cards with `data-tags`. Card hover effect: `border-left: 3px solid transparent` in base state (pre-reserves space), `border-left-color: var(--color-accent)` in hover state — these two rules are coupled and must both be present. Box shadow hover was tried in three configurations in S3 and rejected each time as too UI-heavy on dark backgrounds. Filter bar uses `flex-wrap: wrap` at 480px. "View Project" links use `href="#"` placeholders.
- **Contact:** Three-field form (name, email, message — no subject, no phone), `novalidate` attribute, uppercase letter-spaced labels, accent focus states. Email regex intentionally rejects plus-sign addresses (`name+tag@domain.com`) — this was a product decision made in S4, explicitly declined when a fix was offered, and confirmed again before deployment in S6. Do not change.
- **Footer:** `.site-footer` and `.footer-inner p` rules both isolated at the end of the CSS file in a labeled comment block. The footer rule has been displaced and lost in three separate sessions (S3, S4/S5, S6) during CSS edits near adjacent rules — the comment block isolation is the current mitigation.

**Key Decisions Made**

- Bootstrap abandoned S1 (specificity conflicts)
- Orange accent family rejected S1 (looked like sports team / lifestyle brand)
- CSS entrance animation removed S2 (iOS layout shift)
- Section renamed "Projects" → "Work" in S3 (touched 5 places: HTML id, all href anchors, section heading text, CSS selector — missing the CSS selector caused a silent bug where the section collapsed)
- Box shadow card hover rejected S3 across three configurations (too UI-heavy on dark backgrounds)
- Plus-sign email regex limitation accepted as product decision S4 (do not change)
- Dark mode toggle added S5 (partial — only updated body/nav, left cards and form inputs dark), reviewed in browser S6 as "dark islands floating in a light page," confirmed functionally broken (form inputs unreadable), and removed entirely in S6
- Safari smooth scroll refactored from per-element listeners to single delegated document listener in S6
- Absolute paths corrected to relative paths in S6 (`href="/style.css"` → `href="style.css"`, `src="/images/photo.jpg"` → `src="images/photo.jpg"`) — the stylesheet path was the critical one; a leading slash on GitHub Pages subdirectory deployment would 404 and load the page completely unstyled

**Current Deployment State**

Deployed to GitHub Pages. All features confirmed working in browser before push: nav links, scroll behavior, circular photo, skill tags, six project cards, all three filter categories (Frontend/Backend/Design/All), border-left hover effect, contact form blur validation, submit success message with 3-second timeout, footer styling. Safari smooth scroll verified with `scroll-margin-top: 70px` working correctly. Relative paths resolved correctly through GitHub Pages subdirectory.

**Known Issues / Outstanding Items**

- `images/og-preview.jpg` does not exist — the OG meta tag is in place but the file must be created (1200×630px, JPG, under 300KB) before sharing the URL publicly
- All content is still placeholder: name, photo (`images/photo.jpg`), bio, tagline, and project cards
- Contact form has no backend — submissions are cosmetic only; Formspree integration deferred as a future task
- Dark mode is not implemented; the CSS variable system is the correct infrastructure for a future `prefers-color-scheme` media query implementation that redefines root variables

---

**Coverage assessment:**

- **S1** — Fully covered: Bootstrap abandonment, color system establishment, HTML section scaffolding, nav hover flicker (partial), hero and about section structure, CSS reset, section heading `::after` bars.
- **S2** — Fully covered: nav hover flicker root cause and final fix, hero tagline locked, CSS animation tried and removed (iOS layout shift), circular photo container-clips pattern, 768px responsive stacking.
- **S3** — Fully covered: Work section card grid, tag filtering, box shadow rejection, border-left hover effect, "Projects" → "Work" rename and the CSS selector bug it caused, footer CSS relocation.
- **S4** — Fully covered: contact form construction, blur validation, email regex product decision, setTimeout success message, Safari smooth scroll polyfill (per-element), scroll-margin-top.
- **S5** — Fully covered: IntersectionObserver sticky nav, partial dark mode (broken state), CSS variable sweep, card hover regression and fix, hero image lazy-load correction.
- **S6** — Fully covered: smooth scroll delegation refactor, dark mode removal, SEO meta tags, absolute-path fixes, footer rule restoration, GitHub Pages deployment confirmation, outstanding items.

No gaps — Summary6 contains a complete cumulative account of all six sessions.
