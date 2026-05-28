# Study 4 Data — Group A: Auto-Compaction Chain
Project: Portfolio website vibe coding (6 sessions)

---

## Summary1 — T1 Test Context (after S1)
*Input: S1 (~6,800 words) → compressed to ~1,000 words*

This is a single-page developer portfolio being built from scratch in plain HTML, CSS, and vanilla JavaScript. The project started with Bootstrap but abandoned it partway through the first session after the user hit the specificity wall trying to override Bootstrap's CSS custom properties for container padding. The decision was made to write everything from scratch, and the full Bootstrap CDN links and JavaScript bundle were removed. The replacement is a small custom reset and hand-written CSS that gives full visibility into every rule.

The page structure is in place: a fixed navigation bar at the top, followed by hero, about, projects, and contact sections, then a footer. All sections except hero and about are currently empty skeletons. The navigation is `position: fixed` with `z-index: 100`, using a dark background color slightly lighter than the page body to create a visible separation.

The color system is locked in. Background is `#1a1a2e`, the nav background is `#16213e`, and the accent color is `#e94560`, a coral-red that was chosen after testing burnt orange (`#e07b39`), bright orange (`#f47c3f`), and terra cotta (`#c9622f`) and rejecting all three. The orange family was ruled out entirely because it reads either as a sports team logo or a lifestyle brand depending on how saturated it is. The coral-red was the user's instinct and it landed immediately. All five colors are stored as CSS variables in a `:root` block: `--color-bg`, `--color-nav`, `--color-accent`, `--color-text`, `--color-text-muted`.

The CSS reset at the top of the file includes `box-sizing: border-box`, `margin: 0`, `padding: 0`, and `scroll-behavior: smooth` on `html`. The global `a` rule has `text-decoration: none` and `color: inherit`. The `color: inherit` was added specifically to neutralize the browser's user-agent stylesheet default link color, which was causing a hover flicker on the nav links. The flicker had two layers: a global `a { color: white }` rule the user had written early on during experimentation and forgotten about (removed first), and the underlying UA stylesheet default (neutralized by `color: inherit`). The flicker is mostly resolved but a very faint artifact may still appear on the first hover of a page load on certain browsers. This is noted as an open item to check next session.

The hero section is built with placeholder content: the name heading at `clamp(2.5rem, 6vw, 5rem)` with `line-height: 1.1` (tight for display type), a tagline in a muted color at `clamp(1rem, 2.5vw, 1.5rem)`, and a "See My Work" CTA button using `background-color: var(--color-accent)` with `opacity: 0.85` on hover. The max-width of the hero content is 700px and the layout is left-aligned, which is the more editorial approach. The hero links to `#projects`.

The about section has a two-column grid layout with a 280px photo column and a `1fr` text column, using `gap: 4rem` (3rem was tried and felt too tight). A placeholder image from an external service is in the photo column. The bio has placeholder text and the skill tags are present as `<span>` elements with a semi-transparent accent background and a thin accent border. Section headings use `.section-heading` with a `::after` pseudo-element that places a 50px × 3px coral-red bar beneath each heading, requiring `position: relative` on the heading and `content: ''` with `position: absolute` on the pseudo-element.

The `max-width: 1100px` with `margin: 0 auto` layout constraint is on all sections. The nav uses the same inner content width approach via `.nav-inner`. The footer uses `--color-nav` as its background to create subtle separation from the page.

Still open going into the next session: the projects and contact sections are empty skeletons. The nav hover flicker is mostly fixed but the residual first-hover artifact is noted and should be rechecked. All text content and the photo are placeholders.

---

## Summary2 — T2 Test Context (after S2)
*Input: Summary1 + S2 (~7,800 words) → compressed to ~1,000 words*

A single-page developer portfolio built in plain HTML, CSS, and vanilla JavaScript. Bootstrap was tried and abandoned in the first session when the user couldn't cleanly override the container and nav padding. Everything is custom-written with full CSS variable system.

