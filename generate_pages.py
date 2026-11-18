import os

VERSIONS = [
    {
        "id": "1",
        "side": "ritik",
        "dir": "version-1",
        "title": "Ritik weds Vaibhavi | Wedding Invitation",
        "name1": "Ritik",
        "connector": "weds",
        "name2": "Vaibhavi",
        "story_sign": "-Ritik &amp; Vaibhavi",
        "parents_names": "Kavita &amp; Naresh Arora",
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
        "side": "vaibhavi",
        "dir": "version-2",
        "title": "Vaibhavi weds Ritik | Wedding Invitation",
        "name1": "Vaibhavi",
        "connector": "weds",
        "name2": "Ritik",
        "story_sign": "-Vaibhavi &amp; Ritik",
        "parents_names": "Vivek Singh, Manju Singh &amp; Yash Singh",
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
        "side": "ritik",
        "dir": "version-3",
        "title": "Ritik weds Vaibhavi | Wedding Celebrations",
        "name1": "Ritik",
        "connector": "weds",
        "name2": "Vaibhavi",
        "story_sign": "-Ritik &amp; Vaibhavi",
        "parents_names": "Kavita &amp; Naresh Arora",
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
        "side": "vaibhavi",
        "dir": "version-4",
        "title": "Vaibhavi weds Ritik | Wedding Celebrations",
        "name1": "Vaibhavi",
        "connector": "weds",
        "name2": "Ritik",
        "story_sign": "-Vaibhavi &amp; Ritik",
        "parents_names": "Vivek Singh, Manju Singh &amp; Yash Singh",
        "hero_date_month": "January",
        "hero_date_day": "26 – 27",
        "hero_date_dayname": "Tuesday & Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "26 – 27 January 2027",
        "target_date_iso": "2027-01-26T17:30:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "events_type": "all_events",
        "hashtag": "#VRinLove",
        "preview_name": "Version 4: Vaibhavi's Side (Cocktail & Haldi)"
    },
    {
        "id": "5",
        "side": "vaibhavi",
        "dir": "version-5",
        "title": "Vaibhavi weds Ritik | Wedding Celebrations",
        "name1": "Vaibhavi",
        "connector": "weds",
        "name2": "Ritik",
        "story_sign": "-Vaibhavi &amp; Ritik",
        "parents_names": "Vivek Singh, Manju Singh &amp; Yash Singh",
        "hero_date_month": "January",
        "hero_date_day": "25 – 27",
        "hero_date_dayname": "Monday to Wednesday",
        "hero_date_year": "2027",
        "hero_date_header": "25 – 27 January 2027",
        "target_date_iso": "2027-01-25T17:00:00+05:30",
        "target_date_label": "Until the Celebrations Begin",
        "events_type": "all_events",
        "hashtag": "#VRinLove",
        "preview_name": "Version 5: Vaibhavi's Side (+ Mehendi)"
    }
]

