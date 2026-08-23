# Wedding Website — Redesign Design & Implementation Plan

Status: **Approved — all open items decided, ready to build**
Target file: `index.html` (single-file site, no build step)
Date: 2026-08-23

---

## 1. User Draft (verbatim)

> I am re-designing my wedding website
>
> Note: The design must be mobile first
>
> Current website i think it lacks the dynamic , animated and interactional elements.
>
> What i want:
> 1. I wanna design and build it according to themes. My Media folder has 4 themes and different images.
> 2. I want 4 different themes in backgroup to transition when users scroll to the images of one theme.
> 3. Keep the music play function
> 4. Keep the calender reserve function
> 5. we can keep the #6b7254 , but for #f3ede1 , maybe can change to white, or color close to white which should be romatic.
> 6. Keep the countdown function
> 7. i wanna redesign the Hero Section , i want it to be animated, show our images when the page load

---

## 2. What Exists Today

| Feature | Location | Keep / Change |
|---|---|---|
| Cover page + logo | `index.html:1183` | Keep, restyle — **also the music-gesture gate, see §10.1** |
| Nav + hamburger | `index.html:1233` | Keep |
| Music player (4 tracks, dropdown, toast) | `index.html:1238`, JS `1833` | **Keep as-is** |
| Hero (SVG botanical borders) | `index.html:1306` | **Rebuild** |
| Intro / Our Story | `index.html:1516` | Keep, add photos |
| Story | `index.html:1591` | Keep, add photos |
| Details + Google Map | `index.html:1616` | Keep |
| Gallery — **5 empty placeholders** | `index.html:1707` | **Deleted**, replaced by theme chapters |
| RSVP → Google Calendar link | `index.html:1778` | **Keep as-is** — but see §10.6 |
| Footer | `index.html:1800+` | Keep, restyle |
| Countdown bar (fixed bottom) | `index.html:2035`, JS `2052` | **Keep as-is** |

Key gap: site had **zero real photos**. All 22 images in `Media/` were unused.

---

## 3. The Four Themes

Folders in `Media/` map 1:1 to scroll chapters, in this order:

| # | Theme | Slug | Images | Portrait | Landscape | Mood |
|---|---|---|---|---|---|---|
| 1 | Bank Street | `bank-street` | 5 | **5** | 0 | Urban, editorial |
| 2 | Casual | `casual` | 5 | 3 | 2 | Warm, everyday |
| 3 | Beach | `beach` | 6 | 1 | **5** | Airy, open |
| 4 | Chapel | `chapel` | 6 | 2 | 4 | Formal, sacred |

Order confirmed by user: Bank Street → Casual → Beach → Chapel. Opens dressed-up and urban, relaxes into casual, opens out to the beach, closes at the chapel.

**Orientation drives layout.** Bank Street is all-portrait, Beach is nearly all-landscape. The four chapters must not use one shared grid — a portrait-only chapter in a landscape grid means letterboxing or bad crops. Per-chapter layouts in §7.

### Filename map (originals → web assets)

| Web base | Original |
|---|---|
| `casual-01` … `casual-05` | `2P3A5091`, `2P3A5098`, `2P3A5150`, `2P3A5157-1`, `2P3A5158` |
| `bank-street-01` … `-05` | `2P3A4973`, `2P3A4990`, `2P3A4994`, `2P3A5042`, `2P3A5073` |
| `beach-01` … `beach-06` | `2P3A5196`, `2P3A5210`, `2P3A5256`, `2P3A5280`, `s3_1 拷贝`, `s3_2` |
| `chapel-01` … `chapel-06` | `2P3A5324`, `2P3A5331`, `2P3A5376`, `s4_1`, `s4_2 拷贝`, `s4_3` |

Non-ASCII names (`拷贝`) are resolved — web assets are all ASCII. Originals untouched on disk.

---

## 4. Color System (change #5)

Replace `--cream: #f3ede1` with a near-white romantic base. Keep `#6b7254` as the anchor accent.

