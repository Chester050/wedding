# Wedding Website — Session Summary
**Last updated:** 2026-05-26
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

### 8. Botanical Mobile Responsiveness
- Problem: `preserveAspectRatio="none"` squished ~50 stems into 375px → stems every 6px
- Added `.hero-botanical-desktop` class to existing 1440px SVGs, hidden on ≤768px
- Added `.hero-botanical-mobile` SVGs with 7 stems evenly spread in a 400px viewBox
- Mobile stems: stroke-width 2.5, spaced at x=30,90,155,200,245,310,370
- Both top + bottom botanical have desktop/mobile variants

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
