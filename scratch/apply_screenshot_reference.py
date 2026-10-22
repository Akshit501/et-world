#!/usr/bin/env python3
"""
Applies exact styling, colors, typography and dummy ads from the uploaded ET screenshots:
1. Gutter Ads (Left & Right Takeover):
   - PwC "Aspiring Women Leaders Scholarship" Skyscraper Ad
   - pwc logo, "Empowering the next generation of women engineers"
   - Bullet points: Tuition grant, tech resources, mentorship, industry exposure
   - Orange CTA: "[icon] Know more"
   - Woman engineer visual with tablet & orange geometric graphic
   - Background: #fff2ee to #ffffff soft peach gradient
2. Right Column Ad Card:
   - Matching PwC Scholarship 300x250 Ad Banner
   - Bloomberg "Seize the momentum" AI Insights Card
3. Typography & News Headlines:
   - Faustina serif for all headlines (#111111, weight 600-700)
   - Clean hairline dividers between news items (#ebebeb)
   - Red dots: ⦿ for breaking stories
   - Red circular play bullets: ▶ for category headers (Investment Ideas >, Prime Exclusives >, etc.)
4. Sub-Navigation Bars:
   - Primary categories: Home (Active Red) | ETPrime | Markets | Market Data | Masterclass | News | Industry | ...
   - Trending strip: News Live! | US Midterms (Red) | ET World Summit (Red) | ET Wealth Expo | AI Winter Camp | ...
5. Background Colors:
   - Pure white content canvas with soft peach highlight boxes (#fff5f0 with #ffd8cc border)
"""

import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_SITE_FILE = os.path.join(WORKSPACE_DIR, "build_site.py")
REFINE_STYLES_FILE = os.path.join(WORKSPACE_DIR, "refine_styles.py")
APP_JS_FILE = os.path.join(WORKSPACE_DIR, "app.js")

# ==============================================================================
# 1. NEW HTML TEMPLATE FOR BUILD_SITE.PY
# ==============================================================================
with open(BUILD_SITE_FILE, "r", encoding="utf-8") as f:
    site_code = f.read()

# Replace the gutter ads with the PwC Takeover Skyscraper Ads
pwc_left_ad = """  <!-- =====================================================================
       PwC ASPIRING WOMEN LEADERS SCHOLARSHIP TAKEOVER ADS (Reference Screenshots)
       ===================================================================== -->
  <aside class="et-gutter-ad left-gutter-ad pwc-gutter-ad" id="leftGutterAd" aria-label="PwC Advertisement">
    <div class="gutter-ad-sticky pwc-sticky-card">
      <div class="pwc-top-brand">
        <div class="pwc-logo-wrap">
          <span class="pwc-squares"><span class="sq1"></span><span class="sq2"></span><span class="sq3"></span><span class="sq4"></span></span>
          <span class="pwc-text">pwc</span>
        </div>
        <button class="ad-close-btn" id="closeLeftAdBtn" title="Close Ad">&times;</button>
      </div>
      <a href="#pwc-scholarship" class="pwc-ad-link" id="leftGutterAdLink">
        <h4 class="pwc-title">Aspiring Women Leaders Scholarship</h4>
        <p class="pwc-subtitle">Empowering the next generation of women engineers</p>
        <ul class="pwc-bullets">
          <li>Financial grant for tuition</li>
          <li>Technology resources</li>
          <li>Executive mentorship</li>
          <li>Industry exposure</li>
        </ul>
        <div class="pwc-cta-row">
          <span class="pwc-orange-box">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 13l4 4L19 7"/></svg>
          </span>
          <span class="pwc-cta-text">Know more</span>
        </div>
        <div class="pwc-visual-wrap">
          <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=320&auto=format&fit=crop&q=80" alt="Woman engineer" class="pwc-woman-img">
          <div class="pwc-geom-bar"></div>
        </div>
      </a>
    </div>
  </aside>

  <aside class="et-gutter-ad right-gutter-ad pwc-gutter-ad" id="rightGutterAd" aria-label="PwC Advertisement">
    <div class="gutter-ad-sticky pwc-sticky-card">
      <div class="pwc-top-brand">
        <div class="pwc-logo-wrap">
          <span class="pwc-squares"><span class="sq1"></span><span class="sq2"></span><span class="sq3"></span><span class="sq4"></span></span>
          <span class="pwc-text">pwc</span>
        </div>
        <button class="ad-close-btn" id="closeRightAdBtn" title="Close Ad">&times;</button>
      </div>
      <a href="#pwc-scholarship" class="pwc-ad-link" id="rightGutterAdLink">
        <h4 class="pwc-title">Aspiring Women Leaders Scholarship</h4>
        <p class="pwc-subtitle">Empowering the next generation of women engineers</p>
        <ul class="pwc-bullets">
          <li>Financial grant for tuition</li>
          <li>Technology resources</li>
          <li>Executive mentorship</li>
          <li>Industry exposure</li>
        </ul>
        <div class="pwc-cta-row">
          <span class="pwc-orange-box">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M5 13l4 4L19 7"/></svg>
          </span>
          <span class="pwc-cta-text">Know more</span>
        </div>
        <div class="pwc-visual-wrap">
          <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=320&auto=format&fit=crop&q=80" alt="Woman engineer" class="pwc-woman-img">
          <div class="pwc-geom-bar"></div>
        </div>
      </a>
    </div>
  </aside>"""

