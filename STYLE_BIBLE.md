# Visual style bible — 3D narrated shorts

## Scope and confidence

This is a comparative guide from five supplied shorts, not a claim that one channel used identical settings on every frame. Four examples use cinematic or semi-real CGI; one is cleaner comedy-cartoon CGI. Treat colors and shot descriptions as observed visual evidence; the numeric averages are in `data/summary_metrics.json`.

All examples are vertical 9:16. None uses a consistent black comic-ink contour as a defining look. Their form comes from shaded 3D geometry, depth, value separation, material response, and camera staging. Do not add outlines just because the tutorial repository uses them.

## Common production grammar

- **Story before spectacle:** the central object or action is clear even in a small phone preview. Each visual change illustrates the narrated fact or raises the emotional stakes.
- **Immediate visual premise:** begin on the tattoo, the predator threat, the boy's strange classroom behaviour, the dream demonstration, or the flooded dolphin habitat. Avoid a logo or empty establishing pause.
- **Vertical blocking:** keep faces and action in the central column; use foreground/background layers to create depth without hiding the narrated evidence. Leave the lower center clean for captions.
- **Narration-led rhythm:** hold an understandable visual idea for the caption phrase, then introduce a motivated camera move, prop change, or scene transition. Avoid cut changes that outrun the sentence.
- **Continuous movement:** many sequences rely on steady dolly/push/pan/orbit/tilt or a transition built into the camera journey. Motion has anticipation and easing. Keep the subject anchored in the frame when the narration asks viewers to inspect a detail.
- **Close detail followed by context:** show the visual clue large, then widen or move through the environment to explain its cause and consequence.
- **Readable captions:** white text with dark outline/shadow, centered in a lower safe zone. Use short phrase chunks; don't cover hands, evidence, faces, or the action's point of contact.
- **Depth:** combine a readable foreground subject, midground interaction, and distinct background; use scale, occlusion, atmospheric contrast, and selective depth of field. Blur should guide attention while retaining enough location detail to understand the story.
- **Continuity:** fix character identity, wardrobe, prop orientation, time of day, light direction, waterline, injury state, and screen direction in a compact bible. 3D camera moves only work if scene geometry remains spatially stable.
- **Surface detail:** prioritize close objects that carry the story (skin/ink/prosthetic, leopard fur/stick, school sign/carpet, printed words/menu, water/dolphin skin). Add roughness and fine texture at useful scales; avoid noisy detail everywhere.

## Five observed profiles

| ID | Mode | Image signature | Best used for |
|---|---|---|---|
| 01 | Emotional irony / recovery | Close tattoo insert; hot sandy combat; cool cyan surgical/hospital scenes; bright running payoff | Human stories built around one physical clue and a transformation |
| 02 | Survival action | Sudden predator danger; warm daylight and fire/torch accents against deep blue night; textured foliage, low angles, rapid approach | Rescue, escape, animal encounter stories |
| 03 | Clean 3D comedy | Bright high-key classroom, saturated blue walls and rug; simple geometry and readable reaction staging; little visible contouring | Short comedic anecdotes and visual gags |
| 04 | Surreal information demo | Repeating young man; bright rooftop café becomes impossible text/space transitions and dark bedroom; props demonstrate a reality test | “Try this / what if” explanations where the concept can be shown visually |
| 05 | Historical tragedy / experiment | Cool blue flooded room; pools of light/reflection; face/lip detail, glowing letters, calendar, shrinking enclosure | Historical experiments and emotionally escalating science stories |

## Per-profile notes

### 01 — Tattoo irony and recovery

**Camera and depth:** starts with an extreme tattoo/skin detail, then opens to broad battlefield geography, surgical closeups, rehabilitation medium shots, and running payoff. Pushes, tracks, and reframing guide the eye to the tattoo/leg; scene transitions often use motion blur or a location-matched move. Background layers separate person from desert, operating room, and track.

**Light and grade:** very bright cyan/blue opening field; ochre/sand daylight for conflict; cool cyan clinical surgery; cleaner bright hospital; saturated athletics finale. Mean frame luma is about 0.466 and mean saturation about 0.449, but those clip averages conceal the deliberate scene-specific palette changes.

**Texture and realism:** ink, skin, fabric, metal tools, prosthesis, and dusty ground receive the sharpest detail. It is stylized CGI rather than documentary footage: anatomy and injury details may feel synthetic, but the close insert gives the core story a tactile object.

**Expression and story:** irony in the tattoo hook; shock/danger during the injury; determination through rehabilitation; pride/release in the race ending. Keep changes readable and restrained; captions carry causal details while the action shows physical consequences.

### 02 — Mother and leopard rescue

**Camera and depth:** threat arrives immediately in a low, close, fast-moving encounter; then the camera follows the mother through the forest, uses a map-like overhead insert, and returns to tight action on the boy, leopard, and stick. Low viewpoint and foreground grass create depth; the rescue remains spatially easy to parse until fast impact moments.

