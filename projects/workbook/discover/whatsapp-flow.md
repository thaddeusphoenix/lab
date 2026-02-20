# WhatsApp Conversation Flow Prototype

A scripted interaction design mapping the end-to-end WhatsApp experience for Workbook. Each scenario is written as a back-and-forth dialogue so the interaction is concrete and testable.

---

## 1. Onboarding (First Contact)

The worker discovers Workbook through a peer, a flyer on a job site, or a QR code from a GC.

> **Worker:** Hi
>
> **Bot:** Hey! Welcome to Workbook — the app that turns your work into a portfolio.
>
> Every job you do, you already prove it with your hands. Now you can prove it with photos too. Send us Before, Progress, and Completed shots from your jobs, and we'll build your digital Reference Book — a verified record of your skills that you own and can share with anyone.
>
> What's your first name?
>
> **Worker:** Marco
>
> **Bot:** Good to meet you, Marco. What's your trade? For example: tile, framing, drywall, electrical, plumbing, painting, concrete...
>
> **Worker:** Tile
>
> **Bot:** Got it — Marco, Tile. Your Workbook is set up and linked to this number.
>
> Whenever you're on a job, just send a photo and tell me if it's a Before, Progress, or Completed shot. That's it. I'll handle the rest.
>
> Ready to log your first job?

---

## 2. Photo Submission — The Core Loop

### 2a. Before Photo

> **Worker:** *(sends a photo of an unfinished bathroom floor)*
>
> **Bot:** Nice. Is this a **Before**, **Progress**, or **Completed** photo?
>
> **Worker:** Before
>
> **Bot:** Got it — logged as a Before photo. I can see you're at a site in Brookfield, IL. I'll use this as the starting point for this job.
>
> Send more photos as you go. When you send the Completed shot, I'll bundle the whole job together in your Workbook.

*Behind the scenes: EXIF data extracted — GPS coordinates (41.8236, -87.8484), timestamp (2026-02-19 07:42 AM). No action shown to user.*

### 2b. Progress Photo

> **Worker:** *(sends a photo of partially laid tile with mortar visible)*
>
> **Bot:** Is this a **Before**, **Progress**, or **Completed** photo?
>
> **Worker:** Progress
>
> **Bot:** Added to your current job at the Brookfield site. Looking good, Marco. Keep going.

### 2c. Completed Photo — Job Bundled

> **Worker:** *(sends a photo of the finished tile floor, grouted and clean)*
>
> **Bot:** Is this a **Before**, **Progress**, or **Completed** photo?
>
> **Worker:** Completed
>
> **Bot:** Your tile work at Brookfield, IL is now in your Workbook.
>
> **Job summary:**
> - 3 photos (Before → Progress → Completed)
> - Location verified: Brookfield, IL
> - Date: Feb 19, 2026
>
> This job is now part of your Reference Book. Want to see your full Workbook? Just say "my workbook" anytime.

---

## 3. Peer Validation — Proximity Protocol

Another verified Workbook user (Carlos, also a tile worker) was logged at the same GPS coordinates on the same day.

> **Bot → Carlos:** Hey Carlos — were you on site with Marco at the Brookfield job today?
>
> **Carlos:** Yes
>
> **Bot → Carlos:** Can you vouch for Marco's tile work there?
>
> **Carlos:** Yes
>
> **Bot → Carlos:** Thanks, Carlos. Your validation has been recorded.

---

> **Bot → Marco:** Your Brookfield tile job just got a peer validation from Carlos. That's a trust badge on your Workbook entry — it shows others that a fellow tradesperson verified your work in person.

---

## 4. Portfolio Review

### 4a. Viewing Your Workbook

> **Worker:** My workbook
>
> **Bot:** Here's your Workbook, Marco:
>
> **Marco — Tile**
> 2 jobs logged | 6 photos | 1 peer validation
>
> **Job 1 — Brookfield, IL** (Feb 19, 2026)
> Tile installation, 3 photos, 1 peer validation from Carlos
>
> **Job 2 — Oak Park, IL** (Feb 12, 2026)
> Tile repair, 3 photos, no validations yet
>
> Want to share your Workbook? I can generate a link.

### 4b. Sharing a Public Profile

> **Worker:** Share it
>
> **Bot:** Here's your public Workbook link:
>
> workbook.co/marco-tile-5a3f
>
> Anyone with this link can see your verified jobs, photos, and badges. Send it to contractors, post it anywhere — it's yours.

---

## 5. Error and Edge Cases

### 5a. Photo With No EXIF Data

> **Worker:** *(sends a screenshot or a photo with stripped metadata)*
>
> **Bot:** I couldn't detect the location or time from this photo. This can happen with screenshots or forwarded images.
>
> Can you tell me where this job is? Just type the city or address.
>
> **Worker:** Oak Park IL
>
> **Bot:** Got it — logging this as Oak Park, IL. Is this a Before, Progress, or Completed photo?

### 5b. Blurry or Unrecognizable Photo

> **Worker:** *(sends a very blurry photo)*
>
> **Bot:** That photo came through a little blurry — I can't make out the work clearly. Could you send another shot? Try to get good lighting and hold steady.

### 5c. Duplicate Submission

> **Worker:** *(sends the same Completed photo from the Brookfield job again)*
>
> **Bot:** Heads up — this looks like the same photo from your Brookfield tile job on Feb 19. I've already got it in your Workbook.
>
> If this is from a different job, let me know and I'll log it separately.

### 5d. Unrecognized Message

> **Worker:** How much does this cost
>
> **Bot:** Workbook is free for workers. You own your portfolio — we'll never charge you for building your Reference Book.
>
> If you want to log a job, just send a photo. If you want to see your work, say "my workbook."

### 5e. Multiple Jobs at the Same Time

> **Worker:** *(sends a Before photo with a GPS location different from the current active job)*
>
> **Bot:** This photo is from a different location than your current job in Brookfield. Looks like you're starting a new job.
>
> I'll open a new job entry for this location. Is this a Before photo?
>
> **Worker:** Yes
>
> **Bot:** New job started at Oak Park, IL. Logged as your Before shot.

---

## Flow Summary

```
First message
  → Onboarding (name, trade)
    → Account created (phone = ID)

Send photo
  → Bot asks: Before / Progress / Completed?
    → EXIF extracted silently (GPS, timestamp)
    → Photo filed to current or new job

"Completed" photo arrives
  → Job bundled (Before → Progress → Completed)
  → Summary shown to worker
  → Proximity Protocol checks for peer validators

Peer detected at same site
  → Bot asks peer to vouch → Yes/No
  → Trust badge added to job entry

"My workbook"
  → Portfolio summary (jobs, photos, validations)
  → Option to share public link

Edge cases
  → No EXIF → ask for manual location
  → Blurry photo → ask for retake
  → Duplicate → flag gently
  → New location → open new job
```
