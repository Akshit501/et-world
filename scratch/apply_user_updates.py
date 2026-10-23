import re
import os

workspace_dir = r"c:\Users\DELL\OneDrive\Desktop\et-usa"
build_site_path = os.path.join(workspace_dir, "build_site.py")

with open(build_site_path, "r", encoding="utf-8") as f:
    code = f.read()

# -------------------------------------------------------------------------
# 1. MOVE ET WORLD HEADER (<header class="hd" id="mainHeader">) TO GO ON TOP
# Currently:
# channel-bar -> et-masthead-section -> et-ticker-bar -> header.hd
# We move header.hd to go right after channel-bar:
# channel-bar -> header.hd (ET WORLD) -> et-masthead-section -> et-ticker-bar
# -------------------------------------------------------------------------

header_hd_pattern = r'(  <!-- Primary ET World Regional Navigation Header -->\s*<header class="hd" id="mainHeader">.*?</header>)'
m_hd = re.search(header_hd_pattern, code, re.DOTALL)
if m_hd:
    hd_block = m_hd.group(1)
    # Remove it from its current position
    code = code.replace(hd_block, "")
    # Insert it right after channel-bar (line ~129)
    ch_end = "</nav>\n"
    idx = code.find(ch_end)
    if idx != -1:
        code = code[:idx + len(ch_end)] + "\n" + hd_block + "\n" + code[idx + len(ch_end):]
        print("Moved ET WORLD header on top (right after channel-bar)!")

# -------------------------------------------------------------------------
# 2. REMOVE WATCH LIVE SECTION (<div class="summit-watch-live-banner" id="summitLiveBanner">)
# -------------------------------------------------------------------------
watch_live_pattern = r'    <!-- TOP LEADERBOARD: ET World Summit 2026 Watch Live Banner.*?    </div>\n'
m_wl = re.search(watch_live_pattern, code, re.DOTALL)
if m_wl:
    code = code.replace(m_wl.group(0), "")
    print("Removed summit watch live banner!")

# -------------------------------------------------------------------------
# 3. UPDATE TOP LEAD HERO CARD (change from Summit to Global ET World Exclusive)
# -------------------------------------------------------------------------
old_hero = """      <!-- Column 1 (Left): Stage Hero -->
      <article class="top-hero-card">
        <a href="#summit-lead" class="top-hero-media">
          <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=900&auto=format&fit=crop&q=80" alt="ET World Summit Stage" loading="eager">
          <div class="hero-live-pill">● LIVE IN NEW DELHI</div>
        </a>
        <h2 class="top-hero-title">
          <a href="#summit-lead">ET World Summit LIVE: Global Leaders To Discuss 'World Between Orders'</a>
        </h2>
        <p class="top-hero-excerpt">
          World leaders, global central bankers, and visionary tech founders assemble at the landmark ET World Summit 2026 to chart out resilient trade frameworks, sovereign AI infrastructure, and sustainable growth corridors.
        </p>
      </article>"""

new_hero = """      <!-- Column 1 (Left): ET World Global Lead Hero -->
      <article class="top-hero-card">
        <a href="#global-lead" class="top-hero-media">
          <img src="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=900&auto=format&fit=crop&q=80" alt="Global Trade and Financial Corridors" loading="eager">
          <div class="hero-live-pill">● ET WORLD EXCLUSIVE</div>
        </a>
        <h2 class="top-hero-title">
          <a href="#global-lead">Global Trade &amp; Capital Corridors: How Emerging Blocs Are Rewiring Cross-Border Finance</a>
        </h2>
        <p class="top-hero-excerpt">
          As central banks recalibrate monetary trajectories and sovereign trade routes realign across Asia, Europe, and the Americas, international institutions are establishing resilient financial architecture for a multipolar global economy.
        </p>
      </article>"""

if old_hero in code:
    code = code.replace(old_hero, new_hero)
    print("Updated top hero card to ET World Global Lead!")

# -------------------------------------------------------------------------
# 4. REMOVE ET WORLD SUMMIT 2026 SECTION (<section class="summit-hub-section" id="summit">)
# -------------------------------------------------------------------------
summit_sec_pattern = r'    <!-- =====================================================================\s*SECTION 2: ET WORLD SUMMIT 2026.*?    </section>\n'
m_summit = re.search(summit_sec_pattern, code, re.DOTALL)
if m_summit:
    code = code.replace(m_summit.group(0), "")
    print("Removed ET World Summit 2026 section!")

# -------------------------------------------------------------------------
# 5. REPLACE OFFBEAT SECTION WITH PANACHE SECTION (ET Panache)
# -------------------------------------------------------------------------
old_offbeat_pattern = r'    <!-- =====================================================================\s*SECTION 3: OFFBEAT ›.*?    </section>\n'
m_offbeat = re.search(old_offbeat_pattern, code, re.DOTALL)

