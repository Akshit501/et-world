with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'class="([^"]+)"', html)
all_html_classes = set()
for m in matches:
    for c in m.split():
        all_html_classes.add(c)

missing = []
for c in sorted(all_html_classes):
    # Check if .class or [class... is in css
    if f'.{c}' not in css:
        missing.append(c)

print(f"Total HTML classes: {len(all_html_classes)}")
print(f"Classes missing in styles.css: {len(missing)}")
for c in missing:
    print(f"  - {c}")
