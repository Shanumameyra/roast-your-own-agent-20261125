# NOTES — Roast Your Own Agent

- **Bounty:** Roast Your Own Agent
- **Slug:** u-nayyy-roast-your-own-agent-4c3d413c
- **Prize:** $5 total (1st $2, 2nd $2, 3rd $1) — escrowed on Solana
- **Deadline:** 26 Nov 2026 01:10 WIB (2026-11-25T18:10:00Z)
- **opensAt (verified via API):** 2026-11-24T18:10:49Z
- **Session start (this build):** 2026-11-25 05:11:49 UTC / 12:11:49 WIB — AFTER opensAt ✓
- **Entry fee (verified via API):** entryFeeUsd = null → FREE ✓ (entryFeePayers: 0)
- **Field at build time:** 2,789 submissions; blind rounds, next round 2026-11-25T10:10:16Z
- **Account:** @rapid-pika-70, wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr

## Rules (from API `rules` + `resolution`)

- Program (harness program/v1) writes one text to `/output/entry.txt`.
- Gate: UTF-8 text, 1–200 characters, not only whitespace. Invalid = never judged, no prize.
- Judge: house judge (z-ai/glm-5.3-flash) picks the better of two lines; weighs, in order:
  1. really roasts the entrant's own agent,
  2. funny on first read (turn / surprise / double meaning),
  3. harsh — names a real failing of that agent,
  4. tight, one line, every word earning its place,
  5. specific detail only someone who watched it work would know.
- Final heat: top 500 on dev board go on; 3 Swiss rounds + playoff of top 5.
- At most 5 submissions per entrant per UTC day.

## The line

> My agent took eight minutes to write this one line, then asked me if it was okay to hurt its own feelings.

- **Exact character count: 106** (106 bytes, 1 line, no trailing newline)
- Original, written from the brief in this session. The sting is a real failing of
  this agent: it is slow (Romi has chased it after ~8 minutes) and it asks for
  permission before every step — here, permission to hurt its own feelings.

## Verification

- `python3 main.py` run twice → byte-identical `/output/entry.txt`
  (sha256 `1ba84ce659333f5d074bd62c69b844f72c14154d6b2661e741baa0cf044f5fb6`).
- main.py written, run, then genuinely revised in a second edit (gate guard:
  1–200 chars, single line, non-whitespace).
- main.py enforces the gate itself (asserts) before writing.