# Ritik's All Events List
RITIK_EVENTS = [
    {
        "id": "mehendi",
        "title": "Mehendi",
        "tagline": "Auspicious Henna & Folk Melodies",
        "date_badge": "25 Jan · 5:00 PM",
        "date_full": "Monday, 25 January 2027 · 5:00 PM",
        "venue": "701 Sector 8",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/hfNK1a2bUqbJ2QY28",
        "dress_code": "",
        "desc": "An auspicious beginning filled with vibrant henna, festive Punjabi boliyan, music, and laughter to kick off our wedding festivities.",
        "icon_img": "assets/ramita-capullos.png",
    },
    {
        "id": "hawan",
        "title": "Hawan",
        "tagline": "Auspicious Vedic Prayers & Blessings",
        "date_badge": "26 Jan · 11:00 AM",
        "date_full": "Tuesday, 26 January 2027 · 11:00 AM (Morning)",
        "venue": "701 Sector 8",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/hfNK1a2bUqbJ2QY28",
        "dress_code": "",
        "desc": "Sacred Vedic prayers and yajna to invoke divine blessings of the deities and ancestors for peace, harmony, and prosperity.",
        "icon_img": "assets/hawan-flame.png",
    },
    {
        "id": "cocktail",
        "title": "Cocktail",
        "tagline": "An Evening of Music, Dance & Glamour",
        "date_badge": "26 Jan · 5:30 PM",
        "date_full": "Tuesday, 26 January 2027 · 5:30 PM onwards",
        "venue": "Tara Hall & Lawn, Hotel Jewels",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "All that Sparkles",
        "desc": "Ring ceremony and shagun, followed by an enchanting evening of music, dance performances, and dinner till midnight.",
        "icon_img": "assets/baile-nupcial.png",
    },
    {
        "id": "haldi",
        "title": "Haldi Ceremony",
        "tagline": "Joyous Morning Blessings",
        "date_badge": "27 Jan · 10:30 AM",
        "date_full": "Wednesday, 27 January 2027 · 10:30 AM (Morning)",
        "venue": "Celebrations Hall & Lawn, Hotel Jewels",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Sink into Pink",
        "desc": "Joyous morning rituals smeared in holy turmeric, vibrant yellow marigolds, and cherished family blessings.",
        "icon_img": "assets/flor-almendro.png",
    },
    {
        "id": "gharoli",
        "title": "Gharoli",
        "tagline": "Sacred Water Fetching Ceremony",
        "date_badge": "27 Jan · 2:00 PM",
        "date_full": "Wednesday, 27 January 2027 · 2:00 PM",
        "venue": "Hotel Jewels",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "",
        "desc": "The beloved traditional ritual where family fetches sanctified holy water to bathe the groom before the wedding rituals.",
        "icon_img": "assets/fuente-jardin-mediterraneo.png",
    },
    {
        "id": "sehrabandi",
        "title": "Sehrabandi",
        "tagline": "Tying of the Royal Sehra & Baraat",
        "date_badge": "27 Jan · 5:00 PM",
        "date_full": "Wednesday, 27 January 2027 · 5:00 PM",
        "venue": "701 Sector 8",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/hfNK1a2bUqbJ2QY28",
        "dress_code": "",
        "desc": "The time-honored ceremony where sisters tie the auspicious floral sehra on the groom, followed by the grand Baraat procession.",
        "icon_img": "assets/icono-arco.png",
    },
]

# Vaibhavi's Events for Version 4 (Cocktail & Haldi)
VAIBHAVI_V4_EVENTS = [
    {
        "id": "cocktail",
        "title": "Cocktail",
        "tagline": "An Evening of Music, Dance & Glamour",
        "date_badge": "26 Jan · 5:30 PM",
        "date_full": "Tuesday, 26 January 2027 · 5:30 PM onwards",
        "venue": "Tara Hall & Lawn, Hotel Jewels",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "All that Sparkles",
        "desc": "Ring ceremony and shagun, followed by an enchanting evening of music, dance performances, and dinner till midnight.",
        "icon_img": "assets/baile-nupcial.png",
    },
    {
        "id": "haldi",
        "title": "Haldi Ceremony",
        "tagline": "Joyous Morning Blessings",
        "date_badge": "27 Jan · 10:30 AM",
        "date_full": "Wednesday, 27 January 2027 · 10:30 AM (Morning)",
        "venue": "Celebrations Hall & Lawn, Hotel Jewels",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Sink into Pink",
        "desc": "Joyous morning rituals smeared in holy turmeric, vibrant yellow marigolds, and cherished family blessings.",
        "icon_img": "assets/flor-almendro.png",
    },
]

# Vaibhavi's Events for Version 5 (Mehendi + Cocktail + Haldi)
VAIBHAVI_V5_EVENTS = [
    {
        "id": "mehendi",
        "title": "Mehendi",
        "tagline": "Auspicious Henna & Folk Melodies",
        "date_badge": "25 Jan · 5:00 PM",
        "date_full": "Monday, 25 January 2027 · 5:00 PM",
        "venue": "701 Sector 8",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/hfNK1a2bUqbJ2QY28",
        "dress_code": "",
        "desc": "An auspicious beginning filled with vibrant henna, festive Punjabi boliyan, music, and laughter to kick off our wedding festivities.",
        "icon_img": "assets/ramita-capullos.png",
    },
    {
        "id": "cocktail",
        "title": "Cocktail",
        "tagline": "An Evening of Music, Dance & Glamour",
        "date_badge": "26 Jan · 5:30 PM",
        "date_full": "Tuesday, 26 January 2027 · 5:30 PM onwards",
        "venue": "Tara Hall & Lawn, Hotel Jewels",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "All that Sparkles",
        "desc": "Ring ceremony and shagun, followed by an enchanting evening of music, dance performances, and dinner till midnight.",
        "icon_img": "assets/baile-nupcial.png",
    },
    {
        "id": "haldi",
        "title": "Haldi Ceremony",
        "tagline": "Joyous Morning Blessings",
        "date_badge": "27 Jan · 10:30 AM",
        "date_full": "Wednesday, 27 January 2027 · 10:30 AM (Morning)",
        "venue": "Celebrations Hall & Lawn, Hotel Jewels",
        "city": "Karnal",
        "map_url": "https://maps.app.goo.gl/iPMQNdDQFKcHsKs29",
        "dress_code": "Sink into Pink",
        "desc": "Joyous morning rituals smeared in holy turmeric, vibrant yellow marigolds, and cherished family blessings.",
        "icon_img": "assets/flor-almendro.png",
    },
]

