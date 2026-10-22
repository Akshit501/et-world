import urllib.request
import re

css_url = "https://js.etimg.com/etnextweball/_next/static/css/3fb9e97e860ec34a.css"
req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        css = resp.read().decode('utf-8', errors='ignore')
    
    print(f"Downloaded CSS size: {len(css)} bytes")
    
    # Extract background colors
    bgs = re.findall(r'background(?:-color)?\s*:\s*(#[0-9a-fA-F]{3,6}|rgba?\([^)]+\))', css, re.IGNORECASE)
    from collections import Counter
    bg_counts = Counter(bgs).most_common(20)
    print("\nTop Background Colors on ET:")
    for color, count in bg_counts:
        print(f"  {color}: {count} occurrences")
        
    # Extract colors
    cols = re.findall(r'(?<!background-)color\s*:\s*(#[0-9a-fA-F]{3,6}|rgba?\([^)]+\))', css, re.IGNORECASE)
    col_counts = Counter(cols).most_common(20)
    print("\nTop Text/Element Colors on ET:")
    for color, count in col_counts:
        print(f"  {color}: {count} occurrences")
        
    # Search for header, nav, ticker, section styles
    sections = re.findall(r'(\.[a-zA-Z0-9_-]+(?:header|nav|ticker|section|container|card|strip)[^{]*\{[^}]*\})', css, re.IGNORECASE)
    print(f"\nFound {len(sections)} relevant class rules. First 8:")
    for s in sections[:8]:
        print("---", s[:150])

except Exception as e:
    print(f"Error: {e}")
