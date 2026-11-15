import os

VERSIONS = [
    {
        "id": "1",
        "dir": "version-1",
        "title": "Ritik weds Vaibhavi | Wedding Invitation",
        "name1": "Ritik",
        "connector": "weds",
        "name2": "Vaibhavi",
        "hero_date_month": "January",
        "hero_date_day": "27",
        "hero_date_dayname": "Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "27 January 2027",
        "target_date_iso": "2027-01-27T18:30:00+05:30",
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
        "hero_date_month": "January",
        "hero_date_day": "27",
        "hero_date_dayname": "Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "27 January 2027",
        "target_date_iso": "2027-01-27T18:30:00+05:30",
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
        "hero_date_month": "January",
        "hero_date_day": "26 – 27",
        "hero_date_dayname": "Tuesday & Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "26 – 27 January 2027",
        "target_date_iso": "2027-01-26T19:00:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "welcome_family": "Together with the Chittu Family",
        "welcome_text": "With the divine blessings of Lord Ganesha and our elders, we cordially invite you to join us for the auspicious wedding celebrations, Sangeet night, Haldi ceremony, and wedding reception of Ritik & Vaibhavi.",
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
        "hero_date_month": "January",
        "hero_date_day": "26 – 27",
        "hero_date_dayname": "Tuesday & Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "26 – 27 January 2027",
        "target_date_iso": "2027-01-26T19:00:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "welcome_family": "Together with their Families",
        "welcome_text": "With the divine blessings of Lord Ganesha and our elders, we cordially invite you to join us for the auspicious wedding celebrations, Sangeet night, Haldi ceremony, and wedding reception of Vaibhavi & Ritik.",
        "events_type": "all_events",
        "hashtag": "#VaibhaviWedsRitik",
        "preview_name": "Version 4: Vaibhavi's Side (All 3 Events)"
    }
]

