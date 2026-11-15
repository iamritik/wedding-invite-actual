import os

VERSIONS = [
    {
        "id": "1",
        "dir": "version-1",
        "title": "Ritik weds Vaibhavi | Wedding Invitation",
        "name1": "Ritik",
        "connector": "weds",
        "name2": "Vaibhavi",
        "story_sign": "Ritik and Vaibhavi",
        "hero_date_month": "January",
        "hero_date_day": "27",
        "hero_date_dayname": "Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "27 January 2027",
        "target_date_iso": "2027-01-27T18:00:00+05:30",
        "target_date_label": "Until 27 January 2027",
        "welcome_family": "Together with the Chittu Family",
        "welcome_text": "With the divine blessings of Lord Ganesha and our elders, we cordially invite you and your family to celebrate the auspicious wedding ceremony and reception of Ritik & Vaibhavi.",
        "events_type": "shaadi_only",
        "hashtag": "#RitikWedsVaibhavi",
        "preview_name": "Version 1: Ritik's Side (Shaadi Only)"
    },
    {
        "id": "2",
        "dir": "version-2",
        "title": "Vaibhavi weds Ritik | Wedding Invitation",
        "name1": "Vaibhavi",
        "connector": "weds",
        "name2": "Ritik",
        "story_sign": "Vaibhavi and Ritik",
        "hero_date_month": "January",
        "hero_date_day": "27",
        "hero_date_dayname": "Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "27 January 2027",
        "target_date_iso": "2027-01-27T18:00:00+05:30",
        "target_date_label": "Until 27 January 2027",
        "welcome_family": "Together with their Families",
        "welcome_text": "With the divine blessings of Lord Ganesha and our elders, we cordially invite you and your family to celebrate the auspicious wedding ceremony and reception of Vaibhavi & Ritik.",
        "events_type": "shaadi_only",
        "hashtag": "#VaibhaviWedsRitik",
        "preview_name": "Version 2: Vaibhavi's Side (Shaadi Only)"
    },
    {
        "id": "3",
        "dir": "version-3",
        "title": "Ritik weds Vaibhavi | Wedding Celebrations",
        "name1": "Ritik",
        "connector": "weds",
        "name2": "Vaibhavi",
        "story_sign": "Ritik and Vaibhavi",
        "hero_date_month": "January",
        "hero_date_day": "26 – 27",
        "hero_date_dayname": "Tuesday & Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "26 – 27 January 2027",
        "target_date_iso": "2027-01-26T18:00:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "welcome_family": "Together with the Chittu Family",
        "welcome_text": "With the divine blessings of Lord Ganesha and our elders, we cordially invite you to join us for the wedding festivities, Sangeet night, Haldi ceremony, and wedding reception of Ritik & Vaibhavi.",
        "events_type": "all_events",
        "hashtag": "#RitikWedsVaibhavi",
        "preview_name": "Version 3: Ritik's Side (All 3 Events)"
    },
    {
        "id": "4",
        "dir": "version-4",
        "title": "Vaibhavi weds Ritik | Wedding Celebrations",
        "name1": "Vaibhavi",
        "connector": "weds",
        "name2": "Ritik",
        "story_sign": "Vaibhavi and Ritik",
        "hero_date_month": "January",
        "hero_date_day": "26 – 27",
        "hero_date_dayname": "Tuesday & Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "26 – 27 January 2027",
        "target_date_iso": "2027-01-26T18:00:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "welcome_family": "Together with their Families",
        "welcome_text": "With the divine blessings of Lord Ganesha and our elders, we cordially invite you to join us for the wedding festivities, Sangeet night, Haldi ceremony, and wedding reception of Vaibhavi & Ritik.",
        "events_type": "all_events",
        "hashtag": "#VaibhaviWedsRitik",
        "preview_name": "Version 4: Vaibhavi's Side (All 3 Events)"
    }
]

