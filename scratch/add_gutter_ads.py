#!/usr/bin/env python3
"""
Adds dummy ads to the left and right empty spaces:
1. Masthead left empty space: .masthead-left-ad with HDFC SKY 0% Brokerage promo.
2. Desktop left & right outer gutters: Skyscraper sticky banner ads
   - Left Gutter: ET Markets App real-time feeds
   - Right Gutter: ET Prime 50% Off Festive Special
"""

import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_SITE_FILE = os.path.join(WORKSPACE_DIR, "build_site.py")
REFINE_STYLES_FILE = os.path.join(WORKSPACE_DIR, "refine_styles.py")
APP_JS_FILE = os.path.join(WORKSPACE_DIR, "app.js")

# 1. UPDATE BUILD_SITE.PY
with open(BUILD_SITE_FILE, "r", encoding="utf-8") as f:
    site_code = f.read()

# Replace masthead left spacer with left dummy ad
old_spacer = '<div class="masthead-left-spacer" aria-hidden="true"></div>'
new_left_ad = """<!-- Left: Sponsored Partner Ad Badge (Fills Left Empty Space) -->
      <div class="masthead-left-ad">
        <a href="#partner-offer" class="masthead-ad-card" id="mastheadAdLink" title="Sponsored Offer">
          <span class="m-ad-label">ADVERTISEMENT</span>
          <div class="m-ad-body">
            <img src="https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=120&auto=format&fit=crop&q=80" alt="HDFC Sky Global Trading" class="m-ad-thumb">
            <div class="m-ad-copy">
              <span class="m-ad-brand">HDFC SKY</span>
              <strong class="m-ad-headline">0% Brokerage on US Stocks</strong>
              <span class="m-ad-cta">Open Account →</span>
            </div>
          </div>
        </a>
      </div>"""

if old_spacer in site_code:
    site_code = site_code.replace(old_spacer, new_left_ad)
    print("[build_site.py] Replaced masthead-left-spacer with masthead-left-ad.")
else:
    print("[build_site.py] Notice: old_spacer not found, checking if already replaced.")

# Add Left & Right Skyscraper Gutter Ads directly after <body ...>
gutter_ads_html = """  <!-- =====================================================================
       LEFT & RIGHT GUTTER SKYSCRAPER ADS (Fills Left & Right Empty Spaces)
       ===================================================================== -->
  <aside class="et-gutter-ad left-gutter-ad" id="leftGutterAd" aria-label="Left Skyscraper Advertisement">
    <div class="gutter-ad-sticky">
      <div class="ad-tag-bar">
        <span>ADVERTISEMENT</span>
        <button class="ad-close-btn" id="closeLeftAdBtn" title="Close Ad">&times;</button>
      </div>
      <a href="#ad-markets-app" class="gutter-ad-link" id="leftGutterAdLink">
        <div class="gad-brand">
          <span class="gad-logo-et">ET</span> <strong>MARKETS APP</strong>
        </div>
        <div class="gad-hero-img">
          <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=300&auto=format&fit=crop&q=80" alt="ET Markets App">
        </div>
        <div class="gad-title">Live Sensex &amp; Nifty Feeds</div>
        <p class="gad-desc">Track global portfolios, expert stock calls &amp; alerts 24/7.</p>
        <span class="gad-cta-btn">Download App →</span>
        <div class="gad-sponsor">Google Play ★ 4.7</div>
      </a>
    </div>
  </aside>

  <aside class="et-gutter-ad right-gutter-ad" id="rightGutterAd" aria-label="Right Skyscraper Advertisement">
    <div class="gutter-ad-sticky">
      <div class="ad-tag-bar">
        <span>ADVERTISEMENT</span>
        <button class="ad-close-btn" id="closeRightAdBtn" title="Close Ad">&times;</button>
      </div>
      <a href="#ad-prime-festive" class="gutter-ad-link" id="rightGutterAdLink">
        <div class="gad-brand festive">
          <span>✨ FESTIVE SPECIAL</span>
        </div>
        <div class="gad-hero-img">
          <img src="https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=300&auto=format&fit=crop&q=80" alt="ET Prime 50% Off">
        </div>
        <div class="gad-title">ET PRIME Pass at 50% OFF</div>
        <p class="gad-desc">Exclusive deep-dive analyses &amp; expert stock recommendations.</p>
        <span class="gad-cta-btn festive-btn">Claim 50% Off →</span>
        <div class="gad-sponsor">Limited Festive Offer</div>
      </a>
    </div>
  </aside>
"""

