# Study 4 — T2A Test Answers
Agent: Claude Code (claude-sonnet-4-6)
Source context: STUDY4_DATA_A.md § Summary2 — T2 Test Context (after S2)
Date: 2026-05-23

---

**Q11**: What CSS constraint was established about the nav styling that must be respected in all future sessions?

The nav hover flicker was fully resolved by removing two stale rules — a global `a { color: white }` rule (removed in S1) and `.site-nav a { color: var(--color-text) }` (removed in S2) — plus adding `color: inherit` to the global `a` reset rule. The constraint implied is that `.nav-links a { color: var(--color-text-muted) }` must be the only authority for nav link color from first paint; no competing or stale color declarations should be introduced on nav link selectors.

**Score**: 1 — partial — The context describes what was done to resolve the flicker but does not state a forward-looking constraint in explicit "must be respected" language. The implied constraint is clear (no stale color rules on nav links), but it is inferred rather than directly stated.

---

**Q12**: What are the two core CSS color values that define the site's visual identity?

`--color-bg: #1a1a2e` (dark navy background) and `--color-accent: #e94560` (coral-red accent). These two anchor the visual identity — the navy is the base canvas and the coral-red is the defining accent that replaced the entire orange family.

**Score**: 2 — full — Both values and their roles are explicitly stated in the Summary2 context.

---

**Q13**: What was the explicit decision about CSS animations for the hero section, and what caused it?

The decision was to remove the CSS `fadeInUp` animation entirely rather than patch it. The cause was a mobile layout shift: `animation-fill-mode: both` combined with `transform: translateY(20px)` positioned elements 20px below their final location during the delay period, then triggered a layout recalculation when the animation started. On mobile the render pipeline is tight enough to make this visible as a jump at page load. The hero now renders instantly with no motion, no layout shift.

**Score**: 2 — full — The decision, the specific CSS properties involved, and the exact cause are all stated in the context.

---

**Q14**: How was the circular photo effect achieved for the about section, and why wasn't border-radius: 50% on the img tag sufficient?

`border-radius: 50%` and `overflow: hidden` were placed on the `.about-photo` container div (not on the `<img>` element), and the container was given explicit `width: 280px; height: 280px`. Applying `border-radius: 50%` to the `<img>` tag alone was insufficient because CSS Grid stretches the container to match the height of the adjacent taller text column, making the container non-square. Without the explicit height locked on the container, the border-radius creates an oval rather than a circle. With `overflow: hidden` on the fixed-dimension container, the image is clipped into a true circle regardless of its own dimensions.

**Score**: 2 — full — The approach, the required properties, and the reason the img-tag approach fails are all explicitly in the context.

---

**Q15**: What is the final tagline used in the hero section after multiple iterations?

"Frontend engineer. The details are the whole point."

**Score**: 2 — full — Stated verbatim in the context. "Obsess" was rejected as performative and the two-part philosophical structure was the user's preferred form.

---

**Q16**: What is the current mobile layout status at the end of S2?

The about section collapses to a single column at a 768px breakpoint with the photo centered at 200px. The mobile navigation was reviewed and no hamburger menu was added — three short links fit on one line on all phone sizes. A hamburger menu is deferred: if a fourth nav item is ever added, mobile overflow would need to be addressed. For now the nav is considered complete.

**Score**: 2 — full — Both the about section mobile behavior and the nav mobile status are explicitly described in the context.

---

**Q17**: What were the two root causes of the nav hover flicker, and how was each addressed?

Root cause 1: A stale global `a { color: white }` rule left over from early experimentation. Fix: found and removed in S1, which eliminated most of the flash.

Root cause 2: The browser's user-agent stylesheet default link color, which surfaces briefly before more-specific CSS rules resolve. Fix: `color: inherit` was added to the global `a` reset rule, zeroing out the UA default so `.nav-links a { color: var(--color-text-muted) }` is the only authority from first paint.

(Additional: a third contributing factor found in S2 — `.site-nav a { color: var(--color-text) }` — was creating cascade ambiguity during transition starting-value calculation and was also removed.)

**Score**: 2 — full — Both root causes and their fixes are explicitly stated. The third factor is also documented in context.

---

**Q18**: What CSS property structure is required to make the about photo circular?

The following must go on the `.about-photo` container (not the `<img>`):
- `border-radius: 50%`
- `overflow: hidden`
- `width: 280px`
- `height: 280px` (explicit height is required — without it, CSS Grid stretches the container to match the taller adjacent text column, producing an oval)

**Score**: 2 — full — All four required properties and the reason explicit height is necessary are stated in the context.

---

**Q19**: What must NOT be done when fixing any future nav styling issues?

The context does not state an explicit prohibition in "must NOT" terms for future nav fixes. What is documented is what caused the flicker (stale competing color rules) and what the fix was. The implied rule is: do not introduce additional color rules on nav link selectors that would create cascade ambiguity. But no explicit forward-looking "do not do X" constraint is stated in the Summary2 section.

**Score**: 0 — cannot answer — The context describes the fix and the causes but does not frame any explicit prohibition for future sessions.

---

**Q20**: What sections of the site are complete at the end of S2?

Complete: the nav (hover flicker resolved, mobile reviewed and accepted as-is), hero section (tagline finalized, animation removed, renders statically), and about section (circular photo working on desktop and mobile, skill tags present, section heading with accent bar).

Still open (not complete): projects section and contact section are empty skeletons. About and hero still have placeholder content and placeholder photo.

**Score**: 2 — full — The context explicitly states what is complete and what remains open at the end of S2.

---

## Raw Scores

SCORES: Q11=1,Q12=2,Q13=2,Q14=2,Q15=2,Q16=2,Q17=2,Q18=2,Q19=0,Q20=2

**Total: 17 / 20** *(corrected from agent arithmetic error: Q11=1 + Q19=0 gives 17, not 19)*
