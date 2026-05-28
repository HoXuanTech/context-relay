# Study 4 — T1 Test Results (Agent B)
Source context: Handoff1 — T1 Test Context (after S1)
Date: 2026-05-23

---

**Q1**: What CSS framework was tried and then abandoned in S1, and why?

Bootstrap was tried and then dropped mid-session. The reason: it caused immediate specificity conflicts on `.container` padding that couldn't be cleanly overridden, and the CSS variable system required cascading workarounds the user didn't want.

**Score**: 2/2 — full answer — all details present in context.

---

**Q2**: What was the primary background color chosen, and what was the accent color that was tried and rejected before the final choice?

The primary background color chosen was `#1a1a2e` (stored as `--color-bg`). The final accent color is `#e94560` (coral red). Before settling on it, three orange variants were tried and rejected in sequence: burnt orange (rejected as "sports team logo feel"), bright orange (rejected as "aggressive"), and terra cotta (rejected as "real estate brand").

**Score**: 2/2 — full answer — all rejected variants and reasons are explicitly listed.

---

**Q3**: What color values are stored in the CSS variable system established in S1?

The following variables are locked in `:root`:
- `--color-bg: #1a1a2e`
- `--color-nav: #16213e`
- `--color-accent: #e94560`
- `--color-text: #e0e0e0`
- `--color-text-muted: #8892b0`

**Score**: 2/2 — full answer — all five variables and their exact hex values are present in context.

---

**Q4**: What is the current state of the nav hover flicker bug at the end of S1?

Partially fixed but not fully resolved. A very faint one-frame flash may still appear on first hover in some browsers. The root cause was addressed by adding `a { color: inherit; }` to the global reset, but a full verification across multiple hover cycles is still needed.

**Score**: 2/2 — full answer — both the partial-fix status and residual symptom are explicitly stated.

---

**Q5**: What sections of the website exist at the end of S1?

The full HTML skeleton includes the following sections: nav, hero, about, projects, contact, and footer.

**Score**: 2/2 — full answer — all six sections are explicitly listed.

---

**Q6**: What was the user's reaction to the first orange color option tried in S1?

The first orange variant tried was burnt orange. The user's reaction was that it felt like a "sports team logo feel" — those were the user's own words.

**Score**: 2/2 — full answer — the specific variant and the exact quoted user reaction are in the context.

---

**Q7**: Why did the team choose plain CSS over a framework after the Bootstrap attempt?

Because the Bootstrap specificity wall on its variable system was the reason it was dropped. The user directly hit the specificity conflict trying `padding: 0` on `.container` — it didn't work. Claude explained why, and the user immediately made the call to switch to plain CSS written from scratch (~60 lines, every rule explicit). Plain CSS is intentional — a Safety Rule explicitly states not to add Bootstrap back.

**Score**: 2/2 — full answer — both the technical reason and the user decision moment are documented.

---

**Q8**: What is the HTML structure established at the end of S1?

The HTML skeleton contains: nav, hero, about, projects, contact, and footer sections. Additional structural details documented:
- Nav: fixed position, `z-index: 100`, 3 links (About, Work, Contact), brand in accent color, links uppercase with letter-spacing
- Hero: name + placeholder tagline + coral-red CTA button linking to `#projects`
- About: two-column grid (280px photo + 1fr text), skill tags with accent tint, section heading with `::after` accent bar (50px wide, 3px tall)
- Section layout: `padding: 5rem 2rem`, `max-width: 1100px`, `margin: 0 auto`
- Footer reuses `--color-nav` background

**Score**: 2/2 — full answer — explicit structural details are all present in context.

---

**Q9**: What root cause was identified for the nav hover flicker in S1?

Two root causes were traced in S1:
1. A global `a { color: white }` rule — this was removed.
2. The UA (browser user agent) stylesheet default link color — patched with `a { color: inherit; }` in the global reset.

The Recon Notes state this "may need one more check," indicating the fix was applied but not yet fully verified.

**Score**: 2/2 — full answer — both root causes are explicitly named in the Recon Notes.

---

**Q10**: What are the next actions planned at the end of S1?

Three next actions are listed:
1. Verify nav hover flicker is fully gone across multiple hover cycles.
2. Begin hero content: settle on the actual tagline copy.
3. Build about section content (the two-column grid is scaffolded; needs photo circle treatment and responsive stacking).

**Score**: 2/2 — full answer — all three next actions are directly quoted from the Next Actions section.

---

SCORES: Q1=2,Q2=2,Q3=2,Q4=2,Q5=2,Q6=2,Q7=2,Q8=2,Q9=2,Q10=2

Total: 20/20
