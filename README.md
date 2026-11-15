# Ritik & Vaibhavi - Wedding Invitation Website Suite

A digital wedding invitation static website suite matching the Mediterranean / Italian Fresco aesthetic from [The Digital Yes reel](https://www.instagram.com/reel/Dew6je2R9Fb/).

---

## ✨ Features

1. **Realistic Envelope Opening Experience**:
   - Opens with the deckled handmade paper envelope tied with a silk chiffon ribbon bow.
   - On tap/click, the background music begins, the bow unties on video, and the envelope dissolves into the wedding card.
2. **Looped Cinematic Hero (Slide 1)**:
   - High-definition animated Mediterranean coastal oil painting with gentle coastal breezes and blooming jasmine.
   - Grand serif typography (`Antic Didone` + `Playfair Display`) with hand-illustrated rose botanical sprigs flanking the wedding dates.
   - Venue: **Manka by Cherish**
3. **Live Countdown (Integrated into Impasto Oil Frame)**:
   - Ticking down inside the authentic Italian impasto blue and gold oil painted frame (`marco-azul-impasto.png`) with calligraphic script numbers.
4. **"Our Story" Section (Slide 2)**:
   - Soft floating oil-painted cloud backdrop (`nubes-impasto.png`).
   - The couple's journey narrative with handwritten calligraphy signature.
5. **Celebration Events (Integrated into Fresco Canvas)**:
   - Seamlessly integrated directly into the olive fresco canvas with watercolor event icons, delicate botanical cenefas, and gold typography.
   - Broad timings: **Evening** for Sangeet & Reception, **Morning** for Haldi.
6. **Venue Section**:
   - Illustrated Mediterranean villa motif.
   - Venue Name: **Manka by Cherish**
   - Direct Google Maps link: [https://maps.app.goo.gl/ituhycePZ4x9FFBP8](https://maps.app.goo.gl/ituhycePZ4x9FFBP8)
7. **Background Wedding Music with Floating Audio Control**:
   - Romantic instrumental background music (`mohabbatein-love-theme.mp3`) starts on opening.
   - Floating frosted-glass audio button in the bottom right corner with animated ripple effects and mute/unmute toggle.
8. **Drifting Petals Animation**:
   - Lightweight floating flower petals drifting down with CSS keyframe sway and rotation.
9. **Architectural Arch Footer**:
   - Classical Mediterranean stone arch illustration enclosing the couple's monogram and date.

---

## 📂 The 4 Versions

| Folder | Version | Couple Header | Events Included | Target Audience |
|---|---|---|---|---|
| `version-1/` | **Version 1** | Ritik weds Vaibhavi | **Shaadi & Reception** (27th Jan 2027 · Evening) | Ritik's guests invited to wedding only |
| `version-2/` | **Version 2** | Vaibhavi weds Ritik | **Shaadi & Reception** (27th Jan 2027 · Evening) | Vaibhavi's guests invited to wedding only |
| `version-3/` | **Version 3** | Ritik weds Vaibhavi | **Sangeet & Ring Ceremony** (26th Jan · Evening)<br>**Haldi Ceremony** (27th Jan · Morning)<br>**Shaadi & Reception** (27th Jan · Evening) | Ritik's guests invited to all 3 events |
| `version-4/` | **Version 4** | Vaibhavi weds Ritik | **Sangeet & Ring Ceremony** (26th Jan · Evening)<br>**Haldi Ceremony** (27th Jan · Morning)<br>**Shaadi & Reception** (27th Jan · Evening) | Vaibhavi's guests invited to all 3 events |

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