# Replace the previous gutter ads
site_code = re.sub(
    r'<aside class="et-gutter-ad left-gutter-ad".*?</aside>\s*<aside class="et-gutter-ad right-gutter-ad".*?</aside>',
    pwc_left_ad,
    site_code,
    flags=re.DOTALL
)

# Update the sub-navigation bar below header to match screenshots 1, 2, and 3
subnav_html = """  <!-- Primary ET Navigation Header (White Sticky Bar with Active Red Home) -->
  <header class="hd" id="mainHeader">
    <div class="in container-fit">
      
      <!-- Left: Hamburger Menu -->
      <div class="header-left-tools">
        <button class="menu-search-btn" id="menuToggleBtn" aria-label="Toggle Menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>

      <!-- Center: Category Navigation Links (Exact Screenshot 1) -->
      <nav class="nav" id="mainNav" aria-label="ET Categories">
        <a href="#home" class="nav-link on">Home</a>
        <a href="#et-prime" class="nav-link et-prime-red"><span class="nav-red-play">▶</span> ETPrime</a>
        <a href="#markets" class="nav-link">Markets</a>
        <a href="#market-data" class="nav-link">📊 Market Data</a>
        <a href="#masterclass" class="nav-link nav-maroon">Masterclass</a>
        <a href="#news" class="nav-link">News</a>
        <a href="#industry" class="nav-link">Industry</a>
        <a href="#sme" class="nav-link">SME</a>
        <a href="#politics" class="nav-link">Politics</a>
        <a href="#wealth" class="nav-link">Wealth</a>
        <a href="#mf" class="nav-link">MF</a>
        <a href="#tech" class="nav-link">Tech</a>
        <a href="#ai" class="nav-link">AI</a>
        <a href="#world" class="nav-link">World</a>
        <a href="#opinion" class="nav-link">Opinion</a>
        <a href="#nri" class="nav-link">NRI</a>
        <a href="#panache" class="nav-link">Panache</a>
        <a href="#more" class="nav-link nav-dots" title="More Sections">⋮</a>
      </nav>

      <!-- Right: Search Button + Theme Toggle -->
      <div class="header-right-meta">
        <button class="menu-search-btn" id="searchTriggerBtn" aria-label="Search">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>
      </div>

    </div>
  </header>

  <!-- Trending / Special Topics Sub-bar (Exact Screenshot 1) -->
  <div class="et-trending-subbar">
    <div class="container-fit trending-inner">
      <span class="trend-item trend-bold">News Live!</span>
      <span class="trend-divider">|</span>
      <a href="#midterms" class="trend-item trend-red">US Midterms</a>
      <span class="trend-divider">|</span>
      <a href="#msme" class="trend-item">MSME Awards</a>
      <span class="trend-divider">|</span>
      <a href="#fokw" class="trend-item">FOKW Summit</a>
      <span class="trend-divider">|</span>
      <a href="#wealth-expo" class="trend-item trend-red">ET Wealth Expo</a>
      <span class="trend-divider">|</span>
      <a href="#ai-camp" class="trend-item">AI Winter Camp</a>
      <span class="trend-divider">|</span>
      <a href="#astrology" class="trend-item">Astrology</a>
      <span class="trend-divider">|</span>
      <a href="#biz-growth" class="trend-item">Biz Growth Summit</a>
      <span class="trend-divider">|</span>
      <a href="#advertise" class="trend-item">Advertise on ET</a>
      <span class="trend-divider">|</span>
      <span class="trend-item trend-spotlight">Spotlight ▾</span>
    </div>
  </div>"""

# Replace <header class="hd" id="mainHeader">...</header>
site_code = re.sub(
    r'<header class="hd" id="mainHeader">.*?</header>',
    subnav_html,
    site_code,
    flags=re.DOTALL
)

