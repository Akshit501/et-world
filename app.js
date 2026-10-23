/**
 * ET WORLD – Global News & Live Summit Intelligence
 * Interactive Application Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initDateClock();
  initSummitTabs();
  initSportsTabs();
  initVideoPlayerModal();
  initPodcastPlayer();
  initShortsPlayer();
  initSearch();
  initMobileDrawer();
  initInteractiveActions();
  initEditionNav();
  initMarketTicker();
  initMastheadMeta();
  initGutterAds();
  initScreenshotAds();
  initTopBarAndModals();
  initFeaturedSeriesPodcast();
});

/* ==========================================================================
   THEME CONTROLLER (Light / Dark Mode with Persistence)
   ========================================================================== */
function initTheme() {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const root = document.documentElement;

  const savedTheme = localStorage.getItem('et-theme') || localStorage.getItem('et-theme');
  if (savedTheme) {
    root.setAttribute('data-theme', savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    root.setAttribute('data-theme', 'dark');
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = root.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', newTheme);
      localStorage.setItem('et-theme', newTheme);
      showToast(`Switched to ${newTheme === 'dark' ? 'Dark' : 'Light'} Mode`);
    });
  }
}

/* ==========================================================================
   LIVE DATE & CLOCK
   ========================================================================== */
function initDateClock() {
  const dtEl = document.getElementById('headerDateTime');
  if (!dtEl) return;

  function updateTime() {
    const now = new Date();
    const options = {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    };
    const dateStr = now.toLocaleDateString('en-US', options);
    const timeStr = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
    dtEl.innerHTML = `${dateStr}<br><span class="header-time">${timeStr} IST</span>`;
  }

  updateTime();
  setInterval(updateTime, 60000);
}

/* ==========================================================================
   SUMMIT TABS CONTROLLER
   ========================================================================== */
function initSummitTabs() {
  const tabItems = document.querySelectorAll('#summitTabs .hub-tab, #summitTabs .tab-item');
  tabItems.forEach(tab => {
    tab.addEventListener('click', () => {
      tabItems.forEach(t => t.classList.remove('on'));
      tab.classList.add('on');
      const target = tab.dataset.tab;
      showToast(`Summit Tab: Showing ${target.replace('-', ' ').toUpperCase()}`);
    });
  });
}

/* ==========================================================================
   LIVE SPORTS SCORECARD TABS
   ========================================================================== */
function initSportsTabs() {
  const sportsTabs = document.querySelectorAll('#sportsTabs .tab-item');
  const stageEl = document.getElementById('matchStage');
  const t1El = document.getElementById('scoreTeam1');
  const t2El = document.getElementById('scoreTeam2');
  const noteEl = document.getElementById('matchSummaryNote');
  const refreshBtn = document.getElementById('scoreRefreshBtn');

  const sportsData = {
    all: {
      stage: 'Border-Gavaskar Trophy · Day 4',
      t1: '🇮🇳 IND 286/4 (82.1)',
      t2: '🇦🇺 AUS 312',
      note: 'India trail by 26 runs · K.L. Rahul 88* (142), Pant 42* (39)'
    },
    cricket: {
      stage: 'Border-Gavaskar Trophy · Day 4',
      t1: '🇮🇳 IND 286/4 (82.1)',
      t2: '🇦🇺 AUS 312',
      note: 'India trail by 26 runs · K.L. Rahul 88* (142), Pant 42* (39)'
    },
    football: {
      stage: 'UEFA Champions League · Group Stage',
      t1: '⚽ Real Madrid 2',
      t2: '⚽ Bayern Munich 1',
      note: '78th Min · Vinícius Jr 54\', Bellingham 71\' · Match Live'
    },
    f1: {
      stage: 'Austin GP · Final 10 Laps',
      t1: '🏎️ Norris (McLaren)',
      t2: '🏎️ Verstappen +1.42s',
      note: 'Lap 46/56 · Fastest Lap: Leclerc 1:37.442 · Pit stops complete'
    },
    tennis: {
      stage: 'ATP Masters 1000 · Semi-Final',
      t1: '🎾 Alcaraz 6  4  7 (7)',
      t2: '🎾 Sinner 4  6  6 (4)',
      note: 'Match Point Alcaraz · 3rd Set Tiebreak'
    }
  };

  sportsTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      if (tab.classList.contains('more-sports')) {
        showToast('More sports: Basketball, Badminton, Kabaddi');
        return;
      }
      sportsTabs.forEach(t => t.classList.remove('on'));
      tab.classList.add('on');

      const sportKey = tab.dataset.sport;
      if (sportsData[sportKey]) {
        const d = sportsData[sportKey];
        if (stageEl) stageEl.textContent = d.stage;
        if (t1El) t1El.textContent = d.t1;
        if (t2El) t2El.textContent = d.t2;
        if (noteEl) noteEl.textContent = d.note;
      }
    });
  });

  if (refreshBtn) {
    refreshBtn.addEventListener('click', () => {
      refreshBtn.textContent = '⏳ Refreshing...';
      setTimeout(() => {
        refreshBtn.textContent = '⚡ Refresh Commentary';
        if (t1El && t1El.textContent.includes('IND')) {
          t1El.textContent = '🇮🇳 IND 290/4 (82.5)';
          if (noteEl) noteEl.textContent = 'FOUR! Pant smashes through covers. India trail by 22 runs.';
        }
        showToast('Live scorecard updated with ball-by-ball commentary');
      }, 500);
    });
  }
}

