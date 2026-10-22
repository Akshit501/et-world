with open(r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\361\content.md', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
import json

# Check for __NEXT_DATA__
next_data_match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', text, re.DOTALL)
if next_data_match:
    print("Found __NEXT_DATA__! Parsing JSON...")
    data = json.loads(next_data_match.group(1))
    props = data.get("props", {}).get("pageProps", {})
    print("Keys in pageProps:", list(props.keys()))
    
    # Check for header or sections
    for k in props:
        val = props[k]
        if isinstance(val, dict):
            print(f"Key {k} (dict):", list(val.keys()))
        elif isinstance(val, list):
            print(f"Key {k} (list len {len(val)}):", [str(type(x)) for x in val[:3]])
else:
    print("No __NEXT_DATA__ found. Looking for other JSON...")
