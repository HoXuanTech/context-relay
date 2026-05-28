# Study 4 — Test T5A
Context: Summary5 (after S5)
Date: 2026-05-23

---

**Q41**: What is the intentional limitation in the email validation that must NOT be fixed?

The email regex intentionally rejects plus-sign addresses like `name+tag@domain.com`. This was a product decision — explicitly not an oversight. The fix was offered and explicitly declined because clients reaching out through a portfolio contact form won't use plus addresses. It must not be changed.

**Score**: 2/2 — full and specific answer

---

**Q42**: What is the Safari smooth scroll polyfill's current implementation issue, and what is the planned fix?

Current issue: The polyfill uses per-element listeners — `document.querySelectorAll('a[href^="#"]').forEach(anchor => anchor.addEventListener('click', ...))` — which has a memory-leak-adjacent quality and was explicitly marked for refactor. Planned fix: Refactor to event delegation (a single delegated document listener) before deployment.

**Score**: 2/2 — full and specific answer

---

**Q43**: Why was IntersectionObserver chosen for the sticky nav instead of a scroll event listener?

IntersectionObserver fires at most twice per scroll direction change — not on every frame. That is the core advantage named in the context over a scroll event listener, which fires continuously on every scroll event.

**Score**: 2/2 — full and specific answer

---

**Q44**: What is the current state of dark mode, and what is the critical constraint about it?

Dark mode is partially implemented and in a known broken state. The toggle adds `.light-mode` to `body`, updating the body background to `#f5f5f5` and the nav, but project cards, form inputs, skill tags, and all other elements with explicit dark background variables do not update. In light mode, form inputs show a dark background with dark typed text — completely unreadable. It is broken in a functional sense, not just aesthetic. Critical constraint: it must either be completed fully or removed entirely before shipping. The decision was deferred to S6.

**Score**: 2/2 — full and specific answer

---

**Q45**: What bug appeared after the CSS variable system was introduced in S5?

The card hover effect broke silently. The `.project-card:hover` rule still had a hardcoded `#e94560` instead of `var(--color-accent)` after the sweep, causing the hover effect to stop working. The user noticed and reported it. It was fixed, and a comment was added to both the base and hover rules explaining that the coupled pair must stay together.

**Score**: 2/2 — full and specific answer

---

**Q46**: What was wrong with the hero image's lazy loading attribute, and how was it corrected?

The hero image had `loading="lazy"` incorrectly applied. It was corrected to `loading="eager"`. Reason: lazy loading on above-the-fold images can delay initial render and cause a blank flash on slow connections. Profile photo and future project images below the fold should keep `loading="lazy"`.

**Score**: 2/2 — full and specific answer

---

**Q47**: What CSS variables does the variable system include after the S5 refactor?

After S5, the full variable set in `:root` is:
- `--color-bg`
- `--color-nav`
- `--color-accent`
- `--color-text`
- `--color-text-muted`
- `--color-card: #16213e` (added in S5 — same value as `--color-nav` but kept separate for semantic reasons, as they are different surfaces)
- `--color-border: rgba(136, 146, 176, 0.2)` (added in S5)

Note: `rgba()` tinted accent colors (for skill tag backgrounds and `.form-success`) were left as raw values because CSS cannot cleanly do `rgba(var(--color-accent), 0.15)` with hex-string variables.

**Score**: 2/2 — full and specific answer

---

**Q48**: What is the status of dark mode at the end of S5?

Dark mode is partially implemented and in a known broken state. The partial implementation was accepted as "known debt" and the decision about whether to complete it fully or remove it entirely was deferred to S6.

**Score**: 2/2 — full and specific answer

---

**Q49**: Why were `will-change` and `defer` not added to the codebase in S5?

The context states they "were both considered and correctly not added" but does not provide specific reasoning for each in Summary5. Only the conclusion is recorded — that not adding them was the correct decision.

**Score**: 1/2 — partial — context confirms they were considered and rejected but gives no specific reasoning for why each was excluded

---

**Q50**: What are the open items entering S6?

1. Dark mode toggle in nav is broken — must be completed fully or removed entirely before shipping.
2. Per-element scroll listeners (Safari smooth scroll polyfill) need refactor to event delegation.
3. SEO meta tags not yet added.
4. Paths not audited for GitHub Pages compatibility.
5. About and hero still have placeholder content.

**Score**: 2/2 — full and specific answer

---

## Raw Scores

SCORES: Q41=2,Q42=2,Q43=2,Q44=2,Q45=2,Q46=2,Q47=2,Q48=2,Q49=1,Q50=2

**Total: 19/20**
