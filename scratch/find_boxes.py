import os
from PIL import Image

src_path = r"C:\Users\DELL\.gemini\antigravity-ide\brain\1906a33f-ce04-41d4-bda8-135216b5a335\.user_uploaded\media_1793165621085.png"
out_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa\images\sports"

img = Image.open(src_path).convert('RGB')
W, H = img.size

# Let's find horizontal spans where colors are vivid or brightness > 40
# We know:
# Hero image is in x in [20, 260], y in [50, 240]
# Stack 1 thumbnails are in x in [260, 360]
# Stack 2 thumbnails are in x in [500, 600]

# Let's write a small edge/bounding finder:
def get_bbox(region_box):
    x0, y0, x1, y1 = region_box
    # Find bounding box inside this region where brightness > threshold
    # Background is roughly RGB (30, 27, 27) or (34, 34, 34)
    bg = img.getpixel((10, 10))
    print("Background color:", bg)
    
    # scan for non-bg pixels
    min_x, min_y, max_x, max_y = x1, y1, x0, y0
    for y in range(y0, y1):
        for x in range(x0, x1):
            p = img.getpixel((x, y))
            # if difference from bg is noticeable
            diff = abs(p[0]-bg[0]) + abs(p[1]-bg[1]) + abs(p[2]-bg[2])
            if diff > 35:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    return min_x, min_y, max_x, max_y

print("Hero box:", get_bbox((20, 50, 260, 240)))
print("Col 2 Row 1:", get_bbox((260, 50, 360, 120)))
print("Col 2 Row 2:", get_bbox((260, 120, 360, 185)))
print("Col 2 Row 3:", get_bbox((260, 185, 360, 255)))

print("Col 3 Row 1:", get_bbox((500, 50, 600, 120)))
print("Col 3 Row 2:", get_bbox((500, 120, 600, 185)))
print("Col 3 Row 3:", get_bbox((500, 185, 600, 255)))
