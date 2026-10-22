import re

ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find each H2 section
pos_h2 = []
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', text, re.DOTALL):
    title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    if title:
        pos_h2.append((m.start(), m.end(), title))

print(f"Found {len(pos_h2)} H2s")
for i in range(len(pos_h2)):
    start, end, title = pos_h2[i]
    next_start = pos_h2[i+1][0] if i+1 < len(pos_h2) else start + 10000
    section_html = text[end:next_start]
    
    # Extract images and titles inside section_html
    # Look for links with titles or images
    items = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>.*?<(?:div|h3|h4|span|a)[^>]*class=["\'][^"\']*(?:ttl|title|lnk)[^"\']*["\'][^>]*>(?:<a[^>]*>)?([^<]+)', section_html, re.DOTALL)
    if not items:
        # try another regex
        items = re.findall(r'<(?:div|h3|h4|span|a)[^>]*class=["\'][^"\']*(?:ttl|title|lnk)[^"\']*["\'][^>]*>(?:<a[^>]*>)?([^<]+)', section_html, re.DOTALL)
        items = [('', it) for it in items]
    
    print(f"\n============================\nSECTION: {title}\n============================")
    for img, it_title in items[:6]:
        it_clean = it_title.strip()
        if it_clean and len(it_clean) > 5 and it_clean != title:
            print(f"  • {it_clean}")
            if img:
                print(f"    img: {img[:90]}")