def build_sangeet_haldi_screen():
    return """
  <!-- ============================================================
       6. SANGEET & HALDI SCREEN (TRADITIONAL COURTYARD PAINTING)
       ============================================================ -->
  <section id="sangeetHaldiSection" class="sangeet-haldi-section">
    <img src="assets/screen_sangeet_haldi.jpg" alt="Sangeet & Haldi Courtyard" class="sangeet-haldi-bg" />

    <div class="sangeet-haldi-container">
      <p class="events-screen-label">Pre-Wedding Festivities</p>

      <!-- Interactive Tab Toggle -->
      <div class="events-toggle-bar" role="tablist" aria-label="Ceremony Selection">
        <button id="tabSangeet" class="event-toggle-btn active" role="tab" aria-selected="true" onclick="switchEventTab('sangeet')">
          <span>✦ Sangeet</span>
        </button>
        <button id="tabHaldi" class="event-toggle-btn" role="tab" aria-selected="false" onclick="switchEventTab('haldi')">
          <span>☀️ Haldi</span>
        </button>
      </div>

      <!-- Tab Content: Sangeet -->
      <div id="contentSangeet" class="event-tab-pane active" role="tabpanel">
        <div class="event-icon-wrap">
          <img src="assets/baile-nupcial.png" alt="Sangeet Dance" class="event-icon" />
        </div>
        <p class="event-item-label">An Evening of Music &amp; Dance</p>
        <h3 class="event-item-name">Sangeet &amp; Ring Ceremony</h3>
        <p class="event-item-desc">
          An enchanting evening of music, dance performances, ring exchange, and celebratory dinner.
        </p>
        <div class="event-meta-block">
          <span class="event-timing-tag">Tuesday, 26 January 2027 &nbsp;·&nbsp; Evening</span>
          <span class="event-dress-code">✨ Dress Code: Indo-Western / Glamorous Festive</span>
        </div>
      </div>

      <!-- Tab Content: Haldi -->
      <div id="contentHaldi" class="event-tab-pane" role="tabpanel">
        <div class="event-icon-wrap">
          <img src="assets/flor-almendro-grande.png" alt="Haldi" class="event-icon" />
        </div>
        <p class="event-item-label">Joyous Morning Blessings</p>
        <h3 class="event-item-name">Haldi Ceremony</h3>
        <p class="event-item-desc">
          Joyous morning rituals smeared in holy turmeric, vibrant yellow marigolds, and cherished blessings.
        </p>
        <div class="event-meta-block">
          <span class="event-timing-tag">Wednesday, 27 January 2027 &nbsp;·&nbsp; Morning</span>
          <span class="event-dress-code">💛 Dress Code: Shades of Yellow &amp; Sunshine Traditional</span>
        </div>
      </div>
    </div>
  </section>
"""

def build_shaadi_reception_screen():
    return """
  <!-- ============================================================
       7. SHAADI & RECEPTION SCREEN (ROYAL MANDAP PAINTING)
       ============================================================ -->
  <section id="shaadiReceptionSection" class="shaadi-reception-section">
    <img src="assets/screen_shaadi_reception.jpg" alt="Royal Wedding Mandap" class="shaadi-reception-bg" />

    <div class="shaadi-reception-content">
      <div class="event-icon-wrap">
        <img src="assets/boda-floral-arco.png" alt="Shaadi Arch" class="event-icon" />
      </div>
      <p class="event-item-label">The Auspicious Wedding Union</p>
      <h2 class="shaadi-screen-title">Shaadi &amp; Reception</h2>
      <p class="shaadi-screen-desc">
        The sacred wedding rituals and seven pheras followed by a grand royal dinner, music, and celebrations under the stars.
      </p>
      <div class="event-meta-block">
        <span class="event-timing-tag shaadi-tag">Wednesday, 27 January 2027 &nbsp;·&nbsp; Evening</span>
        <span class="event-dress-code shaadi-dress-code">👑 Dress Code: Traditional Indian Formal / Royal Elegance</span>
      </div>
    </div>
  </section>
"""

