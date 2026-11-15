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
        "parents_names": "Naresh & Kavita Arora",
        "hero_date_month": "January",
        "hero_date_day": "27",
        "hero_date_dayname": "Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "27 January 2027",
        "target_date_iso": "2027-01-27T18:00:00+05:30",
        "target_date_label": "Until 27 January 2027",
        "events_type": "shaadi_only",
        "hashtag": "#VRinLove",
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
        "parents_names": "Vivek & Manju Singh",
        "hero_date_month": "January",
        "hero_date_day": "27",
        "hero_date_dayname": "Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "27 January 2027",
        "target_date_iso": "2027-01-27T18:00:00+05:30",
        "target_date_label": "Until 27 January 2027",
        "events_type": "shaadi_only",
        "hashtag": "#VRinLove",
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
        "parents_names": "Naresh & Kavita Arora",
        "hero_date_month": "January",
        "hero_date_day": "25 – 27",
        "hero_date_dayname": "Monday to Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "25 – 27 January 2027",
        "target_date_iso": "2027-01-25T17:00:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "events_type": "all_events",
        "hashtag": "#VRinLove",
        "preview_name": "Version 3: Ritik's Side (All Events)"
    },
    {
        "id": "4",
        "dir": "version-4",
        "title": "Vaibhavi weds Ritik | Wedding Celebrations",
        "name1": "Vaibhavi",
        "connector": "weds",
        "name2": "Ritik",
        "story_sign": "Vaibhavi and Ritik",
        "parents_names": "Vivek & Manju Singh",
        "hero_date_month": "January",
        "hero_date_day": "26 – 27",
        "hero_date_dayname": "Tuesday & Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "26 – 27 January 2027",
        "target_date_iso": "2027-01-26T17:30:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "events_type": "all_events",
        "hashtag": "#VRinLove",
        "preview_name": "Version 4: Vaibhavi's Side (All Events)"
    }
]

RITIK_EVENTS = [
    {
        "id": "mehendi",
        "title": "Mehendi",
        "tagline": "Auspicious Henna & Folk Melodies",
        "date_badge": "25 Jan · 5:00 PM",
        "date_full": "Monday, 25 January 2027 · 5:00 PM",
        "venue": "701 Sector 8",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/hfNK1a2bUqbJ2QY28",
        "dress_code": "Festive Green / Colourful Traditional",
        "desc": "An auspicious beginning filled with vibrant henna, festive Punjabi boliyan, music, and laughter to kick off our wedding festivities.",
        "icon_symbol": "🌿",
    },
    {
        "id": "hawan",
        "title": "Hawan",
        "tagline": "Auspicious Vedic Prayers & Blessings",
        "date_badge": "26 Jan · 11:00 AM",
        "date_full": "Tuesday, 26 January 2027 · 11:00 AM (Morning)",
        "venue": "701 Sector 8",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/hfNK1a2bUqbJ2QY28",
        "dress_code": "Traditional Indian Ethnic",
        "desc": "Sacred Vedic prayers and yajna to invoke divine blessings of the deities and ancestors for peace, harmony, and prosperity.",
        "icon_symbol": "🔥",
    },
    {
        "id": "sangeet",
        "title": "Sangeet & Ring Ceremony",
        "tagline": "An Evening of Music & Dance",
        "date_badge": "26 Jan · 5:30 PM",
        "date_full": "Tuesday, 26 January 2027 · 5:30 PM onwards",
        "venue": "Hotel Jewels",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Indo-Western / Glamorous Festive",
        "desc": "An enchanting evening of music, dance performances, ring exchange, and celebratory dinner under the stars.",
        "icon_symbol": "💃",
    },
    {
        "id": "haldi",
        "title": "Haldi Ceremony",
        "tagline": "Joyous Morning Blessings",
        "date_badge": "27 Jan · 10:30 AM",
        "date_full": "Wednesday, 27 January 2027 · 10:30 AM (Morning)",
        "venue": "Hotel Jewels",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Shades of Yellow & Sunshine Traditional",
        "desc": "Joyous morning rituals smeared in holy turmeric, vibrant yellow marigolds, and cherished family blessings.",
        "icon_symbol": "💛",
    },
    {
        "id": "gharoli",
        "title": "Gharoli",
        "tagline": "Sacred Water Fetching Ceremony",
        "date_badge": "27 Jan · 2:00 PM",
        "date_full": "Wednesday, 27 January 2027 · 2:00 PM",
        "venue": "Hotel Jewels",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Traditional Indian Ethnic",
        "desc": "The beloved traditional ritual where family fetches sanctified holy water to bathe the groom before the wedding rituals.",
        "icon_symbol": "🏺",
    },
    {
        "id": "sehrabandi",
        "title": "Sehrabandi",
        "tagline": "Tying of the Royal Sehra & Baraat",
        "date_badge": "27 Jan · 5:00 PM",
        "date_full": "Wednesday, 27 January 2027 · 5:00 PM",
        "venue": "701 Sector 8",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/hfNK1a2bUqbJ2QY28",
        "dress_code": "Royal Indian Formal / Sherwani & Turbans",
        "desc": "The time-honored ceremony where sisters tie the auspicious floral sehra on the groom, followed by the grand Baraat procession.",
        "icon_symbol": "👑",
    },
]