/* ==========================================================================
   VIDEO PLAYER MODAL
   ========================================================================== */
function initVideoPlayerModal() {
  const modal = document.getElementById('videoModal');
  const closeBtn = document.getElementById('videoModalCloseBtn');
  const titleEl = document.getElementById('videoModalTitle');
  const playToggleBtn = document.getElementById('ctrlPlayToggle');
  const progressFill = document.getElementById('progressFill');
  const bigPlayBtn = document.getElementById('playerPlayBtn');

  let isPlaying = false;
  let progressInterval = null;
  let progressPct = 25;

  function openVideoModal(title, duration) {
    if (!modal) return;
    if (titleEl) titleEl.textContent = title || 'Featured Video';
    modal.classList.add('open');
    isPlaying = true;
    updatePlayState();
    startProgress();
  }

  function closeVideoModal() {
    if (!modal) return;
    modal.classList.remove('open');
    isPlaying = false;
    clearInterval(progressInterval);
  }

  function updatePlayState() {
    if (playToggleBtn) playToggleBtn.textContent = isPlaying ? '❚❚ Pause' : '▶ Play';
    if (bigPlayBtn) bigPlayBtn.style.display = isPlaying ? 'none' : 'grid';
  }

  function startProgress() {
    clearInterval(progressInterval);
    progressInterval = setInterval(() => {
      if (isPlaying) {
        progressPct = (progressPct + 0.5) % 100;
        if (progressFill) progressFill.style.width = `${progressPct}%`;
      }
    }, 500);
  }

  if (closeBtn) closeBtn.addEventListener('click', closeVideoModal);
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeVideoModal();
    });
  }

  if (playToggleBtn) {
    playToggleBtn.addEventListener('click', () => {
      isPlaying = !isPlaying;
      updatePlayState();
    });
  }

  if (bigPlayBtn) {
    bigPlayBtn.addEventListener('click', () => {
      isPlaying = true;
      updatePlayState();
    });
  }

  // Bind to all video cards
  document.querySelectorAll('.video-card, .vbox-main-video, .mw-item').forEach(card => {
    card.addEventListener('click', (e) => {
      e.preventDefault();
      const title = card.dataset.videoTitle || card.querySelector('h3, h4, h5, p')?.textContent || 'Featured Video';
      const dur = card.dataset.videoDur || '08:42';
      openVideoModal(title, dur);
    });
  });
}

/* ==========================================================================
   SHORTS PLAYER INTERACTION
   ========================================================================== */
function initShortsPlayer() {
  const shortItems = document.querySelectorAll('.short-reel-card, .short-item');
  shortItems.forEach(item => {
    item.addEventListener('click', () => {
      const title = item.dataset.shortTitle || item.querySelector('.short-caption, p')?.textContent.trim();
      showToast(`Playing Short: "${title}"`);
      const modal = document.getElementById('videoModal');
      const titleEl = document.getElementById('videoModalTitle');
      if (modal && titleEl) {
        titleEl.textContent = `ET World Shorts · ${title}`;
        modal.classList.add('open');
      }
    });
  });
}