# Update the top stories 3-column lead to match Screenshot 1 & 2
top_grid_html = """    <!-- =====================================================================
         SECTION 1: TOP STORIES (3-Column Layout from Reference Screenshots)
         Col 1: Main Story + Stacked Headlines + ET Markets Peach Box + StockTalk
         Col 2: ET Prime Sections with Red Circular Bullets (Investment Ideas, Exclusives)
         Col 3: PwC Scholarship 300x250 Banner + Videos / Bloomberg Ad
         ===================================================================== -->
    <div class="top-lead-grid et-screenshot-grid">
      
      <!-- COLUMN 1: Lead Hero + Stacked Headlines + Markets Box + StockTalk -->
      <div class="top-col-1">
        
        <!-- Hero News: Thumbnail Left + Big Serif Headline Right -->
        <article class="lead-hero-split">
          <a href="#lead-rally" class="lead-hero-split-thumb">
            <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=500&auto=format&fit=crop&q=80" alt="IT rally" loading="eager">
          </a>
          <h2 class="lead-hero-split-title">
            <a href="#lead-rally">Rs 4 lakh cr rally, Rs 6,500 cr FII rush: Is IT staging a comeback?</a>
          </h2>
        </article>

        <!-- Stacked Headlines with Hairline Dividers -->
        <div class="lead-stacked-list">
          <div class="stacked-news-item">
            <a href="#news-bears">₹5 lakh crore wiped out as bears drag D-St down</a>
          </div>
          <div class="stacked-news-item">
            <a href="#news-ai-money">AI fear is fast becoming the new money machine</a>
          </div>
          <div class="stacked-news-item">
            <a href="#news-jio">Jio IPO: Subscribe on day 2? What you need to know</a>
          </div>
          <div class="stacked-news-item">
            <a href="#news-telecom">India gives telecom tech 24-month pass to experiment</a>
          </div>
        </div>

        <!-- ET Markets Peach Highlight Box (Exact Screenshot 1) -->
        <div class="et-markets-peach-box">
          <div class="mkt-box-header">
            <span class="et-mkt-black-badge">ET MARKETS ▶</span>
          </div>
          <div class="mkt-box-news">
            <div class="mkt-item"><a href="#swiggy">Swiggy shares slide 5% ahead of Q2 results</a></div>
            <div class="mkt-item"><a href="#mm-fin">M&amp;M Financial crashes 10% after Q2 results</a></div>
            <div class="mkt-item mkt-bullet-item">
              <span class="mkt-red-dot">⦿</span>
              <a href="#sensex-drop">Sensex falls over 300 pts, Nifty below 22,700</a>
            </div>
          </div>
        </div>

        <!-- StockTalk Live Stream Box (Exact Screenshot 1) -->
        <div class="stocktalk-box">
          <div class="st-header">
            <div class="st-brand"><span class="st-red-icon">⦿</span> <strong>StockTalk</strong></div>
            <span class="st-live-pill">🔴 LIVE</span>
          </div>
          <h3 class="st-headline">StockTalk: Get your query answered by expert</h3>
          <div class="st-video-preview">
            <div class="st-badge-overlay">Exclusively for <strong>ETPrime</strong></div>
            <img src="https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=600&auto=format&fit=crop&q=80" alt="StockTalk Video">
            <div class="st-play-btn">▶</div>
          </div>
          <div class="st-footer-action">
            <span class="st-check">✓ Get assured, accurate answers.</span>
            <a href="#join-chat" class="st-join-btn">Join the Live Session &amp; Chat Now!</a>
            <span class="st-timing">🕒 Live Every Day | 9:00 AM - 3:30 PM</span>
          </div>
        </div>

      </div>

      <!-- COLUMN 2: ETPrime Sections with Red Play Badges (Exact Screenshot 1 & 2) -->
      <div class="top-col-2">
        
        <div class="et-prime-header-strip">
          <span class="et-prime-red-dot">⦿</span>
          <strong>ETPrime :</strong> <span class="et-prime-tagline">Invest Smarter. Lead Stronger.</span>
        </div>

        <!-- Section: Investment Ideas -->
        <div class="col2-section">
          <h3 class="col2-sec-head">
            <span class="red-play-badge">▶</span>
            <a href="#invest-ideas">Investment Ideas</a>
            <span class="sec-chevron">&gt;</span>
          </h3>
          <div class="col2-news-list">
            <article class="col2-item">
              <a href="#midcaps" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=160&auto=format&fit=crop&q=80" alt="Midcaps buy">
              </a>
              <h4 class="col2-title">
                <a href="#midcaps">These mid-caps have 'strong buy' &amp; 'buy' recos and an upside potential of over 25%, according to analysts</a>
              </h4>
            </article>
            <article class="col2-item">
              <a href="#multibagger" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=160&auto=format&fit=crop&q=80" alt="Multibagger series">
              </a>
              <h4 class="col2-title">
                <a href="#multibagger">ET Prime Special Series: Multibagger or IBC - Part 81: Momentum in numbers will decide fate of this auto ancillary stock</a>
              </h4>
            </article>
            <article class="col2-item">
              <a href="#bears-water" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=160&auto=format&fit=crop&q=80" alt="Water management">
              </a>
              <h4 class="col2-title">
                <a href="#bears-water">Bears control sentiment. Structural changes control growth. 5 stocks from the water management space</a>
              </h4>
            </article>
          </div>
        </div>

        <!-- Section: Prime Exclusives -->
        <div class="col2-section">
          <h3 class="col2-sec-head">
            <span class="red-play-badge">▶</span>
            <a href="#prime-exclusives">Prime Exclusives</a>
            <span class="sec-chevron">&gt;</span>
          </h3>
          <div class="col2-news-list">
            <article class="col2-item">
              <a href="#coin-job" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=160&auto=format&fit=crop&q=80" alt="Coin job">
              </a>
              <h4 class="col2-title">
                <a href="#coin-job">Coin job to Con jobs: The business of promising more</a>
              </h4>
            </article>
            <article class="col2-item">
              <a href="#bond-yield" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=160&auto=format&fit=crop&q=80" alt="Bond yield">
              </a>
              <h4 class="col2-title">
                <a href="#bond-yield">One company, 2 words. Bond yield and CDS: Will they decide the fate of global markets?</a>
              </h4>
            </article>
          </div>
        </div>

        <!-- Section: The Economist -->
        <div class="col2-section">
          <h3 class="col2-sec-head">
            <span class="red-play-badge">▶</span>
            <a href="#the-economist">The Economist</a>
          </h3>
          <div class="col2-news-list">
            <article class="col2-item">
              <a href="#millennials" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=160&auto=format&fit=crop&q=80" alt="Millennials">
              </a>
              <h4 class="col2-title">
                <a href="#millennials">Don't feel sorry for millennials. They are living it up now</a>
              </h4>
            </article>
            <article class="col2-item">
              <a href="#machines-science" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=160&auto=format&fit=crop&q=80" alt="Machines science">
              </a>
              <h4 class="col2-title">
                <a href="#machines-science">What if the machines take over science?</a>
              </h4>
            </article>
          </div>
        </div>

        <!-- Section: Harvard Business Review Exclusives [New] -->
        <div class="col2-section">
          <h3 class="col2-sec-head">
            <span class="red-play-badge">▶</span>
            <a href="#hbr-exclusives">Harvard Business Review Exclusives</a>
            <span class="new-pill">New</span>
            <span class="sec-chevron">&gt;</span>
          </h3>
          <div class="col2-news-list">
            <article class="col2-item">
              <a href="#hbr-ai" class="col2-thumb">
                <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=160&auto=format&fit=crop&q=80" alt="HBR Research">
              </a>
              <h4 class="col2-title">
                <a href="#hbr-ai">Research: Why Some Junior Employees Work Well with AI—and Others Don't</a>
              </h4>
            </article>
          </div>
        </div>

      </div>

      <!-- COLUMN 3: PwC Scholarship 300x250 Banner + Videos + Bloomberg AI Banner -->
      <aside class="top-col-3">
        
        <!-- PwC Aspiring Women Leaders Scholarship 300x250 Banner Ad (Exact Screenshot 1) -->
        <div class="pwc-rect-ad-card" id="pwcRectAd">
          <div class="pwc-rect-brand">
            <div class="pwc-logo-wrap">
              <span class="pwc-squares"><span class="sq1"></span><span class="sq2"></span><span class="sq3"></span><span class="sq4"></span></span>
              <span class="pwc-text">pwc</span>
            </div>
          </div>
          <h3 class="pwc-rect-title">Aspiring Women Leaders Scholarship</h3>
          <p class="pwc-rect-subtitle">An annual scholarship for women in engineering</p>
          <div class="pwc-rect-cta-row">
            <span class="pwc-orange-box">
              <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M5 13l4 4L19 7"/></svg>
            </span>
            <span class="pwc-cta-text">Know more</span>
          </div>
          <div class="pwc-rect-img-wrap">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500&auto=format&fit=crop&q=80" alt="PwC Aspiring Women Leaders Scholarship" class="pwc-rect-img">
            <div class="pwc-rect-bar"></div>
          </div>
        </div>

        <!-- Videos Section Header & Video Player Ad (Exact Screenshot 1 & 2) -->
        <div class="videos-side-widget">
          <div class="vsw-head">
            <h3>Videos</h3>
          </div>
          <div class="vsw-video-box">
            <span class="vsw-ad-label">Advertisement</span>
            <div class="vsw-player-wrap">
              <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=500&auto=format&fit=crop&q=80" alt="Hero Homes">
              <div class="vsw-overlay-brand">Hero Homes</div>
              <div class="vsw-controls-bar">
                <span>▶ 00:04 / 03:52</span>
                <span class="vsw-sound">🔊</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Bloomberg "Seize the Momentum" AI Insights Ad (Exact Screenshot 2) -->
        <div class="bloomberg-ad-card">
          <div class="bb-img-wrap">
            <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=500&auto=format&fit=crop&q=80" alt="Seize the momentum">
            <div class="bb-headline-overlay">
              <h2>Seize the momentum.</h2>
              <p>INDIA SEMICONDUCTOR-RELATED COMPANIES REVENUE 2020-2026</p>
            </div>
          </div>
          <div class="bb-footer-row">
            <span>Access AI-driven insights on India's top industries.</span>
            <strong>Bloomberg</strong>
          </div>
        </div>

        <!-- ET HR Excellence Awards (Exact Screenshot 3) -->
        <div class="hr-awards-card">
          <div class="hr-badge-row">
            <span class="hr-gold-badge">🏆 THE ECONOMIC TIMES</span>
            <strong>HR Excellence AWARDS</strong>
          </div>
          <h4 class="hr-title">Where People Excellence Becomes Business Impact</h4>
          <div class="hr-tags-row">
            <span>30+ Categories</span>
            <span>3 Tracks</span>
            <span>Industry Recognition</span>
          </div>
          <a href="#nominate" class="hr-nominate-btn">Nominate Now</a>
        </div>

      </aside>

    </div>"""

