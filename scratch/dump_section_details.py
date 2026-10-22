ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

offsets = {
    'Science & Knowledge': 698313,
    'India Global': 703370,
    'Study Abroad': 709123,
    'Climate & Environment': 715270,
    'Lifestyle': 720885,
    'Movies & Entertainment': 750421,
    'Gadgets & Technology': 756894
}

for name, off in offsets.items():
    print(f"\n################################################")
    print(f"### {name}")
    print(f"################################################")
    chunk = text[off:off+5500]
    # Let's extract items:
    # Each item usually has an img src and a title text
    # In NDTV/ET world, featured card has .crd-h or .crd_ttl5 or .crd_img, list has .ls-ns or .crd-c
    # Let's find all (img, title) pairs
    # Pattern 1: <img ... src="..."> ... <a ...>Title</a>
    cards = re.findall(r'<div[^>]*class=["\']([^"\']*(?:crd|vjl-md|ls-ns_li)[^"\']*)["\'][^>]*>(.*?)</div>\s*(?:</div>|\s*<li|\s*<div)', chunk, re.DOTALL)
    print(f"Total card chunks found: {len(cards)}")
    
    # Simple regex search for img and title within each 500 chars
    img_matches = list(re.finditer(r'<img[^>]+src=["\']([^"\']+)["\'](?:[^>]*alt=["\']([^"\']*)["\'])?', chunk))
    for m in img_matches:
        img_url = m.group(1)
        alt = m.group(2) or ''
        # Look forward for title
        post = chunk[m.end():m.end()+600]
        title_m = re.search(r'<(?:div|h3|h4|span|a)[^>]*class=["\'][^"\']*(?:ttl|title|lnk)[^"\']*["\'][^>]*>(?:<a[^>]*>)?([^<]+)', post)
        if title_m:
            title = title_m.group(1).strip()
            print(f"- Title: {title}")
            print(f"  Img: {img_url}")
        elif alt and len(alt) > 10:
            print(f"- Alt Title: {alt}")
            print(f"  Img: {img_url}")