/* ==========================================================================
   ET PODCASTS AUDIO INTERACTION
   ========================================================================== */
function initPodcastPlayer() {
  const podcastCards = document.querySelectorAll('.podcast-card');
  let currentPlayingBtn = null;

  podcastCards.forEach(card => {
    const playBtn = card.querySelector('.podcast-play-btn');
    const title = card.dataset.podcastTitle || card.querySelector('.podcast-ep-title')?.textContent.trim();
    const waveformBars = card.querySelectorAll('.podcast-waveform .bar');

    if (playBtn) {
      playBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const isCurrentlyPlaying = playBtn.textContent === '❚❚';

        // Reset any other playing card
        if (currentPlayingBtn && currentPlayingBtn !== playBtn) {
          currentPlayingBtn.textContent = '▶';
          const prevCard = currentPlayingBtn.closest('.podcast-card');
          if (prevCard) {
            prevCard.querySelectorAll('.podcast-waveform .bar').forEach(b => b.style.animation = 'none');
          }
        }

        if (isCurrentlyPlaying) {
          playBtn.textContent = '▶';
          waveformBars.forEach(b => b.style.animation = 'none');
          showToast(`Paused: "${title}"`);
          currentPlayingBtn = null;
        } else {
          playBtn.textContent = '❚❚';
          waveformBars.forEach((b, i) => {
            b.style.animation = `soundWave 0.8s ease-in-out infinite alternate ${i * 0.15}s`;
          });
          showToast(`🎙️ Playing: "${title}"`);
          currentPlayingBtn = playBtn;
        }
      });
    }
  });
}

/* ==========================================================================
   SEARCH SYSTEM (Modal & Instant Filtering)
   ========================================================================== */
function initSearch() {
  const searchTriggerBtn = document.getElementById('searchTriggerBtn') || document.getElementById('searchTrigger');
  const modal = document.getElementById('searchModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const input = document.getElementById('modalSearchInput');
  const resultsContainer = document.getElementById('searchResultsList');

  const articles = [];
  document.querySelectorAll('h2 a, h3 a, h4 a, h5, .top-hero-title a, .lead-item-title a, .sn-title a, .offbeat-title a, .india-item-headline a, .op-card-headline a, .tl-text a').forEach(el => {
    const text = el.textContent.trim();
    if (text && text.length > 5 && !articles.some(a => a.text === text)) {
      const parentCard = el.closest('article, .lead-list-item, .summit-news-card, .offbeat-card, .india-item, .opinion-author-card, .timeline-item');
      const img = parentCard?.querySelector('img')?.src || '';
      articles.push({ text, img, element: el });
    }
  });

  function openSearch() {
    if (!modal) return;
    modal.classList.add('open');
    if (input) {
      input.value = '';
      input.focus();
    }
    renderResults('');
  }

  function closeSearch() {
    if (!modal) return;
    modal.classList.remove('open');
  }

  function renderResults(query) {
    if (!resultsContainer) return;
    if (!query) {
      resultsContainer.innerHTML = `
        <div class="search-hint">
          <strong>Trending on ET World:</strong>
          <div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:8px;">
            <span class="srch-tag" style="background:var(--ph);padding:3px 8px;border-radius:2px;font-size:11px;cursor:pointer;">ET World Summit 2026</span>
            <span class="srch-tag" style="background:var(--ph);padding:3px 8px;border-radius:2px;font-size:11px;cursor:pointer;">Mohini Dey</span>
            <span class="srch-tag" style="background:var(--ph);padding:3px 8px;border-radius:2px;font-size:11px;cursor:pointer;">Trump India Deal</span>
            <span class="srch-tag" style="background:var(--ph);padding:3px 8px;border-radius:2px;font-size:11px;cursor:pointer;">Anthropic AI</span>
          </div>
        </div>
      `;
      resultsContainer.querySelectorAll('.srch-tag').forEach(tag => {
        tag.addEventListener('click', () => {
          if (input) input.value = tag.textContent;
          renderResults(tag.textContent);
        });
      });
      return;
    }

    const q = query.toLowerCase();
    const filtered = articles.filter(a => a.text.toLowerCase().includes(q));

    if (filtered.length === 0) {
      resultsContainer.innerHTML = `<div style="padding:20px;text-align:center;color:var(--mu);">No articles found matching "${query}". Try searching for Summit, Trump, or Markets.</div>`;
      return;
    }

    resultsContainer.innerHTML = filtered.map((item, idx) => `
      <div class="search-result-item" data-idx="${idx}">
        ${item.img ? `<img src="${item.img}" class="search-result-thumb" alt="thumbnail">` : ''}
        <div style="flex:1;">
          <div style="font-weight:600;font-size:13px;">${highlightMatch(item.text, query)}</div>
          <span style="font-size:10px;color:var(--mu);">ET World Special Coverage</span>
        </div>
      </div>
    `).join('');

    resultsContainer.querySelectorAll('.search-result-item').forEach((itemEl, idx) => {
      itemEl.addEventListener('click', () => {
        closeSearch();
        const matched = filtered[idx];
        if (matched && matched.element) {
          matched.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
          matched.element.style.outline = '2px solid var(--ac)';
          setTimeout(() => {
            matched.element.style.outline = 'none';
          }, 2500);
        }
      });
    });
  }

  function highlightMatch(text, query) {
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark style="background:#fff3b0;color:#111;padding:0 2px;">$1</mark>');
  }

  if (searchTriggerBtn) searchTriggerBtn.addEventListener('click', openSearch);
  if (closeBtn) closeBtn.addEventListener('click', closeSearch);

  if (input) {
    input.addEventListener('input', (e) => {
      renderResults(e.target.value.trim());
    });
  }

  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSearch();
    }
    if (e.key === 'Escape') {
      closeSearch();
      const videoModal = document.getElementById('videoModal');
      if (videoModal) videoModal.classList.remove('open');
    }
  });

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeSearch();
    });
  }
}

