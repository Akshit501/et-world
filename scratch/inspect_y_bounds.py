import os
from PIL import Image

src_path = r"C:\Users\DELL\.gemini\antigravity-ide\brain\1906a33f-ce04-41d4-bda8-135216b5a335\.user_uploaded\media_1793165621085.png"
out_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa\images\sports"

img = Image.open(src_path).convert('RGB')

# Let's inspect Col 2 Row 1 (y around 50 to 120, x=300)
def find_y_bounds(x, y_start, y_end):
    in_img = False
    y_top = None
    y_bot = None
    for y in range(y_start, y_end):
        p = img.getpixel((x, y))
        is_bg = abs(p[0]-30) < 10 and abs(p[1]-31) < 10 and abs(p[2]-31) < 10
        if not is_bg and not in_img:
            in_img = True
            y_top = y
        elif is_bg and in_img:
            in_img = False
            y_bot = y
    return y_top, y_bot

print("Col 2 Row 1 y:", find_y_bounds(300, 50, 120))
print("Col 2 Row 2 y:", find_y_bounds(300, 115, 185))
print("Col 2 Row 3 y:", find_y_bounds(300, 180, 255))

print("Col 3 Row 1 y:", find_y_bounds(540, 50, 120))
print("Col 3 Row 2 y:", find_y_bounds(540, 115, 185))
print("Col 3 Row 3 y:", find_y_bounds(540, 180, 255))
