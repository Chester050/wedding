"""Resize Media/ originals into web-ready srcset assets under Media/web/.

Originals are untouched. Output names are ASCII and ordered per theme.
Run: python optimize-media.py
"""
import json
import os
from PIL import Image, ImageOps

SRC = "Media"
OUT = os.path.join("Media", "web")
WIDTHS = [800, 1200, 1600]
JPEG_QUALITY = 80
WEBP_QUALITY = 82

# folder name -> (slug, ordering of source files)
THEMES = {
    "Casual": "casual",
    "Bank Street": "bank-street",
    "Beach": "beach",
    "Chapel": "chapel",
    "Story": "story",
}

manifest = {}

for folder, slug in THEMES.items():
    src_dir = os.path.join(SRC, folder)
    out_dir = os.path.join(OUT, slug)
    os.makedirs(out_dir, exist_ok=True)

    files = sorted(f for f in os.listdir(src_dir) if f.lower().endswith((".jpg", ".jpeg", ".png")))
    entries = []

    for i, name in enumerate(files, start=1):
        base = f"{slug}-{i:02d}"
        im = ImageOps.exif_transpose(Image.open(os.path.join(src_dir, name))).convert("RGB")
        w, h = im.size

        sources = []
        for target in WIDTHS:
            if target > w:
                continue
            scaled = im.resize((target, round(h * target / w)), Image.LANCZOS)
            jpg = os.path.join(out_dir, f"{base}-{target}.jpg")
            webp = os.path.join(out_dir, f"{base}-{target}.webp")
            scaled.save(jpg, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
            scaled.save(webp, "WEBP", quality=WEBP_QUALITY, method=6)
            sources.append(target)
            print(f"{base}-{target}  {target}x{round(h * target / w)}")

        entries.append({
            "base": base,
            "dir": f"{OUT}/{slug}".replace("\\", "/"),
            "widths": sources,
            "aspect": round(w / h, 4),
            "orientation": "portrait" if h > w else "landscape",
            "original": name,
        })

    manifest[slug] = entries

with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

total = sum(
    os.path.getsize(os.path.join(dp, f))
    for dp, _, fs in os.walk(OUT)
    for f in fs
)
print(f"\nDone. {OUT} = {total / 1_048_576:.1f} MB")