# Replace top-lead-grid in site_code
site_code = re.sub(
    r'<div class="top-lead-grid".*?<!-- =====================================================================\s*SECTION 2',
    top_grid_html + "\n\n    <!-- =====================================================================\n         SECTION 2",
    site_code,
    flags=re.DOTALL
)

with open(BUILD_SITE_FILE, "w", encoding="utf-8") as f:
    f.write(site_code)
print("[build_site.py] Successfully updated HTML template with ET screenshot structure!")

# ==============================================================================
# 2. UPDATE REFINE_STYLES.PY WITH EXACT CSS
# ==============================================================================
with open(REFINE_STYLES_FILE, "r", encoding="utf-8") as f:
    refine_code = f.read()

new_styles_block = """/* ==========================================================================
   PwC ASPIRING WOMEN LEADERS SCHOLARSHIP TAKEOVER ADS (Reference Screenshots)
   ========================================================================== */
.pwc-gutter-ad {
  position: fixed;
  top: 130px;
  width: 160px;
  z-index: 85;
  display: none;
}

@media (min-width: 1620px) {
  .pwc-gutter-ad {
    display: block;
  }
  .left-gutter-ad {
    left: calc(50% - (var(--container-max) / 2) - 172px);
  }
  .right-gutter-ad {
    right: calc(50% - (var(--container-max) / 2) - 172px);
  }
}

@media (min-width: 1360px) and (max-width: 1619px) {
  .pwc-gutter-ad {
    display: block;
    width: 135px;
  }
  .left-gutter-ad {
    left: 8px;
  }
  .right-gutter-ad {
    right: 8px;
  }
}

.pwc-sticky-card {
  background: linear-gradient(180deg, #fff2ee 0%, #ffffff 85%);
  border: 1px solid #ffd8cc;
  border-radius: 4px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  padding: 10px 10px 0;
  display: flex;
  flex-direction: column;
}

:root[data-theme="dark"] .pwc-sticky-card {
  background: linear-gradient(180deg, #2a1b18 0%, #151d28 85%);
  border-color: #4a2822;
}

.pwc-top-brand {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.pwc-logo-wrap {
  display: flex;
  align-items: center;
  gap: 5px;
}

.pwc-squares {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5px;
  width: 14px;
  height: 14px;
}

.pwc-squares span {
  display: block;
  border-radius: 1px;
}

.sq1 { background: #d04a02; }
.sq2 { background: #eb8c00; }
.sq3 { background: #e0301e; }
.sq4 { background: #404041; }

.pwc-text {
  font-family: var(--font-sans);
  font-size: 16px;
  font-weight: 800;
  color: #2d2d2d;
  letter-spacing: -0.03em;
}

:root[data-theme="dark"] .pwc-text {
  color: #ffffff;
}

.pwc-ad-link {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
}

.pwc-title {
  font-family: var(--font-serif);
  font-size: 13px;
  font-weight: 700;
  line-height: 1.25;
  color: #111111;
  margin: 0 0 6px;
}

:root[data-theme="dark"] .pwc-title {
  color: #ffffff;
}

.pwc-subtitle {
  font-family: var(--font-sans);
  font-size: 9.5px;
  line-height: 1.35;
  color: #333333;
  font-weight: 500;
  margin: 0 0 8px;
}

:root[data-theme="dark"] .pwc-subtitle {
  color: #cbd5e1;
}

.pwc-bullets {
  list-style: none;
  padding: 0;
  margin: 0 0 10px;
}

.pwc-bullets li {
  position: relative;
  padding-left: 10px;
  font-size: 9px;
  line-height: 1.4;
  color: #222222;
}

:root[data-theme="dark"] .pwc-bullets li {
  color: #94a3b8;
}

.pwc-bullets li::before {
  content: "•";
  position: absolute;
  left: 0;
  color: #111111;
  font-weight: bold;
}

.pwc-cta-row {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 8px;
}

.pwc-orange-box {
  background: #d04a02;
  color: #ffffff;
  width: 16px;
  height: 16px;
  border-radius: 2px;
  display: grid;
  place-items: center;
}

.pwc-cta-text {
  font-size: 10px;
  font-weight: 700;
  color: #111111;
}

:root[data-theme="dark"] .pwc-cta-text {
  color: #ffffff;
}

.pwc-visual-wrap {
  position: relative;
  width: 100%;
  margin-top: 4px;
}

.pwc-woman-img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
  border-radius: 2px 2px 0 0;
}

.pwc-geom-bar {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 60%;
  height: 8px;
  background: #eb8c00;
  transform: skewX(-25deg);
}

/* ==========================================================================
   SUB-NAVIGATION & TRENDING BAR (Exact Screenshots)
   ========================================================================== */
.et-trending-subbar {
  background: #ffffff;
  border-bottom: 1px solid #ebebeb;
  padding: 6px 0;
  font-size: 11.5px;
  width: 100%;
}

:root[data-theme="dark"] .et-trending-subbar {
  background: #111827;
  border-bottom-color: #1f2937;
}

.trending-inner {
  display: flex;
  align-items: center;
  gap: 12px;
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none;
}

.trending-inner::-webkit-scrollbar {
  display: none;
}

.trend-item {
  color: #4b5563;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.15s ease;
}

.trend-item:hover {
  color: var(--ac);
}

.trend-bold {
  font-weight: 700;
  color: #111111;
}

.trend-red {
  color: var(--ac);
  font-weight: 700;
}

.trend-divider {
  color: #d1d5db;
  font-size: 10px;
}

.trend-spotlight {
  font-weight: 700;
  color: #111111;
  cursor: pointer;
}

.nav-red-play {
  color: var(--ac);
  font-size: 10px;
  margin-right: 2px;
}

.nav-maroon {
  color: #831843 !important;
  font-weight: 700;
}

.nav-dots {
  font-size: 16px;
  padding: 0 4px;
}

/* ==========================================================================
   TOP STORIES 3-COLUMN LAYOUT (Exact Screenshots 1, 2, 3)
   ========================================================================== */
.et-screenshot-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.45fr) minmax(0, 1.45fr) 300px;
  gap: 20px;
  align-items: start;
  margin-bottom: 28px;
  width: 100%;
  background: #ffffff;
  border: 1px solid #ebebeb;
  border-radius: var(--radius-md);
  padding: 18px;
}

:root[data-theme="dark"] .et-screenshot-grid {
  background: var(--sf);
  border-color: var(--ln);
}

/* Column 1 */
.top-col-1 {
  display: flex;
  flex-direction: column;
  border-right: 1px solid #ebebeb;
  padding-right: 18px;
}

:root[data-theme="dark"] .top-col-1 {
  border-color: var(--ln);
}

.lead-hero-split {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  margin-bottom: 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid #ebebeb;
}

:root[data-theme="dark"] .lead-hero-split {
  border-color: var(--ln);
}

.lead-hero-split-thumb {
  width: 140px;
  aspect-ratio: 16/10;
  border-radius: var(--radius-sm);
  overflow: hidden;
  flex-shrink: 0;
  background: #0c1a2e;
}

.lead-hero-split-title {
  font-family: var(--font-serif);
  font-size: 18px;
  font-weight: 700;
  line-height: 1.25;
  color: #111111;
  margin: 0;
}

:root[data-theme="dark"] .lead-hero-split-title {
  color: #ffffff;
}

.lead-hero-split-title a:hover {
  color: var(--ac);
}

.lead-stacked-list {
  display: flex;
  flex-direction: column;
  margin-bottom: 16px;
}

.stacked-news-item {
  padding: 8px 0;
  border-bottom: 1px solid #eeeeee;
  font-family: var(--font-serif);
  font-size: 14.5px;
  font-weight: 600;
  line-height: 1.34;
  color: #111111;
}

:root[data-theme="dark"] .stacked-news-item {
  color: #f3f4f6;
  border-color: var(--ln-subtle);
}

.stacked-news-item a:hover {
  color: var(--ac);
}

/* ET Markets Peach Highlight Box (Exact Screenshot 1) */
.et-markets-peach-box {
  background: #fff5f0;
  border: 1px solid #ffd8cc;
  border-radius: 4px;
  padding: 12px 14px;
  margin-bottom: 18px;
}

:root[data-theme="dark"] .et-markets-peach-box {
  background: #251614;
  border-color: #4d2820;
}

.et-mkt-black-badge {
  display: inline-block;
  background: #000000;
  color: #ffffff;
  font-size: 9.5px;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 2px;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}

.mkt-box-news {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.mkt-item {
  font-family: var(--font-serif);
  font-size: 13.5px;
  font-weight: 600;
  color: #111111;
  line-height: 1.3;
}

:root[data-theme="dark"] .mkt-item {
  color: #f3f4f6;
}

.mkt-item a:hover {
  color: var(--ac);
}

.mkt-bullet-item {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.mkt-red-dot {
  color: var(--ac);
  font-size: 12px;
}

/* StockTalk Box */
.stocktalk-box {
  border: 1px solid #ffd8cc;
  background: #fffdfb;
  border-radius: 4px;
  padding: 14px;
}

:root[data-theme="dark"] .stocktalk-box {
  background: #191b22;
  border-color: #3b2832;
}

.st-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.st-brand {
  font-size: 14px;
  font-weight: 800;
  color: var(--ac);
  display: flex;
  align-items: center;
  gap: 4px;
}

.st-live-pill {
  background: var(--ac);
  color: #ffffff;
  font-size: 9px;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 2px;
}

.st-headline {
  font-family: var(--font-serif);
  font-size: 15px;
  font-weight: 700;
  line-height: 1.3;
  margin: 0 0 10px;
}

.st-video-preview {
  position: relative;
  aspect-ratio: 16/9;
  border-radius: 4px;
  overflow: hidden;
  background: #000;
  margin-bottom: 10px;
}

.st-video-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.85;
}

.st-badge-overlay {
  position: absolute;
  top: 8px;
  left: 8px;
  background: rgba(0, 0, 0, 0.7);
  color: #ffffff;
  font-size: 9.5px;
  padding: 2px 6px;
  border-radius: 2px;
}

.st-play-btn {
  position: absolute;
  inset: 0;
  margin: auto;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(237, 25, 59, 0.9);
  color: #ffffff;
  display: grid;
  place-items: center;
  font-size: 16px;
  box-shadow: 0 4px 12px rgba(237, 25, 59, 0.5);
}

.st-footer-action {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.st-check {
  font-size: 11px;
  color: #166534;
  font-weight: 600;
}

.st-join-btn {
  background: var(--ac);
  color: #ffffff !important;
  font-size: 12px;
  font-weight: 700;
  padding: 8px;
  border-radius: 3px;
  text-align: center;
  text-decoration: none;
  transition: background 0.15s ease;
}

.st-join-btn:hover {
  background: var(--ac-hover);
}

.st-timing {
  font-size: 9.5px;
  color: var(--mu);
  text-align: center;
}

/* Column 2 */
.top-col-2 {
  display: flex;
  flex-direction: column;
  border-right: 1px solid #ebebeb;
  padding-right: 18px;
}

:root[data-theme="dark"] .top-col-2 {
  border-color: var(--ln);
}

.et-prime-header-strip {
  display: flex;
  align-items: baseline;
  gap: 5px;
  font-size: 12px;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--ac);
  margin-bottom: 12px;
}

.et-prime-red-dot {
  color: var(--ac);
}

.et-prime-tagline {
  color: #64748b;
  font-size: 11px;
}

.col2-section {
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f1f1f1;
}

:root[data-theme="dark"] .col2-section {
  border-color: var(--ln-subtle);
}

.col2-sec-head {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-serif);
  font-size: 14.5px;
  font-weight: 700;
  color: #111111;
  margin: 0 0 10px;
}

:root[data-theme="dark"] .col2-sec-head {
  color: #ffffff;
}

.red-play-badge {
  background: var(--ac);
  color: #ffffff;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  display: inline-grid;
  place-items: center;
  font-size: 7px;
  flex-shrink: 0;
}

.sec-chevron {
  color: var(--ac);
  font-weight: bold;
}

.new-pill {
  background: var(--ac);
  color: #ffffff;
  font-size: 8px;
  font-weight: 800;
  padding: 1px 4px;
  border-radius: 2px;
  text-transform: uppercase;
}

.col2-news-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.col2-item {
  display: flex;
  gap: 10px;
  align-items: flex-start;
}

.col2-thumb {
  width: 70px;
  aspect-ratio: 4/3;
  border-radius: 2px;
  overflow: hidden;
  flex-shrink: 0;
  background: #f1f5f9;
}

.col2-title {
  font-family: var(--font-serif);
  font-size: 13px;
  font-weight: 600;
  line-height: 1.34;
  color: #111111;
  margin: 0;
}

:root[data-theme="dark"] .col2-title {
  color: #f3f4f6;
}

.col2-title a:hover {
  color: var(--ac);
}

/* Column 3 */
.top-col-3 {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

/* PwC 300x250 Rectangle Ad Card (Exact Screenshot 1) */
.pwc-rect-ad-card {
  background: linear-gradient(180deg, #fff2ee 0%, #ffffff 85%);
  border: 1px solid #ffd8cc;
  border-radius: 4px;
  padding: 14px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

:root[data-theme="dark"] .pwc-rect-ad-card {
  background: linear-gradient(180deg, #2a1b18 0%, #151d28 85%);
  border-color: #4a2822;
}

.pwc-rect-brand {
  margin-bottom: 8px;
}

.pwc-rect-title {
  font-family: var(--font-serif);
  font-size: 16px;
  font-weight: 700;
  line-height: 1.25;
  color: #111111;
  margin: 0 0 6px;
}

:root[data-theme="dark"] .pwc-rect-title {
  color: #ffffff;
}

.pwc-rect-subtitle {
  font-family: var(--font-sans);
  font-size: 11px;
  color: #4b5563;
  line-height: 1.3;
  margin: 0 0 10px;
}

:root[data-theme="dark"] .pwc-rect-subtitle {
  color: #cbd5e1;
}

.pwc-rect-cta-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 10px;
}

.pwc-rect-img-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 16/10;
  border-radius: 3px;
  overflow: hidden;
  background: #f1f5f9;
}

.pwc-rect-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.pwc-rect-bar {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 50%;
  height: 10px;
  background: #eb8c00;
  transform: skewX(-25deg);
}

/* Videos Side Widget */
.videos-side-widget {
  display: flex;
  flex-direction: column;
}

.vsw-head h3 {
  font-family: var(--font-sans);
  font-size: 16px;
  font-weight: 800;
  margin: 0 0 8px;
}

.vsw-video-box {
  background: #000;
  color: #fff;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}

.vsw-ad-label {
  display: block;
  background: #111;
  color: #aaa;
  font-size: 8.5px;
  padding: 3px 8px;
  text-align: center;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.vsw-player-wrap {
  position: relative;
  aspect-ratio: 16/9;
}

.vsw-player-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.vsw-overlay-brand {
  position: absolute;
  top: 8px;
  left: 8px;
  background: rgba(0, 0, 0, 0.65);
  padding: 2px 6px;
  border-radius: 2px;
  font-size: 10px;
  font-weight: 700;
}

.vsw-controls-bar {
  position: absolute;
  bottom: 6px;
  left: 8px;
  right: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 9.5px;
  background: rgba(0, 0, 0, 0.7);
  padding: 3px 6px;
  border-radius: 2px;
}

/* Bloomberg Ad Card (Exact Screenshot 2) */
.bloomberg-ad-card {
  background: #000000;
  color: #ffffff;
  border-radius: 4px;
  overflow: hidden;
}

.bb-img-wrap {
  position: relative;
  aspect-ratio: 16/10;
}

.bb-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.8;
}

.bb-headline-overlay {
  position: absolute;
  inset: 0;
  padding: 14px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: linear-gradient(180deg, transparent 20%, rgba(0, 0, 0, 0.9) 100%);
}

.bb-headline-overlay h2 {
  font-size: 18px;
  font-weight: 800;
  margin: 0;
  line-height: 1.2;
}

.bb-headline-overlay p {
  font-size: 8px;
  color: #94a3b8;
  letter-spacing: 0.05em;
  margin: 4px 0 0;
}

.bb-footer-row {
  padding: 8px 12px;
  font-size: 9.5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #111;
  color: #cbd5e1;
}

/* HR Excellence Awards Card (Exact Screenshot 3) */
.hr-awards-card {
  background: linear-gradient(135deg, #fef9ee 0%, #fff2d8 100%);
  border: 1px solid #fed7aa;
  border-radius: 4px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

:root[data-theme="dark"] .hr-awards-card {
  background: linear-gradient(135deg, #2a2010 0%, #1c1508 100%);
  border-color: #63431a;
}

.hr-badge-row {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}

.hr-gold-badge {
  font-size: 8.5px;
  color: #92400e;
  font-weight: 800;
}

.hr-badge-row strong {
  font-size: 13px;
  color: #78350f;
}

:root[data-theme="dark"] .hr-badge-row strong {
  color: #fde68a;
}

.hr-title {
  font-family: var(--font-serif);
  font-size: 14.5px;
  font-weight: 700;
  line-height: 1.3;
  color: #111111;
  margin: 0;
}

:root[data-theme="dark"] .hr-title {
  color: #ffffff;
}

.hr-tags-row {
  display: flex;
  gap: 6px;
  font-size: 8px;
  font-weight: 700;
  color: #92400e;
}

.hr-tags-row span {
  background: rgba(217, 119, 6, 0.15);
  padding: 2px 5px;
  border-radius: 2px;
}

.hr-nominate-btn {
  background: #7c2d12;
  color: #ffffff !important;
  font-size: 11px;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 3px;
  text-align: center;
  text-decoration: none;
  align-self: flex-start;
  margin-top: 4px;
}
"""

