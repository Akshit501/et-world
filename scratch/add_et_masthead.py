#!/usr/bin/env python3
"""
Adds the official, permanent The Economic Times masthead exactly as shown
in the reference screenshot (media_1792655326156.png):
- Pure white background (#ffffff)
- Left: balanced spacer
- Center: Red square [ET] + "THE ECONOMIC TIMES" serif masthead
  Subtitle: English Edition ▾ | 22 October, 2026, 01:17 PM IST | Today's ePaper
- Right: [My Watchlist] [Subscribe] Sign In
  Below: Mega Festive Sale ↗ (with hairline borders)
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

masthead_html = """  <!-- =====================================================================
       THE ECONOMIC TIMES OFFICIAL MASTHEAD (Permanent, Reference Screenshot)
       ===================================================================== -->
  <div class="et-masthead-section" id="etOfficialMasthead">
    <div class="container-fit masthead-container">
      
      <!-- Left Spacer for Perfect Center Balancing -->
      <div class="masthead-left-spacer" aria-hidden="true"></div>

      <!-- Center: The Economic Times Logo & Edition / Date Subtitle -->
      <div class="masthead-center">
        <a href="/" class="et-main-brand" aria-label="The Economic Times">
          <span class="et-red-box">ET</span>
          <span class="et-title-text">
            <span class="et-title-the">THE</span>
            <span class="et-title-main">ECONOMIC TIMES</span>
          </span>
        </a>
        <div class="masthead-sub-meta">
          <span class="meta-edition-dropdown" id="editionDropdownBtn">
            English Edition <span class="caret-down">▾</span>
          </span>
          <span class="meta-divider">|</span>
          <span class="meta-datetime" id="mastheadDateTime">22 October, 2026, 01:17 PM IST</span>
          <span class="meta-divider">|</span>
          <a href="#epaper" class="meta-epaper-link">Today's ePaper</a>
        </div>
      </div>

      <!-- Right: Action Buttons & Mega Festive Sale -->
      <div class="masthead-right-actions">
        <div class="masthead-top-actions">
          <a href="#watchlist" class="btn-et-outline" id="mastheadWatchlistBtn">My Watchlist</a>
          <a href="#subscribe" class="btn-et-outline" id="mastheadSubscribeBtn">Subscribe</a>
          <a href="#signin" class="btn-et-signin" id="mastheadSignInBtn">Sign In</a>
        </div>
        <div class="festive-sale-strip">
          <a href="#festive-sale" class="festive-sale-link">
            Mega Festive Sale <span class="festive-arrow">↗</span>
          </a>
        </div>
      </div>

    </div>
  </div>
"""

# Insert the masthead directly above the et-ticker-bar or between channel-bar and et-ticker-bar
if 'class="et-masthead-section"' not in site_code:
    target = '  <!-- ET Live Global Financial Markets Ticker'
    if target in site_code:
        site_code = site_code.replace(target, masthead_html + "\n" + target)
        print("[build_site.py] Injected .et-masthead-section above et-ticker-bar.")
    else:
        print("[build_site.py] Warning: target not found.")

with open(BUILD_SITE_FILE, "w", encoding="utf-8") as f:
    f.write(site_code)

# 2. UPDATE REFINE_STYLES.PY
with open(REFINE_STYLES_FILE, "r", encoding="utf-8") as f:
    refine_code = f.read()

masthead_css = """/* ==========================================================================
   THE ECONOMIC TIMES OFFICIAL MASTHEAD (Exact Reference Screenshot)
   ========================================================================== */
.et-masthead-section {
  background: #ffffff;
  border-bottom: 1px solid #f0f0f0;
  padding: 16px 0 12px;
  width: 100%;
  position: relative;
  z-index: 95;
}

:root[data-theme="dark"] .et-masthead-section {
  background: #111722;
  border-bottom-color: #1f2b3d;
}

.masthead-container {
  display: grid;
  grid-template-columns: 240px 1fr 240px;
  align-items: center;
}

@media (max-width: 992px) {
  .masthead-container {
    grid-template-columns: 1fr;
    gap: 12px;
    text-align: center;
  }
  .masthead-left-spacer {
    display: none;
  }
  .masthead-right-actions {
    align-items: center;
    justify-content: center;
  }
}

.masthead-left-spacer {
  width: 100%;
}

