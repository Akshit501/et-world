import urllib.request
import re

url = "https://economictimes.indiatimes.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    # Find masthead / logo HTML
    print("Searching for masthead HTML...")
    matches = re.findall(r'(<[^>]+(?:logo|masthead|ePaper|Watchlist|Subscribe|Festive)[^>]*>.*?</[^>]+>)', html, re.IGNORECASE)
    print("Found matches:", len(matches))
    for m in matches[:15]:
        print("MATCH:", m[:150])
        
    # Search for "The Economic Times" logo image or text
    logo_img = re.findall(r'<img[^>]+(?:economictimes|etlogo|logo)[^>]+>', html, re.IGNORECASE)
    print("\nLogo images found:", len(logo_img))
    for img in logo_img[:5]:
        print("LOGO IMG:", img)
        
    # Check "English Edition"
    editions = re.findall(r'([^<]*English Edition[^<]*)', html, re.IGNORECASE)
    print("\nEdition texts:", editions[:5])
    
except Exception as e:
    print(f"Error: {e}")