The color scheme is locked: `--color-bg: #1a1a2e`, `--color-nav: #16213e`, `--color-accent: #e94560`, `--color-text: #e0e0e0`, `--color-text-muted: #8892b0`. The accent is a coral-red that replaced the orange family entirely after orange variants were rejected for looking like sports team logos or lifestyle brands. All colors use CSS custom properties throughout.

The nav hover flicker is now fully resolved. It took two sessions to close properly. In S1 the user found and removed a stale `a { color: white }` global rule that had been left in from early experimentation, which eliminated most of the flash. The remaining residual was the browser's user-agent stylesheet default link color, which surfaces briefly before more-specific CSS rules resolve. The fix was adding `color: inherit` to the global `a` reset rule. This completely zeros out the UA default so the `.nav-links a { color: var(--color-text-muted) }` rule is the only authority from first paint with no fallback values to flash through. During S2 a further stale rule was found: `.site-nav a { color: var(--color-text) }` left from early nav experiments. This was creating cascade ambiguity during transition starting-value calculation. Both were removed, and the flicker is confirmed gone across all three nav links on repeated hover. That bug is closed.

The hero tagline was iterated in S2. The user wanted to express caring about polish and detail without using overworked language. "Obsess" was rejected as performative. The final tagline is "Frontend engineer. The details are the whole point." — the two-part structure the user preferred, with a philosophical claim rather than a description. The hero renders hero name, tagline, and CTA button, all left-aligned, statically, with no entrance animation.

A CSS `fadeInUp` animation was tried on the hero elements with staggered delays. It caused a layout shift on mobile: `animation-fill-mode: both` combined with `transform: translateY(20px)` caused the browser to position elements 20px below their final location during the delay period, then trigger a layout recalculation when the animation started. On mobile the render pipeline is tight enough to make this visible as a jump at page load. The animation was removed entirely rather than patched. The hero now renders instantly with no motion, no layout shift.

The about section is working on both desktop and mobile. The circular photo required a specific approach: `border-radius: 50%` and `overflow: hidden` must go on the `.about-photo` container, not on the `<img>` element, and the container needs explicit `width: 280px; height: 280px`. Without the explicit height, the CSS Grid stretches the container to match the taller text column alongside it, making the image render as a non-square shape and the border-radius creates an oval rather than a circle. With the container's height locked and `overflow: hidden` enforcing the clip, the image fills the circular container regardless of its own dimensions. A 768px breakpoint collapses to single column with the photo centered at 200px.

The mobile navigation was reviewed: three short links fit on one line on all phone sizes, so no hamburger menu was added. This remains a deferred concern — if a fourth nav item is ever added, mobile overflow would need to be addressed. For now the nav is complete.

Still open: projects and contact sections are empty skeletons. About section and hero have placeholder content and photo. The `max-width: 700px` on `.hero-content` was confirmed as intentional left-aligned editorial layout.

---

## Summary3 — T3 Test Context (after S3)
*Input: Summary2 + S3 (~7,800 words) → compressed to ~1,000 words*

A single-page portfolio in plain HTML, CSS, and vanilla JavaScript. No frameworks. Full CSS variable system with five root variables. Dark navy background, coral-red accent, system font stack.

The nav hover flicker was resolved across two sessions — a stale global `a` rule and a stale `.site-nav a` rule were removed, and `color: inherit` was added to the global `a` reset to neutralize the browser UA default. The hero has a locked tagline: "Frontend engineer. The details are the whole point." A CSS entrance animation was tried and removed because it caused a mobile layout shift. The about section has a circular photo (container-clips pattern with explicit 280×280 dimensions required), responsive stacking at 768px, skill tags, and section heading accent bars via `::after`.

