# Ritik & Vaibhavi - Wedding Invitation Website Suite

A digital wedding invitation static website suite matching the Mediterranean / Italian Fresco aesthetic from [The Digital Yes reel](https://www.instagram.com/reel/Dew6je2R9Fb/).

---

## ✨ Features Included

1. **Realistic Envelope Opening Experience**:
   - Opens with the deckled handmade paper envelope wrapped with a silk chiffon ribbon bow.
   - On tap/click, the bow unties and the envelope unfolds into the invitation with a smooth dissolve animation.
2. **Looped Cinematic Hero**:
   - High-definition animated Mediterranean coastal oil painting with gentle coastal breezes and blooming jasmine.
   - Elegant serif typography (`Antic Didone` + `Playfair Display`) with hand-illustrated rose botanical sprigs flanking the wedding dates.
3. **Background Wedding Music with Controls**:
   - Acoustic instrumental background music (`semo-fireflies.mp3`) starts on opening.
   - Floating frosted-glass audio button in the bottom right corner with animated ripple effects and mute/unmute toggle.
4. **Live Dynamic Countdown**:
   - Real-time countdown timer ticking down to January 2027 (Days, Hours, Minutes, Seconds).
5. **Interactive Event Cards**:
   - Event cards with watercolor icons (`baile-nupcial.png`, `flor-almendro.png`, `boda-floral-arco.png`).
   - "Add to Google Calendar" button (direct web calendar link).
   - "Download .ICS" button (Apple Calendar, Outlook, Google Calendar import).
6. **Venue Section**:
   - Illustrated Mediterranean villa motif.
   - "View on Google Maps" direct link.
7. **Interactive RSVP Form**:
   - Guest name, attendance status, party size, event selections.
   - Direct "RSVP via WhatsApp" button that pre-formats a WhatsApp message to send straight to the couple.
8. **Drifting Petals Animation**:
   - Lightweight floating flower petals drifting down with CSS keyframe sway and rotation.
9. **Architectural Arch Footer**:
   - Classical Mediterranean stone arch illustration enclosing the couple's monogram and date.

---

## 📂 The 4 Versions

| Folder | Version | Couple Header | Events Included | Target Audience |
|---|---|---|---|---|
| `version-1/` | **Version 1** | Ritik weds Vaibhavi | **Shaadi Reception** (27th Jan 2027) | Ritik's guests invited to wedding only |
| `version-2/` | **Version 2** | Vaibhavi weds Ritik | **Shaadi Reception** (27th Jan 2027) | Vaibhavi's guests invited to wedding only |
| `version-3/` | **Version 3** | Ritik weds Vaibhavi | **Sangeet** (26th Jan night)<br>**Haldi** (27th Jan morning)<br>**Shaadi Reception** (27th Jan evening) | Ritik's guests invited to all 3 events |
| `version-4/` | **Version 4** | Vaibhavi weds Ritik | **Sangeet** (26th Jan night)<br>**Haldi** (27th Jan morning)<br>**Shaadi Reception** (27th Jan evening) | Vaibhavi's guests invited to all 3 events |

---

## 🚀 Quick Local Preview

Run any lightweight web server from this directory:

```bash
# Using Python 3
python3 -m http.server 8080
```

Now open:
- Root & Switcher: [http://localhost:8080/](http://localhost:8080/)
- Version 1: [http://localhost:8080/version-1/](http://localhost:8080/version-1/)
- Version 2: [http://localhost:8080/version-2/](http://localhost:8080/version-2/)
- Version 3: [http://localhost:8080/version-3/](http://localhost:8080/version-3/)
- Version 4: [http://localhost:8080/version-4/](http://localhost:8080/version-4/)

> **Note:** A top navigation bar is included for quick switching between versions during testing.

---

## 🦆 Setting Up with DuckDNS

You can create 4 DuckDNS subdomains, for example:
1. `ritik-shaadi.duckdns.org`
2. `vaibhavi-shaadi.duckdns.org`
3. `ritik-all.duckdns.org`
4. `vaibhavi-all.duckdns.org`

### Option 1: Automatic Routing via `index.html` (Easiest)
If all 4 subdomains point to your server running on a single port (e.g. port 80/443 pointing to `shaadi-invite/`):
- `index.html` contains an automatic host router that inspects the domain name:
  - Subdomains containing `ritik` and `all`/`sangeet` → automatically redirect to `version-3/`
  - Subdomains containing `vaibhavi` and `all`/`sangeet` → automatically redirect to `version-4/`
  - Subdomains containing `ritik` → automatically redirect to `version-1/`
  - Subdomains containing `vaibhavi` → automatically redirect to `version-2/`

### Option 2: Nginx Server Blocks (Direct Hostname to Folder)
If you prefer each DuckDNS domain to serve directly from its folder without redirecting the URL path:

```nginx
# Version 1 (Ritik - Shaadi Only)
server {
    server_name ritik-shaadi.duckdns.org;
    root /var/www/shaadi-invite/version-1;
    index index.html;
    location / {
        try_files $uri $uri/ /index.html;
    }
}

# Version 2 (Vaibhavi - Shaadi Only)
server {
    server_name vaibhavi-shaadi.duckdns.org;
    root /var/www/shaadi-invite/version-2;
    index index.html;
    location / {
        try_files $uri $uri/ /index.html;
    }
}

# Version 3 (Ritik - All 3 Events)
server {
    server_name ritik-all.duckdns.org;
    root /var/www/shaadi-invite/version-3;
    index index.html;
    location / {
        try_files $uri $uri/ /index.html;
    }
}

# Version 4 (Vaibhavi - All 3 Events)
server {
    server_name vaibhavi-all.duckdns.org;
    root /var/www/shaadi-invite/version-4;
    index index.html;
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

### Option 3: Caddyfile Configuration
```caddy
ritik-shaadi.duckdns.org {
    root * /var/www/shaadi-invite/version-1
    file_server
}

vaibhavi-shaadi.duckdns.org {
    root * /var/www/shaadi-invite/version-2
    file_server
}

ritik-all.duckdns.org {
    root * /var/www/shaadi-invite/version-3
    file_server
}

vaibhavi-all.duckdns.org {
    root * /var/www/shaadi-invite/version-4
    file_server
}
```

---

## ✏️ Customizing Details Later

All configurations can be customized at any time:

1. **Venue Details**:
   - In each `version-X/index.html`, search for `Grand Heritage Palace, Jaipur` and update the title, address, and Google Maps query link (`https://www.google.com/maps/search/?api=1&query=...`).
2. **WhatsApp RSVP Phone Number**:
   - In each `version-X/index.html`, find `id="rsvpForm" data-phone=""` and enter your phone number with country code (e.g. `data-phone="919876543210"`). When guests click "RSVP via WhatsApp", it will directly open a chat with this number!
3. **Background Music**:
   - Replace `assets/semo-fireflies.mp3` with any wedding music audio file (MP3 format) of your choice!
