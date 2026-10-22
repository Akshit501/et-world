# Helper to generate the exact HTML for the requested sections

sections_html = """
    <!-- =====================================================================
         SECTION: SCIENCE & KNOWLEDGE › (Below Videos)
         4 Cards Across in Responsive Grid
         ===================================================================== -->
    <section class="portal-section science-knowledge-section" id="science-knowledge">
      <div class="sec-heading">
        <h2><a href="#science-knowledge">Science &amp; Knowledge <span class="sec-chevron">›</span></a></h2>
      </div>
      <div class="science-grid-4">
        
        <!-- Card 1: Planetary Parade -->
        <article class="science-card">
          <a href="#sk-1" class="science-media">
            <img src="https://c.ndtvimg.com/2026-02/kmtf2d7c_solar-system_625x300_19_February_26.jpeg?downsize=450:280&w=450" alt="Planetary Parade" loading="lazy">
          </a>
          <h3 class="science-title">
            <a href="#sk-1">Planetary Parade In February 2026: How And When To Watch Rare Alignment</a>
          </h3>
        </article>

        <!-- Card 2: NASA Auroras -->
        <article class="science-card">
          <a href="#sk-2" class="science-media">
            <img src="https://c.ndtvimg.com/2026-02/57tmoo6s_nasa_625x300_19_February_26.jpeg?downsize=450:280&w=450" alt="NASA Green Auroras" loading="lazy">
          </a>
          <h3 class="science-title">
            <a href="#sk-2">NASA Shares Photo Of Dazzling Green Auroras Captured From Space Station</a>
          </h3>
        </article>

        <!-- Card 3: Ice World Waves -->
        <article class="science-card">
          <a href="#sk-3" class="science-media">
            <img src="https://c.ndtvimg.com/2026-02/j1ognud4_enceladus_625x300_18_February_26.jpeg?downsize=450:280&w=450" alt="Electromagnetic Waves Ice World" loading="lazy">
          </a>
          <h3 class="science-title">
            <a href="#sk-3">Scientists Uncover Vast Web Of Hidden Electromagnetic Waves Around Tiny Ice World</a>
          </h3>
        </article>

        <!-- Card 4: Light Therapy Hair Loss -->
        <article class="science-card">
          <a href="#sk-4" class="science-media">
            <img src="https://c.ndtvimg.com/2026-02/fo8n2pk8_hair-loss_625x300_18_February_26.jpg?downsize=450:280&w=450" alt="Light Therapy Science" loading="lazy">
          </a>
          <h3 class="science-title">
            <a href="#sk-4">Korean Scientists Develop Light Therapy That Cuts Hair Loss Marker By 92%</a>
          </h3>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         DUO PLAYCARD 1: INDIA GLOBAL & STUDY ABROAD (Side by Side Playcard)
         ===================================================================== -->
    <section class="portal-section duo-playcard-section" id="india-global-study-abroad">
      <div class="duo-playcard-grid">
        
        <!-- Left Playcard: India Global -->
        <div class="duo-playcard-col">
          <div class="playcard-sec-head">
            <a href="#india-global">India Global <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <!-- Featured Card Left -->
            <article class="playcard-featured">
              <a href="#ig-feat" class="playcard-feat-media">
                <img src="https://c.ndtvimg.com/2026-10/7oc1584s_ndtv-world-summit-2026_625x300_22_October_26.png?im=FitAndFill,algorithm=dnn,width=640,height=400" alt="India Global Role" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#ig-feat">Live: Industry Experts Decode India's Growing Role In Shaping Future At ET World Summit</a>
              </h3>
            </article>

            <!-- Stacked List Right -->
            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#ig-1" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/rlgqdq7k_alain-ebobisse_625x300_21_October_26.jpeg" alt="Alain Ebobisse" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ig-1">Alain Ebobisse, Africa50 CEO, On India's Role In Developing Africa</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#ig-2" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/43spgnuo_david-petraeus_625x300_20_October_26.jpeg" alt="David Petraeus" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ig-2">Ex-CIA Director To Decode 'War In Times Of AI' At Global Forum</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#ig-3" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2025-10/hsrfqeqo_ge-aerospace-vikram-rai-ndtv-world-summit_650x400_17_October_25.jpg?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="Vikram Rai" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ig-3">Who Is Vikram Rai, CEO South Asia GE Aerospace, Shaping Aviation Corridors</a>
                </h4>
              </article>

            </div>

          </div>
        </div>

        <!-- Right Playcard: Study Abroad -->
        <div class="duo-playcard-col">
          <div class="playcard-sec-head">
            <a href="#study-abroad">Study Abroad <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <!-- Featured Card Left -->
            <article class="playcard-featured">
              <a href="#sa-feat" class="playcard-feat-media">
                <img src="https://c.ndtvimg.com/2026-10/7jmebc6o_study-abroad-guide_625x300_21_October_26.jpeg" alt="Study Abroad Guide" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#sa-feat">Ivy League Admissions Getting Tougher? Know How Indian Students Can Prepare</a>
              </h3>
            </article>

            <!-- Stacked List Right -->
            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#sa-1" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/hnpk01q4_great-scholarships-2027_625x300_15_October_26.jpeg" alt="UK Scholarships" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#sa-1">Study In The UK: 4 Universities To Offer £10,000 Scholarships To Indians</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#sa-2" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/2307fk7c_finland_625x300_13_October_26.jpeg" alt="Finnish Libraries" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#sa-2">'Not Just Books': Check Surprising Objects Found In Finnish Libraries</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#sa-3" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-03/6vuiv7pg_us-visa_625x300_05_March_26.jpg?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="US Student Fee" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#sa-3">US Proposes Rs 67 Lakh Fee For Foreign Students Seeking Temporary Work</a>
                </h4>
              </article>

            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- =====================================================================
         DUO PLAYCARD 2: CLIMATE & ENVIRONMENT & LIFESTYLE (Exact Reference Image 3)
         ===================================================================== -->
    <section class="portal-section duo-playcard-section" id="climate-lifestyle">
      <div class="duo-playcard-grid">
        
        <!-- Left Playcard: Climate & Environment -->
        <div class="duo-playcard-col">
          <div class="playcard-sec-head">
            <a href="#climate-environment">Climate &amp; Environment <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <!-- Featured Card Left (Thermometer Heat) -->
            <article class="playcard-featured">
              <a href="#ce-feat" class="playcard-feat-media">
                <img src="https://c.ndtvimg.com/2025-09/ppo0hvjs_global-warming_625x300_23_September_25.jpg?im=FeatureCrop,algorithm=dnn,width=640,height=400" alt="Global Warming UN" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#ce-feat">World On Track For 2.6 Degrees Celsius Warming This Century: UN</a>
              </h3>
            </article>

            <!-- Stacked List Right -->
            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#ce-1" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-04/o7eqhb6g_emperor-penguins-_625x300_09_April_26.jpeg?im=FaceCrop,algorithm=dnn,width=240,height=160" alt="Penguin Colony" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ce-1">Climate Change Strips Island's Title Of Largest Penguin Colony: Study</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#ce-2" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-09/sfivvhqc_el-nino-reuters_625x300_28_September_26.jpeg?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="El Nino Waves" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ce-2">El Nino Will Intensify, Then Peak In December, United Nations Warns</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#ce-3" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2025-08/9r5a6igc_france-wildfire_625x300_10_August_25.jpeg?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="Ozone Pollution Wildfire" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ce-3">One Third Of World Population Exposed To High Ozone Pollution: Report</a>
                </h4>
              </article>

            </div>

          </div>
        </div>

        <!-- Right Playcard: Lifestyle -->
        <div class="duo-playcard-col">
          <div class="playcard-sec-head">
            <a href="#lifestyle">Lifestyle <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <!-- Featured Card Left (Rashmika Multi-Ring Engagement Stack) -->
            <article class="playcard-featured">
              <a href="#ls-feat" class="playcard-feat-media">
                <img src="https://c.ndtvimg.com/2026-10/lpn1m1n8_rashmika-mandanna-vijay-deverakonda_625x300_22_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=640,height=400" alt="Rashmika Mandanna Engagement Stack" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#ls-feat">Decoding Rashmika Mandanna's Multi-Ring Engagement Stack By Vijay Deverakonda</a>
              </h3>
            </article>

            <!-- Stacked List Right -->
            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#ls-1" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/6j3d724s_ranbir-kapoor_625x300_21_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="Koffee with Karan Fashion" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ls-1">What Rashmika Mandanna And Vijay Deverakonda Wore For <em>Koffee With Karan</em></a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#ls-2" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/h4vokdhg_sai-pallavi-banarasi-saree_625x300_22_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="Sai Pallavi Banarasi" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ls-2">Sai Pallavi Flaunts The Beauty Of Banarasi Weaves At <em>Ramayana</em> Event In Chennai</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#ls-3" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/18ehsk7s_hasan-minhaj-dal-tadka-dharka_625x300_21_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="Hasan Minhaj Tadka" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#ls-3">Internet Debates As Hasan Minhaj Mispronounces <em>Tadka</em> As <em>'Dharka'</em></a>
                </h4>
              </article>

            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- =====================================================================
         SECTION: REGIONAL WORLD QUAD CARDS (Exact Reference Image 1)
         United States | United Kingdom | Middle East | Asia (4 Dark Cards)
         ===================================================================== -->
    <section class="portal-section regional-quad-section" id="world-regional-hub">
      <div class="regional-quad-grid">
        
        <!-- Quad Card 1: United States -->
        <article class="regional-quad-card">
          <h3 class="quad-card-head">
            <a href="#us-news">United States <span class="playcard-chevron">›</span></a>
          </h3>
          <div class="quad-card-list">
            
            <div class="quad-list-item">
              <a href="#us-1" class="quad-thumb-wrap">
                <img src="https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=160&auto=format&fit=crop&q=80" alt="Elon Musk" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#us-1">Elon Musk's Public Endorsement Of SpaceX-Tesla Merger Worries Insiders</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#us-2" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/ojqf8918_us-supreme-court-reuters_625x300_22_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="US Supreme Court" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#us-2">US Top Court Refuses Team Trump's Treatment Curbs On Transgender Inmates</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#us-3" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/vt84rsv8_arizona-university_625x300_22_October_26.jpeg" alt="Arizona University" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#us-3">Arizona University Fraternity Suspended After Female Student's Rape Charge</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#us-4" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2020-07/58i7ecs_ohio-state-university-reuters-650_625x300_09_July_20.jpg?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="Ohio State University" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#us-4">US Justice Department Alleges Anti-Asian Bias At Ohio State University</a>
              </h4>
            </div>

          </div>
        </article>

        <!-- Quad Card 2: United Kingdom -->
        <article class="regional-quad-card">
          <h3 class="quad-card-head">
            <a href="#uk-news">United Kingdom <span class="playcard-chevron">›</span></a>
          </h3>
          <div class="quad-card-list">
            
            <div class="quad-list-item">
              <a href="#uk-1" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/lah9evc_nye-bevan_625x300_22_October_26.jpeg" alt="MI5 Nye Bevan" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#uk-1">Why British Agency MI5 Spied Their Own Health Service Founder For Decades</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#uk-2" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/smlql7i4_mateusz-chmura_625x300_21_October_26.jpeg" alt="British Bodybuilder" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#uk-2">British Bodybuilder Dies After Collapsing On Stage Day Before 34th Birthday</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#uk-3" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2023-02/poj0cg2s_google_625x300_09_February_23.jpg?im=FaceCrop,algorithm=dnn,width=160,height=110" alt="Google UK Bank" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#uk-3">UK Bank Operations Disrupted After Power Outage Hits Google Cloud Services</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#uk-4" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/agleo3to_london-protest_625x300_17_October_26.png?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="UK Protest" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#uk-4">Protest vs Counter-Protest In UK Amid Row Over Poll Body Chief Gyanesh Kumar</a>
              </h4>
            </div>

          </div>
        </article>

        <!-- Quad Card 3: Middle East -->
        <article class="regional-quad-card">
          <h3 class="quad-card-head">
            <a href="#me-news">Middle East <span class="playcard-chevron">›</span></a>
          </h3>
          <div class="quad-card-list">
            
            <div class="quad-list-item">
              <a href="#me-1" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/4kinigvg_saudi-airport-attacked_625x300_22_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="Saudi Airport Indian Killed" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#me-1">Indian Among 2 Killed In Attack On Saudi Airport, 2 Others Injured</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#me-2" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/fiivu648_israel-elections-afp_625x300_22_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="Israel Elections" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#me-2">War, Security And Economy: Factors That Will Shape Israel Elections</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#me-3" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/kn4s606c_mecca-accord-reuters_625x300_22_October_26.jpg?im=FitAndFill,algorithm=dnn,width=160,height=110" alt="Mecca Defence Agreement" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#me-3">How Turkey, Pak And Saudi Will Workout The Mecca Joint Defence Agreement</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#me-4" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/m1hi4gdc_houthi-attacks-saudi-oil-field_625x300_22_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="Saudi Airport Flights Diverted" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#me-4">1 Killed, 8 Injured In Attack On Saudi Airport, Flights Diverted</a>
              </h4>
            </div>

          </div>
        </article>

        <!-- Quad Card 4: Asia -->
        <article class="regional-quad-card">
          <h3 class="quad-card-head">
            <a href="#asia-news">Asia <span class="playcard-chevron">›</span></a>
          </h3>
          <div class="quad-card-list">
            
            <div class="quad-list-item">
              <a href="#as-1" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/rlgqdq7k_alain-ebobisse_625x300_21_October_26.jpeg" alt="Africa50 Fund" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#as-1">Africa50's Principal Investment Fund CEO On India's Role In Developing Africa</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#as-2" class="quad-thumb-wrap">
                <img src="https://i.ndtvimg.com/i/2015-05/dawood-ibrahim-ap-650_650x400_61430819235.jpg?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="Dawood UN" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#as-2">'Dawood Lives In Pak, Like Bin Laden Used To': India Corrects UN Rapporteur</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#as-3" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/kn4s606c_mecca-accord-reuters_625x300_22_October_26.jpg?im=FitAndFill,algorithm=dnn,width=160,height=110" alt="Turkey Saudi" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#as-3">How Turkey, Pak And Saudi Will Workout The Mecca Joint Defence Agreement</a>
              </h4>
            </div>

            <div class="quad-list-item">
              <a href="#as-4" class="quad-thumb-wrap">
                <img src="https://c.ndtvimg.com/2026-10/8prplbc4_donald-trump-jr-afp_625x300_21_October_26.jpg?im=FeatureCrop,algorithm=dnn,width=160,height=110" alt="Donald Trump Jr" class="quad-thumb-img" loading="lazy">
              </a>
              <h4 class="quad-item-title">
                <a href="#as-4">Trump's Son Warned Him Against Dragging US Into War With Middle East: Report</a>
              </h4>
            </div>

          </div>
        </article>

      </div>
    </section>

    <!-- =====================================================================
         DUO PLAYCARD 3: MOVIES & ENTERTAINMENT & GADGETS & TECH (Exact Reference Image 2)
         ===================================================================== -->
    <section class="portal-section duo-playcard-section" id="movies-gadgets">
      <div class="duo-playcard-grid">
        
        <!-- Left Playcard: Movies & Entertainment -->
        <div class="duo-playcard-col">
          <div class="playcard-sec-head">
            <a href="#movies-entertainment">Movies &amp; Entertainment <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <!-- Featured Card Left (AR Rahman Ramayana) -->
            <article class="playcard-featured">
              <a href="#me-feat" class="playcard-feat-media">
                <img src="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=640&auto=format&fit=crop&q=80" alt="AR Rahman Ramayana Producer" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#me-feat">"It's A Gamble": AR Rahman Says He Understands Pressure On <em>Ramayana</em> Producer</a>
              </h3>
            </article>

            <!-- Stacked List Right -->
            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#me-1" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=240&auto=format&fit=crop&q=80" alt="Shabana Azmi" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#me-1">'I Am A Muslim, But We Don't Offer Namaz': Shabana Azmi Opens Up On Religion</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#me-2" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/9ffemdvg_manoj-bajpayee_625x300_22_October_26.png?im=FeatureCrop,algorithm=dnn,width=240,height=160" alt="Manoj Bajpayee Tiger Shroff" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#me-2">Manoj Bajpayee On Tiger Shroff Assassination Bid: 'You Can't Be Alert 24 Hours'</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#me-3" class="playcard-thumb-wrap">
                  <img src="https://c.ndtvimg.com/2026-10/7df3vkn_daler_625x300_22_October_26.png?im=FitAndFill,algorithm=dnn,width=240,height=160" alt="Daler Mehndi" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#me-3">'Daler Mehndi Doesn't Drink': Manoj Bajpayee Backs Singer Amid Viral Video Row</a>
                </h4>
              </article>

            </div>

          </div>
        </div>

        <!-- Right Playcard: Gadgets & Technology -->
        <div class="duo-playcard-col">
          <div class="playcard-sec-head">
            <a href="#gadgets-tech">Gadgets &amp; Technology <span class="playcard-chevron">›</span></a>
          </div>
          <div class="playcard-inner-grid">
            
            <!-- Featured Card Left (Vivo Green Phone) -->
            <article class="playcard-featured">
              <a href="#gt-feat" class="playcard-feat-media">
                <img src="https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=640&auto=format&fit=crop&q=80" alt="Vivo Y600 Battery" class="playcard-feat-img" loading="lazy">
              </a>
              <h3 class="playcard-feat-title">
                <a href="#gt-feat">Vivo Y600 With 10,000mAh Battery Revealed; Launch Date Set for October 30</a>
              </h3>
            </article>

            <!-- Stacked List Right -->
            <div class="playcard-stacked-list">
              
              <article class="playcard-list-item">
                <a href="#gt-1" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=240&auto=format&fit=crop&q=80" alt="iPhone Duo" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#gt-1">Apple's iPhone Duo Hands-On Video Shows Soft Spot Around Display Crease</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#gt-2" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1580910051074-3eb694886505?w=240&auto=format&fit=crop&q=80" alt="Oppo Reno 16" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#gt-2">Oppo Reno 16 Price in India Rises, New 128GB Model Launched</a>
                </h4>
              </article>

              <article class="playcard-list-item">
                <a href="#gt-3" class="playcard-thumb-wrap">
                  <img src="https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=240&auto=format&fit=crop&q=80" alt="iQOO 16R" class="playcard-thumb-img" loading="lazy">
                </a>
                <h4 class="playcard-list-title">
                  <a href="#gt-3">iQOO 16R Spotted on TKDN Certification Website, Could Launch Soon</a>
                </h4>
              </article>

            </div>

          </div>
        </div>

      </div>
    </section>
"""

print("Generated HTML size:", len(sections_html))
