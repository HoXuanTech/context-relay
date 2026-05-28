# S3 — Project Gallery (~7,000 words)

**User:** hey, let's work on the projects section today. we left off with the about section done and projects and contact still empty

**Claude:** Good timing — the projects section is probably the most visually interesting part of the whole site, and it's a good chunk of work. Before I start writing any markup, I need to know a few things:

How many projects are you planning to show? This affects the grid layout significantly — three projects looks different from six or nine. Do you have real project names and descriptions ready, or are we using placeholders? And do you want any kind of filtering system — like filtering by type (frontend, backend, design)? That's a meaningful amount of extra JS and HTML but it can look polished if done right.

**User:** let's say 6 projects for now, all placeholders for the content. and yeah I like the filtering idea — I do a mix of frontend stuff, some backend work, and some design-adjacent things. so three categories would work

**Claude:** Six cards in three categories — that's a good number, it fills a 3-column grid evenly. Let me think through the structure before writing any code.

For the card grid, I'm going to use CSS Grid with `repeat(3, 1fr)` — three equal columns. For the filtering, the simplest approach that works well without a framework is data attributes: each card gets a `data-tags="frontend"` (or backend, or design), and each filter button has a `data-filter="frontend"` attribute. The JavaScript just reads both and shows/hides cards based on matching. No dependencies, easy to understand, easy to maintain.

The alternative approach — using CSS classes for filtering — is slightly cleaner for the CSS but messier for the JS. The data-attribute approach is cleaner overall.

Here's the full section HTML:

```html
<section id="projects">
  <h2 class="section-heading">Projects</h2>
  <div class="filter-bar">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="frontend">Frontend</button>
    <button class="filter-btn" data-filter="backend">Backend</button>
    <button class="filter-btn" data-filter="design">Design</button>
  </div>
  <div class="project-grid">
    <div class="project-card" data-tags="frontend">
      <div class="card-body">
        <span class="card-tag">Frontend</span>
        <h3 class="card-title">Project Alpha</h3>
        <p class="card-desc">A responsive web app built with vanilla JS. Focused on performance and accessibility.</p>
        <a href="#" class="card-link">View Project →</a>
      </div>
    </div>
    <div class="project-card" data-tags="backend">
      <div class="card-body">
        <span class="card-tag">Backend</span>
        <h3 class="card-title">Project Beta</h3>
        <p class="card-desc">REST API built with Node.js and Express. Handles authentication and data management.</p>
        <a href="#" class="card-link">View Project →</a>
      </div>
    </div>
    <div class="project-card" data-tags="design">
      <div class="card-body">
        <span class="card-tag">Design</span>
        <h3 class="card-title">Project Gamma</h3>
        <p class="card-desc">Brand identity and UI design system for a fintech startup.</p>
        <a href="#" class="card-link">View Project →</a>
      </div>
    </div>
    <div class="project-card" data-tags="frontend">
      <div class="card-body">
        <span class="card-tag">Frontend</span>
        <h3 class="card-title">Project Delta</h3>
        <p class="card-desc">E-commerce product page with cart functionality, pure JavaScript.</p>
        <a href="#" class="card-link">View Project →</a>
      </div>
    </div>
    <div class="project-card" data-tags="backend">
      <div class="card-body">
        <span class="card-tag">Backend</span>
        <h3 class="card-title">Project Epsilon</h3>
        <p class="card-desc">WebSocket-based real-time chat server. Handles concurrent users with low latency.</p>
        <a href="#" class="card-link">View Project →</a>
      </div>
    </div>
    <div class="project-card" data-tags="design">
      <div class="card-body">
        <span class="card-tag">Design</span>
        <h3 class="card-title">Project Zeta</h3>
        <p class="card-desc">Mobile app redesign — improved onboarding flow and reduced drop-off rate by 40%.</p>
        <a href="#" class="card-link">View Project →</a>
      </div>
    </div>
  </div>
</section>
```