def build_events_html(events_type, name1, name2):
    if events_type == "shaadi_only":
        return f"""
      <!-- EVENT 1: SHAADI & RECEPTION -->
      <div class="event-card">
        <div class="event-icon-wrap">
          <img src="assets/boda-floral-arco.png" alt="Shaadi Arch" class="event-icon" />
        </div>
        <p class="event-label">The Wedding Ceremony</p>
        <h3 class="event-name">Shaadi & Reception</h3>
        <p class="event-description">
          The sacred wedding rituals and seven pheras followed by an evening of congratulations, dinner, and dancing under the stars.
        </p>
        <div class="event-divider-line"></div>
        <div class="event-time-box">
          <span class="event-date-text">Wednesday, 27 January 2027</span>
          <span class="event-time-text">6:30 PM Onwards</span>
          <span style="font-family: var(--font-sans); font-size: 10px; letter-spacing: 0.18em; opacity: 0.8; margin-top: 4px;">
            Baraat: 6:30 PM &nbsp;·&nbsp; Varmala & Pheras: 8:00 PM &nbsp;·&nbsp; Reception: 8:30 PM
          </span>
        </div>
        <div class="event-actions">
          <button class="btn-event-action" onclick="addToGoogleCalendar('{name1} weds {name2} - Shaadi Reception', '20270127T183000', '20270127T235900', 'Grand Heritage Palace, Jaipur', 'Wedding & Reception of {name1} & {name2}')">
            <span>📅 Add to Google Calendar</span>
          </button>
          <button class="btn-event-action" onclick="downloadIcs('{name1} weds {name2} - Shaadi Reception', '20270127T183000', '20270127T235900', 'Grand Heritage Palace, Jaipur', 'Wedding & Reception of {name1} & {name2}', 'shaadi-invite.ics')">
            <span>📥 Download .ICS</span>
          </button>
        </div>
      </div>
"""
    else:
        return f"""
      <!-- EVENT 1: SANGEET & RING CEREMONY -->
      <div class="event-card">
        <div class="event-icon-wrap">
          <img src="assets/baile-nupcial.png" alt="Sangeet Dance" class="event-icon" />
        </div>
        <p class="event-label">Evening of Melodies & Dance</p>
        <h3 class="event-name">Sangeet & Ring Ceremony</h3>
        <p class="event-description">
          An enchanting evening filled with dance performances, ring exchange, signature cocktails, and musical celebrations.
        </p>
        <div class="event-divider-line"></div>
        <div class="event-time-box">
          <span class="event-date-text">Tuesday, 26 January 2027</span>
          <span class="event-time-text">7:00 PM Onwards</span>
        </div>
        <div class="event-actions">
          <button class="btn-event-action" onclick="addToGoogleCalendar('{name1} & {name2} - Sangeet & Ring Ceremony', '20270126T190000', '20270126T233000', 'Grand Heritage Palace, Jaipur', 'Sangeet & Ring Ceremony')">
            <span>📅 Add to Google Calendar</span>
          </button>
          <button class="btn-event-action" onclick="downloadIcs('{name1} & {name2} - Sangeet & Ring Ceremony', '20270126T190000', '20270126T233000', 'Grand Heritage Palace, Jaipur', 'Sangeet & Ring Ceremony', 'sangeet-invite.ics')">
            <span>📥 Download .ICS</span>
          </button>
        </div>
      </div>

      <!-- EVENT 2: HALDI CEREMONY -->
      <div class="event-card">
        <div class="event-icon-wrap">
          <img src="assets/flor-almendro-grande.png" alt="Haldi Turmeric" class="event-icon" />
        </div>
        <p class="event-label">Joyful Morning Rituals</p>
        <h3 class="event-name">Haldi Ceremony</h3>
        <p class="event-description">
          A vibrant morning celebration smeared with fragrant turmeric, splashes of yellow, flower showers, and cherished laughter.
        </p>
        <div class="event-divider-line"></div>
        <div class="event-time-box">
          <span class="event-date-text">Wednesday, 27 January 2027</span>
          <span class="event-time-text">10:00 AM Onwards</span>
        </div>
        <div class="event-actions">
          <button class="btn-event-action" onclick="addToGoogleCalendar('{name1} & {name2} - Haldi Ceremony', '20270127T100000', '20270127T130000', 'Grand Heritage Palace, Jaipur', 'Haldi Ceremony')">
            <span>📅 Add to Google Calendar</span>
          </button>
          <button class="btn-event-action" onclick="downloadIcs('{name1} & {name2} - Haldi Ceremony', '20270127T100000', '20270127T130000', 'Grand Heritage Palace, Jaipur', 'Haldi Ceremony', 'haldi-invite.ics')">
            <span>📥 Download .ICS</span>
          </button>
        </div>
      </div>

      <!-- EVENT 3: SHAADI & RECEPTION -->
      <div class="event-card">
        <div class="event-icon-wrap">
          <img src="assets/boda-floral-arco.png" alt="Shaadi Arch" class="event-icon" />
        </div>
        <p class="event-label">The Auspicious Wedding</p>
        <h3 class="event-name">Shaadi & Reception</h3>
        <p class="event-description">
          The sacred wedding rituals and seven pheras followed by dinner, laughter, and lifelong celebrations under the stars.
        </p>
        <div class="event-divider-line"></div>
        <div class="event-time-box">
          <span class="event-date-text">Wednesday, 27 January 2027</span>
          <span class="event-time-text">6:30 PM Onwards</span>
          <span style="font-family: var(--font-sans); font-size: 10px; letter-spacing: 0.18em; opacity: 0.8; margin-top: 4px;">
            Baraat: 6:30 PM &nbsp;·&nbsp; Varmala & Pheras: 8:00 PM &nbsp;·&nbsp; Reception: 8:30 PM
          </span>
        </div>
        <div class="event-actions">
          <button class="btn-event-action" onclick="addToGoogleCalendar('{name1} weds {name2} - Shaadi Reception', '20270127T183000', '20270127T235900', 'Grand Heritage Palace, Jaipur', 'Wedding & Reception of {name1} & {name2}')">
            <span>📅 Add to Google Calendar</span>
          </button>
          <button class="btn-event-action" onclick="downloadIcs('{name1} weds {name2} - Shaadi Reception', '20270127T183000', '20270127T235900', 'Grand Heritage Palace, Jaipur', 'Wedding & Reception of {name1} & {name2}', 'shaadi-invite.ics')">
            <span>📥 Download .ICS</span>
          </button>
        </div>
      </div>
"""