if 'id="leftGutterAd"' not in site_code:
    body_tag = '<nav class="channel-bar"'
    if body_tag in site_code:
        site_code = site_code.replace(body_tag, gutter_ads_html + "\n  " + body_tag)
        print("[build_site.py] Injected left and right gutter skyscraper ads.")

with open(BUILD_SITE_FILE, "w", encoding="utf-8") as f:
    f.write(site_code)

# 2. UPDATE REFINE_STYLES.PY
with open(REFINE_STYLES_FILE, "r", encoding="utf-8") as f:
    refine_code = f.read()

ads_css = """/* ==========================================================================
   LEFT & RIGHT GUTTER SKYSCRAPER ADS (Fills Left & Right Empty Spaces)
   ========================================================================== */
.et-gutter-ad {
  position: fixed;
  top: 155px;
  width: 140px;
  z-index: 85;
  display: none;
}

@media (min-width: 1600px) {
  .et-gutter-ad {
    display: block;
  }
  .left-gutter-ad {
    left: calc(50% - (var(--container-max) / 2) - 152px);
  }
  .right-gutter-ad {
    right: calc(50% - (var(--container-max) / 2) - 152px);
  }
}

@media (min-width: 1360px) and (max-width: 1599px) {
  .et-gutter-ad {
    display: block;
    width: 120px;
  }
  .left-gutter-ad {
    left: 8px;
  }
  .right-gutter-ad {
    right: 8px;
  }
}

.gutter-ad-sticky {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-sm);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

:root[data-theme="dark"] .gutter-ad-sticky {
  background: #151d2a;
  border-color: #243245;
}

.gutter-ad-sticky:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
}

.ad-tag-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f1f5f9;
  padding: 3px 6px;
  font-size: 8px;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #64748b;
  border-bottom: 1px solid #e2e8f0;
}

:root[data-theme="dark"] .ad-tag-bar {
  background: #111827;
  color: #94a3b8;
  border-bottom-color: #1f2937;
}

.ad-close-btn {
  background: none;
  border: none;
  font-size: 13px;
  line-height: 1;
  color: #94a3b8;
  cursor: pointer;
  padding: 0 2px;
}

.ad-close-btn:hover {
  color: var(--ac);
}

.gutter-ad-link {
  display: flex;
  flex-direction: column;
  padding: 8px 7px;
  text-decoration: none;
  color: var(--tx);
  gap: 6px;
}

.gad-brand {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 10px;
  font-weight: 800;
  color: #0b1118;
}

:root[data-theme="dark"] .gad-brand {
  color: #ffffff;
}

.gad-brand.festive {
  background: #fff0f2;
  color: var(--ac);
  padding: 2px 4px;
  border-radius: 2px;
  font-size: 9px;
  justify-content: center;
}

:root[data-theme="dark"] .gad-brand.festive {
  background: #2b1218;
}

.gad-logo-et {
  background: var(--ac);
  color: #fff;
  font-size: 8px;
  font-weight: 900;
  padding: 1px 3px;
  border-radius: 2px;
}

.gad-hero-img {
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 2px;
  overflow: hidden;
  background: #e2e8f0;
}

.gad-hero-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gad-title {
  font-family: var(--font-sans);
  font-size: 10.5px;
  font-weight: 700;
  line-height: 1.25;
  color: var(--tx);
}

.gad-desc {
  font-size: 9px;
  color: var(--tx-sec);
  line-height: 1.3;
  margin: 0;
}

.gad-cta-btn {
  background: var(--ac);
  color: #ffffff !important;
  font-size: 9px;
  font-weight: 700;
  padding: 4px 6px;
  border-radius: 2px;
  text-align: center;
  margin-top: 2px;
  letter-spacing: 0.02em;
  transition: background 0.15s ease;
}

.gad-cta-btn:hover {
  background: var(--ac-hover);
}

.gad-cta-btn.festive-btn {
  background: #d97706;
}

.gad-cta-btn.festive-btn:hover {
  background: #b45309;
}

.gad-sponsor {
  font-size: 8px;
  color: var(--mu);
  text-align: center;
  margin-top: 2px;
}

/* Masthead Left Dummy Ad (Fills Left Empty Space in Masthead) */
.masthead-left-ad {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

@media (max-width: 992px) {
  .masthead-left-ad {
    display: none;
  }
}

.masthead-ad-card {
  display: flex;
  flex-direction: column;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 3px;
  padding: 4px 8px;
  max-width: 220px;
  text-decoration: none;
  transition: all 0.15s ease;
}

:root[data-theme="dark"] .masthead-ad-card {
  background: #151d2a;
  border-color: #243245;
}

.masthead-ad-card:hover {
  border-color: var(--ac);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.m-ad-label {
  font-size: 7.5px;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #94a3b8;
  margin-bottom: 2px;
}

.m-ad-body {
  display: flex;
  align-items: center;
  gap: 7px;
}

.m-ad-thumb {
  width: 36px;
  height: 36px;
  border-radius: 2px;
  object-fit: cover;
  flex-shrink: 0;
}

.m-ad-copy {
  display: flex;
  flex-direction: column;
  line-height: 1.15;
}

.m-ad-brand {
  font-size: 8.5px;
  font-weight: 800;
  color: var(--ac);
}

.m-ad-headline {
  font-size: 10.5px;
  font-weight: 700;
  color: var(--tx);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 145px;
}

.m-ad-cta {
  font-size: 9px;
  font-weight: 700;
  color: #2563eb;
  margin-top: 1px;
}
"""