/* ==========================================================================
   MOBILE DRAWER NAVIGATION
   ========================================================================== */
function initMobileDrawer() {
  const menuBtn = document.getElementById('menuToggleBtn') || document.getElementById('mobileMenuBtn');
  const drawer = document.getElementById('mobileDrawer');
  const overlay = document.getElementById('drawerOverlay');
  const closeBtn = document.getElementById('drawerCloseBtn');

  function openDrawer() {
    if (drawer) drawer.classList.add('open');
    if (overlay) overlay.classList.add('open');
  }

  function closeDrawer() {
    if (drawer) drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
  }

  if (menuBtn) menuBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (overlay) overlay.addEventListener('click', closeDrawer);

  document.querySelectorAll('#mobileDrawer a').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });
}

/* ==========================================================================
   INTERACTIVE ACTIONS (Bookmarks, Profile, Channels)
   ========================================================================== */
function initInteractiveActions() {
  const bookmarkBtn = document.getElementById('headerBookmarkBtn');
  if (bookmarkBtn) {
    bookmarkBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('Bookmarks list opened. You have 3 saved stories.');
    });
  }

  const userProfileBtn = document.getElementById('userProfileBtn');
  if (userProfileBtn) {
    userProfileBtn.addEventListener('click', () => {
      showToast('ET World Sign-in / Profile modal opened.');
    });
  }

  // Network channel clicks
  document.querySelectorAll('.channel-links .ch-link').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      document.querySelectorAll('.channel-links .ch-link').forEach(l => l.classList.remove('on'));
      link.classList.add('on');
      showToast(`Navigated to ET ${link.textContent.trim()}`);
    });
  });
}

/* ==========================================================================
   EDITIONS SELECTOR
   ========================================================================== */
function initEditionNav() {
  const navLinks = document.querySelectorAll('#mainNav .nav-link');
  navLinks.forEach(link => {
    if (link.classList.contains('bookmark-icon')) return;
    link.addEventListener('click', (e) => {
      e.preventDefault();
      navLinks.forEach(l => l.classList.remove('on'));
      link.classList.add('on');
      const editionName = link.textContent.trim();
      showToast(`Switched Edition: ${editionName}`);
    });
  });
}

/* ==========================================================================
   NEWSLETTER
   ========================================================================== */
