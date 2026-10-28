import os
from PIL import Image

src_path = r"images\sports\widget_reference.png"
out_dir = r"images\sports"

img = Image.open(src_path).convert('RGBA')

# Let's crop the circular icons:
# BAN flag icon:
# Looking at widget_reference, BAN is below "Day 1 Lunch"
# Let's crop a test region around BAN
ban_crop = img.crop((10, 47, 27, 64))
ban_crop.save(os.path.join(out_dir, "flag_ban.png"))

wi_crop = img.crop((10, 69, 27, 86))
wi_crop.save(os.path.join(out_dir, "flag_wi.png"))

sa_crop = img.crop((10, 148, 27, 165))
sa_crop.save(os.path.join(out_dir, "flag_sa.png"))

aus_crop = img.crop((10, 170, 27, 187))
aus_crop.save(os.path.join(out_dir, "flag_aus.png"))

print("Flags saved")