```css
#projects {
  padding: 5rem 2rem;
}

.filter-bar {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 2.5rem;
}

.filter-btn {
  background: none;
  border: 1px solid var(--color-text-muted);
  color: var(--color-text-muted);
  padding: 0.4rem 1rem;
  border-radius: 3px;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
}

.filter-btn.active,
.filter-btn:hover {
  border-color: var(--color-accent);
  color: var(--color-accent);
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.project-card {
  background-color: #16213e;
  border-radius: 6px;
  overflow: hidden;
  transition: transform 0.2s ease;
}

.card-body {
  padding: 1.75rem;
}

.card-tag {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-accent);
  font-weight: 600;
}

.card-title {
  font-size: 1.2rem;
  color: var(--color-text);
  margin: 0.5rem 0;
}

.card-desc {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  line-height: 1.6;
  margin-bottom: 1.25rem;
}

.card-link {
  color: var(--color-accent);
  font-size: 0.85rem;
  font-weight: 600;
}
```

**User:** ok this looks really good actually. the cards look clean. I want a hover effect on them. like something that makes it feel interactive. what options do I have?

**Claude:** For dark-background card hover effects, here are the main patterns I see working well:

1. **Box shadow / glow** — a shadow or glow appears on hover. Can be a general elevation shadow, or you can tint it with the accent color for a subtle colored glow effect.
2. **Transform / lift** — the card moves up slightly (`translateY(-4px)`) as if being picked up. Often paired with a shadow.
3. **Border highlight** — a colored border appears on one or all edges. Can be done as `box-shadow` (no layout shift) or an actual border.
4. **Background lightens** — the card background gets slightly lighter on hover.
5. **Image zoom** — if cards had images, you'd zoom the image slightly while the card stays put.

Since your cards are text-only, you don't have option 5. What's your gut reaction to the others?

**User:** I'm thinking box shadow, like a glow effect using the accent color. I've seen that look really good on dark backgrounds

**Claude:** Let's try it. The accent color as a glow:

```css
.project-card:hover {
  box-shadow: 0 0 0 2px var(--color-accent), 0 8px 24px rgba(233, 69, 96, 0.15);
}
```

That gives you a thin 2px accent-colored ring around the card, plus a larger diffuse shadow in the accent color below the card. Refresh and hover a card.

**User:** hmm. let me look at it... yeah I don't think I love it. the ring makes it look like a selected element in a UI, like I clicked on a form field or something. it feels more like a "selected" state than a "hovered" state

**Claude:** That's exactly the right critique. The `0 0 0 2px` box shadow is literally the same pattern browsers use for focus rings on form elements — so it reads as "selected" or "focused" rather than "hoverable content." On dark backgrounds it's especially prone to this because it looks like an outline or selection highlight.

You're right that it's too UI-y. What if we try something that feels more like a design choice rather than a UI state? The border-left accent approach is one I like for dark card grids — when you hover the card, a 3px accent-colored bar appears on the left edge. It's subtle, doesn't make the card look selected, and feels intentional rather than like a focus ring:

```css
.project-card {
  background-color: #16213e;
  border-radius: 6px;
  overflow: hidden;
  border-left: 3px solid transparent;
  transition: border-color 0.2s ease;
}

.project-card:hover {
  border-left-color: var(--color-accent);
}
```

The base state has an invisible (`transparent`) 3px border on the left — this reserves the space so the card doesn't shift when the border appears. On hover, the border color transitions to the accent. The card doesn't move, nothing glows, just a clean accent line appears.

**User:** oh yeah that's much better. that looks intentional. like it was designed to be that way, not like an accessibility artifact. let's keep that

**Claude:** Good instinct. The border-left approach has that "editorial" quality you described wanting earlier. Note there's an important technical detail: the transparent border in the base state is essential. Without it, the card would shift right by 3px when the border appears, because the border adds width to the element. The transparent border pre-reserves that space so the card dimensions stay constant.

Now let me write the JavaScript for the filtering. The logic is simple:

1. Attach click listeners to each filter button
2. When clicked, remove `.active` from all buttons, add it to the clicked one
3. Iterate through all cards, hide those that don't match the filter, show those that do

