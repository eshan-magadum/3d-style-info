# Measurement and review method

## Data captured for every frame

Each input was decoded through FFmpeg's `fps=30` filter. For each output frame, the analysis script resized the image to a 320 px working width for general image statistics and to 160 px for phase correlation. The CSV contains:

- Luma mean, 10th/50th/90th percentiles, and standard deviation.
- Luma contrast range (90th minus 10th percentile).
- Mean and 90th-percentile saturation.
- Edge density above a fixed gradient threshold, mean gradient, and Laplacian variance.
- Luma histogram entropy.
- Mean absolute luma difference from the previous frame.
- A 32-bin luma-histogram chi-square distance from the previous frame.
- Phase-correlation translation estimate (`phase_image_dx_px`, `phase_image_dy_px`) and peak ratio.

The data file has one row per frame, with clip ID, source name, frame number, and timecode. Each 2-second contact sheet has up to 60 thumbnails labeled with frame number and time. Full-size one-second keyframes make close inspection easier.

## What the measurements can support

- Luma, contrast, and saturation can show scene-level grade changes and identify possible lighting shifts.
- Edge/gradient/entropy can help compare sharpness and visual complexity.
- Frame delta can identify periods of stillness, movement, or abrupt changes.
- Histogram distance can flag candidate transitions.
- Phase correlation can estimate a dominant translation between adjacent images when the scene is stable.

## What they cannot prove

- A high frame delta does not identify whether the camera, subject, water, particles, or text caused the change.
- Phase correlation is an image-space shift proxy, not a recovered camera path. It under-reports subtle dolly/zoom movement and can be thrown off by subject motion, animated overlays, parallax, cuts, or exposure changes. A low median does not mean the camera is visually static.
- A histogram flag is a candidate, not a confirmed edit. Dissolves, lighting flashes, explosions, and camera moves may trigger it; a visually quiet cut may not.
- Edge density is not an outline detector. It measures contrast boundaries and will respond to fur, text, hair, and lighting edges.
- Luma/saturation numbers do not distinguish an intentional palette from compression, source transfer, subtitle graphics, or display calibration.
- Expression, performance, realism, narrative logic, and whether motion looks physically attached require visual and story review. The CSV alone cannot assess them.

The tutorial transcript itself reports that a stillness statistic misread slow pushes as stationary. This pack therefore uses the numerical series as a map for human review, not as final truth. For close camera analysis on future projects, add background feature tracks or optical flow and compare those estimates against the contact sheets.

## Caption and script evidence

All five clips have visible burned-in captions. This pack uses those captions and the supplied contact sheets to describe the narrative beats. Optional OCR is included, but it is error-prone and is **not an audio transcript**. Exact spoken dialogue, voice acting, music, or sound effects require an audio transcription/listening pass; do not infer them from visual captions alone.

## Reproducibility

`data/manifest.json` records each source file, resolution, nominal frame rate, duration, analysis rate, and decoded frame count. `scripts/analyze_reference_set.py` recreates the per-frame metrics, keyframes, contact sheets, candidate events, and summary JSON when given the source MP4s.