def build_festivities_screen(cfg):
    if cfg["id"] == "3":
        events = RITIK_EVENTS
    elif cfg["id"] == "5":
        events = VAIBHAVI_V5_EVENTS
    else:
        events = VAIBHAVI_V4_EVENTS

    count_class = f"events-count-{len(events)}"

    tiles_html = ""
    for ev in events:
        tiles_html += f"""
        <button type="button" class="event-tile-box"
          data-event-id="{ev['id']}"
          data-event-title="{ev['title']}"
          data-event-tagline="{ev['tagline']}"
          data-event-date="{ev['date_full']}"
          data-event-venue="{ev['venue']}"
          data-event-city="{ev['city']}"
          data-event-map="{ev['map_url']}"
          data-event-dress="{ev['dress_code']}"
          data-event-desc="{ev['desc']}"
          data-event-img="{ev['icon_img']}"
          aria-label="View details for {ev['title']}">
          <div class="tile-icon-bubble">
            <img src="{ev['icon_img']}" alt="" class="tile-img-icon" />
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
      <div class="events-header-card">
        <p class="events-screen-label">Pre-Wedding Festivities</p>
        <h2 class="events-screen-title">Events &amp; Celebrations</h2>
        <p class="events-screen-hint">Tap any celebration to view venue &amp; details</p>
      </div>

      <div class="events-boxes-grid {count_class}">
{tiles_html}
      </div>
    </div>
  </section>
"""

def build_shaadi_reception_screen(cfg):
    dinner_time = "9:00 PM" if cfg["side"] == "ritik" else "8:00 PM"
    return f"""
  <!-- ============================================================
       WEDDING CEREMONY & RECEPTION (WITH INTEGRATED VENUE & MAPS)
       ============================================================ -->
  <section id="shaadiReceptionSection" class="shaadi-reception-section">
    <img src="assets/screen_shaadi_reception.jpg" alt="Royal Wedding Mandap" class="shaadi-reception-bg" />

    <div class="shaadi-reception-content wedding-maroon-card">
      <div class="event-icon-wrap wedding-icon-wrap">
        <img src="assets/boda-floral-arco.png" alt="Wedding Floral Arch" class="event-icon" />
      </div>
      
      <p class="wedding-eyebrow">The Auspicious Wedding Union</p>
      <h2 class="wedding-main-title">Shubh Vivaah</h2>
      
      <div class="wedding-date-tag">
        <span>Wednesday, 27 January 2027</span>
      </div>

      <!-- Wedding Timeline Highlights -->
      <div class="wedding-timeline-card">
        <div class="wedding-timeline-row">
          <span class="wedding-time">{dinner_time}</span>
          <span class="wedding-dot">&bull;</span>
          <span class="wedding-event-name">Gala Dinner</span>
        </div>
        <div class="wedding-timeline-sep"></div>
        <div class="wedding-timeline-row pheres-row">
          <div class="pheras-text-wrap">
            <span class="wedding-event-name pheras-title">Saath Phere and Doli</span>
            <span class="wedding-pheras-sub">Taaron ki chhao mein</span>
          </div>
        </div>
      </div>

      <!-- Integrated Venue & Maps Location -->
      <div class="wedding-venue-section">
        <p class="wedding-venue-eyebrow">WEDDING VENUE</p>
        <h4 class="wedding-venue-title">Manka by Cherish</h4>
        <p class="wedding-venue-location">Karnal</p>
        <a href="https://maps.app.goo.gl/ituhycePZ4x9FFBP8" target="_blank" rel="noopener noreferrer" class="btn-wedding-maps">
          <span>View Location on Google Maps &rarr;</span>
        </a>
      </div>
    </div>
  </section>
"""

