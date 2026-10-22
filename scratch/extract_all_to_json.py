ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
import json

def extract_section_items(h2_title):
    # Find h2
    pos = text.find(h2_title)
    if pos == -1:
        return []
    # Take next 5000 chars
    sub = text[pos:pos+6000]
    
    # In these cards, each item has an <li> or <div class="crd..."> containing an <img ... src="..."> and a title in <a ...>...</a>
    # Let's split by li or crd
    items = []
    # Check for featured item first
    feat_img = re.search(r'class=["\'][^"\']*(?:crd_img-full|crd_img)[^"\']*["\'][^>]*src=["\']([^"\']+)["\']', sub) or re.search(r'<img[^>]+src=["\']([^"\']+)["\']', sub)
    feat_title = re.search(r'class=["\'][^"\']*(?:crd_ttl5|crd_ttl|crd_lnk)[^"\']*["\'][^>]*>(?:<div[^>]*>)?(?:<a[^>]*>)?([^<]+)', sub)
    
    # Or let's find all pairs of img and link
    # Find all <li class="LstWg1-li" or <li class="ls-ns_li" or <div class="vjl-md-3"
    blocks = re.findall(r'(<(?:li|div)[^>]*class=["\'][^"\']*(?:LstWg1-li|ls-ns_li|vjl-md-3|crd-h)[^"\']*["\'].*?)(?=(?:<(?:li|div)[^>]*class=["\'][^"\']*(?:LstWg1-li|ls-ns_li|vjl-md-3|crd-h)|$))', sub, re.DOTALL)
    for b in blocks:
        img_m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', b)
        title_m = re.search(r'<(?:h3|h4|div|a)[^>]*class=["\'][^"\']*(?:crd_ttl|item-title|crd_lnk)[^"\']*["\'][^>]*>(?:<div[^>]*>)?(?:<a[^>]*>)?([^<]+)', b)
        if not title_m:
            title_m = re.search(r'<a[^>]+>([^<]{12,120})</a>', b)
        img_src = img_m.group(1) if img_m else ''
        title_text = title_m.group(1).strip() if title_m else ''
        if title_text and title_text != h2_title and title_text not in [it['title'] for it in items]:
            items.append({'title': title_text, 'image': img_src})
    return items

sections = [
    'Science & Knowledge',
    'India Global',
    'Study Abroad',
    'Climate & Environment',
    'Lifestyle',
    'United States',
    'United Kingdom',
    'Middle East',
    'Asia',
    'Movies & Entertainment',
    'Gadgets & Technology'
]

data = {}
for s in sections:
    data[s] = extract_section_items(s)
    print(f"=== {s} ({len(data[s])} items) ===")
    for it in data[s]:
        print(f"  - {it['title'][:60]} | {it['image'][:50]}")

with open(r'c:\Users\DELL\OneDrive\Desktop\et-usa\scratch\extracted_sections.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
