import re

ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for match in re.finditer(r'<h2[^>]*>.*?Science & Knowledge.*?</h2>', text, re.DOTALL):
    idx = match.start()
    print("Found H2 at", idx)
    print(text[idx-200:idx+2500])