def build_rsvp_events_checkboxes(events_type):
    if events_type == "shaadi_only":
        return """
        <div class="rsvp-checkbox-group">
          <label class="rsvp-checkbox-label">
            <input type="checkbox" name="rsvpEvents" value="Shaadi & Reception (27 Jan)" checked />
            <span>Shaadi & Reception &nbsp;·&nbsp; 27th Jan 2027</span>
          </label>
        </div>
"""
    else:
        return """
        <div class="rsvp-checkbox-group">
          <label class="rsvp-checkbox-label">
            <input type="checkbox" name="rsvpEvents" value="Sangeet & Ring Ceremony (26 Jan)" checked />
            <span>Sangeet & Ring Ceremony &nbsp;·&nbsp; 26th Jan</span>
          </label>
          <label class="rsvp-checkbox-label">
            <input type="checkbox" name="rsvpEvents" value="Haldi Ceremony (27 Jan Morning)" checked />
            <span>Haldi Ceremony &nbsp;·&nbsp; 27th Jan Morning</span>
          </label>
          <label class="rsvp-checkbox-label">
            <input type="checkbox" name="rsvpEvents" value="Shaadi & Reception (27 Jan Evening)" checked />
            <span>Shaadi & Reception &nbsp;·&nbsp; 27th Jan Evening</span>
          </label>
        </div>
"""