def build_countdown_screen(cfg):
    return f"""
  <!-- ============================================================
       COUNTDOWN SECTION (FULL BLEED ROYAL ARCH BACKGROUND)
       ============================================================ -->
  <section id="countdownSection" class="countdown-section" data-target-date="{cfg["target_date_iso"]}">
    <img src="assets/countdown-arch-frame.jpg" alt="Countdown until Celebrations Begin" class="countdown-bg-image" />

    <div class="countdown-inner-content">
      <!-- Vertical Stack of Live Units within Arched Parchment -->
      <div class="countdown-stack-units">
        <div class="countdown-unit-block">
          <span id="cdDays" class="countdown-num">0</span>
          <span class="countdown-lbl">Days</span>
        </div>
        <div class="countdown-unit-block">
          <span id="cdHours" class="countdown-num">00</span>
          <span class="countdown-lbl">Hours</span>
        </div>
        <div class="countdown-unit-block">
          <span id="cdMins" class="countdown-num">00</span>
          <span class="countdown-lbl">Minutes</span>
        </div>
        <div class="countdown-unit-block">
          <span id="cdSecs" class="countdown-num">00</span>
          <span class="countdown-lbl">Seconds</span>
        </div>
      </div>
    </div>
  </section>
"""

def build_last_screen(cfg):
    if cfg["side"] == "ritik":
        # Ritik's Parents screen with family members and Raha note
        return f"""
  <!-- ============================================================
       LAST SCREEN (WARMLY INVITED BY PARENTS & SACRED PHERAS ARCH)
       ============================================================ -->
  <footer id="footerSection" class="footer-section">
    <!-- Royal Arch & Mandap Painting Backdrop -->
    <div class="footer-painting-container">
      <img src="assets/screen_last.jpg" alt="Wedding Mandap Arch" class="footer-painting-bg" />
      <img src="assets/screen_last_lotus.png" alt="" class="footer-moving-lotus" />
      <img src="assets/screen_last_flame.png" alt="" class="footer-moving-flame" />
    </div>

    <div class="footer-content">
      <p class="footer-invitation-lead">Warmly Invited By</p>
      <h3 class="footer-family-member">Kavita &amp; Naresh Arora</h3>
      <h3 class="footer-family-member">Reet &amp; Sanyam Ahuja</h3>

      <p class="footer-grandparents-lead">With best compliments from Grandparents</p>

      <div class="baby-raha-card">
        <p class="baby-raha-quote">&ldquo;Mele maamu ki shaadi mei jalul jalul aana&rdquo;</p>
        <p class="baby-raha-author">&mdash; Raha</p>
      </div>

      <p class="footer-tagline">Looking forward to celebrating with you!</p>

      <p class="footer-hashtag">{cfg["hashtag"]}</p>
    </div>
  </footer>
"""
    else:
        # Vaibhavi's Parents screen with Grandparents & Family illustration
        return f"""
  <!-- ============================================================
       LAST SCREEN (WARMLY INVITED BY PARENTS & GRANDPARENTS BLESSINGS)
       ============================================================ -->
  <footer id="footerSection" class="footer-section vaibhavi-footer">
    <div class="footer-painting-container">
      <img src="assets/vaibhavi-parents-bg.jpg" alt="Vaibhavi Family Blessing" class="footer-painting-bg vaibhavi-footer-bg" />
    </div>

    <div class="footer-content vaibhavi-footer-content">
      <p class="footer-invitation-lead">Warmly Invited By</p>
      <h3 class="footer-parents-names">Vivek Singh, Manju Singh &amp; Yash Singh</h3>
      <p class="vaibhavi-grandparents-lead">With the love and blessings of her grandparents</p>

      <div class="vaibhavi-grandparents-grid">
        <div class="grandparents-col">
          <h4 class="grandparents-heading">Paternal Grandparents</h4>
          <p class="grandparents-names">(Late) Shri Surendrapal Singh Verma<br>&amp; Smt. Kailashvati</p>
        </div>
        <div class="grandparents-col">
          <h4 class="grandparents-heading">Maternal Grandparents</h4>
          <p class="grandparents-names">Shri Mohar Singh Verma<br>&amp; Smt. Mishra Devi</p>
        </div>
      </div>

      <p class="footer-hashtag">{cfg["hashtag"]}</p>
    </div>
  </footer>
"""

