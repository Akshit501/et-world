import os
from PIL import Image

src_path = r"C:\Users\DELL\.gemini\antigravity-ide\brain\1906a33f-ce04-41d4-bda8-135216b5a335\.user_uploaded\media_1793165621085.png"
out_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa\images\sports"
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path).convert('RGB')

# Let's inspect Col 2 Row 1 thumbnail width precisely
# In news thumbnails, aspect ratio is usually 4:3 or 16:9 or around 70-80px wide by 50-60px high.
# Let's crop a slightly wider region and check where the image ends and text begins.
# Let's save slices to see:
c2_r1 = img.crop((273, 56, 347, 116))
c2_r1.save(os.path.join(out_dir, "thumb_test.png"))

# Let's check the right edge of thumbnails in Col 2:
for x in range(330, 365):
    # check column x between y=60 and 110
    col_pixels = [img.getpixel((x, y)) for y in range(60, 110)]
    # count how many are dark background (around 30,31,31)
    dark_count = sum(1 for p in col_pixels if abs(p[0]-30) < 10 and abs(p[1]-31) < 10 and abs(p[2]-31) < 10)
    print(f"x={x}, dark ratio: {dark_count/len(col_pixels):.2f}")

