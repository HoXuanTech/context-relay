# Study 4 — T5B Test Answers (Handoff5, Group B)

Source section: Handoff5 — T5 Test Context (after S5)
Date answered: 2026-05-23
Answering agent: Claude Code (Sonnet 4.6)

---

**Q41**: What is the intentional limitation in the email validation that must NOT be fixed?

The email regex (`/^[a-zA-Z0-9._%\-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/`) intentionally rejects `+` addresses (e.g., `name+work@gmail.com`). The Safety Rules state: "Email regex rejects `+` addresses intentionally — user's explicit product decision from S4, do not change." The user was offered the fix and explicitly declined: "my clients won't use plus addresses, it's a contact form not a mission-critical system."

**Score**: 2 — full and specific answer

---

**Q42**: What is the Safari smooth scroll polyfill's current implementation issue, and what is the planned fix?

Current issue: the polyfill uses per-element event listeners via `forEach` — described as "memory-leak-adjacent." Each anchor element gets its own listener instead of one shared listener.

Planned fix (listed under Next Actions): "Refactor smooth scroll polyfill from forEach per-element to single delegated document listener."

**Score**: 2 — full and specific answer

---

**Q43**: Why was IntersectionObserver chosen for the sticky nav instead of a scroll event listener?

The context states it "observes `#hero`; when hero exits viewport adds `.nav-scrolled` class... fires once per direction, not 60x/sec." The "not 60x/sec" phrase directly gives the rationale — IntersectionObserver fires only on state change (hero in/out of viewport), whereas a scroll event listener fires at the display refresh rate (~60 times per second), making it far more performance-expensive.

**Score**: 2 — full and specific answer

---

**Q44**: What is the current state of dark mode, and what is the critical constraint about it?

Current state: dark mode toggle exists in HTML/CSS/JS but is partial and known-broken. The toggle changes body background and nav color only; project cards, form inputs, about section, and skill tags all stay dark because hardcoded `background-color` values don't cascade from body. Form inputs are unusable in light mode (dark bg + inherited dark text = invisible typed text). The user described the result as "dark islands."

Critical constraint: S6 must make a binary decision — either finish properly (estimated 15–20 more CSS rules) or remove the toggle entirely. It must not ship in its current partial state.

**Score**: 2 — full and specific answer

---

**Q45**: What bug appeared after the CSS variable system was introduced in S5?

The card hover rule was silently broken during the variable sweep. The hover rule (`:hover { border-left-color: ... }`) still had the raw hex value `#e94560` instead of `var(--color-accent)`, so it was missed during the sweep. The user discovered it when testing hover after the session — the hover effect had silently stopped working. It was fixed and a comment was added to the CSS explaining the coupled border-left pair.

**Score**: 2 — full and specific answer

---

**Q46**: What was wrong with the hero image's lazy loading attribute, and how was it corrected?

The user had mistakenly added `loading="lazy"` to all images including the hero image. The hero is above the fold and must load immediately, so `loading="lazy"` was incorrect. It was corrected to `loading="eager"`. Below-the-fold images correctly continue to use `loading="lazy"`. The Safety Rules now state: "Hero image must be `loading='eager'` — user corrected this from an erroneous `lazy` this session."

**Score**: 2 — full and specific answer

---

**Q47**: What CSS variables does the variable system include after the S5 refactor?

Original variables (from S1): `--color-bg: #1a1a2e`, `--color-nav: #16213e`, `--color-accent: #e94560`, `--color-text: #e0e0e0`, `--color-text-muted: #8892b0`

New variables added in S5: `--color-card: #16213e`, `--color-border: rgba(136, 146, 176, 0.2)`

Note: `rgba()` tinted accent values were left as raw values because CSS cannot do `rgba(var(--color-accent), 0.15)` cleanly.

**Score**: 2 — full and specific answer

---

**Q48**: What is the status of dark mode at the end of S5?

At the end of S5, dark mode is partial and known-broken. The toggle infrastructure exists (button in nav, `.light-mode` body class, `body.light-mode` CSS overrides for bg + nav), but it only changes the body background and nav color. Project cards, form inputs, about section, and skill tags remain dark in light mode. Form inputs are unusable in light mode. The decision on whether to finish or remove it is explicitly deferred to S6. (This is the same factual answer as Q44, asked from an end-of-session framing.)

**Score**: 2 — full and specific answer

---

**Q49**: Why were `will-change` and `defer` not added to the codebase in S5?

The Handoff5 context does not mention `will-change` or `defer` at all. There is no explanation for why they were or were not added.

**Score**: 0 — cannot answer — these terms do not appear anywhere in the Handoff5 section

---

**Q50**: What are the open items entering S6?

From the "In Progress" and "Next Actions" sections of Handoff5:

In Progress:
1. Dark mode toggle exists but is partial and known-broken — S6 decision: finish or remove
2. Smooth scroll polyfill still uses per-element forEach listeners — needs delegation refactor (flagged since S4)
3. About section still has placeholder photo and bio
4. No SEO meta tags yet

Next Actions (entering S6):
1. Review dark mode in browser → decide: finish completely (15–20 more CSS rules) or remove toggle entirely
2. Refactor smooth scroll polyfill from forEach per-element to single delegated document listener
3. Add SEO og: and twitter: meta tags
4. Audit all src/href paths for absolute paths that will 404 on GitHub Pages subdirectory

**Score**: 2 — full and specific answer

---

## Summary Table

| Q   | Score | Notes |
|-----|-------|-------|
| Q41 | 2     | Full — regex behavior, rationale, and user quote all in context |
| Q42 | 2     | Full — issue (memory-leak-adjacent forEach) and fix (delegation) both stated |
| Q43 | 2     | Full — "not 60x/sec" directly states the performance rationale |
| Q44 | 2     | Full — broken state, specific broken components, and S6 constraint described |
| Q45 | 2     | Full — missed raw `#e94560` in hover rule during variable sweep |
| Q46 | 2     | Full — wrong attribute (lazy), correct attribute (eager), reason (above fold) |
| Q47 | 2     | Full — all 7 variables named; raw rgba exception noted |
| Q48 | 2     | Full — same substance as Q44, confirmed from end-of-session framing |
| Q49 | 0     | Cannot answer — `will-change` and `defer` not mentioned in Handoff5 |
| Q50 | 2     | Full — all 4 in-progress items and 4 next actions listed |

SCORES: Q41=2,Q42=2,Q43=2,Q44=2,Q45=2,Q46=2,Q47=2,Q48=2,Q49=0,Q50=2