panache_section = """    <!-- =====================================================================
         SECTION: PANACHE › (The Economic Times Panache)
         Luxury, Executive Living, Horology & Culture
         ===================================================================== -->
    <section class="portal-section panache-section" id="panache">
      <div class="sec-heading">
        <h2><a href="#panache">Panache <span class="sec-chevron">›</span></a></h2>
        <span class="panache-subtag">LUXURY, CULTURE &amp; EXECUTIVE LIVING</span>
      </div>
      <div class="panache-grid-3">
        
        <article class="panache-card">
          <a href="#panache-1" class="panache-media">
            <img src="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=600&auto=format&fit=crop&q=80" alt="Luxury Timepieces" loading="lazy">
            <span class="panache-pill">HOROLOGY &amp; WEALTH</span>
          </a>
          <h3 class="panache-title">
            <a href="#panache-1">Inside The Rare Patek Philippe &amp; Audemars Piguet Timepieces Driving Record Global Auctions</a>
          </h3>
          <p class="panache-excerpt">
            How vintage grand complications and sovereign collector demand turned high-end mechanical horology into a premier alternative asset class.
          </p>
        </article>

        <article class="panache-card">
          <a href="#panache-2" class="panache-media">
            <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=600&auto=format&fit=crop&q=80" alt="Billionaire Estates" loading="lazy">
            <span class="panache-pill">EXECUTIVE LIVING</span>
          </a>
          <h3 class="panache-title">
            <a href="#panache-2">The Rise Of Stealth-Wealth Real Estate: Why Global Titans Are Quietly Buying Ultra-Private Havens</a>
          </h3>
          <p class="panache-excerpt">
            From Lake Como villas to private New Zealand sanctuaries, high-net-worth executives prioritize autonomous estates with sovereign privacy.
          </p>
        </article>

        <article class="panache-card">
          <a href="#panache-3" class="panache-media">
            <img src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=600&auto=format&fit=crop&q=80" alt="Executive Longevity" loading="lazy">
            <span class="panache-pill">WELLNESS &amp; TECH</span>
          </a>
          <h3 class="panache-title">
            <a href="#panache-3">The $2-Million-A-Year Executive Longevity Protocol: What Silicon Valley Founders Swear By</a>
          </h3>
          <p class="panache-excerpt">
            Cellular biomarkers, hyperbaric oxygen therapy, and AI biological clocks replace traditional executive health routines.
          </p>
        </article>

      </div>
    </section>
"""

if m_offbeat:
    code = code.replace(m_offbeat.group(0), panache_section)
    print("Replaced Offbeat with Panache section!")

# -------------------------------------------------------------------------
# 6. REMOVE SHORTS SECTION
# -------------------------------------------------------------------------
shorts_pattern = r'    <!-- =====================================================================\s*SECTION 6: SHORTS ›.*?    </section>\n'
m_shorts = re.search(shorts_pattern, code, re.DOTALL)
if m_shorts:
    code = code.replace(m_shorts.group(0), "")
    print("Removed Shorts section!")

# -------------------------------------------------------------------------
# 7. ADD PODCASTS SECTION TO VIDEOS HUB
# -------------------------------------------------------------------------
old_videos_heading = '<h2><a href="#videos-all">Videos ›</a></h2>'
new_videos_heading = '<h2><a href="#videos-all">Videos &amp; Podcasts <span class="sec-chevron">›</span></a></h2>'
if old_videos_heading in code:
    code = code.replace(old_videos_heading, new_videos_heading)

# Add Podcasts pill in vbox-channel-bar if not present
old_channel_bar = """        <div class="vbox-channel-bar">
          <span class="vbox-pill active">Featured Video</span>"""

new_channel_bar = """        <div class="vbox-channel-bar">
          <span class="vbox-pill active">Featured Video</span>
          <span class="vbox-pill vbox-podcast-pill">🎙️ Podcasts</span>"""

if old_channel_bar in code:
    code = code.replace(old_channel_bar, new_channel_bar)

# Insert the Podcasts Showcase right after </aside> before </div> in videos-blue-box
old_vbox_end = """            </div>
          </aside>

        </div>
      </div>
    </section>"""