The Work section (formerly called Projects) was fully built in S3. The section rename touched five places: the HTML section `id`, every anchor `href` pointing to it, the section heading text, and the CSS ID selector. The CSS selector being left at `#projects` after the HTML was changed caused a silent bug where the section collapsed and the nav link appeared to do nothing on click. The fix was updating the CSS selector to `#work`. During the same edit session the footer's `margin-top: 4rem` was accidentally removed from the `.site-footer` rule — it was a proximity casualty of the CSS edits, not part of the rename itself. The footer CSS has been moved to the end of the file in a clearly labelled comment block to isolate it from the area that gets touched when sections are edited.

The Work section has six project cards in a CSS Grid with `grid-template-columns: repeat(3, 1fr)` and `gap: 1.5rem`. Three filter categories — Frontend, Backend, Design — plus All. The filter buttons use `data-filter` attributes and the cards use `data-tags`. JavaScript toggles `display: none/block` with an exact string match (`===`) so each card can only belong to one category. Filter state is managed by adding and removing an `.active` class on the buttons. The "All" button has the `.active` class hardcoded in the HTML for the correct initial state on page load.

The card hover effect is a `border-left` accent line: `border-left: 3px solid transparent` in the base state and `border-left-color: var(--color-accent)` in the hover state, with `transition: border-color 0.2s ease`. The transparent border in the base state pre-reserves the 3px space so the card doesn't shift sideways when the color appears. These two rules are coupled and must both be present. Box shadow was tried in three configurations (ring plus glow, glow alone, radial halo) and rejected each time — it reads as a UI "selected" state rather than a hover on dark backgrounds, and even at very low opacity it has an enterprise-dashboard heaviness that doesn't fit the site.

Responsive breakpoints: 2 columns at 768px (matching the about section breakpoint for consistency), 1 column at 480px. The filter bar gets `flex-wrap: wrap` at 480px as a safety net for narrow viewports. "View Project" links currently use `href="#"` as placeholders and will be replaced with real URLs when real content is added.

Still open: contact section is an empty skeleton. About and hero have placeholder content. The footer rule `.footer-inner p` is confirmed in the footer block. No animations anywhere.

---

## Summary4 — T4 Test Context (after S4)
*Input: Summary3 + S4 (~7,800 words) → compressed to ~1,000 words*

A single-page portfolio in plain HTML, CSS, and vanilla JavaScript. No frameworks, system fonts, full CSS variable system. Dark navy background (`#1a1a2e`), slightly lighter nav (`#16213e`), coral-red accent (`#e94560`). Bootstrap was abandoned in the first session. CSS entrance animation was tried and removed for causing mobile layout shift. Orange was rejected as accent color family.

The Work section has six cards in a three-column CSS Grid with `border-left` accent hover effect — a coupled pair of rules where the base state has `border-left: 3px solid transparent` (pre-reserves space) and hover changes the color. Tag filtering uses data-attributes with exact-string matching in vanilla JavaScript. Box shadow hover was explicitly rejected across three configurations as too UI-heavy on dark backgrounds and should not be reconsidered.

The contact form section was fully built in S4: three fields (name, email, message), no subject line, no phone. The form has `novalidate` to disable browser-native validation UI. Labels are uppercase with letter-spacing. Input fields use `--color-card` background with a subtle muted border and accent focus state. Validation runs on `blur`, not on submit. Each field has its own blur listener. A `validateField` function checks each field by name and calls `showFieldError` which either sets or clears the error text and the `.input-error` border class. The submit handler runs all validations as a final gate before showing the success message.

The email regex is intentionally limited and should not be changed: it rejects plus-sign addresses like `name+tag@domain.com`. The fix was offered and explicitly declined because clients reaching out through a portfolio contact form won't use plus addresses. This was a product decision, not an oversight.

The success message uses a `setTimeout` at 3000ms to hide after three seconds. The form resets immediately on valid submit via `e.target.reset()`. The user confirmed that clearing immediately and showing the success banner feels like the right order. No double-submit guard was added — it was considered and rejected as over-engineering for a contact form.

