ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

for name, off in [('India Global', 703370), ('Study Abroad', 709123)]:
    print(f"\n==================== {name} ====================")
    chunk = text[off:off+4000]
    links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', chunk, re.DOTALL)
    for href, inner in links:
        t = re.sub(r'<[^>]+>', '', inner).strip()
        if len(t) > 15 and name not in t:
            print("TITLE:", t)
            print("URL:", href)
