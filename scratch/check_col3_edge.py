import os
from PIL import Image

src_path = r"C:\Users\DELL\.gemini\antigravity-ide\brain\1906a33f-ce04-41d4-bda8-135216b5a335\.user_uploaded\media_1793165621085.png"
out_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa\images\sports"

img = Image.open(src_path).convert('RGB')

for x in range(575, 605):
    col_pixels = [img.getpixel((x, y)) for y in range(60, 110)]
    dark_count = sum(1 for p in col_pixels if abs(p[0]-30) < 10 and abs(p[1]-31) < 10 and abs(p[2]-31) < 10)
    print(f"Col3 x={x}, dark ratio: {dark_count/len(col_pixels):.2f}")
