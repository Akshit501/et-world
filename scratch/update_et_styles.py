#!/usr/bin/env python3
"""
ET World - Economic Times Color & Background Styler
Applies authentic Economic Times palette and section backgrounds:
- Page Canvas: #f5f5f5 (ET newsprint light gray)
- Market Ticker: #fbf4e4 (ET cream paper) with #d8cbb7 border
- Channel Network Strip: #191919 with #d1d5db text & #f59e0b gold prime
- Summit Hub: #fff3f0 with #e4ccc4 border (Official ET peach highlight)
- Offbeat: #f8faf7 with #e1ebe1 border (Fresh subtle mint)
- Opinion: #fcf9f5 with #e6ded3 border (ET op-ed editorial warm paper)
- Shorts: #141414 with #282828 border (Dark video canvas)
- Videos: #091726 to #0e2338 navy gradient
- Sports Scorecard: #f1f5f6 with #e3e3e3 border (ET stock/indices gray)
- Primary Accent: #ed193b (ET Crimson Red)
- Market Up/Down: #0b8f16 (Green) / #ed193b (Crimson)
"""

import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLES_FILE = os.path.join(WORKSPACE_DIR, "styles.css")
REFINE_FILE = os.path.join(WORKSPACE_DIR, "refine_styles.py")

