ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'html.parser')

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

for sec in sections:
    # Find h2 containing sec
    h2 = None
    for h in soup.find_all('h2'):
        if sec.lower() in h.get_text().lower():
            h2 = h
            break
    print(f"=== {sec.upper()} ===")
    if not h2:
        print("  Not found!")
        continue
    # Let's find parent or next siblings
    parent = h2.find_parent('div', class_='vjl-row') or h2.find_parent('section') or h2.find_parent('div')
    # Find images and titles in this block
    container = h2.find_parent('div', class_=lambda c: c and 'container' in c) or h2.parent.parent
    # let's find links with text
    articles = []
    # Find card containers
    for card in parent.find_all(class_=re.compile(r'crd|ls-ns|vjl-md')):
        t = card.find(class_=re.compile(r'ttl|title|lnk'))
        img = card.find('img')
        if t and t.get_text().strip():
            title_text = t.get_text().strip()
            img_src = img['src'] if img and img.has_attr('src') else ''
            if title_text not in [a[0] for a in articles] and title_text != sec:
                articles.append((title_text, img_src))
    for title_text, img_src in articles[:6]:
        print(f"  * {title_text}")
        if img_src:
            print(f"    img: {img_src[:80]}")