def build_html_page(cfg, is_root=False):
    sangeet_haldi_html = build_sangeet_haldi_screen() if cfg["events_type"] == "all_events" else ""
    shaadi_reception_html = build_shaadi_reception_screen()
    
    switcher_links = ""
    for v in VERSIONS:
        active_cls = "active" if v["id"] == cfg["id"] else ""
        link_target = f"../{v['dir']}/" if not is_root else f"version-{v['id']}/"
        switcher_links += f'<a href="{link_target}" class="preview-switcher-item {active_cls}">{v["preview_name"].split(":")[0]}: {v["name1"][0]}&{v["name2"][0]} ({ "Shaadi" if v["events_type"]=="shaadi_only" else "All" })</a>\n'

    duckdns_router_script = """
  <script>
    // Hostname and Query Router for DuckDNS setup
    (function() {
      var host = window.location.hostname.toLowerCase();
      var params = new URLSearchParams(window.location.search);
      var v = params.get('v');

      if (v === '1') { window.location.replace('version-1/'); return; }
      if (v === '2') { window.location.replace('version-2/'); return; }
      if (v === '3') { window.location.replace('version-3/'); return; }
      if (v === '4') { window.location.replace('version-4/'); return; }

      // Hostname-based routing for DuckDNS:
      if (host.indexOf('ritik') !== -1 && (host.indexOf('all') !== -1 || host.indexOf('sangeet') !== -1)) {
        window.location.replace('version-3/');
      } else if (host.indexOf('vaibhavi') !== -1 && (host.indexOf('all') !== -1 || host.indexOf('sangeet') !== -1)) {
        window.location.replace('version-4/');
      } else if (host.indexOf('vaibhavi') !== -1) {
        window.location.replace('version-2/');
      } else if (host.indexOf('ritik') !== -1) {
        window.location.replace('version-1/');
      }
    })();
  </script>
""" if is_root else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>{cfg["title"]}</title>
  <meta name="description" content="Wedding celebration invitation for {cfg["name1"]} & {cfg["name2"]} - {cfg["hero_date_header"]}" />
{duckdns_router_script}
  <!-- OpenGraph Metadata -->
  <meta property="og:title" content="{cfg["title"]}" />
  <meta property="og:description" content="We invite you to celebrate our wedding. {cfg["hero_date_header"]}" />
  <meta property="og:image" content="assets/envelope-poster-dG0TpNIf.jpg" />
  <meta property="og:type" content="website" />

  <!-- Fonts & Stylesheet -->
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- DEV / PREVIEW VERSION SWITCHER -->
  <div class="preview-switcher-bar">
    <span style="font-family: var(--font-sans); font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.15em; padding-left: 6px; opacity: 0.7;">DuckDNS Preview:</span>
    {switcher_links}
  </div>

  <!-- FLOATING PETALS CONTAINER -->
  <div id="petalsContainer" class="petals-container" aria-hidden="true"></div>

  <!-- FLOATING AUDIO CONTROLLER -->
  <button id="audioToggleBtn" class="audio-toggle-btn" aria-label="Play music" title="Toggle Music">
    <svg id="iconSound" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: none;">
      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
      <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
      <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
    </svg>
    <svg id="iconMute" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
      <line x1="23" y1="9" x2="17" y2="15"></line>
      <line x1="17" y1="9" x2="23" y2="15"></line>
    </svg>
  </button>

  <audio id="weddingAudio" src="assets/semo-fireflies.mp3" preload="auto" loop></audio>

  <!-- ============================================================
       1. ENVELOPE OPENING OVERLAY
       ============================================================ -->
  <div id="envelopeOverlay" class="envelope-overlay" aria-label="Tap to open wedding invitation">
    <img id="envelopePoster" src="assets/envelope-poster-dG0TpNIf.jpg" alt="Wedding Invitation Envelope" class="envelope-media envelope-poster" />
    <video id="envelopeVideo" src="assets/envelope-video-f1CdBR2C.mp4" poster="assets/envelope-poster-dG0TpNIf.jpg" playsinline muted preload="auto" class="envelope-media envelope-video" style="opacity: 0;"></video>
    
    <div class="envelope-prompt">
      <div class="envelope-prompt-btn">
        <span>✉️</span>
        <span>Tap to Open Invitation</span>
      </div>
    </div>
  </div>

  <!-- ============================================================
       2. HERO INVITATION SECTION (SLIDE 1 - LAKE PALACE & MOVING BLOSSOMS)
       ============================================================ -->
  <section id="heroSection" class="hero-section">
    <!-- Lake Palace & Deckled Parchment Painting Backdrop -->
    <div class="hero-painting-container">
      <img src="assets/screen_first_clean.jpg" alt="Wedding Invitation Backdrop" class="hero-painting-bg" />
      <img src="assets/screen_first_flowers_branch.png" alt="" class="hero-moving-branch" />
    </div>

    <div id="heroContent" class="hero-content">
      <div class="hero-names">
        <span>{cfg["name1"]}</span>
        <span class="hero-weds">{cfg["connector"]}</span>
        <span>{cfg["name2"]}</span>
      </div>

      <p class="hero-subtitle">
        We invite you to<br />celebrate our wedding
      </p>

      <div class="hero-date-box">
        <img src="assets/ramita-capullos.png" alt="" class="hero-date-sprig left" />
        <img src="assets/ramita-capullos.png" alt="" class="hero-date-sprig right" />
        <span class="hero-month">{cfg["hero_date_month"]}</span>
        <span class="hero-day">{cfg["hero_date_day"]}</span>
        <span class="hero-day-name">{cfg["hero_date_dayname"]}</span>
        <span class="hero-year">{cfg["hero_date_year"]}</span>
      </div>

      <p class="hero-location-tag">To be held at</p>
      <h3 class="hero-venue-name">Karnal</h3>
    </div>

    <!-- Scroll down indicator -->
    <button id="heroScrollBtn" class="hero-scroll-btn" aria-label="Scroll down to details">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="6 9 12 15 18 9"></polyline>
      </svg>
    </button>
  </section>

  <!-- ============================================================
       3. COUNTDOWN SECTION (INTEGRATED INTO IMPASTO FRAME)
       ============================================================ -->
  <section id="countdownSection" class="countdown-section" data-target-date="{cfg["target_date_iso"]}">
    <h2 class="section-title">Countdown</h2>
    <p class="section-subtitle">{cfg["target_date_label"]}</p>

    <!-- Authentic Impasto Oil Frame -->
    <div class="countdown-frame-wrap">
      <img src="assets/marco-azul-impasto.png" alt="" class="countdown-frame-img" />

      <!-- Large Calligraphic Days -->
      <div class="countdown-days-wrap">
        <span id="cdDays" class="countdown-days-num">0</span>
        <span class="countdown-days-label">Days</span>
      </div>

      <!-- Calligraphic Hours, Minutes, Seconds -->
      <div class="countdown-subunits-wrap">
        <div class="countdown-subunit">
          <span id="cdHours" class="countdown-subunit-num">00</span>
          <span class="countdown-subunit-label">Hours</span>
        </div>
        <div class="countdown-subunit">
          <span id="cdMins" class="countdown-subunit-num">00</span>
          <span class="countdown-subunit-label">Minutes</span>
        </div>
        <div class="countdown-subunit">
          <span id="cdSecs" class="countdown-subunit-num">00</span>
          <span class="countdown-subunit-label">Seconds</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       4. OUR STORY SECTION (SLIDE 2 - INTEGRATED CLOUD OIL PAINTING)
       ============================================================ -->
  <section id="ourStorySection" class="our-story-section">
    <img src="assets/nubes-impasto.png" alt="" class="our-story-clouds" />

    <div class="our-story-inner">
      <h2 class="our-story-title">Our Story</h2>
      <p class="our-story-text">
        Some of the best love stories begin unexpectedly, and ours was no different.
      </p>
      <p class="our-story-text">
        What started as a chance encounter soon became endless conversations, spontaneous adventures, and countless cherished memories together.
      </p>
      <p class="our-story-text">
        Somewhere along the way, we found our favorite place: by each other’s side.
      </p>
      <p class="our-story-text">
        And now, we're ready for our greatest adventure yet — a lifetime together.
      </p>
      <span class="our-story-signature">{cfg["story_sign"]}</span>
    </div>
  </section>

  <!-- ============================================================
       5. WELCOME & BLESSINGS
       ============================================================ -->
  <section id="welcomeSection" class="welcome-section">
    <img src="assets/cenefa-hojas-1.webp" alt="Floral divider" class="floral-divider" />
    <p class="welcome-lead">{cfg["welcome_family"]}</p>
    <p class="welcome-text">
      "{cfg["welcome_text"]}"
    </p>
  </section>

