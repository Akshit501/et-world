ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

for name, off in [('India Global', 703370), ('Study Abroad', 709123), ('Science & Knowledge', 698313)]:
    print(f"\n==================== {name} ====================")
    chunk = text[off:off+4000]
    # Print the raw text excluding SVG/styles
    clean = re.sub(r'<style.*?</style>', '', chunk, flags=re.DOTALL)
    # Print lines that look like titles or images
    for line in clean.splitlines():
        line = line.strip()
        if any(tag in line for tag in ['<h2', '<h3', '<h4', '<img', 'crd_ttl', 'item-title', 'crd_lnk']):
            print(line[:160])
