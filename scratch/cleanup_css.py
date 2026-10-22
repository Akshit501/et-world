import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLES_FILE = os.path.join(WORKSPACE_DIR, "styles.css")
REFINE_FILE = os.path.join(WORKSPACE_DIR, "refine_styles.py")

with open(REFINE_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Fix duplicate/overriding ticker-tag rule
text = re.sub(
    r'\.ticker-tag\s*\{\s*display:\s*inline-flex;\s*align-items:\s*center;\s*gap:\s*5px;\s*background:\s*#000000;[^}]*\}',
    r'''.ticker-tag {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: var(--ac);
  color: #ffffff;
  font-size: 9.5px;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 2px;
  letter-spacing: 0.05em;
  flex-shrink: 0;
  box-shadow: 0 1px 3px rgba(237, 25, 59, 0.35);
}''',
    text
)

# Fix duplicate .ch-link rules
text = re.sub(
    r'\.ch-link\s*\{\s*font-weight:\s*700;\s*color:\s*#555c68;[^}]*\}',
    r'''.ch-link {
  font-weight: 700;
  color: #d1d5db;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  font-size: 10.5px;
  transition: color 0.15s ease;
}''',
    text
)

text = re.sub(
    r'\.ch-link:hover\s*\{\s*color:\s*#0c233c;\s*\}',
    r'.ch-link:hover { color: #ffffff; }',
    text
)

text = re.sub(
    r'\.ch-link\.on\s*\{\s*color:\s*#0c233c;\s*font-weight:\s*800;\s*position:\s*relative;\s*\}',
    r'.ch-link.on { color: #ffffff; font-weight: 800; position: relative; }',
    text
)

with open(REFINE_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaned up refine_styles.py")
