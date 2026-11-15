/**
 * Fresco Wedding Invitation Interactive Logic
 * Tailored for Ritik & Vaibhavi
 */

document.addEventListener('DOMContentLoaded', () => {
  // Check preview mode query param
  if (new URLSearchParams(window.location.search).has('preview')) {
    document.body.classList.add('show-preview');
  }

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

  const prompt = overlay.querySelector('.envelope-prompt');

  overlay.addEventListener('click', () => {
    if (hasStarted) {
      revealHero();
      return;
    }
    hasStarted = true;

    // Fade out tap prompt pill immediately on click
    if (prompt) {
      prompt.style.transition = 'opacity 0.25s ease';
      prompt.style.opacity = '0';
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

  // As soon as the envelope flap opens (at ~3.4s), seamlessly reveal the wedding invitation
  video.addEventListener('timeupdate', () => {
    if (video.currentTime >= 3.4) {
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

// ============================================================
// 6. EVENT CEREMONY TAB SWITCHER
// ============================================================
function switchEventTab(tab) {
  const tabSangeet = document.getElementById('tabSangeet');
  const tabHaldi = document.getElementById('tabHaldi');
  const contentSangeet = document.getElementById('contentSangeet');
  const contentHaldi = document.getElementById('contentHaldi');
  if (!tabSangeet || !tabHaldi || !contentSangeet || !contentHaldi) return;

  if (tab === 'sangeet') {
    tabSangeet.classList.add('active');
    tabSangeet.setAttribute('aria-selected', 'true');
    tabHaldi.classList.remove('active');
    tabHaldi.setAttribute('aria-selected', 'false');
    contentSangeet.classList.add('active');
    contentHaldi.classList.remove('active');
  } else {
    tabHaldi.classList.add('active');
    tabHaldi.setAttribute('aria-selected', 'true');
    tabSangeet.classList.remove('active');
    tabSangeet.setAttribute('aria-selected', 'false');
    contentHaldi.classList.add('active');
    contentSangeet.classList.remove('active');
  }
}
window.switchEventTab = switchEventTab;
