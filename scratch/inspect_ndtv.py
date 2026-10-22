import re

with open(r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Look for .vjl-cntr or main card styling
css_blocks = re.findall(r'<style[^>]*>(.*?)</style>', text, re.DOTALL)
print(f"Found {len(css_blocks)} style blocks in NDTV World")

# Search for typography and card rules in all style blocks
full_css = "\n".join(css_blocks)

rules_to_find = [
    r'\.crd[^{]*\{[^}]*\}',
    r'\.ls-ns[^{]*\{[^}]*\}',
    r'\.tp-ttl[^{]*\{[^}]*\}',
    r'\.ndt-clb[^{]*\{[^}]*\}',
    r'\.Hrlst5[^{]*\{[^}]*\}',
    r'\.CrOpn[^{]*\{[^}]*\}'
]

for r in rules_to_find:
    matches = re.findall(r, full_css)
    print(f"Rule pattern {r} found {len(matches)} matches")
    for m in matches[:3]:
        print("  ", m[:120].strip())