VAIBHAVI_EVENTS = [
    {
        "id": "sangeet",
        "title": "Sangeet & Ring Ceremony",
        "tagline": "An Evening of Music & Dance",
        "date_badge": "26 Jan · 5:30 PM",
        "date_full": "Tuesday, 26 January 2027 · 5:30 PM onwards",
        "venue": "Hotel Jewels",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Indo-Western / Glamorous Festive",
        "desc": "An enchanting evening of music, dance performances, ring exchange, and celebratory dinner under the stars.",
        "icon_symbol": "💃",
    },
    {
        "id": "haldi",
        "title": "Haldi Ceremony",
        "tagline": "Joyous Morning Blessings",
        "date_badge": "27 Jan · 10:30 AM",
        "date_full": "Wednesday, 27 January 2027 · 10:30 AM (Morning)",
        "venue": "Hotel Jewels",
        "city": "Karnal, Haryana",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Shades of Yellow & Sunshine Traditional",
        "desc": "Joyous morning rituals smeared in holy turmeric, vibrant yellow marigolds, and cherished family blessings.",
        "icon_symbol": "💛",
    },
]

def build_festivities_screen(cfg):
    events = RITIK_EVENTS if cfg["id"] == "3" else VAIBHAVI_EVENTS
    count_class = f"events-count-{len(events)}"

    tiles_html = ""
    for ev in events:
        tiles_html += f"""
        <button type="button" class="event-tile-box"
          data-event-title="{ev['title']}"
          data-event-tagline="{ev['tagline']}"
          data-event-date="{ev['date_full']}"
          data-event-venue="{ev['venue']}"
          data-event-city="{ev['city']}"
          data-event-map="{ev['map_url']}"
          data-event-dress="{ev['dress_code']}"
          data-event-desc="{ev['desc']}"
          data-event-icon="{ev['icon_symbol']}"
          aria-label="View details for {ev['title']}">
          <div class="tile-icon-bubble">
            <span class="tile-emoji">{ev['icon_symbol']}</span>
          </div>
          <h3 class="tile-title">{ev['title']}</h3>
          <span class="tile-badge">{ev['date_badge']}</span>
          <span class="tile-tap-hint">Details &rarr;</span>
        </button>"""

    return f"""
  <!-- ============================================================
       PRE-WEDDING FESTIVITIES (INTERACTIVE BOX TILES)
       ============================================================ -->
  <section id="sangeetHaldiSection" class="sangeet-haldi-section">
    <img src="assets/screen_sangeet_haldi.jpg" alt="Courtyard Backdrop" class="sangeet-haldi-bg" />

    <div class="sangeet-haldi-container">
      <p class="events-screen-label">Pre-Wedding Festivities</p>
      <h2 class="events-screen-title">Events &amp; Celebrations</h2>
      <p class="events-screen-hint">Tap any celebration to view venue &amp; details</p>

      <div class="events-boxes-grid {count_class}">
{tiles_html}
      </div>
    </div>
  </section>
"""

def build_shaadi_reception_screen():
    return """
  <!-- ============================================================
       SHAADI & RECEPTION SCREEN (WITH INTEGRATED VENUE & MAPS)
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

      <!-- Integrated Venue & Maps Location -->
      <div class="shaadi-venue-card">
        <div class="shaadi-venue-divider"></div>
        <p class="shaadi-venue-label">WEDDING VENUE</p>
        <h4 class="shaadi-venue-name">Manka by Cherish</h4>
        <p class="shaadi-venue-city">Karnal, Haryana</p>
        <a href="https://maps.app.goo.gl/ituhycePZ4x9FFBP8" target="_blank" rel="noopener noreferrer" class="btn-maps-shaadi">
          <span>📍 View Location on Google Maps &rarr;</span>
        </a>
      </div>
    </div>
  </section>
"""