window.handleNewsletterSubmit = function() {
  const input = document.getElementById('newsletterEmail');
  if (input && input.value) {
    showToast(`Thank you! Morning briefing will be sent to ${input.value}`);
    input.value = '';
  }
};

/* ==========================================================================
   TOAST HELPER
   ========================================================================== */
let toastTimeout = null;
function showToast(message) {
  const toast = document.getElementById('toastNotice');
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add('show');
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 2800);
}

/* ==========================================================================
   ET LIVE MARKET TICKER SIMULATION
   ========================================================================== */
function initMarketTicker() {
  const tickerItems = document.querySelectorAll('.ticker-item, .et-ticker-item');
  if (!tickerItems.length) return;

  // Add click handler to each ticker item
  tickerItems.forEach(item => {
    item.addEventListener('click', () => {
      const name = item.querySelector('.t-name, .et-tick-name')?.textContent.trim() || 'Index';
      const val = item.querySelector('.t-val, .et-tick-val')?.textContent.trim() || '';
      const chg = item.querySelector('.t-change, .et-tick-chg')?.textContent.trim() || '';
      showToast(`${name}: ${val} (${chg}) · ET Markets Live Chart Opened`);
    });
  });

  // Micro-fluctuation simulation every 5 seconds for realism
  setInterval(() => {
    const randomIdx = Math.floor(Math.random() * tickerItems.length);
    const target = tickerItems[randomIdx];
    if (!target) return;
    const valEl = target.querySelector('.t-val, .et-tick-val');
    if (!valEl) return;
    
    // Pulse animation
    target.style.transition = 'background-color 0.4s ease';
    target.style.backgroundColor = 'rgba(237, 25, 59, 0.08)';
    setTimeout(() => {
      target.style.backgroundColor = '';
    }, 700);
  }, 4500);
}



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

/* ==========================================================================
   TOP BAR & INTERACTIVE MODALS CONTROLLER (Reference image copy 2.png)
   ========================================================================== */
