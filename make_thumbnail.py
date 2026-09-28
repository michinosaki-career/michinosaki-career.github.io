#!/usr/bin/env python3
"""
ミチノサキ 記事サムネイル生成テンプレート（デザインシステム_2026-09-28.md 3節に対応）

記事ごとにCanvaで一からイラストを生成しない。共通の背景（assets/hero.jpg）を
使い回し、タイトルテキストとカテゴリータグだけを差し替える。

使い方:
    python3 make_thumbnail.py "記事タイトル" "カテゴリー名" 出力ファイル名.jpg

例:
    python3 make_thumbnail.py "評価されないと感じたら最初に確認したいこと" "仕事の悩み" columns/hyoka-sarenai.jpg
"""
import sys
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
BG_PATH = Path(__file__).parent / "assets" / "hero.jpg"

TEAL = (60, 122, 114)
CHARCOAL = (51, 51, 51)
SAGE_BG = (232, 240, 234)
MUTED = (107, 107, 107)


def make_thumbnail(title: str, category: str, out_path: str):
    img = Image.open(BG_PATH).convert("RGB")
    w, h = img.size
    draw = ImageDraw.Draw(img)

    # カテゴリータグ（左上）
    tag_font = ImageFont.truetype(FONT_PATH, 34)
    tag_padding_x, tag_padding_y = 24, 14
    tag_bbox = draw.textbbox((0, 0), category, font=tag_font)
    tag_w = tag_bbox[2] - tag_bbox[0] + tag_padding_x * 2
    tag_h = tag_bbox[3] - tag_bbox[1] + tag_padding_y * 2
    tag_x, tag_y = int(w * 0.045), int(h * 0.10)
    draw.rounded_rectangle(
        [tag_x, tag_y, tag_x + tag_w, tag_y + tag_h], radius=tag_h // 2, fill=SAGE_BG
    )
    draw.text((tag_x + tag_padding_x, tag_y + tag_padding_y - tag_bbox[1]), category, font=tag_font, fill=TEAL)

    # タイトル（左側の余白に折り返して配置）
    title_font = ImageFont.truetype(FONT_PATH, 78)
    max_chars_per_line = 11
    lines = textwrap.wrap(title, width=max_chars_per_line)
    line_height = 100
    title_y = tag_y + tag_h + 60
    for i, line in enumerate(lines[:4]):
        draw.text((tag_x, title_y + i * line_height), line, font=title_font, fill=CHARCOAL)

    # ブランドマーク（左下）
    brand_font = ImageFont.truetype(FONT_PATH, 32)
    brand_y = h - int(h * 0.12)
    draw.text((tag_x, brand_y), "ミチノサキ / MICHINOSAKI", font=brand_font, fill=MUTED)

    img.save(out_path, quality=90)
    print(f"saved: {out_path} ({w}x{h})")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    make_thumbnail(sys.argv[1], sys.argv[2], sys.argv[3])