```javascript
// main.js
const filterBtns = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;
    
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    projectCards.forEach(card => {
      if (filter === 'all' || card.dataset.tags === filter) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
});
```

**User:** let me test that... yeah the filtering works. I click Frontend and the two frontend cards stay and the rest disappear. All brings them all back. that's working

**Claude:** Good. One thing I should mention: the filtering uses `display: none` / `display: block` for the hide/show. This is the simplest approach and it works, but it means there's no animation — cards just pop in and out. If you want a smoother transition (cards fade or collapse), it would require more JS. For now the instant show/hide is fine.

There's also a potential grid layout issue when some cards are hidden: because Grid reserves space for hidden elements with `display: none`, the layout won't have gaps where hidden cards were. But if you ever switch to `visibility: hidden` instead, you'd get empty grid cells. The `display: none` approach collapses the items out of the flow, which is what you want.

**User:** yeah instant is fine. ok so I tried looking at it on my iPad and the 3 columns are really narrow. too cramped, the text is getting cut off

**Claude:** Right — `repeat(3, 1fr)` doesn't automatically collapse. We need breakpoints. The same 768px breakpoint we used for the about section makes sense here — it's our established tablet boundary. At 480px we go to single column for phone:

```css
@media (max-width: 768px) {
  .project-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .project-grid {
    grid-template-columns: 1fr;
  }
}
```

Desktop: 3 columns. Tablet (768px and below): 2 columns. Phone (480px and below): 1 column. Try it on the iPad.

**User:** yeah that's much better on the iPad. two columns looks right, everything readable

**Claude:** Good. The two-column tablet layout is clean and consistent with how the about section stacks. The 768px breakpoint is now used in two places — good to establish it as the site's standard tablet breakpoint.

Now — I notice I used "Projects" as the section heading and the section ID. I want to flag this before we go further: do you want to keep calling it "Projects" or is there a different name you'd prefer? Some developer portfolios use "Work" which has a more casual, designer-y feel.

**User:** actually yeah, now that you mention it — "Work" is better. it's how a designer would say it, and "See My Work" is already on the hero button so it's consistent language. let's use "Work"

**Claude:** Good instinct — "Work" is cleaner and the "See My Work" CTA on the hero already establishes that vocabulary. Heads up though: this rename touches multiple places. Let me list them all so we don't miss any:

1. `<section id="projects">` → `<section id="work">`
2. Nav link: `<a href="#projects">Projects</a>` → `<a href="#work">Work</a>`
3. Hero CTA button: `href="#projects"` → `href="#work">`
4. Section heading text: "Projects" → "Work"
5. CSS: `#projects { padding: 5rem 2rem; }` → `#work { ... }`
6. The JavaScript uses class selectors (`.filter-btn`, `.project-card`) not the section ID, so the JS is fine

**User:** yeah let's do all of that

**Claude:** Done. Let me update all four places:

```html
<!-- Hero button — was href="#projects" -->
<a href="#work" class="btn-primary">See My Work</a>

<!-- Nav link — was "Projects" -->
<li><a href="#work">Work</a></li>

<!-- Section — was id="projects" -->
<section id="work">
  <h2 class="section-heading">Work</h2>
  ...
```

And the CSS:
```css
#work {
  padding: 5rem 2rem;
}
```

Let me check: does the nav "Work" link scroll to the section correctly?

**User:** hmm the nav link "Work" doesn't scroll anywhere now. it just stays at the top of the page. the other nav links work fine

**Claude:** Right — that's the CSS selector mismatch I'd want to check. The CSS rule that was targeting `#projects` for section padding no longer matches the section now that the ID is `work`. Let me look at what happened...

Actually wait, I just said I updated it. Let me double-check. The HTML anchor `href="#work"` should scroll to `<section id="work">`. The only way the scroll fails is if the section ID isn't actually `work` in the HTML, or if there's a CSS rule that's accidentally hiding or zero-sizing the section.

Can you check the actual HTML — does the section opening tag say `id="work"`?

**User:** let me look... oh! the section still says `id="projects"`. I updated the nav link and the hero button but I missed the actual section tag