def build_html_page(cfg, is_root=False):
    festivities_html = build_festivities_screen(cfg) if cfg["events_type"] == "all_events" else ""
    shaadi_reception_html = build_shaadi_reception_screen(cfg)
    countdown_html = build_countdown_screen(cfg)
    last_screen_html = build_last_screen(cfg)

    switcher_links = ""
    for v in VERSIONS:
        active_cls = "active" if v["id"] == cfg["id"] else ""
        link_target = f"../{v['dir']}/" if not is_root else f"version-{v['id']}/"
        label_text = f"Version {v['id']}: {v['name1'][0]}&{v['name2'][0]}"
        if v["id"] == "5":
            label_text += " (+Mehendi)"
        elif v["events_type"] == "shaadi_only":
            label_text += " (Shaadi)"
        else:
            label_text += " (All)"
        switcher_links += f'<a href="{link_target}" class="preview-switcher-item {active_cls}">{label_text}</a>\n'

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
      if (v === '5') { window.location.replace('version-5/'); return; }

      // Hostname-based routing for DuckDNS:
      if (host.indexOf('ritik') !== -1 && (host.indexOf('all') !== -1 || host.indexOf('sangeet') !== -1 || host.indexOf('cocktail') !== -1)) {
        window.location.replace('version-3/');
      } else if (host.indexOf('vaibhavi') !== -1 && (host.indexOf('all') !== -1 || host.indexOf('sangeet') !== -1 || host.indexOf('cocktail') !== -1)) {
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{cfg["title"]}</title>
{duckdns_router_script}
  <!-- Favicons (Classic & Touch) -->
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png" />

  <!-- WhatsApp / Social Media Rich Link Previews (OpenGraph) -->
  <meta property="og:title" content="{cfg["name1"]} &amp; {cfg["name2"]} — Wedding Invitation" />
  <meta property="og:description" content="We invite you to celebrate our wedding &bull; January 25 &ndash; 27, 2027 &bull; Karnal" />
  <meta name="description" content="Wedding celebration invitation for {cfg["name1"]} &amp; {cfg["name2"]} - {cfg["hero_date_header"]}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://vrinlove.duckdns.org/" />
  <meta property="og:site_name" content="Ritik &amp; Vaibhavi Wedding" />
  <meta property="og:image" content="https://vrinlove.duckdns.org/assets/og-whatsapp-thumb.jpg" />
  <meta property="og:image:secure_url" content="https://vrinlove.duckdns.org/assets/og-whatsapp-thumb.jpg" />
  <meta property="og:image:type" content="image/jpeg" />
  <meta property="og:image:width" content="600" />
  <meta property="og:image:height" content="600" />
  <meta property="og:image:alt" content="Ritik &amp; Vaibhavi Wedding Invitation" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{cfg["name1"]} &amp; {cfg["name2"]} — Wedding Invitation" />
  <meta name="twitter:description" content="We invite you to celebrate our wedding &bull; January 25 &ndash; 27, 2027 &bull; Karnal" />
  <meta name="twitter:image" content="https://vrinlove.duckdns.org/assets/og-whatsapp-thumb.jpg" />

  <!-- CSS Stylesheet -->
  <link rel="stylesheet" href="css/style.css?v=2027h" />
</head>
<body class="envelope-active">

  <!-- DuckDNS Multi-Version Switcher Bar -->
  <aside class="preview-switcher-bar" aria-label="Version preview switcher">
    <div class="preview-switcher-content">
      <span class="preview-switcher-label">DuckDNS Preview:</span>
{switcher_links}    </div>
  </aside>

  <!-- Floating Petals Container -->
  <div id="petalsContainer" class="petals-container" aria-hidden="true"></div>

  <!-- Floating Audio Controller -->
  <button id="audioToggleBtn" class="audio-toggle-btn music-toggle-btn" aria-label="Play music" title="Toggle Music">
    <svg id="iconSound" class="music-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: none;">
      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
      <path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>
      <path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path>
    </svg>
    <svg id="iconMute" class="music-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
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
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="envelope-prompt-svg">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
          <polyline points="22,6 12,13 2,6"></polyline>
        </svg>
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
    </div>

    <!-- Scroll down indicator -->
    <button id="heroScrollBtn" class="hero-scroll-btn" aria-label="Scroll down to Our Story">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="6 9 12 15 18 9"></polyline>
      </svg>
    </button>
  </section>

  <!-- ============================================================
       OUR STORY SECTION (SLIDE 2 - IMMEDIATE NEXT AFTER HERO)
       ============================================================ -->
  <section id="ourStorySection" class="our-story-section">
    <img src="assets/nubes-impasto.png" alt="" class="our-story-clouds" />

    <div class="our-story-inner">
      <h2 class="our-story-title">Our Story</h2>
      <p class="our-story-tagline">Who knew a right swipe could get this right?</p>

      <div class="our-story-content">
        <p class="our-story-text">
          It all started with a swipe. Ritik swiped right, and on 2nd November 2025, Vaibhavi matched. What followed was a month of conversations, even as Vaibhavi travelled for a friend's wedding and Ritik was back home in Karnal. Though both lived in Bangalore, they wouldn't meet just yet.
        </p>

        <p class="our-story-text">
          Finally, on 30th November, they went on their first date. What was supposed to be dinner turned into conversations that lasted until 5 AM.
        </p>

        <p class="our-story-text">
          Since then, they've become each other's favourite gossip partners, intellectual sparring partners and biggest cheerleaders. Whether it's endless banter, celebrating each other's achievements or pushing one another to be better, they've found someone with whom they can be unapologetically themselves.
        </p>

        <div class="our-story-highlight">
          Still each other's favourite notification, favourite person and favourite conversation.
        </div>

        <p class="our-story-signature">{cfg["story_sign"]}</p>
      </div>
    </div>
  </section>

{festivities_html}
{shaadi_reception_html}
{countdown_html}
{last_screen_html}

  <!-- ============================================================
       EVENT DETAILS MODAL
       ============================================================ -->
  <div id="eventDetailModal" class="event-modal-backdrop" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="event-modal-card">
      <button type="button" id="modalCloseBtn" class="modal-close-btn event-modal-close" aria-label="Close modal">&times;</button>
      
      <div class="event-modal-icon-wrap">
        <img id="modalEventImg" src="assets/baile-nupcial.png" alt="" class="modal-event-icon modal-img-icon" />
      </div>

      <p id="modalEventTagline" class="event-modal-eyebrow event-modal-tagline">CEREMONY DETAILS</p>
      <h3 id="modalEventTitle" class="event-modal-title">Event Title</h3>
      
      <div class="event-modal-date-tag event-modal-time-badge">
        <span id="modalEventDate">Date &amp; Time</span>
      </div>

      <p id="modalEventDesc" class="event-modal-desc">Description</p>

      <div class="event-modal-venue-box">
        <div class="event-modal-venue-header">
          <div class="venue-pin-bubble venue-box-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
              <circle cx="12" cy="10" r="3"></circle>
            </svg>
          </div>
          <div class="venue-box-details">
            <p class="venue-box-label venue-header-label">VENUE</p>
            <h4 id="modalEventVenue" class="venue-box-name modal-venue-name">Venue Name</h4>
            <p id="modalEventCity" class="venue-box-city modal-venue-city">City</p>
          </div>
        </div>
        <a id="modalEventMapLink" href="#" target="_blank" rel="noopener noreferrer" class="btn-modal-map btn-modal-maps">
          <span>View Location on Google Maps &rarr;</span>
        </a>
      </div>

      <div id="modalDressCodeWrap" class="event-modal-dress-prominent" style="display: none;">
        <p class="modal-dress-eyebrow">DRESS CODE</p>
        <h4 id="modalEventDress" class="modal-dress-theme">Dress Code</h4>
        <div id="modalDressSwatches" class="palette-swatches-row"></div>
      </div>
    </div>
  </div>

  <!-- JavaScript Bundle -->
  <script src="js/main.js?v=2027h"></script>
</body>
</html>
"""
    return html

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate versioned folders
    for cfg in VERSIONS:
        folder_path = os.path.join(root_dir, cfg["dir"])
        os.makedirs(folder_path, exist_ok=True)

        # Ensure symlinks for assets, css, js, favicon.ico exist in each version folder
        for link_name, target in [("assets", "../assets"), ("css", "../css"), ("js", "../js"), ("favicon.ico", "../favicon.ico")]:
            link_path = os.path.join(folder_path, link_name)
            if not os.path.exists(link_path):
                try:
                    os.symlink(target, link_path)
                except OSError:
                    pass

        html_content = build_html_page(cfg, is_root=False)
        with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {cfg['dir']}/index.html")

    # Generate root index.html (defaulting to Version 1 with client-side DuckDNS routing)
    root_html = build_html_page(VERSIONS[0], is_root=True)
    with open(os.path.join(root_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(root_html)
    print("Generated root index.html")

if __name__ == "__main__":
    main()
