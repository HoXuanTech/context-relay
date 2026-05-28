# Study 4 — Test T3B: Handoff3 Context (after S3)

Source section used: "## Handoff3 — T3 Test Context (after S3)" from STUDY4_DATA_B.md only.
Answering strictly from that section. No prior knowledge applied.

---

**Q21**: What type of CSS effect is permanently banned from the hero section?

**Answer**: CSS animation is permanently banned from the hero section. Specifically, `fadeInUp` keyframes with staggered delays were tried in S2 and caused layout shift on iOS (translateY + animation-fill-mode: both triggers layout recalculation between painted position and end state). The user decided to remove it rather than patch it. The Safety Rules in Handoff3 state: "Do not add any CSS animation to the hero — it caused iOS layout shift; the decision to remove it was explicit and the user confirmed 'it actually feels more confident without the animation'."

**Score**: 2/2 — full and specific answer

---

**Q22**: What is the correct implementation for the about section's circular photo?

**Answer**: `border-radius: 50%` and `overflow: hidden` go on the `.about-photo` container (NOT on the `<img>` element itself). The container must have explicit `width: 280px` AND `height: 280px` — both values are required because the grid stretches the container vertically otherwise, turning the circle into an oval. The Safety Rules state: "`.about-photo` must have explicit `width` AND `height` set to the same value — removing either makes the circle become oval due to grid row height stretching the container."

**Score**: 2/2 — full and specific answer

---

**Q23**: Why was box-shadow rejected as the card hover effect?

**Answer**: Box-shadow was tried in 3 configurations and rejected each time:
1. Ring + shadow — "too UI-y like a form input"
2. Shadow-only — "too corporate/enterprise dashboard"
3. Radial halo — "still not right" / "the glowing thing doesn't fit this design"

The Recon Notes confirm: "Box shadow was rejected progressively — ring version first ('looks like a focused form input'), then shadow-only ('corporate enterprise dashboard'), then radial halo ('still not right') — three tries before user said 'the glowing thing doesn't fit this design'."

**Score**: 2/2 — full and specific answer

---

**Q24**: What CSS properties create the card hover effect currently in use?

**Answer**: The card hover uses a border-left accent line implemented with TWO rules that must coexist:
- Base state: `border-left: 3px solid transparent` (space pre-reserved so no layout shift on hover)
- Hover state: `border-left-color: var(--color-accent)` (reveals the accent color)
- Transition: `transition: border-color 0.2s ease`

The Safety Rules note: removing the base rule causes a 3px card shift on hover; removing the hover rule means nothing happens.

**Score**: 2/2 — full and specific answer

---

**Q25**: Why is the CSS rule for footer spacing located at the end of the stylesheet in an unusual position?

**Answer**: The footer CSS was accidentally displaced (lost as a "proximity casualty") during the rename edits when "Projects" was changed to "Work". It was physically moved to the end of style.css inside a labelled "Footer" comment block to isolate it from the section-editing zone, preventing it from being accidentally dropped again during adjacent CSS edits. The Key Decisions section states: "Footer CSS moved to end of file in labelled comment block → it was accidentally displaced during the rename edits; physically isolating it from the section-editing zone prevents future proximity casualties."

**Score**: 2/2 — full and specific answer

---

**Q26**: What responsive breakpoint is used for the project card grid, and what does it change?

**Answer**: Two breakpoints are used:
- `≤768px` → changes from 3 columns (`repeat(3, 1fr)`) to 2 columns
- `≤480px` → changes from 2 columns to 1 column; the filter bar also wraps at ≤480px

The base (desktop) state is a six-card CSS grid using `repeat(3, 1fr)`.

**Score**: 2/2 — full and specific answer

---

**Q27**: What is the current state of the project section at the end of S3?

**Answer**: The Work section (renamed from "Projects") is complete. Per the Completed This Session list: six-card CSS grid with responsive breakpoints, filter system with JS data-filter/data-tags matching and display: block/none toggling, card hover with border-left accent line, and "Work" nav link confirmed scrolling correctly. Still in progress: "View Project →" links all point to `#` (placeholder) and will be replaced with real URLs when content is ready. Contact section is still an empty skeleton; about section still has placeholder photo and bio.

**Score**: 2/2 — full and specific answer

---

**Q28**: What triggered the "Projects → Work" section rename, and what did it break?

**Answer**: The rename was the user's idea mid-session after noticing inconsistency — the hero CTA button already said "See My Work." User said: "Work sounds more like a designer would say it, more intentional than developer-resume energy." The rename touched 5 locations: section id, nav link text, nav link href, hero CTA href, and CSS selector.

Side effects of the rename: footer `margin-top: 4rem` spacing was accidentally dropped as a proximity casualty during adjacent CSS edits (not caused by rename logic itself), and `.footer-inner p` rule (small + muted copyright text) was also dropped. Both were restored as Last Actions in S3.

**Score**: 2/2 — full and specific answer

---

**Q29**: How does the tag filter system work in the Work section?

**Answer**: The filter JS uses exact string match (`===`) on `data-tags`. Cards have a `data-tags` attribute; filter buttons have a `data-filter` attribute. Matching determines whether a card gets `display: block` or `display: none`. The `.active` class moves between buttons to indicate the active filter. This system supports single-category cards only — multi-tag support would require `split(' ').includes()` but is not needed now.

**Score**: 2/2 — full and specific answer

---

**Q30**: What are the open items / next actions at the end of S3?

**Answer**: Next Actions listed in Handoff3:
1. Build contact form: name, email, message fields, submit button
2. Add blur-triggered field validation (user prefers blur over submit-only)
3. Add Safari smooth scroll polyfill

Still In Progress (open items):
- Contact section is still an empty skeleton
- About section still has placeholder photo and bio text
- "View Project →" links all point to `#` (placeholder) — clicking scrolls to top; will be replaced with real URLs when content is ready

**Score**: 2/2 — full and specific answer

---

SCORES: Q21=2,Q22=2,Q23=2,Q24=2,Q25=2,Q26=2,Q27=2,Q28=2,Q29=2,Q30=2
