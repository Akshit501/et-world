#!/usr/bin/env python3
"""
ET World Site Builder & Layout Refiner
Ensures exact Economic Times World branding, reference layout adherence,
proper margins, and fit-to-border alignment.
"""

import os
import sys

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>The Economic Times World – Global Business, Finance, Politics &amp; ET World Summit 2026</title>
  <meta name="description" content="The Economic Times World Edition: Breaking global business intelligence, ET World Summit 2026 LIVE, international trade, geopolitics, markets, Offbeat, Opinion, Videos and Sports.">
  <meta name="theme-color" content="#0c233c">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='6' fill='%23e0262c'/><text x='50' y='68' font-family='Georgia,serif' font-size='56' font-weight='bold' fill='white' text-anchor='middle'>ET</text></svg>">

  <!-- Google Fonts: Official Economic Times Typography (Montserrat & Faustina) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Faustina:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="styles.css?v=2.2">
</head>
<body>

  <!-- Channel Navigation Bar (ET Network Top Strip) -->
    <!-- =====================================================================
       LEFT & RIGHT GUTTER SKYSCRAPER ADS (Fills Left & Right Empty Spaces)
       ===================================================================== -->
    <!-- =====================================================================
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
  </aside>

  <!-- =====================================================================
       TIER 1: BENCHMARKS LIVE, FEATURED FUNDS & PILL SEARCH BAR (Reference image copy 2.png)
       ===================================================================== -->
  <div class="et-top-benchmarks-strip" id="etTopBenchmarksStrip">
    <div class="container-fit top-benchmarks-inner">
      <div class="benchmarks-group">
        <!-- Sensex Benchmark Live -->
        <a href="#markets" class="bm-block bm-sensex" id="topSensexBenchmark" title="View Sensex Benchmark">
          <div class="bm-label-row">
            <span class="bm-label-title">BENCHMARKS</span>
            <span class="bm-live-badge">LIVE</span>
          </div>
          <div class="bm-data-row">
            <span class="bm-name">Sensex</span>
            <span class="bm-val">72,792.48</span>
            <span class="bm-change down"><span class="bm-arr">↓</span>-456.9</span>
          </div>
        </a>

        <div class="bm-v-divider"></div>

        <!-- Featured Funds 5Y Return UTI -->
        <div class="bm-block bm-funds">
          <div class="bm-label-row">
            <span class="bm-label-title">FEATURED FUNDS</span>
            <span class="bm-stars" aria-label="5 stars">★★★★★</span>
            <span class="bm-label-sub">5Y RETURN</span>
          </div>
          <div class="bm-data-row">
            <a href="#mutual-funds" class="bm-fund-name" id="topFundLink" title="UTI Aggressive Hybrid Fund">UTI Aggressive Hybrid ...</a>
            <span class="bm-change up"><span class="bm-arr">↑</span> 8.69 %</span>
            <button class="bm-invest-btn" id="fundInvestBtn" title="Invest in UTI Aggressive Hybrid Fund">INVEST NOW</button>
          </div>
        </div>
      </div>

      <!-- Right Search Pill Bar -->
      <div class="top-search-col">
        <div class="top-search-pill" id="topSearchPill">
          <svg class="search-red-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#ed193b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" id="topSearchInput" class="search-pill-input" placeholder="Search Stock Quotes, News, Mutual Funds and more" autocomplete="off" aria-label="Search Stock Quotes, News, Mutual Funds and more">
        </div>
        <button class="top-theme-toggle" id="themeToggleBtn" title="Toggle Theme" aria-label="Toggle Theme">
          <span class="theme-icon light-icon">☀️</span>
          <span class="theme-icon dark-icon">🌙</span>
        </button>
      </div>
    </div>
  </div>

  <!-- =====================================================================
       TIER 2: THE ECONOMIC TIMES MASTHEAD (Reference image copy 2.png)
       ===================================================================== -->
  <header class="et-masthead-section" id="etOfficialMasthead">
    <div class="container-fit masthead-container">
      
      <!-- Left: Balanced Empty Space -->
      <div class="masthead-left-spacer"></div>

      <!-- Center: Logo & Edition / Date Subtitle -->
      <div class="masthead-center">
        <a href="/" class="et-main-brand" aria-label="The Economic Times">
          <img src="image.png" alt="The Economic Times" class="et-official-logo-img">
        </a>
        <div class="masthead-sub-meta">
          <span class="meta-edition-dropdown" id="editionDropdownBtn">
            English Edition <span class="caret-down">▾</span>
          </span>
          <span class="meta-divider">|</span>
          <span class="meta-datetime" id="mastheadDateTime">23 October, 2026, 11:16 AM IST</span>
          <span class="meta-divider">|</span>
          <a href="#epaper" class="meta-epaper-link">Today's ePaper</a>
        </div>
      </div>

      <!-- Right: Action Buttons & Mega Festive Sale -->
      <div class="masthead-right-actions">
        <div class="masthead-top-actions">
          <button type="button" class="btn-et-outline" id="mastheadWatchlistBtn" style="white-space: nowrap;">My Watchlist</button>
          <button type="button" class="btn-et-outline" id="mastheadSubscribeBtn" style="white-space: nowrap;">Subscribe</button>
          <button type="button" class="btn-et-signin" id="mastheadSignInBtn" style="white-space: nowrap; background: transparent; border: none; cursor: pointer;">Sign In</button>
        </div>
        <div class="festive-sale-strip">
          <a href="#festive-sale" class="festive-sale-link" id="festiveSaleLink">
            <span class="sale-festive-text">Mega Festive Sale</span> <span class="festive-arrow">↗</span>
          </a>
        </div>
      </div>

    </div>
  </header>

  <!-- =====================================================================
       TIER 3: PEACH CATEGORY NAVIGATION BAR (Reference image copy 2.png)
       ===================================================================== -->
  <nav class="et-peach-catbar" id="etCategoryNav" aria-label="Primary Navigation">
    <div class="container-fit catbar-inner">
      <button class="cat-hamburger-btn" id="menuToggleBtn" aria-label="Open Navigation Menu" title="Browse All Sections">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>

                  <div class="catbar-links-scroll" id="catbarLinksScroll">
        <a href="/" class="cat-item cat-home-tab active" title="ET Home">Home</a>
        <a href="#top-world-stories" class="cat-item" title="Top Stories">Top Stories</a>
        <a href="#world-briefing" class="cat-item" title="World Briefing">Briefing</a>
        <a href="#geopolitics-relations" class="cat-item" title="Geopolitics">Geopolitics</a>
        <a href="#crypto-news" class="cat-item" title="Cryptocurrency News">Crypto</a>
        <a href="#market-data" class="cat-item cat-market-data-btn" id="catMarketDataBtn" title="Market Data"><span class="cat-chart-icon">📊</span>Market Data</a>
        <a href="#masterclass" class="cat-item cat-masterclass-tab" id="catMasterclassBtn" title="ET Masterclass Executive Learning">Masterclass</a>
        <a href="#international-business" class="cat-item" title="Business">Business</a>
        <a href="#us-uk-news" class="cat-item" title="US &amp; UK">US &amp; UK</a>
        <a href="#global-tech-ai" class="cat-item" title="Tech &amp; AI">Tech &amp; AI</a>
        <a href="#science-space" class="cat-item" title="Science &amp; Space">Science</a>
        <a href="#environment-climate" class="cat-item" title="Environment">Climate</a>
        <a href="#global-real-estate" class="cat-item" title="Real Estate">Real Estate</a>
        <a href="#people-leadership-panache" class="cat-item" title="Panache">Panache</a>
        <a href="#global-health" class="cat-item" title="Global Health">Health</a>
        <a href="#world-sports" class="cat-item" title="World Sports">Sports</a>
        <a href="#podcasts-section" class="cat-item" title="Featured Series: Podcasts">Podcasts</a>
      </div>

      <button class="cat-more-btn" id="catMoreBtn" aria-label="More categories" title="More categories">⋮</button>
    </div>
  </nav>

  <!-- =====================================================================
       TIER 4: TRENDING TOPICS SUB-NAVIGATION STRIP (Reference image copy 2.png)
       ===================================================================== -->
  <div class="et-trending-subbar" aria-label="Trending Topics">
    <div class="container-fit trending-inner">
      <div class="trending-scroll" id="trendingScroll">
        <a href="#news-live" class="trend-item trend-live" title="Live Coverage">News Live!</a>
        <a href="#us-midterms" class="trend-item" title="US Midterms Special Coverage"><span class="trend-bold">US</span> <span class="trend-red">Midterms</span></a>
        <a href="#msme-awards" class="trend-item" title="MSME Awards 2026">MSME Awards</a>
        <a href="#fokw-summit" class="trend-item" title="Future of Knowledge Work Summit">FOKW Summit</a>
        <a href="#et-wealth-expo" class="trend-item" title="ET Wealth Investment Expo"><span class="trend-bold">ET</span> <span class="trend-red">Wealth Expo</span></a>
        <a href="#ai-winter-camp" class="trend-item" title="AI Winter Camp 2026">AI Winter Camp</a>
        <a href="#astrology" class="trend-item" title="Weekly Horoscopes & Astrology">Astrology</a>
        <a href="#biz-growth" class="trend-item" title="Business Growth Summit">Biz Growth Summit</a>
        <a href="#advertise" class="trend-item" title="Advertise with The Economic Times">Advertise on ET</a>
        <div class="trend-item trend-spotlight-dropdown" id="spotlightDropdownBtn" tabindex="0" role="button" aria-haspopup="true" aria-expanded="false" title="Spotlight Initiatives">
          Spotlight <span class="spotlight-caret">▾</span>
          <div class="spotlight-menu" id="spotlightMenu">
            <a href="#spotlight-gbs">ET Global Business Summit</a>
            <a href="#spotlight-40u40">ET 40 Under Forty</a>
            <a href="#spotlight-poi">The Power of Ideas</a>
            <a href="#spotlight-women">Women Ahead Awards</a>
          </div>
        </div>
      </div>
    </div>
  </div>



  <!-- Mobile Drawer Menu -->
  <div class="mobile-drawer-overlay" id="drawerOverlay"></div>
  <aside class="mobile-drawer" id="mobileDrawer">
    <div class="drawer-header">
      <div class="brand-logo small">
        <span class="et-badge">ET</span>
        <span class="logo-world">WORLD</span>
      </div>
      <button class="drawer-close-btn" id="drawerCloseBtn">&times;</button>
    </div>
    <div class="drawer-body">
      <div class="drawer-search">
        <input type="text" placeholder="Search news, topics, companies…" id="drawerSearchInput">
      </div>
                  <h4 class="drawer-label">World Sections</h4>
      <div class="drawer-links">
        <a href="#top-world-stories" class="active">1. Top World Stories</a>
        <a href="#world-briefing">2. World Briefing / Latest Updates</a>
        <a href="#geopolitics-relations">3. Geopolitics &amp; International Relations</a>
        <a href="#crypto-news">4. Cryptocurrency News Hub</a>
        <a href="#international-business">5. International Business</a>
        <a href="#us-uk-news">6. US &amp; UK News</a>
        <a href="#global-tech-ai">7. Global Tech &amp; AI</a>
        <a href="#science-space">8. Science &amp; Space</a>
        <a href="#environment-climate">9. Environment &amp; Climate</a>
        <a href="#global-real-estate">10. Global Real Estate</a>
        <a href="#people-leadership-panache">11. Panache &amp; Leadership</a>
        <a href="#global-health">12. Global Health</a>
        <a href="#world-sports">13. World Sports</a>
        <a href="#podcasts-section">14. Featured Series: Podcasts</a>
      </div>
    </div>
  </aside>

  <!-- Main Container: Centered with Proper Margin and Fit to Border -->
  <main id="app" class="main-content container-fit">
    <!-- =====================================================================
         SECTION 1: TOP WORLD STORIES
         Hero story, 3–4 supporting headlines, major breaking news, and ad card
         ===================================================================== -->
    <section class="portal-section" id="top-world-stories">
      <div class="sec-heading">
        <h2><a href="#top-world-stories">Top World Stories <span class="sec-chevron">›</span></a></h2>
      </div>
      <div class="top-lead-grid">
        
        <!-- Column 1 (Left): Hero Story -->
        <article class="top-hero-card">
          <a href="#lead-hero" class="top-hero-media">
            <img src="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=900&auto=format&fit=crop&q=80" alt="Global Trade and Financial Corridors" loading="eager">
            <div class="hero-live-pill">● ET WORLD EXCLUSIVE</div>
          </a>
          <h2 class="top-hero-title">
            <a href="#lead-hero">Global Trade &amp; Capital Corridors: How Emerging Blocs Are Rewiring Cross-Border Finance</a>
          </h2>
          <p class="top-hero-excerpt">
            As central banks recalibrate monetary trajectories and sovereign trade routes realign across Asia, Europe, and the Americas, international institutions are establishing resilient financial architecture for a multipolar global economy.
          </p>
        </article>

        <!-- Column 2 (Middle): 4 Supporting Headlines with Left Thumbnails -->
        <div class="top-list-column">
          
          <article class="lead-list-item">
            <a href="#lead-1" class="lead-thumb">
              <img src="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=500&auto=format&fit=crop&q=80" alt="India US trade deal" loading="lazy">
            </a>
            <h3 class="lead-item-title">
              <a href="#lead-1">Trump Says "Much Different Kind" Of India-US Strategic Trade Deal Is "Pretty Close"</a>
            </h3>
          </article>

          <article class="lead-list-item">
            <a href="#lead-2" class="lead-thumb">
              <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=300&auto=format&fit=crop&q=80" alt="Ukraine war migration" loading="lazy">
            </a>
            <h3 class="lead-item-title">
              <a href="#lead-2">How Ukraine Conflict Triggered Europe's Largest Industrial Workforce Reallocation</a>
            </h3>
          </article>

          <article class="lead-list-item">
            <a href="#lead-3" class="lead-thumb">
              <img src="https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=300&auto=format&fit=crop&q=80" alt="Macron diplomatic summit" loading="lazy">
            </a>
            <h3 class="lead-item-title">
              <a href="#lead-3">'Sovereign Defense Cannot Wait': European Leaders Unveil Joint Military Procurement Blueprint</a>
            </h3>
          </article>

          <article class="lead-list-item">
            <a href="#lead-4" class="lead-thumb">
              <img src="https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=300&auto=format&fit=crop&q=80" alt="Satellite telemetry security" loading="lazy">
            </a>
            <h3 class="lead-item-title">
              <a href="#lead-4">Commercial Space Constellations Deploy Quantum Key Encryption For Maritime Corridors</a>
            </h3>
          </article>

        </div>

        <!-- Column 3 (Right): Sponsored Card + Featured Analysis Card -->
        <aside class="top-side-column">
          
          <div class="side-ad-box pwc-mini-ad">
            <div class="side-ad-header">
              <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150&auto=format&fit=crop&q=80" alt="PwC Scholarship" class="ad-small-thumb">
              <div class="ad-text-wrap">
                <strong>PwC: Aspiring Women Leaders Scholarship</strong>
                <div class="ad-meta-row">
                  <span class="ad-sponsored-tag">PwC | Sponsored</span>
                  <span class="ad-cta-btn">Know More →</span>
                </div>
              </div>
            </div>
          </div>

          <article class="side-featured-card">
            <a href="#featured-lux" class="side-featured-media">
              <img src="https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?w=500&auto=format&fit=crop&q=80" alt="Global Luxury Supply Chain" loading="lazy">
            </a>
            <span class="featured-red-badge">FEATURED ANALYSIS</span>
            <h3 class="side-featured-title">
              <a href="#featured-lux">Global Luxury Houses Overhaul Distribution Lines To Combat Secondary Market Infiltration</a>
            </h3>
          </article>

        </aside>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 2: WORLD BRIEFING / LATEST UPDATES
         Chronological headlines and live updates stream
         ===================================================================== -->
    <section class="portal-section briefing-section" id="world-briefing">
      <div class="sec-heading">
        <h2><a href="#world-briefing">World Briefing / Latest Updates <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">CHRONOLOGICAL LIVE WIRE &amp; REAL-TIME INTELLIGENCE</span>
      </div>

      <div class="briefing-live-status-bar">
        <div class="briefing-status-pulse">
          <span class="live-dot-et"></span>
          <strong>LIVE INTEL STREAM:</strong> 6 Key Developments Recorded Today
        </div>
        <button class="briefing-refresh-btn" onclick="showToast('Live Intel Feed Synced: All timestamps up to date');">⚡ Refresh Live Feed</button>
      </div>

      <div class="briefing-timeline-grid">
        
        <article class="briefing-card">
          <div class="briefing-media">
            <img src="https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=600&auto=format&fit=crop&q=80" alt="G7 Envoys Naval Maritime Escort" class="briefing-img" loading="lazy">
          </div>
          <div class="briefing-meta-row">
            <span class="briefing-time-badge"><span class="briefing-mini-dot">●</span> 12:45 PM IST</span>
            <span class="briefing-topic-pill">DIPLOMACY</span>
          </div>
          <h3 class="briefing-title">
            <a href="#br-1">G7 Envoys Finalize Bab-el-Mandeb Maritime Escort Protocols in Rome</a>
          </h3>
          <p class="briefing-excerpt">
            Senior defense attachés conclude negotiations on an expanded multilateral escort grid to guarantee commercial passage through vital container bottlenecks.
          </p>
        </article>

        <article class="briefing-card">
          <div class="briefing-media">
            <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&auto=format&fit=crop&q=80" alt="ECB Frankfurt Central Bank" class="briefing-img" loading="lazy">
          </div>
          <div class="briefing-meta-row">
            <span class="briefing-time-badge"><span class="briefing-mini-dot">●</span> 12:15 PM IST</span>
            <span class="briefing-topic-pill">CENTRAL BANKS</span>
          </div>
          <h3 class="briefing-title">
            <a href="#br-2">ECB Signals Flexible Rate Glidepath Ahead of Frankfurt Policy Deliberations</a>
          </h3>
          <p class="briefing-excerpt">
            European Central Bank policymakers highlight moderating wage indicators, opening room for rate recalibration without risking price stability.
          </p>
        </article>

        <article class="briefing-card">
          <div class="briefing-media">
            <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600&auto=format&fit=crop&q=80" alt="Brent Crude Oil Tanker Terminal" class="briefing-img" loading="lazy">
          </div>
          <div class="briefing-meta-row">
            <span class="briefing-time-badge"><span class="briefing-mini-dot">●</span> 11:42 AM IST</span>
            <span class="briefing-topic-pill">ENERGY</span>
          </div>
          <h3 class="briefing-title">
            <a href="#br-3">Brent Steady Around $74/bbl as Gulf Export Tanker Schedules Modernize</a>
          </h3>
          <p class="briefing-excerpt">
            Crude oil futures consolidate as prompt physical delivery premiums moderate following inventory builds in North American and European strategic reserves.
          </p>
        </article>

        <article class="briefing-card">
          <div class="briefing-media">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=80" alt="ASML EUV Lithography Scanner Chips" class="briefing-img" loading="lazy">
          </div>
          <div class="briefing-meta-row">
            <span class="briefing-time-badge"><span class="briefing-mini-dot">●</span> 11:10 AM IST</span>
            <span class="briefing-topic-pill">FRONTIER TECH</span>
          </div>
          <h3 class="briefing-title">
            <a href="#br-4">ASML Ships Second High-NA EUV Lithography Scanner to US Commercial Fab</a>
          </h3>
          <p class="briefing-excerpt">
            The next-generation sub-2nm chipmaking tool begins calibration in Ohio, marking an inflection point in Western semiconductor manufacturing sovereignty.
          </p>
        </article>

        <article class="briefing-card">
          <div class="briefing-media">
            <img src="https://images.unsplash.com/photo-1509228468518-180dd4864904?w=600&auto=format&fit=crop&q=80" alt="Quad Maritime Working Group" class="briefing-img" loading="lazy">
          </div>
          <div class="briefing-meta-row">
            <span class="briefing-time-badge"><span class="briefing-mini-dot">●</span> 10:35 AM IST</span>
            <span class="briefing-topic-pill">GEOPOLITICS</span>
          </div>
          <h3 class="briefing-title">
            <a href="#br-5">Quad Maritime Working Group Reaffirms Open Indo-Pacific Navigation Charter</a>
          </h3>
          <p class="briefing-excerpt">
            Naval leaders from India, Japan, Australia, and the US agree on shared satellite AIS feed integration to monitor gray-zone sea maneuvers.
          </p>
        </article>

        <article class="briefing-card">
          <div class="briefing-media">
            <img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&auto=format&fit=crop&q=80" alt="India-EFTA Trade Agreement" class="briefing-img" loading="lazy">
          </div>
          <div class="briefing-meta-row">
            <span class="briefing-time-badge"><span class="briefing-mini-dot">●</span> 09:50 AM IST</span>
            <span class="briefing-topic-pill">TRADE</span>
          </div>
          <h3 class="briefing-title">
            <a href="#br-6">India-EFTA Trade &amp; Economic Partnership Agreement Enters Ratification Stage</a>
          </h3>
          <p class="briefing-excerpt">
            Swiss, Norwegian, and Indian trade secretariats synchronize technical tariff classifications to fast-track $100B investment commitment over 15 years.
          </p>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 3: GEOPOLITICS & INTERNATIONAL RELATIONS
         Wars, elections, diplomacy, sanctions and international policy
         ===================================================================== -->
    <section class="portal-section" id="geopolitics-relations">
      <div class="sec-heading">
        <h2><a href="#geopolitics-relations">Geopolitics &amp; International Relations <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">WARS, ELECTIONS, DIPLOMACY, SANCTIONS &amp; INTERNATIONAL POLICY</span>
      </div>

      <div class="portal-grid-4">
        
        <article class="portal-card">
          <a href="#geo-1" class="portal-media">
            <img src="https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=500&auto=format&fit=crop&q=80" alt="Baltic NATO Defense" loading="lazy">
            <span class="portal-card-tag">DEFENSE ALLIANCES</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#geo-1">NATO Expands Baltic Air-and-Sea Shield: Nordic Allies Deploy Joint Undersea Drone Grid</a>
          </h3>
          <p class="portal-card-excerpt">
            Following Baltic subsea communications cable severances, allied navies commission an autonomous sensor ring covering the Gulf of Finland.
          </p>
        </article>

        <article class="portal-card">
          <a href="#geo-2" class="portal-media">
            <img src="https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=500&auto=format&fit=crop&q=80" alt="Middle East Diplomacy" loading="lazy">
            <span class="portal-card-tag">MIDDLE EAST ACCORDS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#geo-2">The Red Sea Stalemate: How Maritime Shipping Rerouting Reshapes Indian Ocean Hub Ports</a>
          </h3>
          <p class="portal-card-excerpt">
            Transshipment volumes surge 45% in Colombo and Mundra as global container lines permanently adjust voyage timelines around the Cape of Good Hope.
          </p>
        </article>

        <article class="portal-card">
          <a href="#geo-3" class="portal-media">
            <img src="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=500&auto=format&fit=crop&q=80" alt="Sanctions Enforcement" loading="lazy">
            <span class="portal-card-tag">SANCTIONS &amp; AUDITS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#geo-3">Secondary Sanctions Clampdown: US Treasury Freezes $4.2B in Shadow-Fleet Escrow Accounts</a>
          </h3>
          <p class="portal-card-excerpt">
            Western regulatory enforcement tightens on non-compliant maritime insurers and flag registries servicing covert crude transfers.
          </p>
        </article>

        <article class="portal-card">
          <a href="#geo-4" class="portal-media">
            <img src="https://images.unsplash.com/photo-1540910419892-4a36d2c3266c?w=500&auto=format&fit=crop&q=80" alt="Global Elections" loading="lazy">
            <span class="portal-card-tag">GLOBAL ELECTIONS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#geo-4">Global Election Supercycle: Over 60 Democracies Assess Defense Spending and Trade Mandates</a>
          </h3>
          <p class="portal-card-excerpt">
            Voters across Europe, North America, and Asia demand industrial self-reliance, pushing defense budgets above 2.5% of GDP across allied capitals.
          </p>
        </article>

      </div>
    </section>

    

    <!-- =====================================================================
         SECTION 5: CRYPTOCURRENCY NEWS
         EXACT FORMAT FROM REFERENCE IMAGE 2:
         4-Column Layout on Signature Peach Background
         Col 1: Hero Card | Col 2: Headlines List | Col 3: Crypto TV & Expert Speak | Col 4: Crypto Corner Widget
         ===================================================================== -->
    <section class="portal-section crypto-hub-section" id="crypto-news">
      <div class="peach-container-wrap">
        
        <!-- Top Section Header & Newsletter Bar -->
        <div class="crypto-top-bar">
          <h2 class="crypto-main-heading">
            <a href="#crypto-news">CRYPTOCURRENCY NEWS <span class="sec-chevron">›</span></a>
          </h2>
          <div class="crypto-newsletter-subscribe">
            <span class="c-news-label">Subscribe to our Cryptocurrency News Newsletter</span>
            <form class="c-news-form" onsubmit="event.preventDefault(); showToast('Subscribed to Cryptocurrency News Newsletter!');">
              <input type="email" placeholder="akshit.negi@timesinternet.in" value="akshit.negi@timesinternet.in" required>
              <button type="submit">Subscribe</button>
            </form>
          </div>
        </div>

        <!-- 4 Columns Grid matching Image 2 -->
        <div class="crypto-4col-grid">
          
          <!-- Column 1: Big Hero Story -->
          <div class="crypto-col-hero">
            <article class="c-hero-card">
              <a href="#crypto-hero" class="c-hero-thumb">
                <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&auto=format&fit=crop&q=80" alt="Cryptocurrency Bitcoin Gold Coins" loading="lazy">
              </a>
              <h3 class="c-hero-title">
                <a href="#crypto-hero">Crypto’s leverage machine finds new life beyond Bitcoin bets</a>
              </h3>
              <p class="c-hero-desc">
                Despite a decline in crypto trading activities, there is a rising interest in traditional assets among investors. Open interest in real-world asset contracts has increased to $9 billion, claiming 14% of total volume. The transition marks a significant change in the derivatives markets as crypto inroads are being utilized for traditional trading. This shift indicates a maturation of the digital asset space, making it more accessible to mainstream investors.
              </p>
            </article>
          </div>

          <!-- Column 2: 7 Text-Only Headlines List -->
          <div class="crypto-col-headlines">
            <ul class="c-headlines-list">
              <li>
                <a href="#c-1">Bitcoin holds near $81,200, Ethereum at $2,415 as institutional inflows cushion global market pressure</a>
              </li>
              <li>
                <a href="#c-2">Bitcoin reclaims $82,500 as improved ETF flows lift market sentiment. Here is what experts say</a>
              </li>
              <li>
                <a href="#c-3">Bitcoin holds near $86,000 as weak US jobs data lowers October Fed rate hike expectations</a>
              </li>
              <li>
                <a href="#c-4">Bitcoin holds near $84,000, Ethereum moves towards $2,700 as buyers remain active</a>
              </li>
              <li>
                <a href="#c-5">Robinhood stock tokens turbocharge a new era of meme trading</a>
              </li>
              <li>
                <a href="#c-6">CoinSwitch swings to profitability in FY26 as crypto platform's revenue climbs 150% to Rs 324 crore</a>
              </li>
              <li>
                <a href="#c-7">Bitcoin skyrocketed 750% since Warren Buffett called it 'rat poison' in 2018. Why was he cautious?</a>
              </li>
            </ul>
          </div>

          <!-- Column 3: Crypto TV & Expert Speak -->
          <div class="crypto-col-tv-expert">
            
            <!-- Crypto TV -->
            <div class="c-tv-block">
              <h4 class="c-subhead">Crypto TV - <span class="c-subhead-light">Stay in the know</span></h4>
              <div class="c-video-card video-card" data-video-title="Crypto TV | Layer 2 solutions: Faster, cheaper crypto transactions explainer" data-video-dur="04:12">
                <div class="c-video-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1621416894569-0f39ed31d247?w=400&auto=format&fit=crop&q=80" alt="Crypto TV Layer 2" loading="lazy">
                  <div class="c-play-circle">▶</div>
                </div>
                <h5 class="c-video-title">Crypto TV | Layer 2 solutions: Faster, cheaper crypto transactions explainer</h5>
              </div>
            </div>

            <!-- Expert Speak -->
            <div class="c-expert-block">
              <h4 class="c-subhead"><a href="#expert-speak">Expert Speak <span class="sec-chevron">›</span></a></h4>
              
              <div class="c-expert-item">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=crop&q=80" alt="Crypto Tax" class="c-expert-avatar" loading="lazy">
                <div class="c-expert-info">
                  <a href="#exp-1" class="c-exp-heading">Crypto Tax: What investors need to know</a>
                  <span class="c-exp-author">Vimal Sagar Tiwari</span>
                </div>
              </div>

              <div class="c-expert-item">
                <img src="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=100&auto=format&fit=crop&q=80" alt="BlackRock ETF" class="c-expert-avatar" loading="lazy">
                <div class="c-expert-info">
                  <a href="#exp-2" class="c-exp-heading">Reading the tea leaves: Why BlackRock ETF will overcome SEC hurdles</a>
                  <span class="c-exp-author">Rajagopal Menon</span>
                </div>
              </div>

            </div>

          </div>

          <!-- Column 4: Crypto Corner Widget with Sparkline & Top Gainers/Losers -->
          <div class="crypto-col-corner">
            <div class="crypto-corner-box">
              
              <div class="corner-header">
                <span class="corner-icon">🪙</span>
                <span class="corner-title">Crypto Corner</span>
                <span class="corner-icon">🪙</span>
              </div>

              <div class="corner-tickers-row">
                <div class="corner-coin">
                  <div class="coin-name">Bitcoin</div>
                  <div class="coin-price down">↓ 7,762,064</div>
                  <div class="coin-pct down">-0.83%</div>
                </div>
                <div class="corner-coin">
                  <div class="coin-name">Ethereum</div>
                  <div class="coin-price down">↓ 227,988</div>
                  <div class="coin-pct down">-1.07%</div>
                </div>
              </div>

              <!-- Mini Sparkline Graph -->
              <div class="corner-sparkline-wrap">
                <svg viewBox="0 0 240 70" preserveAspectRatio="none" class="corner-sparkline-svg">
                  <defs>
                    <linearGradient id="cornerGradRed" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stop-color="#ed193b" stop-opacity="0.25"/>
                      <stop offset="100%" stop-color="#ed193b" stop-opacity="0.0"/>
                    </linearGradient>
                  </defs>
                  <path d="M 0,20 Q 30,15 60,32 T 120,40 T 180,25 T 240,48 L 240,70 L 0,70 Z" fill="url(#cornerGradRed)"/>
                  <path d="M 0,20 Q 30,15 60,32 T 120,40 T 180,25 T 240,48" fill="none" stroke="#ed193b" stroke-width="1.8"/>
                </svg>
                <div class="corner-time-labels">
                  <span>11:25</span>
                  <span>23:30</span>
                  <span>11:20</span>
                </div>
              </div>

              <!-- Top Gainers / Top Losers Tabs -->
              <div class="corner-tabs" id="cryptoCornerTabs">
                <button class="corner-tab active" data-tab="gainers">TOP GAINERS</button>
                <button class="corner-tab" data-tab="losers">TOP LOSERS</button>
              </div>

              <!-- Mini Movers Table -->
              <div class="corner-movers-list" id="cryptoMoversList">
                <div class="mover-row">
                  <span class="mover-sym">Akedo</span>
                  <span class="mover-val up">3.40 (55.36%)</span>
                </div>
                <div class="mover-row">
                  <span class="mover-sym">MemeCore</span>
                  <span class="mover-val up">83.73 (11.74%)</span>
                </div>
                <div class="mover-row">
                  <span class="mover-sym">Beldex</span>
                  <span class="mover-val up">7.44 (7.60%)</span>
                </div>
                <div class="mover-row">
                  <span class="mover-sym">Dash</span>
                  <span class="mover-val up">5167.13 (7.30%)</span>
                </div>
              </div>

            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 6: INTERNATIONAL BUSINESS
         Global companies, mergers and acquisitions (M&A), trade, corporate earnings
         ===================================================================== -->
    <section class="portal-section" id="international-business">
      <div class="sec-heading">
        <h2><a href="#international-business">International Business <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">GLOBAL ENTERPRISE, M&amp;A, TRADE, CORPORATE EARNINGS &amp; INDUSTRY DEVELOPMENTS</span>
      </div>

      <div class="portal-grid-4">
        
        <article class="portal-card">
          <a href="#ib-1" class="portal-media">
            <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=500&auto=format&fit=crop&q=80" alt="Mergers and Acquisitions" loading="lazy">
            <span class="portal-card-tag">M&amp;A ACTIVITY</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ib-1">The $120-Billion Cross-Border M&amp;A Surge: Sovereign Funds Target Advanced Aerospace Assets</a>
          </h3>
          <p class="portal-card-excerpt">
            Private equity syndicates and Gulf sovereign wealth entities deploy cash to consolidate global industrial supply networks.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ib-2" class="portal-media">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&auto=format&fit=crop&q=80" alt="TSMC ASML 2nm Fab" loading="lazy">
            <span class="portal-card-tag">SEMICONDUCTORS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ib-2">TSMC &amp; ASML's 2nm Foundry Expansion: High-Stakes Silicon Capex Battles in Asia and Europe</a>
          </h3>
          <p class="portal-card-excerpt">
            Dresden and Kumamoto mega-fabs ramp installation schedules as leading chip designers vie for first-wave 2nm wafer allocations.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ib-3" class="portal-media">
            <img src="https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=500&auto=format&fit=crop&q=80" alt="European Carmakers" loading="lazy">
            <span class="portal-card-tag">AUTOMOTIVE TRANSITION</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ib-3">European Carmakers Form Unified Battery Consortium to Counter Low-Cost Electric Competitors</a>
          </h3>
          <p class="portal-card-excerpt">
            Stellantis, Renault, and regional component manufacturers unite behind shared platform architectures to trim manufacturing costs by 30%.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ib-4" class="portal-media">
            <img src="https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?w=500&auto=format&fit=crop&q=80" alt="Big Pharma Metabolic" loading="lazy">
            <span class="portal-card-tag">CORPORATE EARNINGS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ib-4">Big Pharma's Obesity Gold Rush: Corporate Earnings Surge Beyond Traditional Therapeutics</a>
          </h3>
          <p class="portal-card-excerpt">
            Next-gen oral GLP-1 formulations and dual-receptor molecules drive multinational pharmaceutical balance sheets to historic highs.
          </p>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 7: US & UK NEWS
         Regional coverage of politics, business, policies and major national developments
         ===================================================================== -->
    <section class="portal-section duo-playcard-section" id="us-uk-news">
      <div class="duo-playcard-grid">
        
        <!-- Left Playcard: United States -->
        <div class="duo-playcard-col" id="us-news">
          <div class="playcard-sec-head">
            <a href="#us-news">United States News <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <article class="playcard-featured">
              <a href="#us-feat" class="playcard-feat-media">
                <img src="https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=640&auto=format&fit=crop&q=80" alt="US Capitol Washington" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#us-feat">Capitol Hill Deliberations: Debt Ceiling Fiscal Limits, Tariffs &amp; Supreme Court Docket</a>
              </h3>
            </article>

            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#us-1" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=160&auto=format&fit=crop&q=80" alt="Wall St Earnings" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#us-1">Wall Street Megabanks Report Record Q3 Investment Banking Deal Inflows</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#us-2" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=160&auto=format&fit=crop&q=80" alt="FTC AI Inquiry" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#us-2">Federal Trade Commission Broadens Scrutiny Into Cloud Hyperscaler AI Exclusivity</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#us-3" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=160&auto=format&fit=crop&q=80" alt="US LNG Exports" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#us-3">US Gulf Coast LNG Export Terminals Operate At Peak Capacity Ahead Of Winter</a>
                </h4>
              </article>

            </div>

          </div>
        </div>

        <!-- Right Playcard: United Kingdom -->
        <div class="duo-playcard-col" id="uk-news">
          <div class="playcard-sec-head">
            <a href="#uk-news">United Kingdom News <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <article class="playcard-featured">
              <a href="#uk-feat" class="playcard-feat-media">
                <img src="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=640&auto=format&fit=crop&q=80" alt="UK Parliament Westminster" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#uk-feat">Chancellor Unveils UK Autumn Statement: Fiscal Guardrails, NHS Upgrades &amp; Capital Gains</a>
              </h3>
            </article>

            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#uk-1" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=160&auto=format&fit=crop&q=80" alt="Bank of England" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#uk-1">Bank of England Debates Balance Sheet Runoff Velocity Amid Services Inflation</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#uk-2" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=160&auto=format&fit=crop&q=80" alt="London Stock Exchange" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#uk-2">London Stock Exchange Modernizes Prospectus Rules to Attract Global Tech IPOs</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#uk-3" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=160&auto=format&fit=crop&q=80" alt="British Green Industry" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#uk-3">British Clean Aerospace Cluster Secures £14 Billion In Private Green Capital</a>
                </h4>
              </article>

            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 8: GLOBAL TECH & AI
         AI, technology companies, chips, cybersecurity and regulation
         ===================================================================== -->
    <section class="portal-section" id="global-tech-ai">
      <div class="sec-heading">
        <h2><a href="#global-tech-ai">Global Tech &amp; AI <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">ARTIFICIAL INTELLIGENCE, CHIPS, CYBERSECURITY &amp; GLOBAL REGULATION</span>
      </div>

      <div class="portal-grid-4">
        
        <article class="portal-card">
          <a href="#gai-1" class="portal-media">
            <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500&auto=format&fit=crop&q=80" alt="Autonomous AI Systems" loading="lazy">
            <span class="portal-card-tag">AGENTIC SYSTEMS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gai-1">Frontier Reasoning Models &amp; Autonomous Agent Swarms: Replacing Legacy Enterprise Software</a>
          </h3>
          <p class="portal-card-excerpt">
            CIOs deploy multi-agent coordination architectures to execute autonomous financial auditing, software deployment, and supply logistics.
          </p>
        </article>

        <article class="portal-card">
          <a href="#gai-2" class="portal-media">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&auto=format&fit=crop&q=80" alt="Semiconductor Chips" loading="lazy">
            <span class="portal-card-tag">CHIP FOUNDRIES</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gai-2">High-NA EUV &amp; Gate-All-Around: Inside the Race for Sub-2nm Commercial Computing</a>
          </h3>
          <p class="portal-card-excerpt">
            Foundries overcome optical diffraction limits, achieving dramatic energy efficiency improvements for next-generation AI accelerators.
          </p>
        </article>

        <article class="portal-card">
          <a href="#gai-3" class="portal-media">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&auto=format&fit=crop&q=80" alt="Datacenter Nuclear Power" loading="lazy">
            <span class="portal-card-tag">AI INFRASTRUCTURE</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gai-3">Big Tech's Nuclear SMR Bet: Hyperscalers Secure 20-Year Clean Power Contracts for Gigawatt Clusters</a>
          </h3>
          <p class="portal-card-excerpt">
            Dedicated small modular reactors will power next-decade supercomputing hubs without placing strain on municipal public electricity grids.
          </p>
        </article>

        <article class="portal-card">
          <a href="#gai-4" class="portal-media">
            <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=500&auto=format&fit=crop&q=80" alt="AI Cybersecurity" loading="lazy">
            <span class="portal-card-tag">CYBER DEFENSE</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gai-4">Global AI Safety Mandates: International Regulators Introduce Zero-Day Stress Auditing</a>
          </h3>
          <p class="portal-card-excerpt">
            Multilateral agencies establish standardized red-teaming benchmarks to protect critical infrastructure from automated synthetic attacks.
          </p>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 9: SCIENCE & SPACE
         Scientific discoveries, research, NASA, astronomy and space missions
         ===================================================================== -->
    <section class="portal-section" id="science-space">
      <div class="sec-heading">
        <h2><a href="#science-space">Science &amp; Space <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">SCIENTIFIC DISCOVERIES, RESEARCH, NASA, ASTRONOMY &amp; SPACE MISSIONS</span>
      </div>

      <div class="portal-grid-4">
        
        <article class="portal-card">
          <a href="#ss-1" class="portal-media">
            <img src="https://images.unsplash.com/photo-1516849841032-87cbac4d88f7?w=800&auto=format&fit=crop&q=80" alt="NASA Artemis Mission" loading="lazy">
            <span class="portal-card-tag">LUNAR EXPLORATION</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ss-1">NASA's Artemis II Crew Clears Final Environmental Testing For Lunar Orbital Mission</a>
          </h3>
          <p class="portal-card-excerpt">
            Engineers at Kennedy Space Center complete integrated life-support and deep-space communications validation for humanity's return to the Moon.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ss-2" class="portal-media">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&auto=format&fit=crop&q=80" alt="James Webb Exoplanet" loading="lazy">
            <span class="portal-card-tag">DEEP ASTRONOMY</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ss-2">James Webb Telescope Confirms Atmospheric Carbon Molecules on Exoplanet K2-18b</a>
          </h3>
          <p class="portal-card-excerpt">
            High-resolution spectroscopy identifies methane and carbon dioxide in the habitable zone of a red dwarf 120 light-years from Earth.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ss-3" class="portal-media">
            <img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=500&auto=format&fit=crop&q=80" alt="Quantum Physics Discovery" loading="lazy">
            <span class="portal-card-tag">QUANTUM PHYSICS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ss-3">Physicists Demonstrate Fault-Tolerant Topological Qubit in Nanowire Superconductors</a>
          </h3>
          <p class="portal-card-excerpt">
            Majorana zero modes show unprecedented environmental noise resistance, unlocking a viable path toward error-free quantum computing.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ss-4" class="portal-media">
            <img src="https://images.unsplash.com/photo-1507668077129-56e32842fceb?w=500&auto=format&fit=crop&q=80" alt="Deep Ocean Enzymes" loading="lazy">
            <span class="portal-card-tag">BIOTECH FRONTIERS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ss-4">Deep-Sea Hydrothermal Vent Enzymes Accelerate Industrial Synthetic Biology</a>
          </h3>
          <p class="portal-card-excerpt">
            Thermostable biocatalysts discovered 3,000 meters beneath the Pacific cut enzymatic plastic recycling breakdown times by over 80%.
          </p>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 10: ENVIRONMENT & CLIMATE
         Climate change, extreme weather, wildlife, energy transition and sustainability
         ===================================================================== -->
    <section class="portal-section" id="environment-climate">
      <div class="sec-heading">
        <h2><a href="#environment-climate">Environment &amp; Climate <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">CLIMATE DYNAMICS, EXTREME WEATHER, WILDLIFE, ENERGY TRANSITION &amp; SUSTAINABILITY</span>
      </div>

      <div class="portal-grid-4">
        
        <article class="portal-card">
          <a href="#ec-1" class="portal-media">
            <img src="https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9?w=500&auto=format&fit=crop&q=80" alt="Clean Energy Transition" loading="lazy">
            <span class="portal-card-tag">ENERGY TRANSITION</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ec-1">Global Clean Energy Capital Outlays Cross $2-Trillion Annual Run Rate</a>
          </h3>
          <p class="portal-card-excerpt">
            Grid-scale battery storage deployments and utility solar additions outpace upstream fossil capital expenditures for the second straight year.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ec-2" class="portal-media">
            <img src="https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=500&auto=format&fit=crop&q=80" alt="Extreme Weather Forecasting" loading="lazy">
            <span class="portal-card-tag">EXTREME WEATHER</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ec-2">Ocean Heat Domes &amp; Jet Stream Meanders: Meteorological Models Re-Evaluate Cyclone Tracks</a>
          </h3>
          <p class="portal-card-excerpt">
            Anomalously high sea surface temperatures prompt maritime weather institutes to revise tropical storm intensity baselines.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ec-3" class="portal-media">
            <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500&auto=format&fit=crop&q=80" alt="Wildlife Sanctuary Protection" loading="lazy">
            <span class="portal-card-tag">WILDLIFE CONSERVATION</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ec-3">Satellite AI Bio-Acoustics Safeguard Endangered Transboundary Migration Corridors</a>
          </h3>
          <p class="portal-card-excerpt">
            Autonomous audio sensors and orbital monitoring reverse habitat fragmentation across Central Africa and the Himalayan foothills.
          </p>
        </article>

        <article class="portal-card">
          <a href="#ec-4" class="portal-media">
            <img src="https://images.unsplash.com/photo-1466611653911-95081537e5b7?w=500&auto=format&fit=crop&q=80" alt="Carbon Markets Article 6" loading="lazy">
            <span class="portal-card-tag">SUSTAINABLE FINANCE</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#ec-4">Article 6 Sovereign Carbon Credit Markets Reach Global Operational Consensus</a>
          </h3>
          <p class="portal-card-excerpt">
            Cross-border emission offset registries establish strict additionality rules, attracting institutional carbon liquidity from sovereign signatories.
          </p>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 11: GLOBAL REAL ESTATE
         International property markets, housing and real estate investment
         ===================================================================== -->
    <section class="portal-section" id="global-real-estate">
      <div class="sec-heading">
        <h2><a href="#global-real-estate">Global Real Estate <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">INTERNATIONAL PROPERTY MARKETS, HOUSING &amp; REAL ESTATE INVESTMENT</span>
      </div>

      <div class="portal-grid-3">
        
        <article class="portal-card">
          <a href="#re-1" class="portal-media">
            <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=600&auto=format&fit=crop&q=80" alt="Luxury Penthouses Dubai London" loading="lazy">
            <span class="portal-card-tag">PRIME RESIDENTIAL</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#re-1">Trophy Penthouses in Dubai, London &amp; Manhattan Command Benchmark Valuations</a>
          </h3>
          <p class="portal-card-excerpt">
            Cash transactions insulate ultra-prime real estate from elevated borrowing costs as global family offices treat iconic skyline real estate as sovereign stores of value.
          </p>
        </article>

        <article class="portal-card">
          <a href="#re-2" class="portal-media">
            <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&auto=format&fit=crop&q=80" alt="Data Center Land REITs" loading="lazy">
            <span class="portal-card-tag">INDUSTRIAL INFRASTRUCTURE</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#re-2">The Data Center Land Rush: Industrial REITs Pivot Distribution Yards to High-Voltage Substation Hubs</a>
          </h3>
          <p class="portal-card-excerpt">
            Access to utility interconnect capacity emerges as the defining metric for institutional warehouse landlords converting assets to AI colocation facilities.
          </p>
        </article>

        <article class="portal-card">
          <a href="#re-3" class="portal-media">
            <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&auto=format&fit=crop&q=80" alt="Commercial Debt Refinancing" loading="lazy">
            <span class="portal-card-tag">MORTGAGE DYNAMICS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#re-3">Commercial Debt Refinancing: How Institutional Landlords Navigate Elevated Capital Costs</a>
          </h3>
          <p class="portal-card-excerpt">
            Asset managers restructure $1.8 Trillion in maturing commercial real estate paper using preferred equity and mezzanine private credit partnerships.
          </p>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 12: PANACHE
         EXACT FORMAT FROM REFERENCE IMAGE 3:
         4-Column Layout on Signature Peach Background
         Col 1: Tall Vertical Hero with Dark Gradient Overlay
         Col 2: 2 Stacked Visual Stories (Headline Top, Image Below)
         Col 3: 5 Stacked Text + Right Thumbnail Items
         Col 4: Videos & Slideshows with Camera Badge Pill
         ===================================================================== -->
    <section class="portal-section panache-hub-section" id="people-leadership-panache">
      <div class="peach-container-wrap">
        
        <div class="panache-hub-header">
          <h2 class="panache-main-heading">
            <a href="#people-leadership-panache">PANACHE <span class="sec-chevron">›</span></a>
          </h2>
        </div>

        <div class="panache-4col-grid">
          
          <!-- Column 1: Tall Vertical Hero with Dark Gradient Overlay -->
          <div class="panache-col-tall-hero">
            <article class="p-tall-hero-card">
              <a href="#panache-hero" class="p-tall-hero-media">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&auto=format&fit=crop&q=80" alt="Prabhas in Panache" class="p-tall-hero-img" loading="lazy">
                <div class="p-tall-hero-overlay">
                  <h3 class="p-tall-hero-title">
                    Prabhas came from a film family but travelled to college by bus: Actor once shared his father's financial struggle. What shaped his work ethic?
                  </h3>
                </div>
              </a>
            </article>
          </div>

          <!-- Column 2: 2 Stacked Visual Stories (Headline Top, Image Below) -->
          <div class="panache-col-stacked-visuals">
            
            <article class="p-vis-card">
              <h4 class="p-vis-title">
                <a href="#p-v1">Two people, same salary, 20 years: CA Nitin Kaushik reveals what separates the wealthy from the rest</a>
              </h4>
              <a href="#p-v1" class="p-vis-thumb">
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&auto=format&fit=crop&q=80" alt="Wealthy Separation" loading="lazy">
              </a>
            </article>

            <article class="p-vis-card">
              <h4 class="p-vis-title">
                <a href="#p-v2">Prabhas' 84-acre farmhouse in Andhra Pradesh village is a 300-year-old fort. It features vintage doors, hidden rooms, coconut groves and a private gym</a>
              </h4>
              <a href="#p-v2" class="p-vis-thumb">
                <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&auto=format&fit=crop&q=80" alt="Farmhouse Fort" loading="lazy">
              </a>
            </article>

          </div>

          <!-- Column 3: 5 Stacked Text + Right Thumbnail Items -->
          <div class="panache-col-text-thumb-list">
            
            <article class="p-list-item">
              <h5 class="p-list-title">
                <a href="#p-l1">Friday OTT releases of the week: The Paradise to Dhoomakethu to Sumo Didi, new movies and shows on Netflix, JioHotstar, Prime Video and ZEE5</a>
              </h5>
              <a href="#p-l1" class="p-list-thumb">
                <img src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=160&auto=format&fit=crop&q=80" alt="OTT Releases" loading="lazy">
              </a>
            </article>

            <article class="p-list-item">
              <h5 class="p-list-title">
                <a href="#p-l2">Jailer 2 box office collection day 8: Rajinikanth's film crosses Rs 600 crore worldwide. Allu Arjun calls it a 'commercial entertainer'</a>
              </h5>
              <a href="#p-l2" class="p-list-thumb">
                <img src="https://images.unsplash.com/photo-1485846234645-a62644f84728?w=160&auto=format&fit=crop&q=80" alt="Jailer 2 Box Office" loading="lazy">
              </a>
            </article>

            <article class="p-list-item">
              <h5 class="p-list-title">
                <a href="#p-l3">Sanjay Leela Bhansali once scolded Salman Khan for 'touching' Aishwarya Rai's arm, reveals co-star: 'He was in love, so...'</a>
              </h5>
              <a href="#p-l3" class="p-list-thumb">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=160&auto=format&fit=crop&q=80" alt="Bollywood Lore" loading="lazy">
              </a>
            </article>

            <article class="p-list-item">
              <h5 class="p-list-title">
                <a href="#p-l4">Is your favourite diet soda really safe? How it effects weight loss in comparison to water, revealed in new study</a>
              </h5>
              <a href="#p-l4" class="p-list-thumb">
                <img src="https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=160&auto=format&fit=crop&q=80" alt="Diet Soda Study" loading="lazy">
              </a>
            </article>

            <article class="p-list-item">
              <h5 class="p-list-title">
                <a href="#p-l5">10,000 daily steps not needed: A much lower walking target can help reduce brain disease risk, finds new study</a>
              </h5>
              <a href="#p-l5" class="p-list-thumb">
                <img src="https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=160&auto=format&fit=crop&q=80" alt="Daily Steps Health" loading="lazy">
              </a>
            </article>

          </div>

          <!-- Column 4: Videos & Slideshows -->
          <div class="panache-col-slideshows">
            <div class="p-slideshows-head">
              <a href="#slideshows">VIDEOS &amp; SLIDESHOWS <span class="sec-chevron red">›</span></a>
            </div>

            <article class="p-slide-card">
              <a href="#slide-1" class="p-slide-media">
                <img src="https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=400&auto=format&fit=crop&q=80" alt="Weekend OTT watchlist" loading="lazy">
                <span class="p-camera-pill">📷 Weekend OTT watchlist</span>
              </a>
              <h5 class="p-slide-title">
                <a href="#slide-1">What to watch on OTT this weekend: 9 new movies and shows coming to Netflix, JioHotstar, Prime Video and more</a>
              </h5>
            </article>

            <article class="p-slide-card">
              <a href="#slide-2" class="p-slide-media">
                <img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=400&auto=format&fit=crop&q=80" alt="Weekend OTT movies" loading="lazy">
                <span class="p-camera-pill">📷 Weekend OTT watchlist</span>
              </a>
              <h5 class="p-slide-title">
                <a href="#slide-2">What to watch on OTT this weekend: 9 new movies and shows coming to Netflix...</a>
              </h5>
            </article>

          </div>

        </div>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 13: GLOBAL HEALTH
         Major health developments, scientific research, global health policy and outbreaks
         ===================================================================== -->
    <section class="portal-section" id="global-health">
      <div class="sec-heading">
        <h2><a href="#global-health">Global Health <span class="sec-chevron">›</span></a></h2>
        <span class="sec-subtag">MAJOR HEALTH DEVELOPMENTS, SCIENTIFIC RESEARCH, POLICY &amp; OUTBREAKS</span>
      </div>

      <div class="portal-grid-4">
        
        <article class="portal-card">
          <a href="#gh-1" class="portal-media">
            <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=500&auto=format&fit=crop&q=80" alt="mRNA Cancer Oncology" loading="lazy">
            <span class="portal-card-tag">PRECISION ONCOLOGY</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gh-1">Generative AI in Oncology: Personalized mRNA Cancer Vaccines Reach Phase III Trials</a>
          </h3>
          <p class="portal-card-excerpt">
            Custom neoantigen vaccines tailored to individual tumor DNA mutations demonstrate robust multi-year remission rates in multinational patient groups.
          </p>
        </article>

        <article class="portal-card">
          <a href="#gh-2" class="portal-media">
            <img src="https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?w=500&auto=format&fit=crop&q=80" alt="WHO Genomic Surveillance" loading="lazy">
            <span class="portal-card-tag">GLOBAL HEALTH ACCORDS</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gh-2">WHO Pathogen Surveillance Accord: 140 Nations Ratify Real-Time Genomic Data Highway</a>
          </h3>
          <p class="portal-card-excerpt">
            A permanent global bio-surveillance network enables international health agencies to detect and isolate novel respiratory strains within 48 hours.
          </p>
        </article>

        <article class="portal-card">
          <a href="#gh-3" class="portal-media">
            <img src="https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=500&auto=format&fit=crop&q=80" alt="GLP1 Cardiovascular Health" loading="lazy">
            <span class="portal-card-tag">METABOLIC SCIENCE</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gh-3">The GLP-1 Cardioprotection Frontier: Long-Term Studies Reveal Multi-Organ Benefits</a>
          </h3>
          <p class="portal-card-excerpt">
            Clinical cardiology registries confirm significant reductions in systemic arterial inflammation and chronic kidney disease progression.
          </p>
        </article>

        <article class="portal-card">
          <a href="#gh-4" class="portal-media">
            <img src="https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=500&auto=format&fit=crop&q=80" alt="Senolytic Longevity Science" loading="lazy">
            <span class="portal-card-tag">LONGEVITY RESEARCH</span>
          </a>
          <h3 class="portal-card-title">
            <a href="#gh-4">Senolytic Longevity Trials: Clearing Cellular Senescence Rejuvenates Organ Resilience</a>
          </h3>
          <p class="portal-card-excerpt">
            Biotech researchers successfully conclude human safety trials for small-molecule therapeutics targeting inflammatory senescent cells.
          </p>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         SECTION 14: WORLD SPORTS (Exact Reference Screenshot)
         Dark charcoal theme (#1a1a1a), 'Sports ›' with All/Cricket/Football/Tennis tabs,
         Hero story, two columns of 3 stacked stories, and the interactive Playcard
         ===================================================================== -->
    <section class="portal-section sports-dark-hub" id="world-sports">
      <div class="sports-dark-container">
        
        <!-- Header row: Sports › on left, Category tabs on right -->
        <div class="sports-header-row">
          <h2 class="sports-heading">
            <a href="#world-sports">Sports <span class="sec-chevron">›</span></a>
          </h2>
          <div class="sports-cat-tabs" id="sportsCatTabs">
            <button class="sports-tab active" data-cat="all">All</button>
            <button class="sports-tab" data-cat="cricket">Cricket</button>
            <button class="sports-tab" data-cat="football">Football</button>
            <button class="sports-tab" data-cat="tennis">Tennis</button>
          </div>
        </div>

        <!-- 4-Column Layout matching uploaded reference screenshot -->
        <div class="sports-quad-grid">
          
          <!-- Column 1: Big Hero Story -->
          <article class="sports-hero-col">
            <a href="#sp-hero" class="sports-hero-img-wrap">
              <img src="https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=700&auto=format&fit=crop&q=80" alt="Harbhajan On Aussie Coach" class="sports-hero-img" loading="lazy">
            </a>
            <h3 class="sports-hero-headline">
              <a href="#sp-hero">&ldquo;Greg Chappell Divided Players&rdquo;: Harbhajan On Aussie Coach</a>
            </h3>
          </article>

          <!-- Column 2: 3 Stacked Stories -->
          <div class="sports-stack-col">
            <article class="sports-stack-item">
              <a href="#sp-1" class="sports-stack-thumb">
                <img src="https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?w=250&auto=format&fit=crop&q=80" alt="Anahat Singh" loading="lazy">
              </a>
              <h4 class="sports-stack-title">
                <a href="#sp-1">Anahat Claims Biggest Win Of Her Career, Downs Legend El Sherbini</a>
              </h4>
            </article>

            <article class="sports-stack-item">
              <a href="#sp-2" class="sports-stack-thumb">
                <img src="https://images.unsplash.com/photo-1530549387789-4c1017266635?w=250&auto=format&fit=crop&q=80" alt="Para Asiad Swimmer" loading="lazy">
              </a>
              <h4 class="sports-stack-title">
                <a href="#sp-2">Para Asiad: Indian Para Swimmer Deported Over Sexual Misconduct</a>
              </h4>
            </article>

            <article class="sports-stack-item">
              <a href="#sp-3" class="sports-stack-thumb">
                <img src="https://images.unsplash.com/photo-1512719994953-eabf50895df7?w=250&auto=format&fit=crop&q=80" alt="Kohli Rohit World Cup 2027" loading="lazy">
              </a>
              <h4 class="sports-stack-title">
                <a href="#sp-3">Kohli, Rohit To Play 2027 World Cup? BCCI Boss Lists Key Factors</a>
              </h4>
            </article>
          </div>

          <!-- Column 3: 3 Stacked Stories -->
          <div class="sports-stack-col">
            <article class="sports-stack-item">
              <a href="#sp-4" class="sports-stack-thumb">
                <img src="https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=250&auto=format&fit=crop&q=80" alt="Shreyas vs Surya" loading="lazy">
              </a>
              <h4 class="sports-stack-title">
                <a href="#sp-4">Shreyas vs Surya: Ex India Star Says Comparison &ldquo;Out Of The Way&rdquo;</a>
              </h4>
            </article>

            <article class="sports-stack-item">
              <a href="#sp-5" class="sports-stack-thumb">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=250&auto=format&fit=crop&q=80" alt="Kevin Pietersen" loading="lazy">
              </a>
              <h4 class="sports-stack-title">
                <a href="#sp-5">Pietersen&rsquo;s Bold Fix Amid Empty Stands In South Africa</a>
              </h4>
            </article>

            <article class="sports-stack-item">
              <a href="#sp-6" class="sports-stack-thumb">
                <img src="https://images.unsplash.com/photo-1546519638-68e109498ffc?w=250&auto=format&fit=crop&q=80" alt="Shreyas Iyer" loading="lazy">
              </a>
              <h4 class="sports-stack-title">
                <a href="#sp-6">Shreyas Iyer&rsquo;s &ldquo;Sweet Headache&rdquo; Message Amid Sooryavanshi Debate</a>
              </h4>
            </article>
          </div>

          <!-- Column 4: The Playcard / Scorecard Widget (Exact Screenshot Format) -->
          <aside class="playcard-widget" id="sportsPlaycard">
            
            <!-- Segmented Control Bar: In Progress | Upcoming | Recent -->
            <div class="playcard-tabs">
              <button class="pc-tab active" data-tab="inprogress">In Progress</button>
              <button class="pc-tab" data-tab="upcoming">Upcoming</button>
              <button class="pc-tab" data-tab="recent">Recent</button>
            </div>

            <!-- Dynamic Card Content Body -->
            <div class="playcard-body" id="playcardContent">
              
              <!-- Match Header with Live Badge & Bell Icon -->
              <div class="playcard-top-row">
                <div class="playcard-badge-info">
                  <span class="pc-live-dot">● LIVE</span>
                  <span class="pc-match-title" title="Match 7, ICC Men's T20 World Cup Africa Qualifier">Match 7, ICC Men's T20 World Cup Afri...</span>
                </div>
                <button class="pc-bell-btn" title="Toggle Match Notifications" onclick="showToast('🔔 Match notifications enabled for ICC T20 Qualifier');">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
                </button>
              </div>

              <!-- Status line in red -->
              <div class="pc-status-line">Play In Progress</div>

              <!-- Score lines -->
              <div class="pc-scores-block">
                <div class="pc-team-line">
                  <div class="pc-team-name-col">
                    <span class="pc-team-badge ngr-badge">🇳🇬</span>
                    <strong class="pc-team-code">NGR</strong>
                  </div>
                  <div class="pc-team-score-col">
                    <strong class="score-runs">60/1</strong>
                    <span class="score-overs">(5.1)</span>
                  </div>
                </div>

                <div class="pc-team-line muted">
                  <div class="pc-team-name-col">
                    <span class="pc-team-badge moz-badge">🇲🇿</span>
                    <strong class="pc-team-code">MOZ</strong>
                  </div>
                  <div class="pc-team-score-col">
                    <span class="score-runs">93</span>
                    <span class="score-overs">(19.4)</span>
                  </div>
                </div>
              </div>

              <!-- Equation and Run Rates -->
              <div class="pc-footer-row">
                <span class="pc-equation-text">Nigeria need 34 runs in 89 balls at 2.29 rpo</span>
                <span class="pc-crr-badge">CRR: 11.76</span>
              </div>

            </div>
          </aside>

        </div>

      </div>
    </section>

        <!-- =====================================================================
         SECTION 15: AI PODCASTS (Exact Reference Art)
         Dark Burgundy/Chocolate Hub (#14080b), 3 Featured AI Podcast Cards,
         Center Card Prominent, Red IN CONVERSATION Tags, and Center Pill Navigation
         CRITICAL INSTRUCTION: Place this section immediately before the footer.
         ===================================================================== -->
    <section class="portal-section featured-series-section" id="podcasts-section">
      <div id="videos-podcasts"></div>
      <div class="featured-series-container">
        
        <h2 class="featured-series-heading">AI Podcasts</h2>

        <!-- Podcast Carousel Container -->
        <div class="f-series-carousel-wrapper">
          <!-- Page 1 (Active) -->
          <div class="featured-series-grid f-series-page active" id="fSeriesPage1">
            
            <!-- Card 1 (Left): Infosys CTO Rafee Tarafdar -->
            <article class="f-series-card video-card" data-video-title="What will AI agents 'do'? | Infosys CTO Rafee Tarafdar | ET AI Podcast" data-video-dur="24:18">
              <div class="f-series-thumb-wrap">
                <img src="podcast/H6_XWlcp7O8-HD.jpg" alt="What will AI agents 'do'? | Infosys CTO Rafee Tarafdar" class="f-series-img" loading="lazy">
                <div class="f-thumb-overlay-gradient"></div>
                <button class="f-play-circle" aria-label="Play Episode">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                </button>
              </div>

              <div class="f-series-content">
                <div class="series-tag-red">
                  <svg class="mic-svg" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5-3c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/>
                  </svg>
                  <span>IN CONVERSATION</span>
                </div>
                <h3 class="f-series-title">
                  <a href="#pod-rafee">What will AI agents 'do'? | Infosys CTO Rafee Tarafdar | ET AI Podcast</a>
                </h3>
                <p class="f-series-desc">
                  Infosys CTO Rafee Tarafdar discusses enterprise AI, agentic systems, Poly-AI strategy, the rise of Frontier Engineers, and India's role in shaping autonomous workflows.
                </p>
              </div>
            </article>

            <!-- Card 2 (Center / Prominent): Fractal CEO Srikanth Velamakanni -->
            <article class="f-series-card f-series-card-center video-card" data-video-title="What Makes AI Human? | Fractal CEO Srikanth Velamakanni | ET AI Podcast" data-video-dur="32:05">
              <div class="f-series-thumb-wrap">
                <img src="podcast/qi4SZeSOsFc-HD.jpg" alt="What Makes AI Human? Fractal CEO Srikanth Velamakanni" class="f-series-img" loading="lazy">
                <div class="f-thumb-overlay-gradient"></div>
                <button class="f-play-circle f-play-big" aria-label="Play Episode">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                </button>
              </div>

              <div class="f-series-content">
                <div class="series-tag-red">
                  <svg class="mic-svg" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5-3c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/>
                  </svg>
                  <span>IN CONVERSATION</span>
                </div>
                <h3 class="f-series-title">
                  <a href="#pod-fractal">What Makes AI Human? | Fractal CEO Srikanth Velamakanni | ET AI Podcast</a>
                </h3>
                <p class="f-series-desc">
                  Fractal CEO Srikanth Velamakanni delves into cognitive AI architectures, autonomous decision-making, and what defines human empathy versus algorithmic intelligence.
                </p>
              </div>
            </article>

            <!-- Card 3 (Right): Arundhati Bhattacharya -->
            <article class="f-series-card video-card" data-video-title="Managing 270K Humans vs AI Agents | Arundhati Bhattacharya | ET AI Podcast" data-video-dur="28:40">
              <div class="f-series-thumb-wrap">
                <img src="podcast/Zmx8xhsB66A-HD.jpg" alt="Managing 270K Humans vs AI Agents | Arundhati Bhattacharya" class="f-series-img" loading="lazy">
                <div class="f-thumb-overlay-gradient"></div>
                <button class="f-play-circle" aria-label="Play Episode">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                </button>
              </div>

              <div class="f-series-content">
                <div class="series-tag-red">
                  <svg class="mic-svg" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5-3c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/>
                  </svg>
                  <span>IN CONVERSATION</span>
                </div>
                <h3 class="f-series-title">
                  <a href="#pod-arundhati">Managing 270K Humans vs AI Agents | Arundhati Bhattacharya | ET AI Podcast</a>
                </h3>
                <p class="f-series-desc">
                  Salesforce South Asia CEO Arundhati Bhattacharya on leadership at scale, AI ethics, and the co-existence of massive human workforces with agentic AI systems.
                </p>
              </div>
            </article>

          </div>

          <!-- Page 2 (Rotated when clicking NEXT) -->
          <div class="featured-series-grid f-series-page" id="fSeriesPage2" style="display: none;">
            
            <!-- Card 4 (Left): Andrew Ng on AI Panic = Billions -->
            <article class="f-series-card video-card" data-video-title="AI Panic = Billions: The Economics of Fear & Hype | Andrew Ng | ET AI Podcast" data-video-dur="35:10">
              <div class="f-series-thumb-wrap">
                <img src="podcast/IKExqTIRTVg-HD.jpg" alt="AI Panic = Billions | Andrew Ng" class="f-series-img" loading="lazy">
                <div class="f-thumb-overlay-gradient"></div>
                <button class="f-play-circle" aria-label="Play Episode">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                </button>
              </div>
              <div class="f-series-content">
                <div class="series-tag-red">
                  <svg class="mic-svg" width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5-3c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/></svg>
                  <span>IN CONVERSATION</span>
                </div>
                <h3 class="f-series-title">
                  <a href="#pod-andrew-1">AI Panic = Billions: The Economics of Fear &amp; Hype | Andrew Ng | ET AI Podcast</a>
                </h3>
                <p class="f-series-desc">
                  AI pioneer Andrew Ng analyzes who truly profits from apocalyptic AI narratives, why open-source models remain vital, and where capital is generating real value.
                </p>
              </div>
            </article>

            <!-- Card 5 (Center / Prominent): Who Profits From AI Fear -->
            <article class="f-series-card f-series-card-center video-card" data-video-title="Who Profits From AI Fear? | Andrew Ng on Silicon Valley & AI Reality | ET AI Podcast" data-video-dur="31:22">
              <div class="f-series-thumb-wrap">
                <img src="podcast/VNDkAsjhe5Y-SD.jpg" alt="Who Profits From AI Fear? Andrew Ng & Deepak Ajwani" class="f-series-img" loading="lazy">
                <div class="f-thumb-overlay-gradient"></div>
                <button class="f-play-circle f-play-big" aria-label="Play Episode">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                </button>
              </div>
              <div class="f-series-content">
                <div class="series-tag-red">
                  <svg class="mic-svg" width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5-3c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/></svg>
                  <span>IN CONVERSATION</span>
                </div>
                <h3 class="f-series-title">
                  <a href="#pod-andrew-2">Who Profits From AI Fear? | Andrew Ng on Silicon Valley &amp; AI Reality</a>
                </h3>
                <p class="f-series-desc">
                  Andrew Ng in conversation with Deepak Ajwani on the geopolitical arms race in compute, safety regulations, and cutting through corporate fear-mongering.
                </p>
              </div>
            </article>

            <!-- Card 6 (Right): Frontier AI Agents -->
            <article class="f-series-card video-card" data-video-title="Autonomous Agent Workflows: From Prompt Engineering to Frontier Action | ET AI Podcast" data-video-dur="27:45">
              <div class="f-series-thumb-wrap">
                <img src="podcast/H6_XWlcp7O8-HD.jpg" alt="Autonomous AI Agents in Action" class="f-series-img" loading="lazy">
                <div class="f-thumb-overlay-gradient"></div>
                <button class="f-play-circle" aria-label="Play Episode">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                </button>
              </div>
              <div class="f-series-content">
                <div class="series-tag-red">
                  <svg class="mic-svg" width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5-3c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/></svg>
                  <span>IN CONVERSATION</span>
                </div>
                <h3 class="f-series-title">
                  <a href="#pod-agents">Autonomous Agent Workflows: From Prompt Engineering to Frontier Action</a>
                </h3>
                <p class="f-series-desc">
                  Inside the next era of enterprise automation: how self-correcting agent chains and multi-modal models are taking over routine corporate operations.
                </p>
              </div>
            </article>

          </div>
        </div>

        <!-- Centered Navigation Buttons (Exact Reference Screenshot) -->
        <div class="featured-series-nav-row">
          <button class="f-series-btn" id="fSeriesPrevBtn" aria-label="Previous Episodes">
            <span class="arr">&larr;</span> BACK
          </button>
          <button class="f-series-btn" id="fSeriesNextBtn" aria-label="Next Episodes">
            NEXT <span class="arr">&rarr;</span>
          </button>
        </div>

      </div>
    </section>

  </main>

  <!-- Global Footer -->
  <footer class="site-footer">
    <div class="footer-inner container-fit">
      <div class="footer-top">
        <div class="footer-brand">
          <div class="brand-logo footer-logo">
            <span class="et-badge">ET</span>
            <span class="logo-world">WORLD</span>
          </div>
          <p class="footer-tagline">The Economic Times – India's Leading Business Newspaper &amp; Global Financial Authority.</p>
        </div>
        <div class="footer-newsletter">
          <h4>Get the ET World Global Morning Briefing</h4>
          <p>Hand-curated geopolitical intelligence and market insights delivered to your inbox daily.</p>
          <form class="newsletter-form" id="newsletterForm" onsubmit="event.preventDefault(); window.handleNewsletterSubmit();">
            <input type="email" placeholder="Enter your business email…" required id="newsletterEmail">
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-copyright">
          © 2026 Bennett, Coleman &amp; Co. Ltd. All rights reserved. For reprint rights: Times Syndication Service.
        </div>
        <div class="footer-legal-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Use</a>
          <a href="#">Grievance Redressal</a>
          <a href="#">Sitemap</a>
          <a href="#">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Search Modal Overlay -->
  <div class="search-modal-backdrop" id="searchModal">
    <div class="search-modal-box">
      <div class="search-modal-header">
        <svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text" id="modalSearchInput" placeholder="Search ET World news, topics, summit..." autofocus>
        <button class="modal-close-btn" id="modalCloseBtn">&times;</button>
      </div>
      <div class="search-modal-results" id="searchResultsList">
        <div class="search-hint">Type to instantly filter stories across all categories...</div>
      </div>
    </div>
  </div>

  <!-- Video Playback Modal -->
  <div class="video-modal-backdrop" id="videoModal">
    <div class="video-modal-box">
      <div class="video-modal-header">
        <span class="video-modal-title" id="videoModalTitle">Featured Video</span>
        <button class="modal-close-btn" id="videoModalCloseBtn">&times;</button>
      </div>
      <div class="video-player-container">
        <div class="simulated-player" id="simulatedPlayer">
          <div class="video-player-overlay">
            <button class="big-play-btn" id="playerPlayBtn">▶</button>
            <div class="player-controls">
              <button class="ctrl-btn" id="ctrlPlayToggle">❚❚ Pause</button>
              <div class="progress-bar-wrap">
                <div class="progress-bar-fill" id="progressFill"></div>
              </div>
              <span class="time-display" id="playerTime">02:15 / 08:42</span>
              <button class="ctrl-btn" id="ctrlMute">🔊</button>
              <button class="ctrl-btn" id="ctrlFullscreen">⛶</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- =====================================================================
       INTERACTIVE MODAL 1: OFFICIAL ET SIGN IN MODAL
       ===================================================================== -->
  <div class="site-modal-backdrop" id="etSignInModal" role="dialog" aria-modal="true" aria-labelledby="signInModalTitle">
    <div class="site-modal-box signin-box">
      <button class="modal-close-icon-btn" id="closeSignInModalBtn" aria-label="Close Sign In Modal">&times;</button>
      <div class="signin-header">
        <div class="signin-logo-badge">
          <span class="et-sq">ET</span>
          <span class="signin-brand-title">THE ECONOMIC TIMES</span>
        </div>
        <h3 id="signInModalTitle" class="signin-title">Sign in to your ET Account</h3>
        <p class="signin-desc">Access your personalized portfolio, real-time market alerts, premium ETPrime stories, and saved bookmarks.</p>
      </div>

      <div class="signin-form-wrap">
        <form id="signInForm" onsubmit="event.preventDefault(); window.handleSignInSubmit();">
          <label for="signInInput" class="signin-label">Mobile Number or Email Address</label>
          <div class="signin-input-group">
            <input type="text" id="signInInput" placeholder="Enter 10-digit mobile or email…" required autocomplete="username">
          </div>
          <button type="submit" class="signin-submit-btn" id="signInSubmitBtn">Continue with OTP / Password →</button>
        </form>

        <div class="signin-divider">
          <span>OR CONTINUE WITH</span>
        </div>

        <div class="signin-social-row">
          <button class="social-btn google-btn" id="signInGoogleBtn">
            <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/></svg>
            Google
          </button>
          <button class="social-btn apple-btn" id="signInAppleBtn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.37c.62-.75 1.04-1.8 0.92-2.85-.9.04-1.99.6-2.63 1.35-.57.65-1.06 1.72-.93 2.74 1.01.08 2.03-.5 2.64-1.24z"/></svg>
            Apple
          </button>
        </div>

        <div class="signin-perks">
          <div class="perk-item">✓ Sync portfolio across mobile &amp; web</div>
          <div class="perk-item">✓ Unlimited access to saved articles</div>
          <div class="perk-item">✓ Real-time breaking news notifications</div>
        </div>
      </div>
    </div>
  </div>

  <!-- =====================================================================
       INTERACTIVE MODAL 2: MY WATCHLIST MODAL
       ===================================================================== -->
  <div class="site-modal-backdrop" id="etWatchlistModal" role="dialog" aria-modal="true" aria-labelledby="watchlistModalTitle">
    <div class="site-modal-box watchlist-box">
      <button class="modal-close-icon-btn" id="closeWatchlistModalBtn" aria-label="Close Watchlist Modal">&times;</button>
      <div class="modal-inner-header">
        <div class="m-tag"><span class="live-dot-et"></span> LIVE PORTFOLIO</div>
        <h3 id="watchlistModalTitle" class="m-title">My Tracked Equities &amp; Funds</h3>
        <p class="m-subtitle">Real-time valuation updates and price movement alerts.</p>
      </div>

      <div class="watchlist-add-bar">
        <input type="text" id="watchlistSearchInput" placeholder="Add stock, ETF or mutual fund (e.g. INFY, HDFC)...">
        <button id="addWatchlistBtn">+ Add Symbol</button>
      </div>

      <div class="watchlist-items-list" id="watchlistItemsContainer">
        <div class="wl-row">
          <div class="wl-info">
            <strong class="wl-sym">SENSEX</strong>
            <span class="wl-sub">BSE Benchmark Index</span>
          </div>
          <div class="wl-metric">
            <span class="wl-price">72,792.48</span>
            <span class="wl-change down">↓ -456.90 (-0.62%)</span>
          </div>
        </div>
        <div class="wl-row">
          <div class="wl-info">
            <strong class="wl-sym">NIFTY 50</strong>
            <span class="wl-sub">NSE Benchmark Index</span>
          </div>
          <div class="wl-metric">
            <span class="wl-price">25,482.40</span>
            <span class="wl-change up">▲ +114.60 (+0.45%)</span>
          </div>
        </div>
        <div class="wl-row">
          <div class="wl-info">
            <strong class="wl-sym">UTI Aggressive Hybrid</strong>
            <span class="wl-sub">Mutual Fund · 5Y Return</span>
          </div>
          <div class="wl-metric">
            <span class="wl-price">₹348.62</span>
            <span class="wl-change up">▲ +8.69%</span>
          </div>
        </div>
        <div class="wl-row">
          <div class="wl-info">
            <strong class="wl-sym">RELIANCE</strong>
            <span class="wl-sub">Reliance Industries Ltd</span>
          </div>
          <div class="wl-metric">
            <span class="wl-price">₹2,842.10</span>
            <span class="wl-change up">▲ +18.40 (+0.65%)</span>
          </div>
        </div>
        <div class="wl-row">
          <div class="wl-info">
            <strong class="wl-sym">APPLE (AAPL)</strong>
            <span class="wl-sub">NASDAQ Global Select</span>
          </div>
          <div class="wl-metric">
            <span class="wl-price">$231.85</span>
            <span class="wl-change up">▲ +3.12 (+1.36%)</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- =====================================================================
       INTERACTIVE MODAL 3: LIVE MARKET DATA HUB
       ===================================================================== -->
  <div class="site-modal-backdrop" id="etMarketDataModal" role="dialog" aria-modal="true" aria-labelledby="marketDataModalTitle">
    <div class="site-modal-box marketdata-box">
      <button class="modal-close-icon-btn" id="closeMarketDataModalBtn" aria-label="Close Market Data Modal">&times;</button>
      <div class="modal-inner-header">
        <div class="m-tag"><span class="live-dot-et"></span> ET MARKETS LIVE</div>
        <h3 id="marketDataModalTitle" class="m-title">Comprehensive Global Market Data</h3>
        <p class="m-subtitle">Indices, commodities, bond yields, currencies and top movers.</p>
      </div>

      <div class="mdata-tabs" id="marketDataTabs">
        <button class="mdata-tab active" data-tab="indices">Major Indices</button>
        <button class="mdata-tab" data-tab="gainers">Top Gainers</button>
        <button class="mdata-tab" data-tab="losers">Top Losers</button>
        <button class="mdata-tab" data-tab="commodities">Commodities &amp; FX</button>
      </div>

      <div class="mdata-content" id="marketDataContent">
        <table class="mdata-table">
          <thead>
            <tr>
              <th>Instrument</th>
              <th>LTP</th>
              <th>Change</th>
              <th>% Change</th>
              <th>High</th>
              <th>Low</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>SENSEX</strong></td>
              <td>72,792.48</td>
              <td class="diff-dn">-456.90</td>
              <td class="diff-dn">-0.62%</td>
              <td>73,310.20</td>
              <td>72,680.15</td>
            </tr>
            <tr>
              <td><strong>NIFTY 50</strong></td>
              <td>25,482.40</td>
              <td class="diff-up">+114.60</td>
              <td class="diff-up">+0.45%</td>
              <td>25,510.80</td>
              <td>25,390.10</td>
            </tr>
            <tr>
              <td><strong>S&amp;P 500</strong></td>
              <td>5,864.67</td>
              <td class="diff-up">+23.25</td>
              <td class="diff-up">+0.40%</td>
              <td>5,872.10</td>
              <td>5,840.30</td>
            </tr>
            <tr>
              <td><strong>NASDAQ 100</strong></td>
              <td>20,385.12</td>
              <td class="diff-up">+145.20</td>
              <td class="diff-up">+0.72%</td>
              <td>20,410.50</td>
              <td>20,240.00</td>
            </tr>
            <tr>
              <td><strong>FTSE 100</strong></td>
              <td>8,243.80</td>
              <td class="diff-dn">-18.30</td>
              <td class="diff-dn">-0.22%</td>
              <td>8,265.40</td>
              <td>8,230.10</td>
            </tr>
            <tr>
              <td><strong>BRENT CRUDE</strong></td>
              <td>$74.28</td>
              <td class="diff-dn">-0.62</td>
              <td class="diff-dn">-0.83%</td>
              <td>$75.40</td>
              <td>$73.90</td>
            </tr>
            <tr>
              <td><strong>GOLD (10g)</strong></td>
              <td>₹78,450</td>
              <td class="diff-up">+240.00</td>
              <td class="diff-up">+0.31%</td>
              <td>₹78,600</td>
              <td>₹78,150</td>
            </tr>
            <tr>
              <td><strong>USD / INR</strong></td>
              <td>₹84.06</td>
              <td class="diff-up">+0.02</td>
              <td class="diff-up">+0.02%</td>
              <td>₹84.10</td>
              <td>₹84.02</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- =====================================================================
       INTERACTIVE MODAL 4: ET MASTERCLASS EXECUTIVE LEARNING
       ===================================================================== -->
  <div class="site-modal-backdrop" id="etMasterclassModal" role="dialog" aria-modal="true" aria-labelledby="masterclassModalTitle">
    <div class="site-modal-box masterclass-box">
      <button class="modal-close-icon-btn" id="closeMasterclassModalBtn" aria-label="Close Masterclass Modal">&times;</button>
      <div class="masterclass-header-banner">
        <div class="mc-tag">ET MASTERCLASS · EXECUTIVE EXCELLENCE</div>
        <h3 id="masterclassModalTitle" class="mc-title">Upskill with Global Business Pioneers</h3>
        <p class="mc-desc">Curated executive masterclasses with certificate from The Economic Times &amp; accredited global faculty.</p>
        <div class="mc-festive-badge">🎉 Festive Offer: Flat 50% Off on All Cohorts</div>
      </div>

      <div class="mc-grid">
        <div class="mc-card">
          <div class="mc-card-top">
            <span class="mc-badge">HOT &amp; TRENDING</span>
            <span class="mc-dur">4 Weeks · Live Online</span>
          </div>
          <h4 class="mc-name">Enterprise AI &amp; Generative Intelligence for C-Suite</h4>
          <p class="mc-fac"><strong>Faculty:</strong> Prof. Arvind Narayanan &amp; Silicon Valley AI Leaders</p>
          <ul class="mc-points">
            <li>Deploying autonomous multi-agent enterprise workflows</li>
            <li>Cost economics of LLMs &amp; private sovereign models</li>
            <li>Risk, IP governance, and board fiduciary compliance</li>
          </ul>
          <div class="mc-footer">
            <div class="mc-price-col">
              <span class="mc-cut-price">₹48,000</span>
              <strong class="mc-now-price">₹24,000</strong>
            </div>
            <button class="mc-enroll-btn" data-course="AI Strategy">Enroll Cohort →</button>
          </div>
        </div>

        <div class="mc-card">
          <div class="mc-card-top">
            <span class="mc-badge">EXECUTIVE COHORT</span>
            <span class="mc-dur">6 Weeks · Masterclass</span>
          </div>
          <h4 class="mc-name">Global Value Investing &amp; Corporate Capital Allocation</h4>
          <p class="mc-fac"><strong>Faculty:</strong> Prof. Aswath Damodaran (NYU Stern)</p>
          <ul class="mc-points">
            <li>Discounted cash flow, terminal multiple, and real options</li>
            <li>Deconstructing distressed and high-growth balance sheets</li>
            <li>Cross-border valuation across emerging and developed markets</li>
          </ul>
          <div class="mc-footer">
            <div class="mc-price-col">
              <span class="mc-cut-price">₹65,000</span>
              <strong class="mc-now-price">₹32,500</strong>
            </div>
            <button class="mc-enroll-btn" data-course="Value Investing">Enroll Cohort →</button>
          </div>
        </div>

        <div class="mc-card">
          <div class="mc-card-top">
            <span class="mc-badge">VENTURE &amp; M&amp;A</span>
            <span class="mc-dur">3 Weeks · Intensive</span>
          </div>
          <h4 class="mc-name">Venture Capital Deal Structuring &amp; Term Sheet Mastery</h4>
          <p class="mc-fac"><strong>Faculty:</strong> Former Sequoia &amp; Peak XV Partners</p>
          <ul class="mc-points">
            <li>Liquidation preferences, anti-dilution, and drag-along rights</li>
            <li>Modeling waterfall exit simulations for seed to pre-IPO</li>
            <li>Negotiation tact for founders and GP/LP syndicates</li>
          </ul>
          <div class="mc-footer">
            <div class="mc-price-col">
              <span class="mc-cut-price">₹42,000</span>
              <strong class="mc-now-price">₹21,000</strong>
            </div>
            <button class="mc-enroll-btn" data-course="VC Deal Structuring">Enroll Cohort →</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="toast-notification" id="toastNotice">Action confirmed!</div>

  <script src="app.js"></script>
</body>
</html>
"""

def build():
    print("[Python Builder] Writing index.html with ET World branding and strict border fitting...")
    with open(os.path.join(WORKSPACE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print("[Python Builder] index.html successfully generated.")

if __name__ == "__main__":
    build()