def build_html_page(cfg, is_root=False):
    events_html = build_events_html(cfg["events_type"], cfg["name1"], cfg["name2"])
    rsvp_checkboxes = build_rsvp_events_checkboxes(cfg["events_type"])
    
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
      // Examples:
      // ritik-shaadi.duckdns.org -> version-1
      // vaibhavi-shaadi.duckdns.org -> version-2
      // ritik-all.duckdns.org -> version-3
      // vaibhavi-all.duckdns.org -> version-4
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
       2. HERO INVITATION SECTION
       ============================================================ -->
  <section class="hero-section">
    <!-- Looped background video with poster fallback -->
    <video class="hero-video-bg" src="assets/hero-video.mp4" poster="assets/fresco-hero-original.jpg" autoplay loop muted playsinline></video>

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
      <h3 class="hero-venue-name">Grand Heritage Palace, Jaipur</h3>
    </div>

    <!-- Scroll down indicator -->
    <button id="heroScrollBtn" class="hero-scroll-btn" aria-label="Scroll down to details">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="6 9 12 15 18 9"></polyline>
      </svg>
    </button>
  </section>

  <!-- ============================================================
       3. COUNTDOWN SECTION
       ============================================================ -->
  <section id="countdownSection" class="countdown-section" data-target-date="{cfg["target_date_iso"]}">
    <h2 class="section-title">Countdown</h2>
    <p class="section-subtitle">{cfg["target_date_label"]}</p>

    <div class="countdown-grid">
      <div class="countdown-card">
        <span id="cdDays" class="countdown-num">00</span>
        <span class="countdown-label">Days</span>
      </div>
      <div class="countdown-card">
        <span id="cdHours" class="countdown-num">00</span>
        <span class="countdown-label">Hours</span>
      </div>
      <div class="countdown-card">
        <span id="cdMins" class="countdown-num">00</span>
        <span class="countdown-label">Minutes</span>
      </div>
      <div class="countdown-card">
        <span id="cdSecs" class="countdown-num">00</span>
        <span class="countdown-label">Seconds</span>
      </div>
    </div>
  </section>

  <!-- ============================================================
       4. WELCOME & BLESSINGS
       ============================================================ -->
  <section class="welcome-section">
    <img src="assets/cenefa-hojas-1.webp" alt="Floral divider" class="floral-divider" />
    <p class="welcome-lead">{cfg["welcome_family"]}</p>
    <p class="welcome-text">
      "{cfg["welcome_text"]}"
    </p>
  </section>

  <!-- ============================================================
       5. CELEBRATION EVENTS ITINERARY
       ============================================================ -->
  <section class="events-section" style="background-image: url('assets/marco-azul-impasto.png');">
    <div class="events-header">
      <h2 class="section-title">The Celebration</h2>
      <p class="section-subtitle">{cfg["hero_date_header"]}</p>
    </div>

    <div class="events-container">
      {events_html}
    </div>
  </section>

  <!-- ============================================================
       6. VENUE & LOCATION
       ============================================================ -->
  <section class="venue-section">
    <img src="assets/villa-mediterranea.png" alt="Palace Venue Art" class="venue-art" />
    <h2 class="venue-title">The Wedding Venue</h2>
    <p class="venue-address">
      Grand Heritage Palace<br />
      Amer Road, Jaipur, Rajasthan 302002
    </p>
    <a href="https://www.google.com/maps/search/?api=1&query=Grand+Heritage+Palace+Jaipur" target="_blank" rel="noopener noreferrer" class="btn-maps">
      <span>📍 View Location on Google Maps</span>
    </a>
  </section>

  <!-- ============================================================
       7. RSVP SECTION
       ============================================================ -->
  <section id="rsvpSection" class="rsvp-section">
    <div class="rsvp-card">
      <div style="text-align: center; margin-bottom: 24px;">
        <h2 class="section-title">RSVP</h2>
        <p class="section-subtitle">Kindly confirm your presence</p>
      </div>

      <form id="rsvpForm" data-phone="">
        <div class="rsvp-form-group">
          <label class="rsvp-label" for="rsvpName">Your Full Name *</label>
          <input type="text" id="rsvpName" class="rsvp-input" placeholder="e.g. Rahul Sharma" required />
        </div>

        <div class="rsvp-form-group">
          <label class="rsvp-label" for="rsvpStatus">Will You Be Joining Us? *</label>
          <select id="rsvpStatus" class="rsvp-select">
            <option value="accept">Joyfully Accepts (Will Attend)</option>
            <option value="decline">Regretfully Declines (Cannot Attend)</option>
          </select>
        </div>

        <div class="rsvp-form-group">
          <label class="rsvp-label" for="rsvpGuests">Number of Guests</label>
          <select id="rsvpGuests" class="rsvp-select">
            <option value="1">1 Guest</option>
            <option value="2">2 Guests</option>
            <option value="3">3 Guests</option>
            <option value="4">4 Guests</option>
            <option value="5+">5+ Guests (Family)</option>
          </select>
        </div>

        <div class="rsvp-form-group">
          <label class="rsvp-label">Events You Will Attend</label>
          {rsvp_checkboxes}
        </div>

        <div class="rsvp-form-group">
          <label class="rsvp-label" for="rsvpMessage">Wishes for the Couple</label>
          <textarea id="rsvpMessage" class="rsvp-textarea" rows="3" placeholder="Write your heartfelt wishes or dietary notes..."></textarea>
        </div>

        <button type="submit" class="btn-rsvp-submit">
          <span>Submit RSVP</span>
        </button>

        <button type="button" id="whatsappRsvpBtn" class="btn-whatsapp-rsvp">
          <span>💬 RSVP directly via WhatsApp</span>
        </button>
      </form>
    </div>
  </section>

  <!-- ============================================================
       8. FOOTER ARCH SECTION
       ============================================================ -->
  <footer class="footer-section">
    <div class="footer-arch-wrap">
      <img src="assets/arco-mediterraneo.png" alt="Decorative Arch" class="footer-arch-img" />
      <div class="footer-arch-content">
        <span class="footer-arch-name">{cfg["name1"]}</span>
        <span class="footer-arch-amp">{cfg["connector"]}</span>
        <span class="footer-arch-name">{cfg["name2"]}</span>
        <span class="footer-arch-date">{cfg["hero_date_header"]}</span>
      </div>
    </div>

    <p class="footer-tagline">Looking forward to celebrating with you!</p>
    <p class="footer-hashtag">{cfg["hashtag"]}</p>
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

# Generate root index.html using Version 1 as default with host routing enabled
root_content = build_html_page(VERSIONS[0], is_root=True)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(root_content)
print("Generated root index.html")
