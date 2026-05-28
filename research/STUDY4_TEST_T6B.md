# Study 4 — Test T6B (Agent B answer using Handoff6 only)

## Q51

**Q51**: The portfolio website was built across 6 sessions. Here is a comprehensive description based solely on the Handoff6 context document:

### Overall Structure
The site is a single-page portfolio with the following sections in HTML:
- Fixed position navigation bar (brand link + 3 nav links: About, Work, Contact)
- Hero section (name + tagline + coral-red CTA button linking to `#work`)
- About section (two-column grid: circular photo + bio text + skill tags)
- Work section (project card gallery with filter buttons above)
- Contact section (form with name, email, message, submit)
- Footer

### Technologies and Approaches
- **HTML/CSS/JS only** — no framework. Bootstrap was dropped in S1 due to CSS specificity conflicts.
- **CSS written from scratch**, ~60 lines initially; CSS variables defined in `:root`:
  - `--color-bg: #1a1a2e`
  - `--color-nav: #16213e`
  - `--color-accent: #e94560` (coral red)
  - `--color-text: #e0e0e0`
  - `--color-text-muted: #8892b0`
  - `--color-card: #16213e`
  - `--color-border: rgba(136, 146, 176, 0.2)`
- **No CSS animations** — hero animation removed in S2 (caused iOS layout shift); no animation added since.
- **Single responsive breakpoint** at `768px`; additional breakpoint at `480px` for the card grid and filter bar.
- **Footer CSS** lives at the end of `style.css` in a clearly labelled comment block (intentional; restored 3 times across sessions). Both `.site-footer` and `.footer-inner p` must reside there together.
- **System fonts only** — no Google Fonts or external CDN; intentional for zero external loading overhead.

### JavaScript Features
- **Tag filter system**: `data-filter` / `data-tags` attribute matching using `===` exact string match; `display: block/none` toggling; `.active` class moves between filter buttons.
- **Blur-triggered form validation**: `validateField()` + `showFieldError()` functions; submit handler runs all validations as final gate; email regex intentionally rejects `+` addresses (user's explicit product decision confirmed in S4 and again in S6 pre-ship review).
- **Safari smooth scroll polyfill**: Refactored in S6 from per-element `forEach` listeners to a single **event-delegated** `document.addEventListener('click', ...)` using `e.target.closest('a[href^="#"]')`. This resolves the memory-leak-adjacent pattern flagged since S4. `scroll-margin-top: 70px` on all sections prevents fixed nav from clipping headings.
- **IntersectionObserver sticky nav**: Observes `#hero`; when hero exits viewport, adds `.nav-scrolled` class with semi-opaque background and box-shadow. Fires once per direction, not 60x/sec.
- **Dark mode toggle REMOVED in S6**: Toggle button HTML, `.nav-right` wrapper div, all `.theme-toggle` CSS, `body.light-mode` CSS blocks, and JS handler were fully deleted. Nav reverted to brand + `ul.nav-links` (no wrapper div). Reason: partial implementation "looked like someone broke the CSS and half the page forgot to update — not a feature, looks like a bug."

### Key Decisions Across Sessions
- Orange accent rejected (3 variants: "sports team," "aggressive," "real estate brand"); coral red `#e94560` settled in S1.
- Section renamed from "Projects" to "Work" in S3 ("Work sounds more like a designer would say it").
- Card hover: `border-left: 3px solid transparent` base + `border-left-color: var(--color-accent)` on hover. Box-shadow tried in 3 configurations, all rejected. The two rules must coexist; removing either silently breaks the effect.
- Form success message: cosmetic only (no backend), shows for 3 seconds then hides; form resets immediately.
- Email regex rejects `name+work@gmail.com` addresses — confirmed intentional in S4 and again during S6 pre-ship review.
- Hero image must use `loading="eager"` (corrected from erroneous `lazy` in S5).

### Deployment State
- **Deployed to GitHub Pages** and verified live.
- Path audit completed in S6: 2 absolute paths (`href="/style.css"` and `src="/images/photo.jpg"`) fixed to relative paths (`href="style.css"`, `src="images/photo.jpg"`). Absolute paths would have caused a completely unstyled page on GitHub Pages.
- **SEO meta tags added**: `og:title`, `og:description`, `og:image`, `og:type`, `og:url`, and full Twitter Card equivalents. `og:image` points to `images/og-preview.jpg` which does not yet exist — tag infrastructure is in place but the file will 404 until created (1200×630px, <300KB).
- Safari smooth scroll + `scroll-margin-top: 70px` nav offset verified working on the live URL.

### Known Limitations / Remaining Post-Launch Tasks
- **No real project content**: all 6 Work cards have placeholder titles and `href="#"` links.
- **No real photo**: About section uses placeholder image (`images/photo.jpg`) with placeholder bio.
- **No form backend**: contact form submit is cosmetic only; Formspree identified as lowest-friction integration path when ready.
- **`og:image` placeholder**: `images/og-preview.jpg` doesn't exist; must be created before sharing URL publicly.
- Hero still shows placeholder name.

---

**Score**: 2/2 — full — All major elements from the ground truth are present and specific:
- Structure (fixed nav, hero, about, Work gallery, contact form, footer) ✓
- CSS approach (no framework, CSS variables with exact hex values `#1a1a2e` and `#e94560`, no animations, 768px breakpoint, footer CSS at end of file) ✓
- JS (tag filter with exact-match, blur validation, IntersectionObserver sticky nav, event-delegated scroll refactored in S6, dark mode toggle REMOVED) ✓
- Deployment (GitHub Pages, relative paths fixed, SEO meta tags added) ✓
- Known limitations (no real project content, no real photo, no form backend, og:image placeholder) ✓
