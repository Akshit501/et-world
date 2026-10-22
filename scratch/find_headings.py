import re

ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

titles = re.findall(r'<h2[^>]*>(.*?)</h2>', text, re.DOTALL)
clean_titles = [re.sub(r'<[^>]+>', '', t).strip() for t in titles]
for i, t in enumerate(clean_titles):
    print(f"{i+1}: {t}")