with open(REFINE_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Update root variables with authentic ET color & background tokens
old_root = """  /* Official Economic Times Colors */
  --bg: #f8f9fa;
  --sf: #ffffff;
  --ph: #f0f2f5;
  --ln: #eceaea;
  --ln-subtle: #f4f4f4;
  --tx: #111827;
  --tx-sec: #4b5563;
  --mu: #6b7280;
  
  /* ET Crimson Red Accents */
  --ac: #ed193b;
  --ac-hover: #b80e2b;
  --ac-dark: #99001a;
  
  /* ET Royal Navy & Brand Backgrounds */
  --navy: #0c233c;
  --navy-dark: #071728;
  --navy-card: #0a1f38;
  --purple-summit: #472064;
  --purple-light: #f5edf9;
  
  /* ET Markets Green & Warm Highlights */
  --green-up: #147014;
  --red-down: #b80e2b;
  --peach-highlight: #fff8f6;
  --peach-border: #ffd8cc;"""

new_root = """  /* Official Economic Times Colors & Backgrounds */
  --bg: #f5f5f5;
  --sf: #ffffff;
  --ph: #edeef2;
  --ln: #eceaea;
  --ln-subtle: #f4f4f4;
  --tx: #111111;
  --tx-sec: #4d4d4d;
  --mu: #686868;
  
  /* ET Signature Crimson Red Accents */
  --ac: #ed193b;
  --ac-hover: #b80e2b;
  --ac-dark: #99001a;
  --ac-tint: #fff0f2;
  
  /* ET Signature Paper Backgrounds & Section Colors */
  --et-ticker-bg: #fbf4e4;
  --et-ticker-border: #d8cbb7;
  --et-peach-bg: #fff3f0;
  --et-peach-border: #e4ccc4;
  --et-peach-deep: #ffe9e2;
  --et-opinion-bg: #fcf9f5;
  --et-opinion-border: #e6ded3;
  --et-offbeat-bg: #f8faf7;
  --et-offbeat-border: #e1ebe1;
  --et-stocks-bg: #f1f5f6;
  --et-stocks-border: #e3e3e3;
  --et-dark-bg: #191919;
  
  /* ET Royal Navy & Brand Backgrounds */
  --navy: #0c233c;
  --navy-dark: #071728;
  --navy-card: #0a1f38;
  --purple-summit: #472064;
  --purple-light: #f5edf9;
  
  /* ET Markets Green & Market Red */
  --green-up: #0b8f16;
  --red-down: #ed193b;
  --peach-highlight: #fff3f0;
  --peach-border: #e4ccc4;"""

if old_root in content:
    content = content.replace(old_root, new_root)
    print("Replaced root variables with authentic ET color tokens.")
else:
    print("Notice: old_root pattern not exact, checking alternative replacement...")

# Replace dark mode variables as well
old_dark = """  :root:not([data-theme="light"]) {
    --bg: #0b0f17;
    --sf: #131b26;
    --ph: #1f2b3d;
    --ln: #223042;
    --ln-subtle: #192330;
    --tx: #f3f4f6;
    --tx-sec: #9ca3af;
    --mu: #94a3b8;
    --navy: #081626;
    --navy-card: #0e1d2e;
    --purple-light: #1f182b;
    --peach-highlight: #1a151b;
    --peach-border: #3b2832;
    color-scheme: dark;
  }"""

new_dark = """  :root:not([data-theme="light"]) {
    --bg: #0e121a;
    --sf: #161e2b;
    --ph: #1f2b3d;
    --ln: #243245;
    --ln-subtle: #1c2738;
    --tx: #f3f4f6;
    --tx-sec: #9ca3af;
    --mu: #94a3b8;
    --et-ticker-bg: #1c1813;
    --et-ticker-border: #3d3429;
    --et-peach-bg: #1c1518;
    --et-peach-border: #3b2832;
    --et-peach-deep: #261b21;
    --et-opinion-bg: #1c1815;
    --et-opinion-border: #3a3229;
    --et-offbeat-bg: #141c16;
    --et-offbeat-border: #233527;
    --et-stocks-bg: #151d27;
    --et-stocks-border: #243242;
    --et-dark-bg: #0a0e14;
    --navy: #081626;
    --navy-card: #0e1d2e;
    --purple-light: #1f182b;
    color-scheme: dark;
  }"""

if old_dark in content:
    content = content.replace(old_dark, new_dark)
    print("Replaced dark mode variables.")

# Update channel-bar styling to dark ET network strip
old_ch_bar = """.channel-bar {
  background: #edeef2;
  border-bottom: 1px solid #dcdfe6;
  font-size: 11px;
  height: 34px;
  width: 100%;
  display: flex;
  align-items: center;
}"""

new_ch_bar = """.channel-bar {
  background: var(--et-dark-bg);
  border-bottom: 1px solid #282828;
  font-size: 11px;
  height: 36px;
  width: 100%;
  display: flex;
  align-items: center;
}

.channel-bar .ch-link {
  color: #d1d5db;
}

.channel-bar .ch-link:hover {
  color: #ffffff;
}

.channel-bar .ch-link.on {
  color: #ffffff;
}

.channel-bar .prime-chip {
  color: #f59e0b !important;
}

.channel-bar .theme-toggle-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.22);
  color: #d1d5db;
}

.channel-bar .theme-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.18);
  color: #ffffff;
}"""

if old_ch_bar in content:
    content = content.replace(old_ch_bar, new_ch_bar)
    print("Updated channel-bar to ET dark network strip.")

# Update ticker bar styling
old_ticker = """.et-ticker-bar {
  background: #ffffff;
  border-bottom: 1px solid var(--ln);
  height: 32px;
  display: flex;
  align-items: center;
  font-size: 11px;
  width: 100%;
}"""

new_ticker = """.et-ticker-bar {
  background: var(--et-ticker-bg);
  border-top: 1px solid var(--et-ticker-border);
  border-bottom: 1px solid var(--et-ticker-border);
  height: 36px;
  display: flex;
  align-items: center;
  font-size: 11px;
  width: 100%;
  box-sizing: border-box;
}

.et-ticker-bar .ticker-tag {
  background: var(--ac);
  color: #ffffff;
  box-shadow: 0 1px 4px rgba(237, 25, 59, 0.3);
}

.et-ticker-bar .live-dot-et {
  background: #ffffff;
}

.et-ticker-bar .t-change.up {
  color: var(--green-up);
}

.et-ticker-bar .t-change.down {
  color: var(--red-down);
}"""

if old_ticker in content:
    content = content.replace(old_ticker, new_ticker)
    print("Updated ticker bar to ET cream paper styling.")

# Ensure top-lead-grid has white card background and border
old_lead = """.top-lead-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.45fr) minmax(0, 1fr) 300px;
  gap: 20px;
  align-items: start;
  margin-bottom: 28px;
  width: 100%;
}"""

new_lead = """.top-lead-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.45fr) minmax(0, 1fr) 300px;
  gap: 20px;
  align-items: start;
  margin-bottom: 28px;
  width: 100%;
  background: var(--sf);
  border: 1px solid var(--ln);
  border-radius: var(--radius-md);
  padding: 18px;
}"""

if old_lead in content:
    content = content.replace(old_lead, new_lead)
    print("Updated top-lead-grid with card boundary.")

# Update summit hub section background
old_summit_hub = """.summit-hub-section {
  background: var(--sf);
  border: 1px solid var(--ln);
  border-radius: var(--radius-md);
  padding: 16px;
  margin-bottom: 28px;
  width: 100%;
}"""

new_summit_hub = """.summit-hub-section {
  background: var(--et-peach-bg);
  border: 1px solid var(--et-peach-border);
  border-radius: var(--radius-md);
  padding: 18px;
  margin-bottom: 28px;
  width: 100%;
}

.summit-cards-row .summit-news-card {
  background: var(--sf);
  border: 1px solid #f0ded8;
  border-radius: var(--radius-sm);
  padding: 10px;
  transition: var(--transition);
}

:root[data-theme="dark"] .summit-cards-row .summit-news-card {
  border-color: #3b2832;
}

.summit-cards-row .summit-news-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(237, 25, 59, 0.08);
}

.summit-live-timeline-strip {
  background: var(--et-peach-deep);
  border: 1px solid var(--et-peach-border);
}"""

if old_summit_hub in content:
    content = content.replace(old_summit_hub, new_summit_hub)
    print("Updated summit-hub-section to ET peach highlight.")

# Update portal-section specific backgrounds
old_portal = """.portal-section {
  background: var(--sf);
  border: 1px solid var(--ln);
  border-radius: var(--radius-md);
  padding: 16px;
  margin-bottom: 26px;
  width: 100%;
}"""

new_portal = """.portal-section {
  background: var(--sf);
  border: 1px solid var(--ln);
  border-radius: var(--radius-md);
  padding: 18px;
  margin-bottom: 26px;
  width: 100%;
}

/* Specific Section Backgrounds matching The Economic Times */
.portal-section#offbeat {
  background: var(--et-offbeat-bg);
  border-color: var(--et-offbeat-border);
}

.portal-section#offbeat .offbeat-card {
  background: var(--sf);
  border: 1px solid #e1ebe1;
  border-radius: var(--radius-sm);
  padding: 12px;
  transition: var(--transition);
}

:root[data-theme="dark"] .portal-section#offbeat .offbeat-card {
  border-color: #233527;
}

.portal-section#offbeat .offbeat-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
  border-color: #bcd4bc;
}

.portal-section#india-section {
  background: var(--sf);
  border-color: var(--ln);
}

.portal-section#india-section .india-item {
  padding: 8px 6px;
  border-radius: var(--radius-sm);
  transition: background-color 0.15s ease;
}

.portal-section#india-section .india-item:hover {
  background: #fbfbfb;
}

:root[data-theme="dark"] .portal-section#india-section .india-item:hover {
  background: #1c2736;
}

.portal-section#opinion {
  background: var(--et-opinion-bg);
  border-color: var(--et-opinion-border);
}

.portal-section#opinion .opinion-author-card {
  background: var(--sf);
  border: 1px solid #e6ded3;
  border-radius: var(--radius-sm);
  padding: 16px;
  transition: var(--transition);
}

:root[data-theme="dark"] .portal-section#opinion .opinion-author-card {
  border-color: #3a3229;
}

.portal-section#opinion .opinion-author-card:hover {
  border-color: var(--ac);
  box-shadow: 0 4px 12px rgba(237, 25, 59, 0.08);
  transform: translateY(-2px);
}

.portal-section#shorts-section {
  background: #141414;
  border-color: #282828;
  color: #ffffff;
}

.portal-section#shorts-section .sec-heading h2,
.portal-section#shorts-section .sec-heading h2 a {
  color: #ffffff;
}

.portal-section#videos-section {
  background: var(--sf);
  border-color: var(--ln);
}

.sports-row#sports-section {
  background: var(--sf);
  border: 1px solid var(--ln);
  border-radius: var(--radius-md);
  padding: 18px;
  margin-bottom: 26px;
}

.sports-row#sports-section .live-score-widget {
  background: var(--et-stocks-bg);
  border: 1px solid var(--et-stocks-border);
  border-radius: var(--radius-sm);
  padding: 14px;
}

.regional-grid {
  background: var(--sf);
  border: 1px solid var(--ln);
  border-radius: var(--radius-md);
  padding: 18px;
  margin-bottom: 26px;
}"""

if old_portal in content:
    content = content.replace(old_portal, new_portal)
    print("Updated portal sections with specific ET background colors.")

# Update section headings with ET signature crimson red accent line
old_sec_h2 = """.sec-heading h2 {
  font-family: var(--font-sans);
  font-size: 18px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--tx);
  display: flex;
  align-items: center;
}"""

new_sec_h2 = """.sec-heading h2 {
  font-family: var(--font-sans);
  font-size: 18px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--tx);
  display: flex;
  align-items: center;
  border-left: 4px solid var(--ac);
  padding-left: 10px;
  line-height: 1.2;
}

.summit-hub-title,
.sh h2 {
  border-left: 4px solid var(--ac);
  padding-left: 10px;
}"""

if old_sec_h2 in content:
    content = content.replace(old_sec_h2, new_sec_h2)
    print("Updated section headings with ET signature crimson accent.")

# Update footer background
old_ft = """.ft {
  background: var(--navy);
  color: #ffffff;
  padding: 36px 0 24px;
  margin-top: 40px;
}"""

new_ft = """.ft {
  background: var(--et-dark-bg);
  border-top: 4px solid var(--ac);
  color: #d1d5db;
  padding: 36px 0 24px;
  margin-top: 40px;
}"""

if old_ft in content:
    content = content.replace(old_ft, new_ft)
    print("Updated footer to ET dark corporate style.")

# Save updated refine_styles.py
with open(REFINE_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("[Python Styler] refine_styles.py updated successfully.")