```css
:root {
  /* keep */
  --green:       #6b7254;
  --green-dark:  #545a41;
  --green-light: #8a9070;

  /* NEW base — replaces --cream */
  --shell:       #fdfcfa;  /* page background, warm near-white */
  --shell-soft:  #f8f4f1;  /* alternating section band */
  --shell-edge:  #ece5e0;  /* hairlines, borders */

  /* NEW romantic accent */
  --blush:       #e3cfc7;  /* dusty rose, decorative only */

  --dark: #2a2a25;
  --mid:  #5a5a50;
}
```

Per-theme tint driven by two variables, animated on scroll:

```css
body {
  background: var(--theme-bg);
  transition: background-color 900ms ease;
}
```

| Theme | `--theme-bg` | `--theme-accent` |
|---|---|---|
| Bank Street | `#f7f4f0` | `#a89b8c` |
| Casual | `#fdfcfa` | `#c9a99c` |
| Beach | `#f6f8f8` | `#9fb3b5` |
| Chapel | `#f4f5f0` | `#6b7254` |

`--theme-accent` is **not background-only** — it also drives nav underline, music-player bars, countdown separators, and section hairlines. The whole page shifts mood per chapter, not just the backdrop. That is what makes the transition read as intentional rather than as a rendering glitch.

Kept deliberately subtle — a wash, not a color flip. Text contrast stays AA on every value.

---

## 5. New Page Structure

```
Cover  →  Hero (animated)
       →  Countdown (existing fixed bar)
       →  Our Story
       →  Chapter 1: Bank Street   ┐
       →  Chapter 2: Casual        │ background + accent transition here
       →  Chapter 3: Beach         │
       →  Chapter 4: Chapel        ┘
       →  Day-of Timeline           (new, §13.2)
       →  Details + Map
       →  RSVP (calendar button)
       →  Footer
```

Gallery section is **replaced** by the 4 theme chapters. Each chapter = label, serif title, hairline, scripture couplet (§13.1), then its photos.

---

## 6. Hero Redesign (change #7)

**Mobile (default, ≤767px)**

- Full-viewport (`100svh`) stacked layout, `padding-bottom` reserved for the fixed countdown bar (see §10.8).
- Background: **`chapel-04`** (landscape, `s4_1.jpg`) — confirmed. `object-fit: cover`, with a `linear-gradient` scrim so text stays readable.
- **Timeline must be gated on image decode** — see §10.4. Sequence starts only after the hero image is painted.

| t | Element | Motion |
|---|---|---|
| 0ms | Hero photo | scale `1.08 → 1.0`, opacity `0 → 1`, 1400ms `cubic-bezier(.16,1,.3,1)` |
| 300ms | Monogram / label | fade up 16px, 700ms |
| 550ms | Names (serif, 2 lines) | each line clip-reveal from below, 800ms, 120ms stagger |
| 900ms | Hairline rule | scale-X `0 → 1` from center, 600ms |
| 1100ms | Date + venue | fade up 12px, 600ms |
| 1400ms | Scroll cue | fade in, then infinite 2.4s gentle bob |
| 1800ms | Hero photo | hands off to 20s Ken Burns loop, `scale(1.0 → 1.06)` |

- Behind the text, a **3-photo peek strip**: small offset cards (`casual-01`, `beach-02`, `bank-street-02`) fade+slide in at 1200ms at low opacity. Delivers "show our images on load" without burying the names.

**Desktop (≥768px)**

- Two-column magazine grid: names left, staggered photo collage right — 4 images, one per theme, different sizes, slight rotations ±2°.
- Same timeline; collage images stagger in at 700/850/1000/1150ms.
- Slight parallax on the collage tied to scroll (`translateY`, max 40px).

Existing decorative SVG botanicals: keep as a thin bottom border only. They currently occupy ~200 lines of markup and read heavy on mobile.

---

## 7. Theme Chapter Behavior (changes #1, #2)

### Per-chapter layouts (mobile-first, orientation-aware)