{sangeet_haldi_html}
{shaadi_reception_html}

  <!-- ============================================================
       8. VENUE & LOCATION
       ============================================================ -->
  <section id="venueSection" class="venue-section">
    <img src="assets/villa-mediterranea.png" alt="Palace Venue Art" class="venue-art" />
    <h2 class="venue-title">The Wedding Venue</h2>
    <h3 style="font-family: var(--font-display); font-size: 1.85rem; color: var(--text-olive); margin-bottom: 6px;">Manka by Cherish</h3>
    <p class="venue-address">
      Karnal, Haryana
    </p>
    <a href="https://maps.app.goo.gl/ituhycePZ4x9FFBP8" target="_blank" rel="noopener noreferrer" class="btn-maps">
      <span>📍 View Location on Google Maps</span>
    </a>
  </section>

  <!-- ============================================================
       9. LAST SCREEN (SACRED PHERAS & ROYAL ARCH PAINTING)
       ============================================================ -->
  <footer id="footerSection" class="footer-section">
    <!-- Royal Arch & Mandap Painting Backdrop -->
    <div class="footer-painting-container">
      <img src="assets/screen_last.jpg" alt="Wedding Mandap Arch" class="footer-painting-bg" />
      <!-- Moving lotus garland layer at top -->
      <img src="assets/screen_last_lotus.png" alt="" class="footer-moving-lotus" />
      <!-- Flickering sacred flame at bottom -->
      <img src="assets/screen_last_flame.png" alt="" class="footer-moving-flame" />
    </div>

    <div class="footer-content">
      <div class="footer-names">
        <span>{cfg["name1"]}</span>
        <span class="footer-weds">{cfg["connector"]}</span>
        <span>{cfg["name2"]}</span>
      </div>
      <p class="footer-date">{cfg["hero_date_header"]}</p>
      <p class="footer-tagline">Looking forward to celebrating with you!</p>
      <p class="footer-hashtag">{cfg["hashtag"]}</p>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="js/main.js"></script>
</body>
</html>
"""
    return html

# Generate the 4 standalone version files
for cfg in VERSIONS:
    path = os.path.join(cfg["dir"], "index.html")
    content = build_html_page(cfg, is_root=False)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {path}")

# Generate root index.html
root_cfg = VERSIONS[0].copy()
root_cfg["dir"] = "."
root_html = build_html_page(root_cfg, is_root=True)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(root_html)
print("Generated root index.html")