# Append new styles to refine_styles.py
refine_code = refine_code + "\n\n" + new_styles_block

with open(REFINE_STYLES_FILE, "w", encoding="utf-8") as f:
    f.write(refine_code)
print("[refine_styles.py] Added screenshot-matching CSS classes and layout rules.")

# ==============================================================================
# 3. UPDATE APP.JS WITH NEW ACTIONS
# ==============================================================================
with open(APP_JS_FILE, "r", encoding="utf-8") as f:
    js_code = f.read()

if 'initScreenshotAds()' not in js_code:
    js_code = js_code.replace(
        '  initGutterAds();',
        '  initGutterAds();\n  initScreenshotAds();'
    )
    
    extra_js = """
/* ==========================================================================
   PwC & BLOOMBERG ADS CONTROLLER
   ========================================================================== */
function initScreenshotAds() {
  const pwcLinks = document.querySelectorAll('#leftGutterAdLink, #rightGutterAdLink, #pwcRectAd');
  pwcLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('PwC: Aspiring Women Leaders Scholarship application opened.');
    });
  });

  const hrBtn = document.querySelector('.hr-nominate-btn');
  if (hrBtn) {
    hrBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('ET HR Excellence Awards 2026: Nomination portal opened.');
    });
  }
}
"""
    js_code += "\n" + extra_js
    print("[app.js] Added initScreenshotAds implementation.")

with open(APP_JS_FILE, "w", encoding="utf-8") as f:
    f.write(js_code)

print("[apply_screenshot_reference.py] All files updated successfully!")
