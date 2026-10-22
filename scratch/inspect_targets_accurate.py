ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

target_sections = ['Science & Knowledge', 'India Global', 'Study Abroad', 'Climate & Environment', 'Lifestyle', 'Movies & Entertainment', 'Gadgets & Technology']

for sec in target_sections:
    # Find exact string '>sec<' or with spaces
    matches = [m.start() for m in re.finditer(re.escape(sec), text)]
    print(f"\n====================\n{sec} (matches: {len(matches)})\n====================")
    for idx in matches:
        # Check context
        ctx = text[max(0, idx-80):min(len(text), idx+120)].replace('\n', ' ')
        if 'tp-ttl' in ctx or 'vjl-md' in text[idx:idx+300] or 'crd' in text[idx:idx+300]:
            print(f"  FOUND HEADING at {idx}!")
            # Print next 1500 chars
            chunk = text[idx:idx+2500]
            # Find articles in chunk
            art_titles = re.findall(r'<a[^>]+>([^<]{15,120})</a>', chunk)
            for a in art_titles[:6]:
                print(f"    - {a.strip()}")
            break
