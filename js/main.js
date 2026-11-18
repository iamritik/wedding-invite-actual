/**
 * Fresco Wedding Invitation Interactive Logic
 * Tailored for Ritik & Vaibhavi
 */

// Force browser to not remember scroll position on refresh
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}

document.addEventListener('DOMContentLoaded', () => {
  // Always scroll to top immediately on page load
  window.scrollTo(0, 0);
  document.documentElement.scrollTop = 0;
  document.body.scrollTop = 0;

  // Check preview mode query param
  if (new URLSearchParams(window.location.search).has('preview')) {
    document.body.classList.add('show-preview');
  }

  initEnvelope();
  initAudio();
  initCountdown();
  initPetals();
  initScrollNav();
  initEventModal();
});

// Also reset scroll on pageshow (e.g. back/forward or reload from cache)
window.addEventListener('pageshow', () => {
  const urlParams = new URLSearchParams(window.location.search);
  if (!urlParams.has('opened') && !window.location.hash) {
    window.scrollTo(0, 0);
  }
});

// ============================================================
// 1. ENVELOPE OPENING EXPERIENCE
// ============================================================
function initEnvelope() {
  const overlay = document.getElementById('envelopeOverlay');
  const video = document.getElementById('envelopeVideo');
  const poster = document.getElementById('envelopePoster');
  const heroContent = document.getElementById('heroContent');

  if (!overlay || !video) return;

  let hasStarted = false;
  let hasRevealed = false;

  const revealHero = () => {
    if (hasRevealed) return;
    hasRevealed = true;
    document.body.classList.remove('envelope-active');
    // Ensure viewport is pinned to absolute top as invitation reveals
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    if (heroContent) {
      heroContent.classList.add('revealed');
    }
    overlay.classList.add('fading');
    setTimeout(() => {
      overlay.classList.add('hidden');
    }, 1500);
  };

  // Immediate bypass if opened or anchored
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('opened') || window.location.hash) {
    if (poster) poster.style.display = 'none';
    overlay.style.display = 'none';
    if (heroContent) heroContent.classList.add('revealed');
    hasRevealed = true;
    if (window.location.hash) {
      setTimeout(() => {
        const target = document.querySelector(window.location.hash);
        if (target) {
          target.scrollIntoView({ behavior: 'instant', block: 'start' });
        }
      }, 50);
    }
    return;
  }

  // Lock body scroll and pin to top while envelope animation is active
  document.body.classList.add('envelope-active');
  window.scrollTo(0, 0);

  const prompt = overlay.querySelector('.envelope-prompt');

  overlay.addEventListener('click', () => {
    if (hasStarted) {
      revealHero();
      return;
    }
    hasStarted = true;

    // Fade out tap prompt pill immediately on click
    if (prompt) {
      prompt.style.animation = 'none';
      prompt.style.transition = 'opacity 0.25s ease';
      prompt.style.opacity = '0';
      setTimeout(() => {
        prompt.style.display = 'none';
      }, 250);
    }

    // Start background music
    playAudio();

    // Fade out poster and play ribbon untying video
    if (poster) {
      poster.style.opacity = '0';
    }
    video.style.opacity = '1';

    const playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise.catch(err => {
        console.warn('Video auto-playback was blocked or failed:', err);
        revealHero();
      });
    }
  });

  // Allow the envelope opening animation to fully complete before revealing the invitation
  video.addEventListener('timeupdate', () => {
    const dur = video.duration || 0;
    if ((dur > 0 && video.currentTime >= dur - 0.4) || video.currentTime >= 7.6) {
      revealHero();
    }
  });

  video.addEventListener('ended', revealHero);
  video.addEventListener('error', revealHero);

  // Fallback keyboard/click handlers
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' || e.key === ' ' || e.key === 'Enter') {
      overlay.click();
    }
  }, { once: true });
}

// ============================================================
// 2. BACKGROUND MUSIC CONTROLLER
// ============================================================
let audioElem = null;
let isAudioPlaying = false;

function initAudio() {
  audioElem = document.getElementById('weddingAudio');
  const toggleBtn = document.getElementById('audioToggleBtn');
  const iconSound = document.getElementById('iconSound');
  const iconMute = document.getElementById('iconMute');

  if (!audioElem || !toggleBtn) return;

  audioElem.volume = 0.5;

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (audioElem.paused) {
      playAudio();
    } else {
      pauseAudio();
    }
  });
}

