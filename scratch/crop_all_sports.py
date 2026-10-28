import os
from PIL import Image

src_path = r"C:\Users\DELL\.gemini\antigravity-ide\brain\1906a33f-ce04-41d4-bda8-135216b5a335\.user_uploaded\media_1793165621085.png"
out_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa\images\sports"
os.makedirs(out_dir, exist_ok=True)

img = Image.open(src_path).convert('RGB')

# 1. Hero Image
hero = img.crop((26, 56, 252, 225))
hero.save(os.path.join(out_dir, "vaibhav-hero.jpg"), quality=95)
print("Hero:", hero.size)

# Col 2 Thumbnails (x: 273 to 341, width 68)
c2_r1 = img.crop((273, 56, 341, 108))
c2_r1.save(os.path.join(out_dir, "ex-india-opener.jpg"), quality=95)
print("Col2 R1:", c2_r1.size)

c2_r2 = img.crop((273, 125, 341, 177))
c2_r2.save(os.path.join(out_dir, "abhishek-sharma.jpg"), quality=95)
print("Col2 R2:", c2_r2.size)

c2_r3 = img.crop((273, 194, 341, 246))
c2_r3.save(os.path.join(out_dir, "carrick-man-utd.jpg"), quality=95)
print("Col2 R3:", c2_r3.size)

# Col 3 Thumbnails (x: 519 to 587, width 68)
c3_r1 = img.crop((519, 56, 587, 108))
c3_r1.save(os.path.join(out_dir, "nz-captain-reaction.jpg"), quality=95)
print("Col3 R1:", c3_r1.size)

c3_r2 = img.crop((519, 125, 587, 177))
c3_r2.save(os.path.join(out_dir, "badoni-century.jpg"), quality=95)
print("Col3 R2:", c3_r2.size)

c3_r3 = img.crop((519, 194, 587, 246))
c3_r3.save(os.path.join(out_dir, "mbappe-apology.jpg"), quality=95)
print("Col3 R3:", c3_r3.size)
