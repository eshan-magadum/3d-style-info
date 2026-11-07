# 3D Narrated Shorts — Analysis and Production Skill

Use this workflow to build a fact-based, narrated vertical short in one selected 3D style. Start with the five reference profiles in `STYLE_BIBLE.md`; do not blend profiles without explicitly deciding what carries over.

## Phase 1 — Define the brief

Record:

- Working title and one-sentence premise.
- Audience and desired feeling (surprise, fear, wonder, empathy, comedy).
- Target duration and aspect ratio (default: 9:16).
- Chosen reference profile(s), with one primary profile.
- Required facts, forbidden inventions, and intended ending.
- Toolchain, target resolution, frame rate, and delivery format.

## Phase 2 — Verify the story

1. Gather reliable sources for each factual claim. Save source name, URL, date, exact claim, and confidence in `facts.md`.
2. Separate verified history from reenacted/staged visual interpretation.
3. Remove or qualify uncertain numbers, quotes, motives, and causal claims.
4. Confirm that the hook, midpoint reveal, and payoff can be shown in 3D.

## Phase 3 — Write a retention-first narration

Use this flexible structure:

1. **Hook (0–2 s):** an imageable contradiction, danger, unusual object, or direct question.
2. **Promise (2–5 s):** tell viewers what they are about to discover.
3. **Escalation (middle):** add one concrete fact or consequence per phrase; each must change the picture.
4. **Pivot:** reveal the missing reason or reversal.
5. **Payoff:** show the result, twist, or cost.
6. **Final image/line:** close on one specific visual echo; avoid a generic subscribe line unless it serves the channel.

Write for a spoken pace that remains easy to follow. Read aloud against a stopwatch. Do not use arbitrary words-per-second targets; reserve pauses for visual comprehension. Keep one sentence aligned to one or two visual beats. Add voiceover timecodes only after a real read or generated audio is available.

## Phase 4 — Create continuity bibles

Create one `characters.md` entry per character with: name/role, age range, body proportions, face landmarks, hair, clothing, materials, colors, silhouette, expression range, movement traits, and locked continuity details.

Create one `locations.md` entry per set with: dimensions and layout, time/weather, key props, foreground/midground/background layers, surfaces, light sources and direction, water/fire/smoke rules, practical camera paths, and details that must not move between shots.

For every recurring prop, record scale, orientation, hand, condition/state, and the story fact it represents. Track injury, wetness, damage, chronology, and wardrobe changes shot to shot.

## Phase 5 — Build the visual beat sheet

Before writing generation prompts or coding scenes, map each narration phrase to:

- In/out time.
- What the viewer must understand.
- Character action and expression.
- Story evidence/prop.
- Shot size and viewing angle.
- Foreground, subject, and background placement.
- Camera path with start/end positions and easing.
- Light source, direction, quality, color, shadow destination.
- Depth of field and focus target.
- Palette and material cues.
- Transition into the next beat.
- Continuity checks and known risk.

Use `templates/shot_plan_template.csv` and `templates/scene_prompt_template.md`.

## Phase 6 — Specify full 3D shots

Each shot prompt or scene specification must say:

1. Exact subject identity and current state.
2. Exact starting pose and the action over time.
3. The world layout and physical contacts.
4. Camera focal character, framing, path, speed, and focus behavior.
5. Key/fill/rim/practical lights and ambient contribution.
6. Surface response: roughness, texture scale, reflections, subsurface scattering where needed.
7. Atmosphere and particles only when motivated.
8. What is static, what moves, and what must remain locked.
9. Caption-safe region and where the focal point must remain.
10. Negative constraints: no floating props, no sliding feet, no disconnected hands, no face/wardrobe drift, no geometry popping, no unintended cuts, no physically impossible contact.

Prefer animating the camera and environment through a continuous path when a scene transition can be motivated that way. Use cuts when they clearly improve comprehension or impact.

## Phase 7 — Prototype and compare

1. Render a still at the first frame, a midpoint, and the last frame of each shot.
2. Compare these against a reference frame from the correct profile. Change one or two specific things per iteration.
3. Render a 2–5 second motion test for camera easing, contact, facial expression, water, cloth, particles, and shadows.
4. Inspect at full speed and frame by frame. A camera that looks smooth in stills may snap or float in motion.
5. Fix the cause, not the symptom: e.g. contact point, bad rig, wrong light direction, excessive blur, inconsistent set geometry, slow motion estimate misread.
6. Only then render the full sequence. Optimize resolution, samples, denoising, and upscaling after quality has passed.

## Phase 8 — Final quality gates

- **Story:** each line is supported by the image; no missing cause/effect beat; ending pays off the opening.
- **Continuity:** face, hair, clothing, props, room geometry, screen direction, object state, water level, and injury status match.
- **Physicality:** weight, foot contact, hand contact, momentum, shadows, reflections, and fluid motion read as attached to the world.
- **Camera:** move is motivated, starts and ends deliberately, eases naturally, preserves screen direction, and respects focus.
- **Lighting/grade:** subject reads against background; highlights do not clip; shadows retain useful information; palette supports the beat; shots match within a scene.
- **Depth/materials:** foreground/midground/background separation and believable material roughness; texture density fits shot size.
- **Expression:** eyes, brows, mouth, head angle, and body posture agree with the current emotion; no frozen or exaggerated face without intent.
- **Captions:** correct words and timing, readable on phone, within safe area, no overlap with the evidence/face/hands.
- **Sound:** voice intelligible; music/SFX support the beat without masking it; verify actual mixed audio, not only a waveform.
- **Export:** target dimensions/fps/duration/codec and final playback verified.

## Reference analysis protocol

For a reference video set, decode to a consistent 30 fps analysis timeline. Make a two-second sheet with all 60 frame tiles, inspect the sheets in sequential order, and record transitions/shot changes separately from continuous camera motion. Generate per-frame brightness, contrast, saturation, edge, frame-difference, cut-candidate, and camera-shift data. Validate every numeric finding visually. Include one-second full-size keyframes and a summary plot.

Do not treat phase correlation as ground truth for camera motion. It can miss slow pushes or confuse subject movement with camera movement. Do not treat edge density as an outline measurement. Do not infer script or audio solely from image statistics.