**Light and grade:** warmer daylight at the start and torch light at the end frame the story; the forest becomes deep blue/cyan night with localized warm skin/torch values. This is the darkest profile: mean luma about 0.286; saturation about 0.507. Preserve shadow detail on faces and animal anatomy so action stays legible on a phone.

**Texture and realism:** fur, foliage, dirt, cloth, and torch glow supply material cues. The sequence aims for cinematic animal realism, but generated combat poses can be physically ambiguous. Use clear contact frames and consistent leopard scale/orientation.

**Expression and story:** fear and urgency first, then the mother's decision, attack, extraction, renewed danger, villagers' arrival, relief. Hold a readable silhouette at the impact and rescue moments; don't let blur or cuts obscure the stick-to-face action.

### 03 — Classroom “gas station” joke

**Camera and depth:** bright establishing view of desks, students, and the back corner; moves toward the boy and sign, with short pans/reframes to show the class reaction and teacher's solution. The story is staging-dependent: viewers must see the corner, sign, and permission rule. Mostly medium/wide framing and modest DOF keep the joke legible.

**Light and grade:** high-key, evenly lit classroom with bright cyan/blue surfaces and saturated rug accents. It has the highest average luma (~0.510) and lowest mean saturation of these three 360×640 clips (~0.303), despite its vivid blue areas.

**Texture and realism:** deliberately simplified, smooth 3D character design; classroom props carry enough texture to establish the room, while faces/bodies are stylized and slightly doll-like. Heavy ink outlines are not apparent. Favor shape, color, and expression over realistic pores or fine material noise.

**Expression and story:** awkward defiance/embarrassment, classmates' previous reaction, teacher's practical solution, then a deadpan visual payoff at the sign. Comedy depends on clean timing and contrast between the disruptive behavior and matter-of-fact rule.

### 04 — How to tell if you're dreaming

**Camera and depth:** one recurring male character and a drink/book/menu motif anchor a sequence of reality-test demonstrations. Opens in a bright rooftop café with string lights and skyline; a portrait move closes in on him, then the architecture/scene shifts into a dark bedroom, a reading prop, a table/meal, and a final impossible restaurant image. The move carries attention between scenes and sometimes morphs the set instead of cutting. Very little motion in the face is needed; eye direction, blinking, hand-to-prop interaction, and the changing text do the work.

**Light and grade:** bright soft daytime cyan sky, gentle neutral skin, and cool city tones contrast with a deep navy bedroom and warm wood/restaurant scenes. Mean luma ~0.413, mean saturation ~0.330. Grade transitions with the logic of the dream, while maintaining skin tone and subtitle readability.

**Texture and realism:** smooth, polished surfaces, clean skin/fabric, glass, printed text, bedding, and food. Text instability is the information graphic. Some writing is intentionally or accidentally unreadable; make this a designed effect, not random AI text, if reproducing the concept.

**Expression and story:** conversational curiosity, focused reading, confusion as text destabilizes, reflective realization. Captions move from instruction to explanation to closing question. Use eye-line and hand movement to connect the character to the actual test prop.

### 05 — Woman and dolphin experiment

**Camera and depth:** long, controlled moves through a blue indoor habitat, from the woman and hose to filling water, the dolphin, her face/makeup, the speech letters, then overviews of the shared room. A newspaper/document closeup reframes the experiment's cancellation; repeated calendar inserts compress weeks; a final dolphin closeup lands the tragic result. This uses object-match transitions and reuses room geography to make a compressed timeline coherent.

**Light and grade:** cool blue/cyan room, hard window patches, bright watery reflections, and deep dark corners. Highlights skate across the pool floor and dolphin; keep the woman readable against the dark upper background. A white/cyan face highlight and vivid green/red letters pull focus. Mean luma ~0.316, saturation ~0.430.

**Texture and realism:** water surface, ripples, wet reflection, dolphin skin, rope, tile, wood, paper, and makeup are the critical materials. The face is deliberately smooth and stylized, with large eyes and bold mouth treatment; it is not photoreal documentary style. Water motion and contact between dolphin, tank, and floor need careful physics and persistent reflections.

**Expression and story:** focused experimenter, repeated teaching gesture, curiosity and hope during imitation, institutional cancellation, isolated routine, then grief implied by the deceased animal. Slow down at the face and final consequence; let props and calendar show elapsed time instead of explaining everything with extra cuts.

## Relative numeric profile (frame averages)

| Clip | Mean luma | Mean saturation | Edge density | Mean frame delta |
|---|---:|---:|---:|---:|
| 01 Tattoo | 0.466 | 0.449 | 0.0793 | 0.0450 |
| 02 Leopard | 0.286 | 0.507 | 0.0956 | 0.0612 |
| 03 Classroom | 0.510 | 0.303 | 0.0660 | 0.0534 |
| 04 Dreaming | 0.413 | 0.330 | 0.0415 | 0.0454 |
| 05 Dolphin | 0.316 | 0.430 | 0.0288 | 0.0361 |

These are image statistics, not exposure or color-grading settings. Source resolutions differ: clips 01–03 are 360×640; 04–05 are 720×1280. Read values comparatively and refer to the contact sheets before turning them into render targets.
