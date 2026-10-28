import os
from PIL import Image

src_path = r"C:\Users\DELL\.gemini\antigravity-ide\brain\1906a33f-ce04-41d4-bda8-135216b5a335\.user_uploaded\media_1793165621085.png"
out_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa\images\sports"

img = Image.open(src_path).convert('RGB')

# Let's inspect rows 220 to 240 of hero image at x=100 (which is in the grass):
for y in range(215, 235):
    p = img.getpixel((100, y))
    print(f"y={y}: RGB={p}")