**Claude:** That's the issue. The anchor link `href="#work"` is looking for an element with `id="work"` and finding nothing, so the page doesn't scroll. Update the section opening tag:

```html
<section id="work">
```

After that, the nav link should scroll correctly.

**User:** yeah! that fixed it, it scrolls correctly now. I just forgot to update the actual section id, everything else was right

**Claude:** Easy miss. The rename touched 5 places and one slipped through. Good news: the CSS rule was already updated to `#work`, so once the section ID matched, everything aligned. Let me do a mental check of everything "Work" related now: nav link says "Work" with `href="#work"` ✓, hero button has `href="#work"` ✓, section tag is `id="work"` ✓, section heading says "Work" ✓, CSS targets `#work` ✓, JavaScript uses class selectors so it's unaffected ✓.

Now I want to check something else. During that rename process, I was making changes to the CSS file, and there's a history of the footer CSS getting displaced when we edit the section rules. Let me ask: does the footer look right right now?

**User:** actually now that you mention it, the footer looks weird. the spacing is off, it's floating in the middle of the page a bit. like there's not enough margin above it

**Claude:** That confirms it. The footer spacing rule got knocked loose during the rename editing. The original `.site-footer` rule had `margin-top: 4rem` — that's what creates the gap between the last section and the footer. Is the `margin-top` still in there?

**User:** let me check the CSS... no, I see `.site-footer` and it has the background-color and padding but no margin-top. it got removed

**Claude:** That explains the footer floating up. The `margin-top: 4rem` is what separates the footer from the content section above it. When I was editing the section padding rules during the rename, the footer rule got caught in the shuffle and the margin got stripped.

Add it back. I'm actually going to put the footer rule in a dedicated spot at the end of the CSS file with a comment, so it's clearly separated from the section rules and less likely to get caught in future edits:

```css
/* ==================
   Footer
   ================== */
.site-footer {
  background-color: var(--color-nav);
  padding: 2rem;
  text-align: center;
  margin-top: 4rem;
}

.footer-inner p {
  color: var(--color-text-muted);
  font-size: 0.85rem;
}
```

I'm keeping the `.footer-inner p` rule right with it, since that's the rule that controls the small muted copyright text.

**User:** yeah that fixed the footer. it looks right again. that was a cascade of issues from one rename

**Claude:** It always is. A rename that touches an ID means hunting down every reference across HTML, CSS, and JS. We got all the references, but the editing process shook loose the footer rule in the process. Everything is aligned now: nav says "Work", section ID is `work`, hero button points to `#work`, CSS targets `#work`, footer spacing is restored.

Let me also double-check: did the "Work" rename affect any of the JS? The filtering code uses `document.querySelectorAll('.project-card')` and `document.querySelectorAll('.filter-btn')` — both are class-based, not ID-based, so those are fine.

**User:** yeah the filtering still works after the rename. I just tested it

**Claude:** Good. Let me take a full inventory of the Work section as it stands: six project cards in a three-column grid (collapses to two at 768px, one at 480px), four filter buttons (All/Frontend/Backend/Design), filtering JS is working, hover effect is the border-left accent line (not box shadow — you specifically rejected the glow effect as too UI-y), and the section is called "Work" everywhere.

**User:** this is looking really solid. I'm pretty happy with how the project section turned out. I think that's enough for today actually

**Claude:** Good session. Let me summarize what's left open going into next session: contact form is still a completely empty skeleton. About section still has placeholder photo and bio text. No animations anywhere — that was decided early on and stands. The footer CSS is now at the end of the CSS file rather than where the original rule was — worth knowing for manual edits. The `#projects` to `#work` rename is complete everywhere. The project filtering works.

One thing I want to flag specifically: the footer CSS got displaced twice now during editing sessions. The rule pair (`.site-footer` with `margin-top: 4rem` and `.footer-inner p` with the small muted text styling) lives at the very end of the CSS file. If you're manually editing the CSS and reorganizing rules, be careful not to accidentally drop that block.

**User:** yeah noted. the footer seems weirdly fragile. let's call it. talk next time