| Chapter | Mobile | Desktop |
|---|---|---|
| **Bank Street** (5P) | Vertical portrait run, alternating 100% / 84%-width offset left-right | 3-col portrait wall, middle column dropped 80px |
| **Casual** (3P/2L) | Alternating: portrait full-bleed → landscape inset → portrait 2-up | Mixed 12-col, heavy-left |
| **Beach** (5L/1P) | Landscape stack full-bleed, generous vertical gaps | Wide 2-up landscape pairs, heavy-right |
| **Chapel** (2P/4L) | Portrait hero → landscape run → portrait close | Editorial split: portrait sidebar + landscape main |

Each chapter opens with: `section-label` → serif title → hairline → scripture couplet (§13.1).

### Background transition mechanism

- One `IntersectionObserver` on the 4 chapter roots, `rootMargin: '-45% 0px -45% 0px'` → fires when a chapter crosses the viewport midline.
- On intersect: `document.body.dataset.theme = 'beach'`.
- CSS reacts:

```css
body[data-theme="beach"] { --theme-bg: #f6f8f8; --theme-accent: #9fb3b5; }
```

- Only custom properties change; `transition` does the fade. No layout thrash, no scroll listener.

### Photo reveal animation

- Second `IntersectionObserver` (threshold `0.15`, unobserve after fire) adds `.in-view`.
- Effect: opacity `0 → 1` + `translateY(28px → 0)` + inner `<img>` `scale(1.06 → 1)`, 900ms `cubic-bezier(.16,1,.3,1)`, 90ms stagger within a chapter.
- No bounce, no spring — matches the editorial rule.

### Interaction

- **Lightbox**: tap a photo → full-screen, swipe left/right within the chapter, tap/ESC to close, background scroll locked. `z-index` above music player and countdown; countdown bar hides while open.
- **Chapter progress rail**: one vertical rail at the right edge, 4 segments, fills as you scroll, tap a segment to jump. Replaces the dot nav and gives continuous motion feedback. Desktop + tablet; collapses to 4 small dots on mobile.
- **Differential parallax**: within a chapter, photo 1 scrolls at 1.0x, photo 2 at 0.94x, photo 3 at 1.0x. Subtle depth. Driven by one shared `requestAnimationFrame` loop, not per-element scroll listeners.

---

## 8. Preserved Functions (changes #3, #4, #6)

Move these three blocks over **unmodified**; only their CSS colors get retokenized to the new palette.

| Function | Source lines | Note |
|---|---|---|
| Music player + playlist + toast | `1238–1298`, `1833–2007` | 4 mp3s stay in repo root |
| Save to Calendar | `1785–1793` | Google Calendar template URL, unchanged |
| Countdown bar | `2035–2089` | Target 2026-11-22 16:00 `Asia/Kuala_Lumpur` |

**Enhancement — audio-reactive music bars.** The bars currently fake motion with a CSS keyframe. Wire a WebAudio `AnalyserNode` to the existing `<audio>` element so they move to the actual piano. ~20 lines, no library, directly answers the "lacks dynamic elements" complaint. Falls back to the CSS animation if WebAudio is unavailable.

---

## 9. Media Pipeline — DONE

Script: `optimize-media.py` (Pillow). Originals in `Media/<Theme>/` are read-only inputs; output goes to `Media/web/<slug>/`.

| | Before | After |
|---|---|---|
| Total size | **388 MB** | **18.1 MB** |
| Files | 22 | 132 + `manifest.json` |
| Names | spaces, `拷贝` | ASCII, ordered |

- Widths `800 / 1200 / 1600`, each as **WebP** (q82) + **JPEG** (q80, progressive) fallback.
- EXIF orientation applied then stripped.
- `Media/web/manifest.json` records base name, available widths, aspect ratio, orientation, and source filename per image — the chapter markup is generated from it, so no hand-typed paths.

**Git:** `.gitignore` excludes `Media/*` but keeps `Media/web/`. Originals never enter git history. Verified: 133 files staged-visible, all under `Media/web/`.

### Delivery rules