function playAudio() {
  if (!audioElem) return;
  const toggleBtn = document.getElementById('audioToggleBtn');
  const iconSound = document.getElementById('iconSound');
  const iconMute = document.getElementById('iconMute');

  audioElem.play().then(() => {
    isAudioPlaying = true;
    if (toggleBtn) {
      toggleBtn.classList.add('playing');
      toggleBtn.setAttribute('aria-label', 'Mute music');
    }
    if (iconSound) iconSound.style.display = 'block';
    if (iconMute) iconMute.style.display = 'none';
  }).catch(err => {
    console.log('Audio playback waiting for gesture:', err);
  });
}

function pauseAudio() {
  if (!audioElem) return;
  const toggleBtn = document.getElementById('audioToggleBtn');
  const iconSound = document.getElementById('iconSound');
  const iconMute = document.getElementById('iconMute');

  audioElem.pause();
  isAudioPlaying = false;
  if (toggleBtn) {
    toggleBtn.classList.remove('playing');
    toggleBtn.setAttribute('aria-label', 'Play music');
  }
  if (iconSound) iconSound.style.display = 'none';
  if (iconMute) iconMute.style.display = 'block';
}

// ============================================================
// 3. LIVE COUNTDOWN TIMER (INSIDE IMPASTO FRAME)
// ============================================================
function initCountdown() {
  const container = document.getElementById('countdownSection');
  if (!container) return;

  const targetDateStr = container.dataset.targetDate || '2027-01-27T18:00:00+05:30';
  const targetDate = new Date(targetDateStr).getTime();

  const daysElem = document.getElementById('cdDays');
  const hoursElem = document.getElementById('cdHours');
  const minsElem = document.getElementById('cdMins');
  const secsElem = document.getElementById('cdSecs');

  function update() {
    const now = new Date().getTime();
    const diff = targetDate - now;

    if (diff <= 0) {
      if (daysElem) daysElem.textContent = '0';
      if (hoursElem) hoursElem.textContent = '00';
      if (minsElem) minsElem.textContent = '00';
      if (secsElem) secsElem.textContent = '00';
      return;
    }

    const d = Math.floor(diff / (1000 * 60 * 60 * 24));
    const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((diff % (1000 * 60)) / 1000);

    if (daysElem) daysElem.textContent = String(d);
    if (hoursElem) hoursElem.textContent = String(h).padStart(2, '0');
    if (minsElem) minsElem.textContent = String(m).padStart(2, '0');
    if (secsElem) secsElem.textContent = String(s).padStart(2, '0');
  }

  update();
  setInterval(update, 1000);
}

// ============================================================
// 4. FLOATING PETALS ANIMATION
// ============================================================
function initPetals() {
  const container = document.getElementById('petalsContainer');
  if (!container) return;

  const petalImages = [
    'assets/petalo-1.png',
    'assets/petalo-2.png',
    'assets/petalo-3.png',
    'assets/petalo-crema.png'
  ];

  const petalConfigs = [
    { left: '8%', size: 24, fall: 14, sway: 3.2, delay: 0, src: 0 },
    { left: '22%', size: 20, fall: 16, sway: 2.6, delay: 4, src: 1 },
    { left: '36%', size: 28, fall: 15, sway: 3.8, delay: 7.5, src: 2 },
    { left: '50%', size: 22, fall: 17, sway: 3.0, delay: 2, src: 3 },
    { left: '64%', size: 26, fall: 14.5, sway: 3.4, delay: 9.5, src: 1 },
    { left: '78%', size: 19, fall: 16.5, sway: 2.8, delay: 5.5, src: 2 },
    { left: '90%', size: 23, fall: 15.0, sway: 3.5, delay: 11.0, src: 0 }
  ];

  petalConfigs.forEach(cfg => {
    const petal = document.createElement('img');
    petal.src = petalImages[cfg.src % petalImages.length];
    petal.alt = '';
    petal.className = 'falling-petal';
    petal.style.left = cfg.left;
    petal.style.width = cfg.size + 'px';
    petal.style.height = 'auto';
    petal.style.animation = `petalFall ${cfg.fall}s linear ${cfg.delay}s infinite, petalSway ${cfg.sway}s ease-in-out infinite alternate`;
    container.appendChild(petal);
  });
}