if '.et-gutter-ad' not in refine_code:
    target_pos = '/* ==========================================================================\n   THE ECONOMIC TIMES OFFICIAL MASTHEAD'
    if target_pos in refine_code:
        refine_code = refine_code.replace(target_pos, ads_css + "\n" + target_pos)
        print("[refine_styles.py] Added gutter ads and masthead-left-ad styles.")
    else:
        refine_code = ads_css + "\n" + refine_code
        print("[refine_styles.py] Prepended gutter ads styles.")

with open(REFINE_STYLES_FILE, "w", encoding="utf-8") as f:
    f.write(refine_code)

# 3. UPDATE APP.JS WITH AD ACTIONS
with open(APP_JS_FILE, "r", encoding="utf-8") as f:
    js_code = f.read()

if 'initGutterAds()' not in js_code:
    js_code = js_code.replace(
        '  initMastheadMeta();',
        '  initMastheadMeta();\n  initGutterAds();'
    )
    
    gutter_js = """
/* ==========================================================================
   LEFT & RIGHT GUTTER ADS CONTROLLER
   ========================================================================== */
function initGutterAds() {
  const closeLeft = document.getElementById('closeLeftAdBtn');
  const closeRight = document.getElementById('closeRightAdBtn');
  const leftAd = document.getElementById('leftGutterAd');
  const rightAd = document.getElementById('rightGutterAd');

  if (closeLeft && leftAd) {
    closeLeft.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      leftAd.style.display = 'none';
      showToast('Left Skyscraper Ad closed.');
    });
  }

  if (closeRight && rightAd) {
    closeRight.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      rightAd.style.display = 'none';
      showToast('Right Skyscraper Ad closed.');
    });
  }

  const leftAdLink = document.getElementById('leftGutterAdLink');
  if (leftAdLink) {
    leftAdLink.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('ET Markets App: Download prompt opened for your device.');
    });
  }

  const rightAdLink = document.getElementById('rightGutterAdLink');
  if (rightAdLink) {
    rightAdLink.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('ET Prime Festive Offer: 50% discount coupon applied!');
    });
  }

  const mastheadAd = document.getElementById('mastheadAdLink');
  if (mastheadAd) {
    mastheadAd.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('HDFC Sky: 0% Brokerage Global Equities application opened.');
    });
  }
}
"""
    js_code += "\n" + gutter_js
    print("[app.js] Added initGutterAds implementation.")

with open(APP_JS_FILE, "w", encoding="utf-8") as f:
    f.write(js_code)

print("[add_gutter_ads.py] Completed all updates!")
