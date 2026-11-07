# Method reverse-engineered from the supplied tutorial transcript

The tutorial describes an iterative style-reconstruction project, not a prompt-only workflow. Its sequence is useful for this package, with several adaptations for fully 3D information shorts.

## The creator's described sequence

1. **Collect a coherent reference set.** They studied 20 shorts from one channel and selected examples that matched the target style. That reduces noise from mixing unrelated looks.
2. **Recover the source narration.** They found that an automatic transcript was from a German dub, so they switched to the original English audio and transcribed the source videos. The narration was analyzed for hook, escalation, pivot, payoff, and pacing.
3. **Inspect at frame rate.** They decoded video at 30 fps and arranged every two seconds as a sheet of 60 labeled frames.
4. **Measure instead of relying on memory.** They tracked frame-to-frame image shifts, flagged possible cuts, and recorded brightness, contrast, and saturation.
5. **Write a rulebook.** They separated script design, visuals, and measurement into reproducible notes.
6. **Make a short test before scaling.** They built a five-second proof, found camera and staging problems, then changed tools after identifying that the target had flat characters in a real 3D world.
7. **Build the actual scene system.** The tutorial describes using 3D assets, code-painted textures, facial expressions, a physics-driven bridge, and an outline effect for the hybrid 2D/3D style.
8. **Render stills first and compare.** They checked frames before producing the final video, then compared their output with references by category: edges, color, light/shadow, texture, character proportions, depth, framing, and motion.
9. **Fix named causes, not vague impressions.** Their examples include a blur pass erasing the outlines, an overly abrupt camera move, pure-black shadows, poor sunset shadow color, thick limbs, and incorrectly assumed head shapes.
10. **Keep work reviewable.** The creator split agent work by domain and gave build roles separate file ownership to reduce collisions. For a solo workflow, use the same domain-separated checklist and checkpoint commits; agents are optional.
11. **Optimize after quality is stable.** The transcript mentions a separate realistic 3D workflow with a rigged character, optimized render settings, and upscaling. Treat render optimization as a measured step after a small scene has passed visual QA.

## Adaptation to the five supplied examples

These references are not the tutorial's outlined 2D-character / 3D-world style. They use full 3D people, props, creatures, and environments. So this pack does **not** copy the tutorial's black edge-outline specification. It carries over the method—frame-level measurement, a visual rulebook, prototypes, still-frame QA, and objective comparison—while setting the 3D rules from the supplied clips.

The five clips also differ internally. The emotional tattoo story, leopard rescue, dream explainer, and dolphin tragedy lean toward cinematic CGI; the classroom story is more comic and simplified. A production should choose one profile or deliberately specify a mixed profile, then keep characters, lighting, surface detail, camera, and grade coherent within that choice.

## The main lesson

Do not ask a model only to “make it cinematic.” Give it the evidence-backed style rules, the story beat, the exact scene state, the camera path, the light sources, the depth cues, the texture priorities, and a list of continuity constraints. Render a still or a very short motion test, compare it to a target frame, name the measurable gap, then revise.