// ============================================================
// 5. SMOOTH SCROLL NAV HELPER
// ============================================================
function initScrollNav() {
  const scrollBtn = document.getElementById('heroScrollBtn');
  if (scrollBtn) {
    scrollBtn.addEventListener('click', () => {
      const ourStory = document.getElementById('ourStorySection');
      if (ourStory) {
        ourStory.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }
}

// ============================================================
// 6. EVENT CEREMONY DETAILS MODAL
// ============================================================
function initEventModal() {
  const modal = document.getElementById('eventDetailModal');
  const closeBtn = document.getElementById('closeEventModalBtn');
  const tiles = document.querySelectorAll('.event-tile-box');

  if (!modal || !tiles.length) return;

  function openModal(tile) {
    const title = tile.getAttribute('data-event-title') || '';
    const tagline = tile.getAttribute('data-event-tagline') || '';
    const date = tile.getAttribute('data-event-date') || '';
    const venue = tile.getAttribute('data-event-venue') || '';
    const city = tile.getAttribute('data-event-city') || '';
    const map = tile.getAttribute('data-event-map') || '#';
    const dress = tile.getAttribute('data-event-dress') || '';
    const desc = tile.getAttribute('data-event-desc') || '';
    const eventImg = tile.getAttribute('data-event-img') || '';
    const eventId = tile.getAttribute('data-event-id') || '';

    const modalTitle = document.getElementById('modalEventTitle');
    const modalTagline = document.getElementById('modalEventTagline');
    const modalDate = document.getElementById('modalEventDate');
    const modalVenue = document.getElementById('modalEventVenue');
    const modalCity = document.getElementById('modalEventCity');
    const modalMap = document.getElementById('modalEventMapLink');
    const modalDress = document.getElementById('modalEventDress');
    const modalDressWrap = document.getElementById('modalDressCodeWrap');
    const modalSwatches = document.getElementById('modalDressSwatches');
    const modalDesc = document.getElementById('modalEventDesc');
    const modalImg = document.getElementById('modalEventImg');

    if (modalTitle) modalTitle.textContent = title;
    if (modalTagline) modalTagline.textContent = tagline;
    if (modalDate) modalDate.textContent = date;
    if (modalVenue) modalVenue.textContent = venue;
    if (modalCity) modalCity.textContent = city;
    if (modalMap) modalMap.href = map;
    if (modalDesc) modalDesc.textContent = desc;
    if (modalImg && eventImg) {
      modalImg.src = eventImg;
      modalImg.alt = title;
    }

    if (modalDressWrap) {
      if (dress) {
        if (modalDress) modalDress.textContent = dress;
        modalDressWrap.style.display = 'block';

        if (modalSwatches) {
          if (eventId === 'haldi') {
            modalSwatches.innerHTML = `
              <span class="swatch-circle" style="background: #801538;" title="Deep Magenta"></span>
              <span class="swatch-circle" style="background: #c92a63;" title="Rose Pink"></span>
              <span class="swatch-circle" style="background: #e85d88;" title="Bubblegum"></span>
              <span class="swatch-circle" style="background: #f498b5;" title="Blush"></span>
              <span class="swatch-circle" style="background: #fcd1de;" title="Pastel Pink"></span>
            `;
          } else if (eventId === 'cocktail' || eventId === 'sangeet') {
            modalSwatches.innerHTML = `
              <span class="swatch-circle" style="background: #0c1e54;" title="Midnight Blue"></span>
              <span class="swatch-circle" style="background: #c59b4e;" title="Gold Glitter"></span>
              <span class="swatch-circle" style="background: #d8d8d8;" title="Silver Sparkle"></span>
              <span class="swatch-circle" style="background: #1b3260;" title="Navy Blue"></span>
              <span class="swatch-circle" style="background: #ebd5a8;" title="Champagne Shimmer"></span>
            `;
          } else {
            modalSwatches.innerHTML = '';
          }
        }
      } else {
        modalDressWrap.style.display = 'none';
        if (modalSwatches) modalSwatches.innerHTML = '';
      }
    }

    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');
  }

  function closeModal() {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');
  }

  tiles.forEach(tile => {
    tile.addEventListener('click', () => openModal(tile));
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });
}
