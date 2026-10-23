with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    '1. Watch live banner removed': 'summitLiveBanner' not in html and 'summit-watch-live-banner' not in html,
    '2. ET World header on top (before masthead)': html.find('id="mainHeader"') < html.find('id="etOfficialMasthead"'),
    '3. ET World Summit 2026 section removed': 'id="summit"' not in html and 'summit-hub-section' not in html,
    '4. Panache section replaces Offbeat': 'id="panache"' in html and 'id="offbeat"' not in html,
    '5. Shorts section removed': 'id="shorts-section"' not in html and 'shorts-reel-track' not in html,
    '6. Podcasts present in Videos': 'id="podcasts-hub"' in html and 'The Morning Brief' in html,
    '7. Science & Knowledge present': 'id="science-knowledge"' in html,
    '8. India Global & Study Abroad present': 'id="india-global"' in html and 'id="study-abroad"' in html,
    '9. Climate & Lifestyle present': 'id="climate-environment"' in html and 'id="lifestyle"' in html,
    '10. Regional Quad cards present': 'id="us"' in html and 'id="uk"' in html and 'id="middle-east"' in html and 'id="asia"' in html,
    '11. Movies & Gadgets present': 'id="movies-entertainment"' in html and 'id="gadgets-tech"' in html,
    '12. Sports section present': 'id="sports-section"' in html
}

all_passed = True
for k, v in checks.items():
    print(f'{k}: {"PASS" if v else "FAIL"}')
    if not v:
        all_passed = False

print("\nALL VERIFICATIONS PASSED:", all_passed)