def build_html_page(cfg, is_root=False):
    festivities_html = build_festivities_screen(cfg) if cfg["events_type"] == "all_events" else ""
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

  <audio id="weddingAudio" src="assets/mohabbatein-love-theme.mp3" preload="auto" loop></audio>

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
       2. HERO INVITATION SECTION (SLIDE 1 - FRESCO MEDITERRANEAN COAST & SWAYING BRANCH)
       ============================================================ -->
  <section id="heroSection" class="hero-section">
    <!-- Authentic Fresco Mediterranean Painting Backdrop with Swaying Almond Branch -->
    <div class="hero-painting-container">
      <video class="hero-painting-bg" src="assets/hero-video.mp4" poster="assets/fresco-hero-original.jpg" autoplay loop muted playsinline></video>
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
       4. OUR STORY SECTION (INTEGRATED CLOUD OIL PAINTING)
       ============================================================ -->
  <section id="ourStorySection" class="our-story-section">
    <img src="assets/nubes-impasto.png" alt="" class="our-story-clouds" />

    <div class="our-story-inner">
      <h2 class="our-story-title">Our Story</h2>
      <p class="our-story-tagline">Who knew a right swipe could get this right?</p>

      <p class="our-story-text">
        It all started with a swipe. Ritik swiped right, and on 2nd November 2025, Vaibhavi matched. What followed was a month of conversations, even as Vaibhavi travelled for a friend's wedding and Ritik was back home in Karnal. Though both lived in Bangalore, they wouldn't meet just yet.
      </p>
      <p class="our-story-text">
        Finally, on 30th November, they went on their first date. What was supposed to be dinner turned into conversations that lasted until 5 AM.
      </p>
      <p class="our-story-text">
        Since then, they've become each other's favourite gossip partners, intellectual sparring partners and biggest cheerleaders. Whether it's endless banter, celebrating each other's achievements or pushing one another to be better, they've found someone with whom they can be unapologetically themselves.
      </p>

      <p class="our-story-highlight">
        Still each other's favourite notification, favourite person and favourite conversation.
      </p>

      <span class="our-story-signature">{cfg["story_sign"]}</span>
    </div>
  </section>

{festivities_html}
{shaadi_reception_html}

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
      <p class="footer-invitation-lead">Warmly Invited By</p>
      <h3 class="footer-parents-names">{cfg["parents_names"]}</h3>
      <p class="footer-tagline">Looking forward to celebrating with you!</p>
      <p class="footer-hashtag">{cfg["hashtag"]}</p>
    </div>
  </footer>

  <!-- ============================================================
       EVENT DETAILS MODAL
       ============================================================ -->
  <div id="eventDetailModal" class="event-modal-backdrop" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="event-modal-card">
      <button type="button" class="event-modal-close" id="closeEventModalBtn" aria-label="Close details">&times;</button>
      
      <div class="event-modal-icon-wrap">
        <span id="modalEventEmoji" class="event-modal-emoji">✨</span>
      </div>

      <p id="modalEventTagline" class="event-modal-tagline">Ceremony Details</p>
      <h3 id="modalEventTitle" class="event-modal-title">Event Title</h3>
      
      <div class="event-modal-time-badge">
        <span id="modalEventDate">Date &amp; Time</span>
      </div>

      <p id="modalEventDesc" class="event-modal-desc">Description</p>

      <div class="event-modal-venue-box">
        <div class="event-modal-venue-header">
          <span class="venue-pin-icon">📍</span>
          <div>
            <p class="venue-header-label">VENUE</p>
            <h4 id="modalEventVenue" class="modal-venue-name">Venue Name</h4>
            <p id="modalEventCity" class="modal-venue-city">City</p>
          </div>
        </div>
        <a id="modalEventMapLink" href="#" target="_blank" rel="noopener noreferrer" class="btn-modal-maps">
          <span>View on Google Maps &rarr;</span>
        </a>
      </div>

      <div id="modalDressCodeWrap" class="event-modal-dress">
        <span id="modalEventDress">Dress Code</span>
      </div>
    </div>
  </div>

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
