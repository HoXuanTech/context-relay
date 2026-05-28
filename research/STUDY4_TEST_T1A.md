# Study 4 — T1 Test Answers (Agent: Claude Code / Sonnet 4.6)
Test context: Summary1 only (after S1)
Date: 2026-05-23

---

**Q1**: What CSS framework was tried and then abandoned in S1, and why?

Bootstrap was tried and then abandoned. The reason was that the user hit the "specificity wall" — they could not cleanly override Bootstrap's CSS custom properties for container padding. The full Bootstrap CDN links and JavaScript bundle were then removed.

**Score**: 2/2 — full and specific answer

---

**Q2**: What was the primary background color chosen, and what was the accent color that was tried and rejected before the final choice?

Primary background color: `#1a1a2e`. Three accent colors were tried and rejected before the final choice: burnt orange (`#e07b39`), bright orange (`#f47c3f`), and terra cotta (`#c9622f`). The final chosen accent color is coral-red `#e94560`.

**Score**: 2/2 — full and specific answer

---

**Q3**: What color values are stored in the CSS variable system established in S1?

Five variables are stored in a `:root` block:
- `--color-bg` (value: `#1a1a2e`)
- `--color-nav` (value: `#16213e`)
- `--color-accent` (value: `#e94560`)
- `--color-text`
- `--color-text-muted`

The context names all five variable names and gives explicit values for the first three, but does not state the specific hex values for `--color-text` and `--color-text-muted` within Summary1.

**Score**: 1/2 — partial — variable names all listed, but exact values for `--color-text` and `--color-text-muted` are not given in Summary1

---

**Q4**: What is the current state of the nav hover flicker bug at the end of S1?

The flicker is "mostly resolved" but a very faint artifact may still appear on the first hover of a page load on certain browsers. It is noted as an open item to check next session — it is not fully closed at the end of S1.

**Score**: 2/2 — full and specific answer

---

**Q5**: What sections of the website exist at the end of S1?

The page has: a fixed navigation bar at the top, followed by hero, about, projects, and contact sections, then a footer. All sections except hero and about are currently empty skeletons.

**Score**: 2/2 — full and specific answer

---

**Q6**: What was the user's reaction to the first orange color option tried in S1?

The context does not record the user's reaction to the first orange option specifically. It states the entire orange family was "ruled out entirely because it reads either as a sports team logo or a lifestyle brand depending on how saturated it is," and that the coral-red "was the user's instinct and it landed immediately." No per-color reaction to the first orange attempt is described.

**Score**: 0/2 — cannot answer — no per-color reaction to the first orange option is recorded in Summary1

---

**Q7**: Why did the team choose plain CSS over a framework after the Bootstrap attempt?

The decision was made to write everything from scratch because the replacement approach — a small custom reset and hand-written CSS — gives "full visibility into every rule." The implicit reason is to avoid the specificity problems that Bootstrap caused.

**Score**: 2/2 — full and specific answer

---

**Q8**: What is the HTML structure established at the end of S1?

The page structure includes: a fixed navigation bar (`position: fixed`, `z-index: 100`) with dark background slightly lighter than the page body; a hero section (with name heading using `clamp(2.5rem, 6vw, 5rem)`, tagline, and a "See My Work" CTA button linking to `#projects`); an about section (two-column grid with 280px photo column and `1fr` text column, `gap: 4rem`, placeholder image, bio placeholder text, skill tag `<span>` elements, section heading with `::after` accent bar); and empty skeleton projects and contact sections; followed by a footer. All sections share `max-width: 1100px` with `margin: 0 auto`. The nav uses `.nav-inner` for the same content width constraint.

**Score**: 2/2 — full and specific answer

---

**Q9**: What root cause was identified for the nav hover flicker in S1?

Two layers were identified:
1. A global `a { color: white }` rule the user had written early on during experimentation and forgotten about — this was removed first.
2. The underlying browser user-agent (UA) stylesheet default link color — neutralized by adding `color: inherit` to the global `a` rule.

**Score**: 2/2 — full and specific answer

---

**Q10**: What are the next actions planned at the end of S1?

The open items going into the next session are:
1. The projects and contact sections are empty skeletons (need to be built out).
2. The nav hover flicker residual first-hover artifact should be rechecked.
3. All text content and the photo are placeholders (need real content).

**Score**: 2/2 — full and specific answer

---

## Summary Scores

SCORES: Q1=2,Q2=2,Q3=1,Q4=2,Q5=2,Q6=0,Q7=2,Q8=2,Q9=2,Q10=2

**Total: 19 / 20**