function initTopBarAndModals() {
  // Modal Elements
  const signInModal = document.getElementById('etSignInModal');
  const watchlistModal = document.getElementById('etWatchlistModal');
  const marketDataModal = document.getElementById('etMarketDataModal');
  const masterclassModal = document.getElementById('etMasterclassModal');
  const allModals = [signInModal, watchlistModal, marketDataModal, masterclassModal].filter(Boolean);

  function openModal(modal) {
    if (!modal) return;
    allModals.forEach(m => m.classList.remove('open'));
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal(modal) {
    if (!modal) return;
    modal.classList.remove('open');
    const anyStillOpen = allModals.some(m => m.classList.contains('open'));
    if (!anyStillOpen) {
      document.body.style.overflow = '';
    }
  }

  function closeAllModals() {
    allModals.forEach(m => m.classList.remove('open'));
    document.body.style.overflow = '';
  }

  // Bind close buttons
  document.getElementById('closeSignInModalBtn')?.addEventListener('click', () => closeModal(signInModal));
  document.getElementById('closeWatchlistModalBtn')?.addEventListener('click', () => closeModal(watchlistModal));
  document.getElementById('closeMarketDataModalBtn')?.addEventListener('click', () => closeModal(marketDataModal));
  document.getElementById('closeMasterclassModalBtn')?.addEventListener('click', () => closeModal(masterclassModal));

  // Close on outside click
  allModals.forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal(modal);
      }
    });
  });

  // Close on Escape key
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllModals();
    }
  });

  // Top Search Pill Interaction
  const topSearchInput = document.getElementById('topSearchInput');
  const searchModal = document.getElementById('searchModal');
  const modalSearchInput = document.getElementById('modalSearchInput');

  if (topSearchInput) {
    topSearchInput.addEventListener('focus', () => {
      if (searchModal) {
        searchModal.classList.add('open');
        if (modalSearchInput) {
          modalSearchInput.value = topSearchInput.value;
          modalSearchInput.focus();
        }
      }
    });

    topSearchInput.addEventListener('input', (e) => {
      if (searchModal) {
        searchModal.classList.add('open');
        if (modalSearchInput) {
          modalSearchInput.value = e.target.value;
          modalSearchInput.focus();
          modalSearchInput.dispatchEvent(new Event('input'));
        }
      }
    });
  }

  // Benchmarks Live Trigger -> Market Data Modal
  const topSensexBenchmark = document.getElementById('topSensexBenchmark');
  if (topSensexBenchmark) {
    topSensexBenchmark.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(marketDataModal);
    });
  }

  // Category Bar "Market Data" Button -> Market Data Modal
  const catMarketDataBtn = document.getElementById('catMarketDataBtn');
  if (catMarketDataBtn) {
    catMarketDataBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(marketDataModal);
    });
  }

  // Category Bar "Masterclass" Button -> Masterclass Modal
  const catMasterclassBtn = document.getElementById('catMasterclassBtn');
  if (catMasterclassBtn) {
    catMasterclassBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(masterclassModal);
    });
  }

  // Masthead Sign In Button -> Sign In Modal
  const mastheadSignInBtn = document.getElementById('mastheadSignInBtn');
  if (mastheadSignInBtn) {
    mastheadSignInBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(signInModal);
    });
  }

  // Masthead Watchlist Button -> Watchlist Modal
  const mastheadWatchlistBtn = document.getElementById('mastheadWatchlistBtn');
  if (mastheadWatchlistBtn) {
    mastheadWatchlistBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal(watchlistModal);
    });
  }

  // Featured Fund Invest Button
  const fundInvestBtn = document.getElementById('fundInvestBtn');
  if (fundInvestBtn) {
    fundInvestBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('📈 UTI Aggressive Hybrid: Instant SIP / Lump Sum portal loaded.');
    });
  }

  // Festive Sale Link
  const festiveSaleLink = document.getElementById('festiveSaleLink');
  if (festiveSaleLink) {
    festiveSaleLink.addEventListener('click', (e) => {
      e.preventDefault();
      showToast('🎉 Mega Festive Sale: 50% discount coupon applied on ETPrime Annual Plan!');
    });
  }

  // Watchlist Add Symbol Interaction
  const watchlistAddBtn = document.getElementById('addWatchlistBtn');
  const watchlistSearchInput = document.getElementById('watchlistSearchInput');
  const watchlistItemsContainer = document.getElementById('watchlistItemsContainer');

  if (watchlistAddBtn && watchlistSearchInput && watchlistItemsContainer) {
    function addSymbol() {
      const sym = watchlistSearchInput.value.trim().toUpperCase();
      if (!sym) return;

      const randomPrice = (Math.random() * 2000 + 100).toFixed(2);
      const isUp = Math.random() > 0.4;
      const changePct = (Math.random() * 2.5).toFixed(2);

      const row = document.createElement('div');
      row.className = 'wl-row';
      row.innerHTML = `
        <div class="wl-info">
          <strong class="wl-sym">${sym}</strong>
          <span class="wl-sub">Tracked Symbol · Live Feed</span>
        </div>
        <div class="wl-metric">
          <span class="wl-price">₹${randomPrice}</span>
          <span class="wl-change ${isUp ? 'up' : 'down'}">${isUp ? '▲ +' : '↓ -'}${changePct}%</span>
        </div>
      `;
      watchlistItemsContainer.prepend(row);
      watchlistSearchInput.value = '';
      showToast(`Added ${sym} to your active Watchlist!`);
    }

    watchlistAddBtn.addEventListener('click', addSymbol);
    watchlistSearchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        addSymbol();
      }
    });
  }

  // Market Data Modal Tabs Interaction
  const mdataTabs = document.querySelectorAll('#marketDataTabs .mdata-tab');
  const mdataContent = document.getElementById('marketDataContent');

  const marketDatasets = {
    indices: `
      <table class="mdata-table">
        <thead>
          <tr><th>Instrument</th><th>LTP</th><th>Change</th><th>% Change</th><th>High</th><th>Low</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>SENSEX</strong></td><td>72,792.48</td><td class="diff-dn">-456.90</td><td class="diff-dn">-0.62%</td><td>73,310.20</td><td>72,680.15</td></tr>
          <tr><td><strong>NIFTY 50</strong></td><td>25,482.40</td><td class="diff-up">+114.60</td><td class="diff-up">+0.45%</td><td>25,510.80</td><td>25,390.10</td></tr>
          <tr><td><strong>S&amp;P 500</strong></td><td>5,864.67</td><td class="diff-up">+23.25</td><td class="diff-up">+0.40%</td><td>5,872.10</td><td>5,840.30</td></tr>
          <tr><td><strong>NASDAQ 100</strong></td><td>20,385.12</td><td class="diff-up">+145.20</td><td class="diff-up">+0.72%</td><td>20,410.50</td><td>20,240.00</td></tr>
          <tr><td><strong>FTSE 100</strong></td><td>8,243.80</td><td class="diff-dn">-18.30</td><td class="diff-dn">-0.22%</td><td>8,265.40</td><td>8,230.10</td></tr>
        </tbody>
      </table>
    `,
    gainers: `
      <table class="mdata-table">
        <thead>
          <tr><th>Stock</th><th>LTP</th><th>Change</th><th>% Change</th><th>Volume</th><th>Sector</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>TATA MOTORS</strong></td><td>₹984.50</td><td class="diff-up">+45.20</td><td class="diff-up">+4.81%</td><td>14.2M</td><td>Auto</td></tr>
          <tr><td><strong>ADANI PORTS</strong></td><td>₹1,420.10</td><td class="diff-up">+53.40</td><td class="diff-up">+3.91%</td><td>8.6M</td><td>Infra</td></tr>
          <tr><td><strong>SUN PHARMA</strong></td><td>₹1,745.00</td><td class="diff-up">+54.10</td><td class="diff-up">+3.20%</td><td>4.1M</td><td>Pharma</td></tr>
          <tr><td><strong>COAL INDIA</strong></td><td>₹512.30</td><td class="diff-up">+14.20</td><td class="diff-up">+2.85%</td><td>11.0M</td><td>Energy</td></tr>
        </tbody>
      </table>
    `,
    losers: `
      <table class="mdata-table">
        <thead>
          <tr><th>Stock</th><th>LTP</th><th>Change</th><th>% Change</th><th>Volume</th><th>Sector</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>INFOSYS</strong></td><td>₹1,842.00</td><td class="diff-dn">-39.50</td><td class="diff-dn">-2.10%</td><td>9.4M</td><td>IT Services</td></tr>
          <tr><td><strong>WIPRO</strong></td><td>₹528.10</td><td class="diff-dn">-9.70</td><td class="diff-dn">-1.80%</td><td>6.2M</td><td>IT Services</td></tr>
          <tr><td><strong>HDFC BANK</strong></td><td>₹1,678.40</td><td class="diff-dn">-25.60</td><td class="diff-dn">-1.50%</td><td>18.1M</td><td>Banking</td></tr>
          <tr><td><strong>AXIS BANK</strong></td><td>₹1,180.20</td><td class="diff-dn">-14.30</td><td class="diff-dn">-1.20%</td><td>7.9M</td><td>Banking</td></tr>
        </tbody>
      </table>
    `,
    commodities: `
      <table class="mdata-table">
        <thead>
          <tr><th>Commodity / FX</th><th>LTP</th><th>Change</th><th>% Change</th><th>Unit</th><th>Trend</th></tr>
        </thead>
        <tbody>
          <tr><td><strong>BRENT CRUDE</strong></td><td>$74.28</td><td class="diff-dn">-0.62</td><td class="diff-dn">-0.83%</td><td>Barrel</td><td>Bearish</td></tr>
          <tr><td><strong>GOLD (10g)</strong></td><td>₹78,450</td><td class="diff-up">+240.00</td><td class="diff-up">+0.31%</td><td>10 Grams</td><td>Bullish</td></tr>
          <tr><td><strong>SILVER (1kg)</strong></td><td>₹94,800</td><td class="diff-up">+650.00</td><td class="diff-up">+0.69%</td><td>1 Kg</td><td>Bullish</td></tr>
          <tr><td><strong>USD / INR</strong></td><td>₹84.06</td><td class="diff-up">+0.02</td><td class="diff-up">+0.02%</td><td>Currency</td><td>Stable</td></tr>
          <tr><td><strong>EUR / INR</strong></td><td>₹91.24</td><td class="diff-dn">-0.18</td><td class="diff-dn">-0.20%</td><td>Currency</td><td>Mild Soft</td></tr>
        </tbody>
      </table>
    `
  };

  mdataTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      mdataTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const category = tab.dataset.tab;
      if (mdataContent && marketDatasets[category]) {
        mdataContent.innerHTML = marketDatasets[category];
      }
    });
  });

  // Masterclass Cohort Enrollment buttons
  document.querySelectorAll('.mc-enroll-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const course = btn.dataset.course || 'Executive Program';
      showToast(`🎓 Enrolled in "${course}" with Flat 50% Festive Discount applied!`);
      closeModal(masterclassModal);
    });
  });

  // Sign In Form Submission
  window.handleSignInSubmit = function() {
    const input = document.getElementById('signInInput');
    const val = input ? input.value.trim() : '';
    showToast(`✓ Welcome to The Economic Times! Verification code sent to ${val || 'your device'}.`);
    setTimeout(() => {
      closeModal(signInModal);
      if (input) input.value = '';
    }, 1200);
  };

  // Social Sign In buttons
  document.getElementById('signInGoogleBtn')?.addEventListener('click', () => {
    showToast('✓ Signed in successfully with Google account.');
    setTimeout(() => closeModal(signInModal), 1000);
  });

  document.getElementById('signInAppleBtn')?.addEventListener('click', () => {
    showToast('✓ Signed in successfully with Apple ID.');
    setTimeout(() => closeModal(signInModal), 1000);
  });
}

