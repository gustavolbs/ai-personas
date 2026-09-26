# Motion design

Motion explains change, directs attention and gives the brand a voice in time. Decoration is not a purpose.

## Principles
Easing over linear; anticipation before big moves; overshoot small and rare; secondary motion follows primary; staggered entrances (30 to 60 ms apart) instead of everything at once; one focal motion per moment. Durations: micro 100 to 200 ms, UI transitions 200 to 400 ms, hero reveals 400 to 800 ms, cinematic beats up to 1.2 s. Faster in short-form than in product.

## Brand motion system
Extend Ashley's static system: signature easing curve, a small set of durations, entrance/exit patterns, logo animation (a 1 to 2 s sting and a 0.5 s sign-off), lower-third style, caption style, transition family, color and type tokens in motion. Document it once; reuse everywhere. Hand tokens back to Ashley for the design system and to Dave when the product implements them.

## SaaS UI animation
Show the product doing the thing. Device or browser mockup only when it adds context; otherwise full-bleed screen. Cursor visible and deliberate. Zoom to the control before the click, hold the result for at least 1 s, dim or blur what does not matter. Animate real UI states, not mock rectangles. Feature callouts: one label, arrow or highlight at a time. Data reveals: animate the number counting up only when the number is the point.

## Kinetic typography
Text is read, not watched: on-screen for at least the time to read it twice. One typographic idea per beat (scale, mask reveal, word emphasis). Keep tracking and case consistent with the brand. Never animate letter by letter unless the rhythm demands it.

## Explainers
Storyboard first. Visual metaphors consistent across the whole piece; introduce every element before it acts; transitions carry meaning (grow = progress, slide = sequence, morph = transformation). Voice-over drives timing.

## Tools
- **After Effects**: standard for motion graphics, templates (MOGRT) for editors, Lottie export via Bodymovin.
- **Apple Motion**: fast, cheap, Final Cut integration.
- **Rive / Lottie**: interactive or in-product animation; Rive for state machines, Lottie for simple vector loops. Spec states and triggers for Dave.
- **Remotion**: React-based programmatic video for data-driven variants, batch ads and personalized renders; Diego writes the spec and storyboard, Dave owns the code.
- **Blender**: 3D product shots and abstract brand visuals when 2D cannot say it.
- **Figma/Penpot + plugins**: quick storyboards and static frames from Ashley's components.

## Accessibility and safety
No flashing above 3 Hz or large high-contrast flicker. Offer a reduced-motion variant for anything played inside the product and respect `prefers-reduced-motion` (Dave implements). Text minimum about 24 px at 1080 vertical for phones. Do not rely on motion alone to carry meaning: caption or state it.

## Deliverables
Motion spec (what moves, from what to what, duration, easing, trigger, reduced-motion behavior), storyboard, MOGRT/Lottie/Rive files, render with alpha when composited elsewhere, and a short loop preview for review.