```html
<picture>
  <source type="image/webp" srcset="Media/web/beach/beach-02-800.webp 800w,
                                    Media/web/beach/beach-02-1200.webp 1200w,
                                    Media/web/beach/beach-02-1600.webp 1600w"
          sizes="(max-width: 767px) 100vw, 50vw">
  <img src="Media/web/beach/beach-02-1200.jpg" width="5472" height="3648"
       loading="lazy" decoding="async" alt="">
</picture>
```

- Every chapter photo: `loading="lazy"`, `decoding="async"`, explicit `width`/`height` to stop layout shift.
- Hero photo only: `loading="eager"` + `<link rel="preload" as="image" imagesrcset=...>`.
- `prefers-reduced-motion: reduce` → reveals become instant opacity, background transition 0ms, Ken Burns and parallax off.

---

## 10. Gaps Found In Review

Things the original draft missed. Ranked by risk.

1. **Music autoplay depends on the cover-page tap.** Browsers block `audio.play()` without a user gesture. The cover-page "enter" tap *is* that gesture. Rebuilding the cover without re-wiring `audio.play()` to that tap = music silently never starts on mobile, with no error. **Must be preserved explicitly during the cover restyle.**
2. **388 MB and no `.gitignore`.** Resolved (§9). Committing originals once bloats history permanently, even after deletion, and most free hosts reject >100 MB files.
3. **No Open Graph meta tags.** The link will be pasted into WhatsApp / WeChat constantly. Today it renders as a bare URL — no title, no preview image. Add `og:title`, `og:description`, `og:image` (a dedicated 1200×630 crop), `twitter:card`, plus a favicon. Cheap, high visibility.
4. **Hero timeline races image decode.** The 0→1800ms sequence assumes the hero photo exists. If not yet decoded, the names animate over a blank box. Gate on `heroImg.decode().then(start)` with a ~2s `setTimeout` fallback so a slow network can't stall the hero forever.
5. **Single 1600px resize is not mobile-first.** Resolved (§9) — 800/1200/1600 srcset + WebP. A 390px phone now pulls ~60 KB, not a 1600px JPEG.
6. **"RSVP" section contains no RSVP.** It is a calendar button only. **Decided:** keep as-is — calendar button only, no response form.
7. **Portrait vs landscape unknown.** Resolved (§3) — measured, and chapter layouts now differ accordingly.
8. **Countdown bar overlaps the `100svh` hero on mobile.** The fixed bottom bar sits on top of the hero scroll cue on short phones. Hero needs `padding-bottom: <bar height>` and the scroll cue offset above it.

---

## 11. Open Items — need your decision

| # | Item | Status |
|---|---|---|
| 1 | Rename non-ASCII files | **Done** (§3) |
| 2 | Image optimization | **Done** (§9) |
| 3 | Chapter order | **Decided** — Bank Street → Casual → Beach → Chapel |
| 4 | Chapter captions | **Decided** — scripture couplet per chapter, see §13.1 |
| 5 | Hero photo | **Decided** — `chapel-04` (`s4_1.jpg`, landscape) |
| 6 | Old Intro / Story sections | **Decided** — keep both |
| 7 | RSVP | **Decided** — keep current calendar button, no form |
| 8 | OG preview image | **Decided** — use `chapel-04` for now (already preloaded), 1200×630 crop; swap later if wanted |

---

## 12. Build Order

1. Palette swap: `--cream` → `--shell` / `--theme-*` tokens across all CSS.
2. ~~Rename + optimize images~~ — **done**.
3. Cover restyle — **re-verify `audio.play()` still fires on the enter tap**.
4. Hero rebuild (mobile → desktop), with decode gate + Ken Burns.
5. Chapter markup ×4, generated from `manifest.json`, orientation-aware layouts — including scripture couplet block (§13.1).
6. Theme `IntersectionObserver` → `body[data-theme]` background + accent transition.
7. Reveal `IntersectionObserver` + stagger.
8. Chapter progress rail + differential parallax (one shared rAF loop).
9. Lightbox + swipe.
9b. Day-of timeline section (§13.2), reusing the progress-rail visual language.
10. Audio-reactive music bars.
11. OG meta tags + favicon.
12. Retest music / calendar / countdown after restyle.
13. Mobile pass: 375px, 390px, 768px, 1440px. Reduced-motion pass.