Safari smooth scroll: CSS `scroll-behavior: smooth` on the `html` element is not supported on older Safari (added in Safari 15.4 in 2022). A JavaScript polyfill was added using `document.querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', ...))` with `target.scrollIntoView({ behavior: 'smooth', block: 'start' })`. This per-element listener pattern was flagged at the time of writing as having a memory-leak-adjacent quality and was explicitly marked for refactor before deployment. The polyfill covers all anchor links on the page including the hero CTA button.

`scroll-margin-top: 70px` was added to the `section` rule to prevent the fixed nav from covering section headings when scrolling to them. This interacts with both the CSS `scroll-behavior` and the JS `scrollIntoView` polyfill. A duplicate `.section-heading::after` rule with `background-color: transparent` was found during S4 testing and removed — it was overriding the accent bar and making the Contact section heading bar invisible. It was a leftover from early experimentation.

Still open before deployment: smooth scroll polyfill uses per-element listeners and is marked for refactor to event delegation. About section and hero have placeholder content. Dark mode was not started. Footer CSS is at the end of the file in a labelled block — both `.site-footer` and `.footer-inner p` must remain together there.

---

## Summary5 — T5 Test Context (after S5)
*Input: Summary4 + S5 (~7,800 words) → compressed to ~1,000 words*

A single-page portfolio in plain HTML, CSS, and vanilla JavaScript. Dark navy theme, coral-red accent `#e94560`, system font stack, full CSS variable system in `:root`. Bootstrap abandoned in S1. No animations anywhere — CSS fadeInUp was tried in S2 and removed for causing iOS layout shift. Orange accent family rejected. Box shadow hover on project cards rejected across three configurations as too heavy on dark backgrounds.

The nav now has sticky behavior using `IntersectionObserver`. The observer watches `#hero`; when the hero exits the viewport, `.nav-scrolled` is added to `.site-nav`, giving it `background-color: rgba(22, 33, 62, 0.98)` and `box-shadow: 0 2px 20px rgba(0, 0, 0, 0.4)`. The `.site-nav` has `transition: background-color 0.3s ease, box-shadow 0.3s ease` so the change animates. The observer uses `{ threshold: 0.1 }` for an early trigger and the callback uses array destructuring `([entry])` since only one element is observed. This fires at most twice per scroll direction change — not on every frame — which is the core advantage over a scroll event listener.

A dark mode toggle was added, partially implemented, and is in a known broken state. The toggle button is in the nav, wrapped in a `.nav-right` flex container alongside the nav links. Clicking it adds `.light-mode` to `body`, changing the body background to `#f5f5f5` and the nav. Project cards, form inputs, skill tags, and all other elements with explicit dark background variables do not update. In light mode the form inputs show dark background with dark typed text — completely unreadable. This is broken in a functional sense, not just aesthetic. The partial implementation was accepted as "known debt" and the decision about whether to complete or remove it was deferred to S6.

