import re

with open('index.html', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<([a-z0-9]+)[^>]*class=[\'"]([^\'"]*(?:section|row|hub|banner|portal|grid|box|bar|hd|ft)[^\'"]*)[\'"]', text)
for tag, c in matches[:35]:
    print(f"<{tag} class='{c}'>")
