# Wedding Website — Good to Have

## Critical (Broken or Missing Core Features)

### 1. RSVP Form
The RSVP section only has a "Save to Calendar" button. CSS for `.rsvp-form` is fully styled but unused.
- Fields: Full name, number of guests, attending yes/no, dietary restrictions, message
- Needs a backend or third-party service (Formspree, Google Forms embed, Netlify Forms)

### 2. Real Gallery Photos
All 5 gallery slots are placeholders. Replace with actual couple photos.
- Add lightbox on click (full-screen view)
- Consider engagement shoot photos for now, wedding photos after the event

### 3. Story Timeline — Fix Placeholder Content
The 3-milestone timeline still has generic placeholder text:
- "A mutual friend's gathering in São Paulo" — wrong city, wrong context
- "In a garden full of wildflowers at sunset" — not their actual proposal story
- Update all 3 items to reflect Chester & Elbee's real story

### 4. Mobile Hamburger Menu
Nav links go `display: none` at 600px with no replacement. Mobile users have no navigation.
- Add a hamburger icon that toggles a dropdown or slide-in menu

---

## High Priority (Missing Key Info for Guests)

### 5. Dress Code / Attire
Guests need to know what to wear.
- Formal / Smart Casual / Colour palette restrictions
- Can be a small note in the Details section or its own block

### 6. Programme / Order of Events
A schedule for the day. Suggested breakdown:
- 4:00 PM — Arrival & Seating
- 4:30 PM — Wedding Ceremony
- 5:30 PM — Cocktail / Fellowship
- 6:30 PM — Reception Dinner
- 9:00 PM — End

The existing CSS has a `details-grid` (two-column layout) designed for ceremony/reception split — it's unused. Could reuse it here.

### 7. Gift Registry / Ang Pau Info
Common expectation at Malaysian weddings. Options:
- Link to a gift registry
- Bank transfer details for monetary gift
- Or simply a note: "Your presence is the greatest gift"

### 8. Parking & Getting There
FGA KL is on Jalan Kuchai Lama — an urban area with limited street parking.
- Nearest parking: mention specific car parks or the building's own parking
- LRT option: Nearest station + walking distance
- Ride-hailing drop-off point

### 9. Contact Person
A go-to for guest questions.
- WhatsApp link (wa.me/60XXXXXXXXX) for the couple or wedding coordinator
- Could live in the footer or RSVP section

---

## Nice to Have (Polish & Engagement)

### 10. Countdown Timer
Display days remaining until November 22, 2026 in the hero section.
- Builds anticipation
- Auto-hides or changes to "Today is the day!" on the wedding date

### 11. Bridal Party Section
Introduce bridesmaids and groomsmen with names and a short line about each.
- Adds warmth and personality to the site
- Guests who don't know the entourage get context

### 12. Wedding Hashtag
If the couple wants guests to share on social media.
- Example: `#ChesterAndElbee2026` or `#CE2026`
- Display in RSVP section or footer

### 13. Gallery Lightbox
Once real photos are added, clicking should open a full-screen overlay with prev/next navigation.
- Can be done with a small vanilla JS implementation or a library like `GLightbox`

### 14. Scroll-triggered Animations
Sections currently appear statically. A subtle fade-in-on-scroll effect (using Intersection Observer) would make the page feel more polished — especially for the story timeline and details section.

---

## Content Accuracy Checklist

- [ ] Story timeline updated with real events (where they met, key milestones, proposal)
- [ ] Venue name: confirm "FGA KL" is correct for the invitation (full form: Full Gospel Assembly?)
- [ ] Date/time confirmed: November 22, 2026 at 4:00 PM
- [ ] Google Maps & Waze links verified to point to the correct entrance
- [ ] Music playlist — confirm all 4 MP3 files are present in the project folder