The CSS variable system was fully swept in S5. Two new variables were added: `--color-card: #16213e` (same value as `--color-nav` currently but kept separate for semantic reasons — they're different surfaces) and `--color-border: rgba(136, 146, 176, 0.2)`. All hardcoded hex values in component rules were replaced with variable references. The `rgba()` tinted accent colors (used for skill tag backgrounds and the `.form-success` message) were left as raw values because CSS cannot do `rgba(var(--color-accent), 0.15)` cleanly with hex-string variables.

The card hover broke silently during the variable sweep: the `.project-card:hover` rule still had a hardcoded `#e94560` instead of `var(--color-accent)`. This caused the hover effect to stop working. It was fixed after the user noticed and reported it. A comment was added to both the base and hover rule explaining that the coupled pair must stay together.

The hero image was found to have `loading="lazy"` incorrectly applied. This was corrected to `loading="eager"`. Lazy loading on above-the-fold images can delay initial render and cause a blank flash on slow connections. Profile photo and any future project images below the fold should keep `loading="lazy"`.

The Safari smooth scroll polyfill is still using per-element listeners from S4 and is still flagged for refactor to event delegation before deployment. Debug `console.log` statements and a commented-out `alert()` were cleaned from `main.js`. `defer` on the script tag and `will-change` on the nav were both considered and correctly not added.

Open items before deployment: dark mode toggle in nav is broken — must either be completed fully or removed entirely before shipping. Per-element scroll listeners need refactor to event delegation. SEO meta tags not yet added. Paths not audited for GitHub Pages compatibility. About and hero still have placeholder content.

---

## Summary6 — T6 Test Context (after S6)
*Input: Summary5 + S6 (~7,800 words) → compressed to ~1,000 words*

A single-page portfolio in plain HTML, CSS, and vanilla JavaScript. Deployed to GitHub Pages. Dark navy theme only — `#1a1a2e` background, `#16213e` nav and card surfaces, `#e94560` coral-red accent. Full CSS variable system. System font stack with zero external font loading. No frameworks, no build step, no animations.

The Safari smooth scroll polyfill was refactored in S6 from per-element listeners to a single delegated document listener. The old `querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', ...))` pattern was replaced with `document.addEventListener('click', function(e) { const anchor = e.target.closest('a[href^="#"]'); if (!anchor) return; ... })`. The `closest()` method handles clicks on child elements inside anchors and has solid Safari support since Safari 9. The single listener has no closure references per element, handles dynamically added links automatically, and doesn't accumulate if the code runs more than once. The `scroll-margin-top: 70px` on all sections is unchanged and works with the delegated listener.

Dark mode was reviewed with fresh eyes in S6 and removed entirely. In light mode the project cards remained dark navy, the form inputs remained dark navy with light-colored typed text becoming invisible against the dark background, the skill tags remained dark, the footer remained dark — roughly half the page was visually broken. The partial state was described as "dark islands floating in a light page" and confirmed not passable even as an intentional design choice because the form inputs were functionally unusable. The toggle button was removed from the HTML, the `.nav-right` wrapper div was removed (nav links are back to a direct `<ul>` inside `.nav-inner`), `.theme-toggle` and `.nav-right` CSS was removed, `body.light-mode` CSS was removed, and the toggle JS handler was removed. The site is dark theme only. The CSS variable system remains in place as the right infrastructure for a proper `prefers-color-scheme` implementation later, which would use a media query to redefine root variables rather than per-component overrides.

SEO meta tags were added: `<meta name="description">`, Open Graph tags (`og:type`, `og:url`, `og:title`, `og:description`, `og:image`), and Twitter Card equivalents. The `og:image` points to `images/og-preview.jpg` which does not yet exist — the tag is in place waiting for the file. OG tags use absolute URLs because social scrapers fetch them in standalone HTTP requests without page context. All other paths in the HTML use relative paths.

Two absolute paths were corrected for GitHub Pages compatibility: `href="/style.css"` was the critical one — with a leading slash on a GitHub Pages subdirectory deployment, the stylesheet would 404 and the page would load completely unstyled. Fixed to `href="style.css"`. The profile photo `src="/images/photo.jpg"` was also corrected to `src="images/photo.jpg"`. The script tag `src="main.js"` was already correct.

The `.footer-inner p` rule was restored for the third time in the project's history. The footer comment block at the end of the CSS file had `.site-footer` but the companion `.footer-inner p` rule had been dropped again during S5 edits. Both rules are now confirmed present together in the footer block. The footer styling has been displaced in every session where significant CSS editing occurred near that area.

At deployment the site is confirmed working: nav IntersectionObserver sticky behavior, blur-validated contact form with intentionally limited email regex (rejects plus-sign addresses — product decision, do not change), six project cards with tag filtering and border-left hover, circular about photo with container-clips approach, all responsive breakpoints, Safari smooth scroll via delegated listener.

Still outstanding before publicly sharing: create `images/og-preview.jpg` at 1200×630px before sharing the URL anywhere. Replace placeholder name, photo, bio, tagline, and project content. Optionally wire the contact form to Formspree or similar for actual email delivery.