/* ==========================================================================
   FEATURED SERIES PODCAST CONTROLLER (Reference Image)
   Controls 2-page podcast rotation with ← BACK and NEXT → pill buttons,
   and hooks up player modal with episode playback.
   ========================================================================== */
function initFeaturedSeriesPodcast() {
  const prevBtn = document.getElementById('fSeriesPrevBtn');
  const nextBtn = document.getElementById('fSeriesNextBtn');
  const page1 = document.getElementById('fSeriesPage1');
  const page2 = document.getElementById('fSeriesPage2');

  let activePage = 1;

  function switchPage(targetPage) {
    if (targetPage === activePage) return;

    const fromEl = activePage === 1 ? page1 : page2;
    const toEl = targetPage === 1 ? page1 : page2;

    if (!fromEl || !toEl) return;

    // Fade out current
    fromEl.style.opacity = '0';
    fromEl.style.transform = targetPage > activePage ? 'translateX(-20px)' : 'translateX(20px)';

    setTimeout(() => {
      fromEl.style.display = 'none';
      toEl.style.display = 'grid';
      toEl.style.opacity = '0';
      toEl.style.transform = targetPage > activePage ? 'translateX(20px)' : 'translateX(-20px)';

      // Trigger reflow
      void toEl.offsetWidth;

      toEl.style.opacity = '1';
      toEl.style.transform = 'translateX(0)';
      activePage = targetPage;

      if (typeof showToast === 'function') {
        const desc = activePage === 1 ? 'Page 1: AI Agents & Enterprise Transformation' : 'Page 2: Compute Missions & Semiconductor Fabs';
        showToast(`🎙️ Featured Series: ${desc}`);
      }
    }, 200);
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      const nextP = activePage === 1 ? 2 : 1;
      switchPage(nextP);
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      const prevP = activePage === 2 ? 1 : 2;
      switchPage(prevP);
    });
  }

  // Hook all featured series cards to video/podcast modal
  document.querySelectorAll('.f-series-card').forEach(card => {
    card.addEventListener('click', (e) => {
      // Prevent double firing if clicking a link
      if (e.target.tagName.toLowerCase() === 'a') {
        e.preventDefault();
      }
      const title = card.dataset.videoTitle || card.querySelector('.f-series-title')?.textContent.trim() || 'ET AI Podcast';
      const dur = card.dataset.videoDur || '28:00';

      const modal = document.getElementById('videoModal');
      const titleEl = document.getElementById('videoModalTitle');
      if (modal && titleEl) {
        titleEl.textContent = `🎙️ ET In Conversation: ${title}`;
        modal.classList.add('open');
      }

      if (typeof showToast === 'function') {
        showToast(`▶ Playing: "${title.slice(0, 45)}..." (${dur})`);
      }
    });
  });
}
