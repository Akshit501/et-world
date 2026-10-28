import os
from PIL import Image

src_path = r"C:\Users\DELL\.gemini\antigravity-ide\brain\1906a33f-ce04-41d4-bda8-135216b5a335\.user_uploaded\media_1793165621085.png"
out_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa\images\sports"
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path)
print("Image dimensions:", img.size)

# We can find coordinates. Let's inspect by printing slices or saving draft crops.
# Let's see the total width and height first.