.masthead-center {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.et-main-brand {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-decoration: none;
  color: #0b1118;
  line-height: 1;
}

.et-red-box {
  background: var(--ac);
  color: #ffffff;
  font-family: var(--font-serif);
  font-size: 26px;
  font-weight: 800;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  letter-spacing: -0.04em;
  border-radius: 2px;
  flex-shrink: 0;
  box-shadow: 0 2px 6px rgba(237, 25, 59, 0.25);
}

.et-title-text {
  display: flex;
  align-items: baseline;
  gap: 7px;
  color: #0b1118;
  font-family: var(--font-serif);
}

:root[data-theme="dark"] .et-title-text {
  color: #ffffff;
}

.et-title-the {
  font-size: 20px;
  font-weight: 700;
  letter-spacing: 0.02em;
  color: inherit;
}

.et-title-main {
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: inherit;
}

.masthead-sub-meta {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  margin-top: 6px;
  font-family: var(--font-sans);
  font-size: 11.5px;
  color: #555555;
  white-space: nowrap;
}

:root[data-theme="dark"] .masthead-sub-meta {
  color: #9ca3af;
}

.meta-edition-dropdown {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-weight: 500;
  transition: color 0.15s ease;
}

.meta-edition-dropdown:hover {
  color: var(--ac);
}

.caret-down {
  font-size: 9px;
}

.meta-divider {
  color: #d1d5db;
  font-size: 11px;
}

.meta-datetime {
  font-weight: 500;
}

.meta-epaper-link {
  font-weight: 700;
  color: #111111;
  text-decoration: none;
  transition: color 0.15s ease;
}

:root[data-theme="dark"] .meta-epaper-link {
  color: #ffffff;
}

.meta-epaper-link:hover {
  color: var(--ac);
}

/* Right Actions */
.masthead-right-actions {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;
}

.masthead-top-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-et-outline {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 4px 10px;
  border: 1px solid #555555;
  border-radius: 2px;
  background: #ffffff;
  color: #111111;
  font-family: var(--font-sans);
  font-size: 11.5px;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.15s ease;
}

:root[data-theme="dark"] .btn-et-outline {
  background: transparent;
  border-color: #6b7280;
  color: #f3f4f6;
}

.btn-et-outline:hover {
  border-color: var(--ac);
  color: var(--ac);
}

.btn-et-signin {
  font-family: var(--font-sans);
  font-size: 12px;
  font-weight: 600;
  color: #111111;
  text-decoration: none;
  margin-left: 6px;
  cursor: pointer;
  transition: color 0.15s ease;
}

:root[data-theme="dark"] .btn-et-signin {
  color: #f3f4f6;
}

.btn-et-signin:hover {
  color: var(--ac);
}

.festive-sale-strip {
  margin-top: 8px;
  border-top: 1px solid #ffe8ec;
  border-bottom: 1px solid #ffe8ec;
  padding: 3px 0;
  width: 100%;
  text-align: right;
}

:root[data-theme="dark"] .festive-sale-strip {
  border-top-color: #3b2832;
  border-bottom-color: #3b2832;
}

.festive-sale-link {
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 700;
  color: #c41230;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  transition: color 0.15s ease;
}

.festive-sale-link:hover {
  color: var(--ac);
}

.festive-arrow {
  font-size: 13px;
  font-weight: 800;
}
"""

if 'class="et-masthead-section"' not in refine_code and '.et-masthead-section' not in refine_code:
    target_css = '/* ==========================================================================\n   ET LIVE MARKETS BENCHMARK TICKER STRIP (.et-ticker-bar)'
    if target_css in refine_code:
        refine_code = refine_code.replace(target_css, masthead_css + "\n" + target_css)
        print("[refine_styles.py] Injected masthead CSS.")
    else:
        # Fallback to inserting before ticker
        refine_code = refine_code.replace('.et-ticker-bar {', masthead_css + "\n.et-ticker-bar {")
        print("[refine_styles.py] Injected masthead CSS before .et-ticker-bar.")

with open(REFINE_STYLES_FILE, "w", encoding="utf-8") as f:
    f.write(refine_code)

# 3. UPDATE APP.JS WITH DYNAMIC MASTHEAD CLOCK & ACTIONS
with open(APP_JS_FILE, "r", encoding="utf-8") as f:
    js_code = f.read()

if 'initMastheadMeta()' not in js_code:
    # Add to DOMContentLoaded
    js_code = js_code.replace(
        '  initMarketTicker();',
        '  initMarketTicker();\n  initMastheadMeta();'
    )
    
    masthead_js = """
/* ==========================================================================
   OFFICIAL ET MASTHEAD CONTROLLER
   ========================================================================== */
function initMastheadMeta() {
  const dtEl = document.getElementById('mastheadDateTime');
  if (dtEl) {
    function updateMastheadTime() {
      const now = new Date();
      const day = now.getDate();
      const month = now.toLocaleDateString('en-US', { month: 'long' });
      const year = now.getFullYear();
      const timeStr = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
      dtEl.textContent = `${day} ${month}, ${year}, ${timeStr} IST`;
    }
    updateMastheadTime();
    setInterval(updateMastheadTime, 30000);
  }

  const dropdownBtn = document.getElementById('editionDropdownBtn');
  if (dropdownBtn) {
    dropdownBtn.addEventListener('click', () => {
      showToast('English Edition selected. Other editions: Hindi, Gujarati, Marathi');
    });
  }

  const watchlistBtn = document.getElementById('mastheadWatchlistBtn');
  if (watchlistBtn) {
    watchlistBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('My Watchlist: 5 stocks tracked (NIFTY, RELIANCE, TCS, INFY, HDFCBANK)');
    });
  }

  const subscribeBtn = document.getElementById('mastheadSubscribeBtn');
  if (subscribeBtn) {
    subscribeBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('ET Prime Subscription Plan: Special Festive Discount Applied!');
    });
  }
}
"""
    js_code += "\n" + masthead_js
    print("[app.js] Added initMastheadMeta implementation.")

with open(APP_JS_FILE, "w", encoding="utf-8") as f:
    f.write(js_code)

print("[add_et_masthead.py] All files updated successfully!")
