import re

ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

target_sections = ['Science & Knowledge', 'India Global', 'Study Abroad', 'Climate & Environment', 'Lifestyle', 'Movies & Entertainment', 'Gadgets & Technology']

for sec in target_sections:
    m = re.search(r'<h2[^>]*>.*?' + re.escape(sec) + r'.*?</h2>', text, re.DOTALL | re.IGNORECASE)
    if not m:
        print(f"NOT FOUND: {sec}")
        continue
    start = m.start()
    sub = text[start:start+4000]
    print(f"\n====================\n{sec}\n====================")
    # find all img and title
    # let's look for href and title
    cards = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', sub, re.DOTALL)
    for href, inner in cards:
        t = re.sub(r'<[^>]+>', '', inner).strip()
        imgs = re.findall(r'src=["\']([^"\']+)["\']', inner)
        if len(t) > 10 and sec not in t:
            print(f"Title: {t}")
            if imgs:
                print(f"  Img: {imgs[0]}")
