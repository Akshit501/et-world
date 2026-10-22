ref_path = r'C:\Users\DELL\.gemini\antigravity-ide\brain\a1b80c01-ca7c-4921-8917-8a4a4e9e475a\.system_generated\steps\287\content.md'
with open(ref_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

search_titles = [
    "Elon Musk's Public Endorsement",
    "US Top Court Refuses",
    "Arizona University Fraternity",
    "Ohio State University",
    "Why British Agency MI5",
    "British Bodybuilder Dies",
    "UK Bank Operations",
    "Protest vs Counter-Protest In UK",
    "Indian Among 2 Killed In Attack On Saudi",
    "War, Security And Economy: Factors",
    "How Turkey, Pak And Saudi",
    "1 Killed, 8 Injured In Attack On Saudi",
    "Africa50's Principal Investment",
    "Dawood Lives In Pak",
    "Trump's Son Warned Him Against Dragging",
    "It's A Gamble",
    "I Am A Muslim",
    "Manoj Bajpayee On Tiger Shroff",
    "Daler Mehndi Doesn't Drink",
    "Vivo Y600 With",
    "Apple's iPhone Duo Hands-On",
    "Oppo Reno 16 Price",
    "iQOO 16R Spotted",
    "World On Track For 2.6 Degrees",
    "Climate Change Strips Island",
    "El Nino Will Intensify",
    "One Third Of World Population",
    "Decoding Rashmika Mandanna",
    "What Rashmika Mandanna",
    "Sai Pallavi Flaunts",
    "Internet Debates As Hasan Minhaj",
    "Planetary Parade",
    "NASA Shares Photo Of Dazzling",
    "Scientists Uncover Vast Web",
    "Korean Scientists Develop Light"
]

results = {}
for st in search_titles:
    m = re.search(re.escape(st), text, re.IGNORECASE)
    if m:
        idx = m.start()
        # Look backwards for image
        before = text[max(0, idx-500):idx]
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', before)
        img = imgs[-1] if imgs else ''
        if not img:
            after = text[idx:idx+400]
            imgs2 = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', after)
            img = imgs2[0] if imgs2 else ''
        results[st] = img
        print(f"FOUND: {st[:35]}... -> {img[:80]}")
    else:
        print(f"NOT FOUND: {st}")
