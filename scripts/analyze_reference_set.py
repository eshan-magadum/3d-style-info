#!/usr/bin/env python3
"""Decode every input at 30 fps and build frame metrics and contact sheets."""
from __future__ import annotations

import argparse
import csv
import json
import math
import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.fft import fft2, ifft2


def run_json(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(p.stdout)


def phase_shift(a, b, full_width):
    """Translation of the visible image from a to b, estimated at 160px width."""
    h, w = a.shape
    wy = np.hanning(h).astype(np.float32)
    wx = np.hanning(w).astype(np.float32)
    win = wy[:, None] * wx[None, :]
    fa = fft2((a - a.mean()) * win)
    fb = fft2((b - b.mean()) * win)
    cross = fa * np.conj(fb)
    cross /= np.maximum(np.abs(cross), 1e-9)
    corr = np.abs(ifft2(cross))
    y, x = np.unravel_index(np.argmax(corr), corr.shape)
    if x > w // 2:
        x -= w
    if y > h // 2:
        y -= h
    # Parabolic subpixel peak refinement.
    def refine(arr, i, axis_len):
        im, ip = (i - 1) % axis_len, (i + 1) % axis_len
        c0 = float(arr[i]); cm = float(arr[im]); cp = float(arr[ip])
        den = cm - 2 * c0 + cp
        return 0.5 * (cm - cp) / den if abs(den) > 1e-9 else 0.0
    subx = refine(corr[y % h, :], x % w, w)
    suby = refine(corr[:, x % w], y % h, h)
    scale = full_width / w
    return (x + subx) * scale, (y + suby) * scale, float(corr.max() / (corr.mean() + 1e-9))


def frame_metrics(rgb, prev_rgb, prev_gray, prev_motion, width, height):
    aw = min(320, width)
    ah = round(height * aw / width)
    im = Image.fromarray(rgb).resize((aw, ah), Image.Resampling.BILINEAR)
    arr = np.asarray(im, dtype=np.float32) / 255.0
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    sat = (mx - mn) / np.maximum(mx, 1e-5)
    gx = np.diff(y, axis=1, prepend=y[:, :1])
    gy = np.diff(y, axis=0, prepend=y[:1, :])
    grad = np.hypot(gx, gy)
    lap = np.zeros_like(y)
    lap[1:-1, 1:-1] = (y[:-2, 1:-1] + y[2:, 1:-1] + y[1:-1, :-2] + y[1:-1, 2:] - 4*y[1:-1, 1:-1])
    hist, _ = np.histogram(y, bins=32, range=(0, 1), density=False)
    prob = hist / max(1, hist.sum())
    entropy = -float(np.sum(prob[prob > 0] * np.log2(prob[prob > 0])))
    delta = float(np.mean(np.abs(y - prev_gray))) if prev_gray is not None else 0.0
    # A compact 32-bin luma histogram distance is stable and useful for cuts.
    if prev_rgb is None:
        histdist = 0.0
    else:
        pim = Image.fromarray(prev_rgb).resize((aw, ah), Image.Resampling.BILINEAR)
        parr = np.asarray(pim, dtype=np.float32) / 255.0
        py = 0.2126*parr[..., 0] + 0.7152*parr[..., 1] + 0.0722*parr[..., 2]
        ph, _ = np.histogram(py, bins=32, range=(0, 1), density=False)
        pprob = ph / max(1, ph.sum())
        histdist = float(0.5*np.sum((prob-pprob)**2/(prob+pprob+1e-8)))
    # Motion phase correlation uses a 160px-wide gray image.
    mw = min(160, width)
    mh = round(height * mw / width)
    gray_im = Image.fromarray(rgb).convert('L').resize((mw, mh), Image.Resampling.BILINEAR)
    gray = np.asarray(gray_im, dtype=np.float32)
    if prev_rgb is None:
        pdx = pdy = pcorr = 0.0
    else:
        pdx, pdy, pcorr = phase_shift(prev_motion, gray, width)
    vals = {
        'luma_mean': float(y.mean()), 'luma_p10': float(np.percentile(y, 10)),
        'luma_p50': float(np.percentile(y, 50)), 'luma_p90': float(np.percentile(y, 90)),
        'luma_std': float(y.std()), 'contrast_p90_p10': float(np.percentile(y, 90)-np.percentile(y, 10)),
        'saturation_mean': float(sat.mean()), 'saturation_p90': float(np.percentile(sat, 90)),
        'edge_density_gt_0_10': float((grad > .10).mean()), 'gradient_mean': float(grad.mean()),
        'laplacian_variance': float(lap.var()), 'luma_entropy_bits': entropy,
        'frame_delta_mean': delta, 'luma_histogram_chi2': histdist,
        'phase_image_dx_px': float(pdx), 'phase_image_dy_px': float(pdy),
        'phase_peak_ratio': float(pcorr),
    }
    return vals, y, gray


def contact_tile(rgb, frame_idx, t, tile_w=120, tile_h=213, label_h=18):
    im = Image.fromarray(rgb).resize((tile_w, tile_h), Image.Resampling.LANCZOS)
    tile = Image.new('RGB', (tile_w, tile_h + label_h), (15, 15, 15))
    tile.paste(im, (0, label_h))
    d = ImageDraw.Draw(tile)
    d.text((3, 2), f'{frame_idx:05d}  {t:06.2f}s', fill=(245, 245, 245))
    return tile


def save_sheet(tiles, outpath, start, end, cols=10):
    tw, th = tiles[0].size
    rows = math.ceil(len(tiles) / cols)
    sheet = Image.new('RGB', (cols*tw, rows*th), (30, 30, 30))
    for i, tile in enumerate(tiles):
        sheet.paste(tile, ((i % cols)*tw, (i // cols)*th))
    sheet.save(outpath, quality=86, optimize=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True, help='Folder of source MP4s')
    ap.add_argument('--out', required=True, help='Output analysis package directory')
    ap.add_argument('--fps', type=float, default=30.0)
    args = ap.parse_args()
    inp, out = Path(args.input), Path(args.out)
    (out/'data').mkdir(parents=True, exist_ok=True)
    (out/'references'/'sheets').mkdir(parents=True, exist_ok=True)
    (out/'references'/'keyframes').mkdir(parents=True, exist_ok=True)
    videos = sorted(inp.glob('*.mp4'))
    manifest = []
    all_rows = []
    summary = []
    for clip_no, path in enumerate(videos, 1):
        info = run_json(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)])
        vs = next(s for s in info['streams'] if s.get('codec_type') == 'video')
        width, height = int(vs['width']), int(vs['height'])
        duration = float(info['format']['duration'])
        stem = f'{clip_no:02d}_{path.stem}'
        safe = ''.join(c if c.isalnum() or c in '-_' else '_' for c in stem).strip('_')[:80]
        keydir = out/'references'/'keyframes'/safe
        keydir.mkdir(parents=True, exist_ok=True)
        cmd = ['ffmpeg','-hide_banner','-loglevel','error','-i',str(path),'-vf',f'fps={args.fps}','-f','rawvideo','-pix_fmt','rgb24','pipe:1']
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        bytes_per = width*height*3
        rows=[]; tiles=[]; prev=None; prev_y=None; prev_gray_motion=None; frame_idx=0; sheet_no=0
        while True:
            raw = proc.stdout.read(bytes_per)
            if len(raw) != bytes_per:
                break
            rgb = np.frombuffer(raw, dtype=np.uint8).reshape((height,width,3)).copy()
            metrics, gray_for_delta, gray_motion = frame_metrics(rgb, prev, prev_y, prev_gray_motion, width, height)
            t = frame_idx/args.fps
            row = {'clip_id': safe, 'source_file': path.name, 'frame': frame_idx, 'time_s': t, **metrics}
            rows.append(row)
            tiles.append(contact_tile(rgb,frame_idx,t))
            if frame_idx % int(args.fps) == 0:
                Image.fromarray(rgb).save(keydir/f'f{frame_idx:05d}_t{t:06.2f}s.jpg',quality=90,optimize=True)
            prev=rgb; prev_y=gray_for_delta; prev_gray_motion=gray_motion
            frame_idx+=1
            if len(tiles)==60:
                start=(frame_idx-60)/args.fps; end=frame_idx/args.fps
                name=f'{safe}_{start:06.2f}-{end:06.2f}s.jpg'
                save_sheet(tiles,out/'references'/'sheets'/name,start,end)
                tiles=[]; sheet_no+=1
        if tiles:
            start=(frame_idx-len(tiles))/args.fps; end=frame_idx/args.fps
            name=f'{safe}_{start:06.2f}-{end:06.2f}s.jpg'
            save_sheet(tiles,out/'references'/'sheets'/name,start,end)
        stderr=proc.stderr.read().decode('utf-8','replace')
        rc=proc.wait()
        if rc:
            raise RuntimeError(f'ffmpeg failed for {path}: {stderr}')
        all_rows.extend(rows)
        manifest.append({
            'clip_id':safe,'source_file':path.name,'duration_s':duration,'source_width':width,
            'source_height':height,'source_fps':vs.get('avg_frame_rate'),'analysis_fps':args.fps,
            'decoded_frames':frame_idx,'contact_sheets':sheet_no+(1 if tiles else 0),
            'has_audio':any(s.get('codec_type')=='audio' for s in info['streams']),
        })
        summary.append({'clip_id':safe,'duration_s':duration,'decoded_frames':frame_idx,'rows':rows})
        print(f'{path.name}: {frame_idx} frames at {args.fps:g} fps')
    if all_rows:
        fields=list(all_rows[0].keys())
        with (out/'data'/'frame_metrics_30fps.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(all_rows)
    with (out/'data'/'manifest.json').open('w',encoding='utf-8') as f:
        json.dump({'analysis_fps':args.fps,'clips':manifest},f,indent=2,ensure_ascii=False)
    # Per-clip cuts and frame statistics. Thresholds are stored as candidate flags for review.
    with (out/'data'/'candidate_events.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['clip_id','frame','time_s','event','value','threshold_note'])
        for r in all_rows:
            if r['luma_histogram_chi2'] >= 0.35:
                w.writerow([r['clip_id'],r['frame'],f"{r['time_s']:.3f}",'candidate_cut',f"{r['luma_histogram_chi2']:.5f}",'luma histogram chi2 >= 0.35; visual review required'])
            if r['frame_delta_mean'] <= 0.0008 and r['frame'] > 0:
                w.writerow([r['clip_id'],r['frame'],f"{r['time_s']:.3f}",'candidate_freeze_or_duplicate',f"{r['frame_delta_mean']:.6f}",'mean luma delta <= 0.0008; check intentional holds'])
    aggregate={}
    for clip in summary:
        rr=clip['rows']
        keys=['luma_mean','luma_p10','luma_p50','luma_p90','luma_std','contrast_p90_p10','saturation_mean','saturation_p90','edge_density_gt_0_10','gradient_mean','laplacian_variance','luma_entropy_bits','frame_delta_mean','luma_histogram_chi2','phase_image_dx_px','phase_image_dy_px']
        aggregate[clip['clip_id']]={
            'duration_s':clip['duration_s'],'decoded_frames':clip['decoded_frames'],
            'metrics':{k:{'mean':float(np.mean([x[k] for x in rr])),'p10':float(np.percentile([x[k] for x in rr],10)),'p50':float(np.percentile([x[k] for x in rr],50)),'p90':float(np.percentile([x[k] for x in rr],90))} for k in keys},
            'candidate_cuts':[{'frame':x['frame'],'time_s':x['time_s'],'hist_chi2':x['luma_histogram_chi2']} for x in rr if x['luma_histogram_chi2']>=0.35]
        }
    with (out/'data'/'summary_metrics.json').open('w',encoding='utf-8') as f:
        json.dump(aggregate,f,indent=2,ensure_ascii=False)
    print(f'Total frames: {len(all_rows)}; contact sheets: {len(list((out/"references"/"sheets").glob("*.jpg")))}')


if __name__ == '__main__':
    main()
