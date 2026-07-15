from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "images" / "social-preview.png"
FONT_DIR = Path("C:/Windows/Fonts")


def font(name: str, size: int):
    return ImageFont.truetype(str(FONT_DIR / name), size)


canvas = Image.new("RGB", (1200, 630), "#f7fafc")
draw = ImageDraw.Draw(canvas)

draw.rectangle((0, 0, 1200, 18), fill="#1769aa")
draw.rounded_rectangle((72, 64, 1128, 566), radius=22, fill="#ffffff", outline="#d6e4ef", width=2)
draw.rounded_rectangle((104, 100, 248, 146), radius=8, fill="#e9f3fa")
draw.text((128, 109), "CHONGGROK", font=font("arialbd.ttf", 20), fill="#1769aa")

draw.text((104, 190), "Gemini / Google AI", font=font("arialbd.ttf", 58), fill="#12202f")
draw.text((104, 274), "国内订阅与排障指南", font=font("msyhbd.ttc", 50), fill="#12202f")
draw.text((104, 360), "自有账号 · 付款失败 · 权益未生效 · Google Play", font=font("msyh.ttc", 27), fill="#43566a")

for i, label in enumerate(("套餐选择", "账号对应", "付款验收", "安全边界")):
    x = 104 + i * 236
    draw.rounded_rectangle((x, 432, x + 204, 486), radius=8, fill="#edf5fb")
    draw.text((x + 28, 445), label, font=font("msyhbd.ttc", 22), fill="#1769aa")

draw.text((104, 522), "he20000405-pixel.github.io", font=font("arial.ttf", 21), fill="#66798c")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
canvas.save(OUTPUT, optimize=True)
print(OUTPUT)