podcasts_showcase = """            </div>
          </aside>

        </div>

        <!-- ET Podcasts Showcase inside Videos Hub -->
        <div class="vbox-podcasts-showcase" id="podcasts-hub">
          <div class="vbox-podcasts-head">
            <div class="vbox-podcasts-title">
              <span class="podcast-mic-icon">🎙️</span>
              <h4>ET Podcasts</h4>
              <span class="podcast-subtext">Business Intelligence, Tech Frontiers &amp; Market Insights</span>
            </div>
            <a href="#podcasts-all" class="vbox-podcasts-more">All Episodes →</a>
          </div>

          <div class="podcasts-grid-4">
            
            <article class="podcast-card" data-podcast-title="The Morning Brief: India's Semiconductor Ambitions & The Global Chip Race" data-podcast-dur="24:18">
              <div class="podcast-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=300&auto=format&fit=crop&q=80" alt="The Morning Brief" class="podcast-thumb-img" loading="lazy">
                <button class="podcast-play-btn" aria-label="Play Episode">▶</button>
              </div>
              <div class="podcast-meta-row">
                <span class="podcast-show-name">The Morning Brief</span>
                <span class="podcast-dur-badge">24:18</span>
              </div>
              <h5 class="podcast-ep-title">
                <a href="#pod-1">The Semiconductor Race: India's Fab Ambitions &amp; Global Supply Chains</a>
              </h5>
              <div class="podcast-waveform">
                <span class="bar b1"></span><span class="bar b2"></span><span class="bar b3"></span><span class="bar b4"></span><span class="bar b5"></span>
              </div>
            </article>

            <article class="podcast-card" data-podcast-title="Market Makers: Global Equities & FII Capital Reallocation" data-podcast-dur="31:45">
              <div class="podcast-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=300&auto=format&fit=crop&q=80" alt="Market Makers" class="podcast-thumb-img" loading="lazy">
                <button class="podcast-play-btn" aria-label="Play Episode">▶</button>
              </div>
              <div class="podcast-meta-row">
                <span class="podcast-show-name">Market Makers</span>
                <span class="podcast-dur-badge">31:45</span>
              </div>
              <h5 class="podcast-ep-title">
                <a href="#pod-2">Global Valuations &amp; Central Bank Easing: Navigating Market Turbulence</a>
              </h5>
              <div class="podcast-waveform">
                <span class="bar b1"></span><span class="bar b2"></span><span class="bar b3"></span><span class="bar b4"></span><span class="bar b5"></span>
              </div>
            </article>

            <article class="podcast-card" data-podcast-title="Tech Tonic: Agentic AI & The Autonomous Enterprise" data-podcast-dur="19:22">
              <div class="podcast-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=300&auto=format&fit=crop&q=80" alt="Tech Tonic" class="podcast-thumb-img" loading="lazy">
                <button class="podcast-play-btn" aria-label="Play Episode">▶</button>
              </div>
              <div class="podcast-meta-row">
                <span class="podcast-show-name">Tech Tonic</span>
                <span class="podcast-dur-badge">19:22</span>
              </div>
              <h5 class="podcast-ep-title">
                <a href="#pod-3">Agentic AI in Enterprise: What Fortune 500 CTOs Are Deploying in 2026</a>
              </h5>
              <div class="podcast-waveform">
                <span class="bar b1"></span><span class="bar b2"></span><span class="bar b3"></span><span class="bar b4"></span><span class="bar b5"></span>
              </div>
            </article>

            <article class="podcast-card" data-podcast-title="The Global View: Geopolitics, Maritime Chokepoints & Energy Corridors" data-podcast-dur="22:50">
              <div class="podcast-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=300&auto=format&fit=crop&q=80" alt="The Global View" class="podcast-thumb-img" loading="lazy">
                <button class="podcast-play-btn" aria-label="Play Episode">▶</button>
              </div>
              <div class="podcast-meta-row">
                <span class="podcast-show-name">The Global View</span>
                <span class="podcast-dur-badge">22:50</span>
              </div>
              <h5 class="podcast-ep-title">
                <a href="#pod-4">Geopolitical Hotspots: Maritime Chokepoints &amp; Future Freight Trajectories</a>
              </h5>
              <div class="podcast-waveform">
                <span class="bar b1"></span><span class="bar b2"></span><span class="bar b3"></span><span class="bar b4"></span><span class="bar b5"></span>
              </div>
            </article>

          </div>
        </div>

      </div>
    </section>"""

if old_vbox_end in code:
    code = code.replace(old_vbox_end, podcasts_showcase)
    print("Added ET Podcasts Showcase to Videos section!")

# -------------------------------------------------------------------------
# 8. UPDATE DRAWER NAVIGATION
# -------------------------------------------------------------------------
old_drawer_sections = """      <h4 class="drawer-label">Sections</h4>
      <div class="drawer-links">
        <a href="#summit">ET World Summit 2026</a>
        <a href="#offbeat">Offbeat</a>
        <a href="#india-section">India News</a>
        <a href="#opinion">Opinion &amp; Blogs</a>
        <a href="#shorts-section">Shorts</a>
        <a href="#videos-section">Must Watch Videos</a>
      </div>"""

new_drawer_sections = """      <h4 class="drawer-label">Sections</h4>
      <div class="drawer-links">
        <a href="#panache">Panache (Executive Lifestyle)</a>
        <a href="#india-section">India News</a>
        <a href="#opinion">Opinion &amp; Blogs</a>
        <a href="#videos-section">Videos &amp; Podcasts</a>
        <a href="#science-knowledge">Science &amp; Knowledge</a>
        <a href="#india-global">India Global</a>
        <a href="#study-abroad">Study Abroad</a>
        <a href="#climate-environment">Climate &amp; Environment</a>
        <a href="#lifestyle">Lifestyle</a>
        <a href="#movies-entertainment">Movies &amp; Entertainment</a>
        <a href="#gadgets-tech">Gadgets &amp; Tech</a>
        <a href="#sports-section">Sports</a>
      </div>"""

if old_drawer_sections in code:
    code = code.replace(old_drawer_sections, new_drawer_sections)
    print("Updated drawer navigation links!")

with open(build_site_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved updated build_site.py!")
