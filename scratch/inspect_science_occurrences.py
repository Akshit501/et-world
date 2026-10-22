ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'Science &amp; Knowledge|Science & Knowledge', text)]
print("Total occurrences:", len(matches))
for i, idx in enumerate(matches):
    surr = text[max(0, idx-50):min(len(text), idx+100)].replace('\n', ' ')
    print(f"[{i}] {surr}")
