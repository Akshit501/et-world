ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

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
    'Gadgets & Technology',
    'Sports'
]

for sec in sections:
    m = re.search(r'<h2[^>]*>.*?' + re.escape(sec) + r'.*?</h2>', text, re.DOTALL | re.IGNORECASE)
    if m:
        start = m.start()
        # Find next section or next 2500 chars
        snippet = text[start:start+1800]
        # Extract headlines
        headlines = re.findall(r'<a[^>]+>(.*?)</a>', snippet)
        clean_heads = [re.sub(r'<[^>]+>', '', h).strip() for h in headlines if len(re.sub(r'<[^>]+>', '', h).strip()) > 15]
        print(f"=== {sec.upper()} ===")
        for h in clean_heads[:6]:
            print(f"  * {h}")
    else:
        print(f"=== {sec.upper()} (NOT FOUND AS H2) ===")
