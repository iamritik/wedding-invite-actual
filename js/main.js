/**
 * Fresco Wedding Invitation Interactive Logic
 * Tailored for Ritik & Vaibhavi
 */

document.addEventListener('DOMContentLoaded', () => {
  initEnvelope();
  initAudio();
  initCountdown();
  initPetals();
  initScrollNav();
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
    if (heroContent) {
      heroContent.classList.add('revealed');
    }
    overlay.classList.add('fading');
    setTimeout(() => {
      overlay.classList.add('hidden');
    }, 1500);
  };

  overlay.addEventListener('click', () => {
    if (hasStarted) return;
    hasStarted = true;

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

  // Fade into invitation 1.2s before video ends for a seamless blend
  video.addEventListener('timeupdate', () => {
    const dur = video.duration || 0;
    if (dur > 0 && video.currentTime >= dur - 1.2) {
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
      const countdown = document.getElementById('countdownSection');
      if (countdown) {
        countdown.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }
}
