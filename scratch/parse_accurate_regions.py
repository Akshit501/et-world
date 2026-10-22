ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

def parse_region(name, start_idx):
    chunk = text[start_idx:start_idx+6500]
    print(f"\n============================\nSECTION: {name} (at {start_idx})\n============================")
    # 1. Featured card (if present)
    # Usually in <div class="crd-h ...">
    feat_m = re.search(r'class=["\'][^"\']*crd-h[^"\']*["\'].*?<img[^>]+src=["\']([^"\']+)["\'].*?<h3[^>]*>.*?<a[^>]*>(.*?)</a>', chunk, re.DOTALL)
    if feat_m:
        f_img = feat_m.group(1)
        f_title = re.sub(r'<[^>]+>', '', feat_m.group(2)).strip()
        print(f"FEATURED: {f_title}")
        print(f"  Img: {f_img}")
    
    # 2. List items
    # In <li class="ls-ns_li" or <li class="LstWg1-li" or <div class="vjl-md-3"
    list_items = re.findall(r'<li[^>]*class=["\'][^"\']*(?:ls-ns_li|LstWg1-li)[^"\']*["\'].*?<img[^>]+src=["\']([^"\']+)["\'].*?<(?:h3|h4|div)[^>]*class=["\'][^"\']*crd_ttl[^"\']*["\'].*?<a[^>]*>(.*?)</a>', chunk, re.DOTALL)
    for img, title in list_items:
        t_clean = re.sub(r'<[^>]+>', '', title).strip()
        print(f"LIST: {t_clean}")
        print(f"  Img: {img}")

    # If vjl-md-3 cards (like Science & Knowledge)
    sk_cards = re.findall(r'<div[^>]*class=["\'][^"\']*vjl-md-3[^"\']*["\'].*?<img[^>]+src=["\']([^"\']+)["\'].*?class=["\'][^"\']*item-title[^"\']*["\'][^>]*>(.*?)</a>', chunk, re.DOTALL)
    for img, title in sk_cards:
        t_clean = re.sub(r'<[^>]+>', '', title).strip()
        print(f"GRID4: {t_clean}")
        print(f"  Img: {img}")

offsets = [
    ('Science & Knowledge', 698313),
    ('India Global', 703370),
    ('Study Abroad', 709123),
    ('Climate & Environment', 715270),
    ('Lifestyle', 720885),
    ('United States', 726880),
    ('United Kingdom', 732800),
    ('Middle East', 738700),
    ('Asia', 744600),
    ('Movies & Entertainment', 750421),
    ('Gadgets & Technology', 756894)
]

for name, off in offsets:
    # Find exact H2 near off
    h2_pos = text.find(name, off - 500)
    if h2_pos != -1:
        parse_region(name, h2_pos)
    else:
        parse_region(name, off)
