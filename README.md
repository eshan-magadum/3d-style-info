# 3D Narrated Shorts — Reference Analysis Pack

This package reverse-engineers five supplied vertical shorts to build a reusable reference kit for **fully 3D narrated information and story shorts**. It is inspired by the frame-measurement and reusable-skill approach described in the supplied YouTube tutorial transcript, and the [claude-animated-shorts repository](https://github.com/mromidev/claude-animated-shorts/tree/main).

## Scope

The five examples are **not one identical style**. Four use cinematic or semi-real 3D story imagery; the classroom clip uses cleaner, brighter cartoon CGI. The package keeps each profile distinct and identifies shared production grammar (vertical framing, readable staging, narration-led beats, continuous image motion, frequent close-ups, and captions). It does not impose the tutorial repo's black comic-ink outline look: the supplied five clips do not use that as a consistent defining feature.

## What's included

- `SKILL.md` — reusable workflow for analyzing references and producing a 3D narrated short.
- `STYLE_BIBLE.md` — shared rules plus five separate visual profiles.
- `PROFILE_SELECTION.md` — which reference mode suits different story types.
- `METHOD_FROM_TUTORIAL.md` — the creator's described method, translated to this 3D reference set.
- `ANALYSIS_METHOD.md` — exactly what was measured and where automation can be misleading.
- `SCRIPT_AND_SOUND_NOTES.md` — caption-based story beats and the limits of the script/audio analysis.
- `data/frame_metrics_30fps.csv` — 5,163 rows, one for every normalized 30 fps frame.
- `data/frame_review_index.csv` — frame-to-contact-sheet/keyframe lookup for all 5,163 frames.
- `data/manifest.json`, `data/summary_metrics.json`, and `data/candidate_events.csv` — source metadata, per-clip statistics, and events flagged for review.
- `references/sheets/` — 88 contact sheets, two seconds each; every analyzed frame appears in a labeled tile.
- `references/keyframes/` — one full-resolution frame per second for quick lookup.
- `references/clip_notes/` — individual shot, lighting, camera, depth, color, texture, expression, realism, and story analyses for all five clips.
- `templates/` — fact sheet, script, continuity bible, scene prompt, shot plan, and final review templates.
- `scripts/analyze_reference_set.py` — repeatable 30 fps extraction and metric generation.
- `scripts/ocr_visible_captions.py` — optional caption OCR helper; text is only a rough visual-caption read, not audio transcription.
- `reports/frame_metric_summary.png` — visual comparison of frame-level image measurements.
- `reports/reference_overview.jpg` — five opening frames for quick identification.

## Start here

1. Read `STYLE_BIBLE.md` and select one style profile before creating a new short.
2. Read the relevant clip note and `METHOD_FROM_TUTORIAL.md`.
3. Use the templates in `SKILL.md` to build the fact-checked script, cast/location bible, visual beat sheet, per-shot plan, lighting and camera plan, and final QA list.
4. For a new reference set, use the analysis command below, then visually check the generated contact sheets in order.

## Re-run analysis

Requirements: FFmpeg/ffprobe, Python 3, NumPy, Pillow, SciPy.

```bash
python scripts/analyze_reference_set.py --input path/to/mp4s --out path/to/analysis --fps 30
```

Inputs are sorted alphabetically; keep only the intended reference videos in that folder. The script writes a metrics row per decoded frame and 60-frame contact sheets. Use a separate folder per target visual style so conflicting looks do not get averaged into one rulebook.

## Frame count

The supplied videos total **172.31 seconds**. At a normalized 30 frames per second, the analysis contains **5,163 frames**:

| ID | Reference | Length | Frames | Source size |
|---|---|---:|---:|---:|
| 01 | His Tattoo Turned Ironic After Amputation | 35.37 s | 1,059 | 360 × 640 |
| 02 | Mother Fights Leopard To Save Her Son | 37.44 s | 1,121 | 360 × 640 |
| 03 | The Classroom With A Farting Corner | 23.79 s | 712 | 360 × 640 |
| 04 | How To Tell If You're Dreaming | 36.24 s | 1,087 | 720 × 1280 |
| 05 | The Woman Who Lived With A Dolphin | 39.47 s | 1,184 | 720 × 1280 |

Four sources report approximately 29.97 fps; one reports 30 fps. The analysis uses FFmpeg `fps=30` resampling. It is a consistent analysis timeline, not a claim that every source was originally captured at exactly 30.000 fps.

## Important reading note

Numeric measures support inspection; they do not replace it. The camera-motion fields are image-space estimates and can miss slow dolly/zoom motion or confuse character movement with camera movement. The candidate cut list requires visual review. See `ANALYSIS_METHOD.md` before using numeric thresholds as creative rules.
