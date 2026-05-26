# Wedding Website — Session Summary
**Last updated:** 2026-05-27
**File:** `index.html`

---

## Changes Made

### 1. Music Player — Noticeable Toggle
- Added chevron SVG that rotates 180° when playlist dropdown opens
- Changed label from "Virlyn Music" → "Now Playing"
- Added `title="Browse playlist"` tooltip on hover
- Added `cursor: pointer` to music info area
- Player gets a soft green glow pulse 1.8s after page load to draw attention

### 2. Cover / Splash Page
- Full-screen overlay appears on load before the site
- Shows logo, couple names, date, "Enter" button with pulsing ring
- Botanical SVG decorations (top-left, bottom-right corners)
- Click anywhere → dismisses cover + autoplays music (satisfies browser autoplay policy)
- Fades out smoothly (0.9s opacity transition)

### 3. Music Autoplay
- Attempted direct autoplay on load — blocked by all modern browsers without user gesture
- Solution: play triggered on cover page click (guaranteed user gesture)
- Music player pulses after cover fades to confirm it's playing

### 4. Logo (logo.jpeg) Integration
- **Hero monogram:** SVG "CE" replaced with `logo.jpeg`, clipped to circle via `overflow: hidden` + `object-fit: cover`
- **Cover page monogram:** same treatment, 140px circle
- **Footer monogram:** SVG replaced with `logo.jpeg`, white-tinted via CSS `filter`
- **Nav (top-left):** "C & E" text replaced with `logo.jpeg` as 48px circle with green border
- Removed inner double-ring since image fills full circle
- `mix-blend-mode: multiply` used on nav logo to blend background

### 5. Logo Float Animation (hero)
- ~~Removed~~ — animation deleted, logo is now static

### 6. Botanical Stem Animation
- Both `.hero-botanical-top` and `.hero-botanical-bottom` SVGs split into 4 `<g>` groups by x-position
- Groups: `stem-g1` (x≤360), `stem-g2` (x 390–720), `stem-g3` (x 740–1060), `stem-g4` (x 1065+)
- Each group sways with `stemSway` keyframe (0.7° rotate + 3px translateY) with 1.2s staggered delays
- Creates a left-to-right breeze wave effect
- `transform-box: fill-box; transform-origin: bottom center` for correct pivot point

### 7. Footer Logo Fix
- Was: `width: 48px; object-fit: contain` → white rectangle visible inside circle
- Fixed: `width: 100%; height: 100%; object-fit: cover; border-radius: 50%` (matches hero style)
- Removed `filter: brightness(0) invert(1)` white-tint

### 9. Scroll Toast — "Pick a Song" Notification
- On first scroll past 60px, a toast slides in (top-right, below nav)
- Shows music note icon + "Pick a song / Use the music player above" message
- Auto-dismisses after 5s; has manual ✕ close button
- Only triggers once per page load
- Styled with `#songToast`, `.show` class handles opacity/transform transition

### 10. Botanical Top Stems Uncovered
- Tops of hero botanical stems were hidden behind fixed nav (~88px tall)
- Fixed: `.hero-botanical-top { top: 88px }` — stems now fully visible below nav

### 11. Nav Logo Transparency
- Added `opacity: 0.7` to `.nav-logo img`

### 12. Hero Monogram Transparency
- Added `opacity: 0.5` to `.monogram img`

### 13. Hero Monogram Border — Invisible
- Changed `.monogram` border from `var(--green)` → `var(--cream)` (matches page bg `#f3ede1`)

### 14. Hero Monogram Removed
- Deleted `<div class="monogram">` + `<img>` from hero section entirely
- "Chester & Elbee" heading naturally moves up; no spacing adjustments needed

### 8. Botanical Mobile Responsiveness
- Problem: `preserveAspectRatio="none"` squished ~50 stems into 375px → stems every 6px
- Added `.hero-botanical-desktop` class to existing 1440px SVGs, hidden on ≤768px
- Added `.hero-botanical-mobile` SVGs with 7 stems evenly spread in a 400px viewBox
- Mobile stems: stroke-width 2.5, spaced at x=30,90,155,200,245,310,370
- Both top + bottom botanical have desktop/mobile variants

### 15. Hero Divider Symbol Removed
- Removed `<div class="hero-divider">` (droplet SVG between two lines) from hero section
- Removed standalone `<p class="hero-date">` above names

### 16. Hero Date Merged into Sub-line
- Date moved into `.hero-sub` alongside location: "Kuala Lumpur · November 22, 2026"
- Full date (Nov 22) used instead of just month/year

### 17. Countdown Bar — Sticky Bottom
- Fixed sticky bar at bottom of viewport (`z-index: 9998`)
- Counts down days · hours · min · sec to November 22, 2026, ticking every second
- On/after wedding day shows "It's the day!" in italic Cormorant Garamond serif
- Styled with cream background, green border-top, backdrop blur

### 18. Countdown Labels — More Visible
- Changed label color from `#6b7254` → `#2a2a25` (dark)
- Added `font-weight: 500` to DAYS / HOURS / MIN / SEC labels

### 19. RSVP Form Removed — Save to Calendar
- Removed entire form (first name, last name, email, attendance, guests, dietary note)
- Removed `handleRsvp()` JS function
- Replaced with Google Calendar link button (opens calendar pre-filled: "Chester & Elbee Wedding", Nov 22 2026, Kuala Lumpur)
- Button reuses existing `.btn-submit` style with calendar icon SVG

---

## File Structure
```
wedding/
  index.html       — main site (all changes here)
  logo.jpeg        — couple's monogram logo
  *.mp3            — music tracks (2 songs in playlist)
```

## Key CSS Classes Added
| Class | Purpose |
|---|---|
| `.music-chevron` | Dropdown arrow on music player |
| `.music-player.open` | Rotates chevron when playlist open |
| `.music-player.pulse` | One-shot glow animation |
| `#coverPage` | Full-screen splash overlay |
| `#coverPage.hide` | Fades out cover on click |
| `.cover-*` | Cover page component styles |
| `.stem-g1` – `.stem-g4` | Animated botanical groups |
| `@keyframes stemSway` | Breeze wave on stems |
| ~~`@keyframes logoFloat`~~ | Removed — logo static |
| `@keyframes coverFadeIn` | Cover content entrance |
| `@keyframes coverPulseBtn` | Enter button pulse ring |
| `.hero-botanical-desktop` | Desktop botanical SVG (hidden on mobile) |
| `.hero-botanical-mobile` | Mobile botanical SVG (7 stems, shown on ≤768px) |