---

## 13. Asian Christian Layer

Two additions agreed on top of the editorial Western base. Nothing else from that discussion is in scope — no red accent, no monogram rework, no angpow block, no dress-code row.

### 13.1 Scripture couplet as chapter caption

Replaces the deferred one-line caption (§11.4). Each chapter carries one verse, English over Chinese.

| Chapter | Verse | English | Chinese |
|---|---|---|---|
| Bank Street | Song of Songs 3:4 | I found the one my heart loves. | 我遇見我心所愛的。 |
| Casual | 1 Corinthians 13:4 | Love is patient, love is kind. | 愛是恆久忍耐，又有恩慈。 |
| Beach | Ecclesiastes 4:12 | A cord of three strands is not quickly broken. | 三股合成的繩子不容易折斷。 |
| Chapel | Matthew 19:6 | What God has joined together, let no one separate. | 神配合的，人不可分開。 |

Chinese lines above follow 和合本 (CUV), traditional characters, trimmed to one clause each. **Open:** confirm CUV vs 新譯本 (CNV), and traditional vs simplified — that choice also decides the `lang` attribute (`zh-Hant` vs `zh-Hans`) and which font subset gets built.

Markup, inside each chapter header:

```html
<blockquote class="chapter-verse">
  <p class="verse-en">Love is patient, love is kind.</p>
  <p class="verse-zh" lang="zh-Hant">愛是恆久忍耐，又有恩慈。</p>
  <cite>1 Corinthians 13:4</cite>
</blockquote>
```

Styling:

- `.verse-en` — italic serif, `1.05rem`, `--mid`, max-width `34ch`, centered.
- `.verse-zh` — `0.9rem`, `letter-spacing: .08em`, `--mid` at 75% opacity.
- `cite` — `0.7rem`, uppercase, `letter-spacing: .18em`, `--theme-accent`, not italic.
- Reveals with the chapter header, before the photo stagger begins.

**CJK font is required.** Playfair Display has no CJK glyphs; without an explicit stack the Chinese line falls back to system sans and breaks visually against the serif.

```css
--font-serif: 'Playfair Display', Georgia, serif;
--font-cjk:   'Noto Serif SC', 'Source Han Serif SC', 'Songti SC', serif;
```

`.verse-zh { font-family: var(--font-cjk); }`. Subset the CJK webfont to only the characters actually used across the 4 verses — full Noto Serif SC is ~9 MB, the subset is a few KB.

### 13.2 Day-of timeline section

New section between Chapter 4 and Details. Answers the question relatives will otherwise WhatsApp about: when is tea ceremony, when is church, when is dinner.

Placement: after Chapel chapter, so the page reads photos → schedule → logistics → RSVP.

| Time | English | Chinese | Venue |
|---|---|---|---|
| 06:30 | Gate games | 門口遊戲 | Bride's home |
| 08:00 | Tea ceremony | 茶禮 | Bride's home |
| 16:00 | Church ceremony | 教堂婚禮 | *(venue)* |
| 18:30 | Dinner reception | 晚宴 | *(venue)* |

**Open:** all four times and the two venue names are placeholders except 16:00, which is taken from the existing countdown target (2026-11-22 16:00 `Asia/Kuala_Lumpur`). Confirm before build.

Layout:

- Mobile — single vertical rail on the left, `2px` line in `--shell-edge`, one filled dot per entry in `--theme-accent`. Time in tabular figures, event title serif, Chinese line beneath at `0.85rem`, venue in `--mid` small caps.
- Desktop — same rail centered, entries alternating left/right.
- Reuses the chapter progress rail's dot and line tokens; no new visual language.
- Entries reveal on scroll with the existing `.in-view` observer, 120ms stagger.
- `font-variant-numeric: tabular-nums` on the time column so the digits align.

This section sits outside the 4 chapters, so the `IntersectionObserver` in §7 must not fire on it — it inherits whatever theme Chapel left behind. Keep it off the observer's node list.
