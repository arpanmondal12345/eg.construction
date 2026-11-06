/* =========================================================================
   Excellent Great Construction — site script (plain JavaScript, no build)
   ========================================================================= */

/* ---------- 1. BUSINESS SETTINGS (edit here) ---------- */
const BUSINESS = {
  name: 'Excellent Great Construction',
  phoneDisplay: '+1 876-434-5647',
  whatsapp: 'https://wa.me/18764345647',
  instagramUrl: 'https://www.instagram.com/eg.construction/',
  instagramHandle: '@eg.construction',
};

/* Contact form delivery. There is no server, so by default a valid form opens
   WhatsApp with the details filled in. To also receive submissions by email,
   create a free form at https://formspree.io and paste its endpoint below,
   e.g. 'https://formspree.io/f/abcdwxyz'. */
const FORM_ENDPOINT = '';

/* ---------- 2. PROJECT GALLERY DATA ---------- */
const CATEGORY_LABELS = {
  foundation: 'Foundation Work', concrete: 'Concrete Pouring', masonry: 'Block & Masonry Work',
  roofing: 'Roofing', structural: 'Structural Work', staircase: 'Staircase Construction',
  plastering: 'Wall Plastering', finishing: 'Building Finishing',
};

/* photo = file name in /images (without -720/-1440/-2400.webp). feature = large tile in "All Work". */
const PROJECTS = [
  { photo: 'site-supervisor-blockwork', title: 'Block structure with slab formwork', cats: ['structural', 'masonry'], feature: true },
  { photo: 'foundation-rebar-columns', title: 'Foundation footings and column steel', cats: ['foundation'] },
  { photo: 'slab-concrete-pour', title: 'Pouring and screeding a concrete slab', cats: ['concrete'] },
  { photo: 'roof-trusses', title: 'Timber roof truss installation', cats: ['roofing'] },
  { photo: 'staircase-concrete', title: 'Reinforced concrete staircase', cats: ['staircase', 'concrete'], feature: true },
  { photo: 'mason-block-laying', title: 'Laying block walls to the line', cats: ['masonry'] },
  { photo: 'column-formwork-pour', title: 'Column formwork and concrete pour', cats: ['structural', 'concrete'] },
  { photo: 'wall-plastering', title: 'Exterior wall plastering', cats: ['plastering', 'finishing'] },
  { photo: 'roof-deck-steel', title: 'Steel reinforcement for a concrete roof deck', cats: ['structural', 'roofing'] },
  { photo: 'block-wall-on-foundation', title: 'Block walls rising from the foundation', cats: ['masonry', 'foundation'] },
  { photo: 'slab-pour-power-float', title: 'Concrete deck pour and power floating', cats: ['concrete', 'roofing'], feature: true },
  { photo: 'block-structure-formwork', title: 'Block and column structure in progress', cats: ['structural', 'masonry'] },
  { photo: 'render-float-finish', title: 'Float finish on a rendered block wall', cats: ['finishing', 'plastering'] },
  { photo: 'floor-power-float', title: 'Hand-floating a fresh concrete floor', cats: ['finishing', 'concrete'] },
];

/* ---------- helpers ---------- */
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const srcset = (n) => `images/${n}-720.webp 720w, images/${n}-1440.webp 1440w, images/${n}-2400.webp 2400w`;
const ICON = {
  expand: '<svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-7 7"/><path d="M3 21l7-7"/></svg>',
  x: '<svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
  left: '<svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>',
  right: '<svg class="h-6 w-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>',
  alert: '<svg class="h-3.5 w-3.5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>',
  check: '<svg class="mt-0.5 h-5 w-5 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>',
  whatsapp: '<svg viewBox="0 0 24 24" class="h-5 w-5" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35M12.05 21.5h-.01a9.4 9.4 0 0 1-4.8-1.32l-.34-.2-3.57.94.95-3.48-.22-.36a9.4 9.4 0 0 1-1.44-5.01c0-5.2 4.23-9.43 9.44-9.43a9.38 9.38 0 0 1 9.43 9.44c0 5.2-4.24 9.42-9.44 9.42m8.02-17.45A11.27 11.27 0 0 0 12.05.75C5.8.75.72 5.83.72 12.08c0 2 .52 3.95 1.52 5.66L.62 23.62l6.02-1.58a11.3 11.3 0 0 0 5.41 1.38h.01c6.24 0 11.33-5.08 11.33-11.33 0-3.03-1.18-5.87-3.32-8.01"/></svg>',
  instagram: '<svg viewBox="0 0 24 24" class="relative h-8 w-8" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.3"/><circle cx="17.6" cy="6.4" r="1.1" fill="currentColor" stroke="none"/></svg>',
};

/* =========================================================================
   3. HEADER: solid on scroll, scroll progress, active link, mobile menu
   ========================================================================= */
(function header() {
  const headerEl = $('#site-header');
  const bar = $('#header-bar');
  const progress = $('#scroll-progress');
  const menuBtn = $('#menu-btn');
  const menu = $('#mobile-menu');
  const links = $$('.nav-link');
  let open = false;

  const SOLID = ['bg-navy/95', 'shadow-[0_10px_40px_-20px_rgba(0,0,0,.6)]', 'backdrop-blur-md'];
  const CLEAR = ['bg-gradient-to-b', 'from-navy/70', 'to-transparent'];

  function paint() {
    const scrolled = window.scrollY > 24;
    const solid = scrolled || open;
    headerEl.classList.remove(...(solid ? CLEAR : SOLID));
    headerEl.classList.add(...(solid ? SOLID : CLEAR));
    bar.classList.toggle('h-[72px]', solid);
    bar.classList.toggle('h-[88px]', !solid);
    const max = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = '100%';
    progress.style.transform = `scaleX(${max > 0 ? Math.min(1, window.scrollY / max) : 0})`;
    progress.classList.toggle('opacity-100', scrolled);
    progress.classList.toggle('opacity-0', !scrolled);
  }
  window.addEventListener('scroll', paint, { passive: true });
  paint();

  function setActive(hash) {
    links.forEach((a) => {
      const on = a.getAttribute('href') === hash;
      a.classList.toggle('text-white', on);
      a.classList.toggle('text-white/70', !on);
      a.classList.toggle('hover:text-white', !on);
      on ? a.setAttribute('aria-current', 'true') : a.removeAttribute('aria-current');
      const u = a.querySelector('.nav-underline');
      u.classList.toggle('scale-x-100', on);
      u.classList.toggle('scale-x-0', !on);
    });
  }
  setActive('#home');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && setActive(`#${e.target.id}`)),
      { rootMargin: '-45% 0px -50% 0px' },
    );
    links.forEach((a) => { const s = $(a.getAttribute('href')); if (s) io.observe(s); });
  }

  function toggleMenu(state) {
    open = state;
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menuBtn.innerHTML = open
      ? '<svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>'
      : '<svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>';
    menu.classList.toggle('max-h-[calc(100dvh-72px)]', open);
    menu.classList.toggle('opacity-100', open);
    menu.classList.toggle('max-h-0', !open);
    menu.classList.toggle('opacity-0', !open);
    $$('a', menu).forEach((a) => (a.tabIndex = open ? 0 : -1));
    document.body.style.overflow = open ? 'hidden' : '';
    paint();
  }
  menuBtn.addEventListener('click', () => toggleMenu(!open));
  $$('a', menu).forEach((a) => a.addEventListener('click', () => toggleMenu(false)));
  window.addEventListener('keydown', (e) => e.key === 'Escape' && open && toggleMenu(false));
})();

/* =========================================================================
   4. SCROLL REVEAL — only for elements that start below the fold
   ========================================================================= */
(function reveal() {
  const els = $$('.reveal');
  if (!('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.remove('reveal-pending');
      e.target.classList.add('reveal-in');
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach((el) => {
    if (el.getBoundingClientRect().top < window.innerHeight * 0.9) return;
    el.classList.add('reveal-pending');
    io.observe(el);
  });
})();

/* =========================================================================
   5. PROJECTS: filters, gap-free grid, lightbox
   ========================================================================= */
(function projects() {
  const grid = $('#project-grid');
  const buttons = $$('.filter-btn');
  let filter = 'all';
  let items = PROJECTS;

  // Counts on the filter buttons
  buttons.forEach((b) => {
    const c = b.dataset.filter;
    b.querySelector('.filter-count').textContent = c === 'all' ? PROJECTS.length : PROJECTS.filter((p) => p.cats.includes(c)).length;
  });

  function paintButtons() {
    buttons.forEach((b) => {
      const on = b.dataset.filter === filter;
      b.setAttribute('aria-selected', String(on));
      ['border-navy', 'bg-navy', 'text-white'].forEach((c) => b.classList.toggle(c, on));
      ['border-concrete-line', 'bg-white', 'text-ink-muted', 'hover:border-royal', 'hover:text-royal'].forEach((c) => b.classList.toggle(c, !on));
      const n = b.querySelector('.filter-count');
      n.classList.toggle('text-site', on);
      n.classList.toggle('text-ink-faint', !on);
    });
  }

  // Picks which tiles are large so every filter fills complete rows (4 cols desktop, 2 cols tablet).
  function layout() {
    const n = items.length;
    const big = new Set(
      filter === 'all' ? items.filter((p) => p.feature).map((p) => p.photo)
        : n === 2 ? items.map((p) => p.photo)
        : n >= 1 ? [items[0].photo] : [],
    );
    const cells = items.reduce((t, p) => t + (big.has(p.photo) ? 4 : 1), 0);
    const lg = n === 1 ? 'lg:col-span-2 lg:row-span-2' : ['lg:col-span-4', 'lg:col-span-3', 'lg:col-span-2', 'lg:col-span-1'][cells % 4];
    const sm = cells % 2 ? 'sm:col-span-1' : 'sm:col-span-2';
    return { big, ig: `${sm} ${lg} ${n === 1 ? 'sm:row-span-2' : ''}` };
  }

  function render() {
    items = filter === 'all' ? PROJECTS : PROJECTS.filter((p) => p.cats.includes(filter));
    const { big, ig } = layout();
    grid.innerHTML = items.map((p, i) => {
      const isBig = big.has(p.photo);
      return `
        <button type="button" data-index="${i}" aria-label="View photo: ${esc(p.title)}"
          class="group relative animate-rise overflow-hidden rounded-[4px] bg-navy text-left ${isBig ? 'sm:col-span-2 sm:row-span-2' : ''}"
          style="animation-delay:${i * 50}ms">
          <img src="images/${p.photo}-1440.webp" srcset="${srcset(p.photo)}"
            sizes="${isBig ? '(min-width:1024px) 620px, 100vw' : '(min-width:1024px) 310px, (min-width:640px) 50vw, 100vw'}"
            alt="${esc(p.title)}" width="1440" height="1080" loading="lazy" decoding="async"
            class="object-cover absolute inset-0 h-full w-full transition-transform duration-[1.2s] ease-out group-hover:scale-[1.06]">
          <div class="absolute inset-0 bg-gradient-to-t from-navy-deep via-navy-deep/40 to-transparent to-70% opacity-95 transition-opacity duration-500 group-hover:opacity-100"></div>
          <div class="absolute inset-x-0 bottom-0 flex items-end justify-between gap-3 p-5">
            <div class="min-w-0">
              <p class="sheet-label text-site">${CATEGORY_LABELS[p.cats[0]]}</p>
              <p class="mt-1.5 font-display font-extrabold uppercase leading-tight text-white ${isBig ? 'text-2xl' : 'text-[15px]'}" style="font-stretch:108%">${esc(p.title)}</p>
            </div>
            <span class="grid h-10 w-10 shrink-0 translate-y-2 place-items-center rounded-full bg-white/15 text-white opacity-0 backdrop-blur transition-all duration-500 group-hover:translate-y-0 group-hover:opacity-100">${ICON.expand}</span>
          </div>
        </button>`;
    }).join('') + `
      <a href="${BUSINESS.instagramUrl}" target="_blank" rel="noopener noreferrer"
        class="group relative flex flex-col justify-between overflow-hidden rounded-[4px] bg-royal p-6 ${ig} text-white transition hover:bg-royal-dark">
        <div class="blueprint absolute inset-0 opacity-70" aria-hidden="true"></div>
        ${ICON.instagram}
        <div class="relative">
          <p class="font-display text-xl font-extrabold uppercase leading-tight" style="font-stretch:110%">More work on Instagram</p>
          <p class="mt-2 text-sm text-white/75">Follow ${BUSINESS.instagramHandle} for new site updates.</p>
        </div>
      </a>`;
    paintButtons();
  }

  buttons.forEach((b) => b.addEventListener('click', () => { filter = b.dataset.filter; render(); }));
  grid.addEventListener('click', (e) => {
    const tile = e.target.closest('button[data-index]');
    if (tile) openLightbox(Number(tile.dataset.index));
  });
  render();

  /* ---- Lightbox ---- */
  let lb = null, index = 0, lastFocus = null, touchX = null;

  function openLightbox(i) {
    index = i;
    lastFocus = document.activeElement;
    lb = document.createElement('div');
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Project photo viewer');
    lb.className = 'fixed inset-0 z-[100] flex animate-[rise_.35s_ease-out] flex-col bg-navy-deep/[.97] backdrop-blur-sm';
    lb.style.cssText = 'padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)';
    lb.innerHTML = `
      <div class="wrap flex h-16 shrink-0 items-center justify-between text-white">
        <span class="lb-count font-mono text-sm tabular-nums text-white/70"></span>
        <button class="lb-close grid h-11 w-11 place-items-center rounded-full border border-white/20 hover:bg-white/10" aria-label="Close viewer">${ICON.x}</button>
      </div>
      <div class="lb-stage relative flex min-h-0 flex-1 items-center justify-center px-4 sm:px-20">
        <img class="lb-img max-h-full max-w-full animate-[rise_.4s_ease-out] rounded-[3px] object-contain shadow-2xl" alt="" sizes="100vw">
        ${items.length > 1 ? `
        <button class="lb-prev absolute left-2 top-1/2 grid h-12 w-12 -translate-y-1/2 place-items-center rounded-full bg-white/10 text-white backdrop-blur transition hover:bg-site sm:left-5" aria-label="Previous photo">${ICON.left}</button>
        <button class="lb-next absolute right-2 top-1/2 grid h-12 w-12 -translate-y-1/2 place-items-center rounded-full bg-white/10 text-white backdrop-blur transition hover:bg-site sm:right-5" aria-label="Next photo">${ICON.right}</button>` : ''}
      </div>
      <div class="wrap shrink-0 py-5 text-center text-white">
        <p class="lb-cats sheet-label text-site"></p>
        <p class="lb-title mt-2 font-display text-lg font-extrabold uppercase" style="font-stretch:108%"></p>
        <div class="lb-thumbs mx-auto mt-4 flex max-w-full justify-center gap-2 overflow-x-auto pb-1">
          ${items.map((p, n) => `<button data-thumb="${n}" aria-label="Show ${esc(p.title)}" class="h-12 w-16 shrink-0 overflow-hidden rounded-[2px] border-2 transition"><img src="images/${p.photo}-720.webp" alt="" loading="lazy" class="h-full w-full object-cover"></button>`).join('')}
        </div>
      </div>`;
    document.body.appendChild(lb);
    document.body.style.overflow = 'hidden';

    lb.addEventListener('click', (e) => {
      if (e.target === lb || e.target.classList.contains('lb-stage') || e.target.closest('.lb-close')) return closeLightbox();
      if (e.target.closest('.lb-prev')) return go(-1);
      if (e.target.closest('.lb-next')) return go(1);
      const t = e.target.closest('[data-thumb]');
      if (t) { index = Number(t.dataset.thumb); show(); }
    });
    lb.addEventListener('touchstart', (e) => (touchX = e.touches[0].clientX), { passive: true });
    lb.addEventListener('touchend', (e) => {
      if (touchX == null) return;
      const dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1);
      touchX = null;
    });
    window.addEventListener('keydown', onKey);
    show();
    $('.lb-close', lb).focus();
  }

  function show() {
    const p = items[index];
    const img = $('.lb-img', lb);
    img.classList.remove('animate-[rise_.4s_ease-out]'); void img.offsetWidth; img.classList.add('animate-[rise_.4s_ease-out]');
    img.src = `images/${p.photo}-1440.webp`;
    img.srcset = `images/${p.photo}-1440.webp 1440w, images/${p.photo}-2400.webp 2400w`;
    img.alt = p.title;
    $('.lb-count', lb).textContent = `${String(index + 1).padStart(2, '0')} / ${String(items.length).padStart(2, '0')}`;
    $('.lb-cats', lb).textContent = p.cats.map((c) => CATEGORY_LABELS[c]).join(' · ');
    $('.lb-title', lb).textContent = p.title;
    $$('[data-thumb]', lb).forEach((t, n) => {
      t.classList.toggle('border-site', n === index);
      t.classList.toggle('opacity-100', n === index);
      t.classList.toggle('border-transparent', n !== index);
      t.classList.toggle('opacity-50', n !== index);
    });
  }
  const go = (d) => { index = (index + d + items.length) % items.length; show(); };
  function onKey(e) {
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') go(1);
    if (e.key === 'ArrowLeft') go(-1);
  }
  function closeLightbox() {
    window.removeEventListener('keydown', onKey);
    lb.remove(); lb = null;
    document.body.style.overflow = '';
    lastFocus && lastFocus.focus && lastFocus.focus();
  }
})();

/* =========================================================================
   6. CONTACT FORM: validation + WhatsApp hand-off (or Formspree if set)
   ========================================================================= */
(function contact() {
  const form = $('#quote-form');
  const status = $('#form-status');
  const note = $('#form-note');
  const submit = $('#form-submit');
  const submitHTML = submit.innerHTML;
  const f = (k) => $(`#f-${k}`);
  const FIELDS = ['name', 'phone', 'email', 'service', 'details'];

  // "Learn More" on a service card pre-selects that service.
  $$('[data-service]').forEach((a) => a.addEventListener('click', () => {
    f('service').value = a.dataset.service;
    clearError('service');
  }));

  const values = () => Object.fromEntries(FIELDS.map((k) => [k, f(k).value]));
  function validate(v) {
    const e = {};
    if (v.name.trim().length < 2) e.name = 'Please enter your full name.';
    if (v.phone.replace(/\D/g, '').length < 7) e.phone = 'Please enter a phone number we can reach you on.';
    if (v.email.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.email.trim())) e.email = 'This email address doesn’t look right. Check it or leave it blank.';
    if (!v.service) e.service = 'Please choose the service you need.';
    if (v.details.trim().length < 10) e.details = 'Tell us a little about the project (at least 10 characters).';
    return e;
  }
  function showError(k, msg) {
    const input = f(k);
    input.classList.add('field-error');
    input.setAttribute('aria-invalid', 'true');
    input.setAttribute('aria-describedby', `e-${k}`);
    let p = $(`#e-${k}`);
    if (!p) { p = document.createElement('p'); p.id = `e-${k}`; p.className = 'mt-1.5 flex items-center gap-1.5 text-[13px] text-red-600'; input.after(p); }
    p.innerHTML = `${ICON.alert}${esc(msg)}`;
  }
  function clearError(k) {
    const input = f(k);
    input.classList.remove('field-error');
    input.setAttribute('aria-invalid', 'false');
    input.removeAttribute('aria-describedby');
    const p = $(`#e-${k}`); if (p) p.remove();
  }
  FIELDS.forEach((k) => f(k).addEventListener('input', () => { clearError(k); setStatus('idle'); }));
  FIELDS.forEach((k) => f(k).addEventListener('change', () => clearError(k)));

  function message(v) {
    return [
      `Hello ${BUSINESS.name}, I'd like a quote.`, '',
      `Name: ${v.name.trim()}`, `Phone: ${v.phone.trim()}`,
      v.email.trim() ? `Email: ${v.email.trim()}` : null,
      `Service: ${v.service}`, '', `Project details: ${v.details.trim()}`,
    ].filter((l) => l !== null).join('\n');
  }
  const waLink = (v) => `${BUSINESS.whatsapp}?text=${encodeURIComponent(message(v))}`;

  function setStatus(state, v) {
    if (note) note.hidden = !(state === 'idle' && !FORM_ENDPOINT);
    submit.disabled = state === 'sending';
    submit.innerHTML = state === 'sending' ? 'Sending…' : submitHTML;
    if (state === 'idle' || state === 'sending') { status.innerHTML = ''; return; }
    if (state === 'whatsapp') {
      status.innerHTML = `
        <div class="rounded-[4px] border border-site/40 bg-site-light p-5">
          <p class="font-semibold text-navy">Your request is ready. One more step:</p>
          <p class="mt-1.5 text-sm leading-relaxed text-ink-muted">Online form delivery isn’t connected yet, so nothing has been sent. Tap below to open WhatsApp with your details filled in, then press send. You can also call ${BUSINESS.phoneDisplay}.</p>
          <a href="${esc(waLink(v))}" target="_blank" rel="noopener noreferrer" class="btn mt-4 bg-[#25D366] text-navy hover:bg-[#3BE27A]">${ICON.whatsapp} Send on WhatsApp</a>
        </div>`;
    } else if (state === 'sent') {
      status.innerHTML = `<p class="flex items-start gap-2 rounded-[4px] border border-green-600/30 bg-green-50 p-5 text-green-800">${ICON.check} Thank you. Your request was received and our team will contact you soon.</p>`;
    } else if (state === 'error') {
      status.innerHTML = `
        <div class="rounded-[4px] border border-red-500/30 bg-red-50 p-5 text-red-800">
          <p class="font-semibold">Your request couldn’t be sent.</p>
          <p class="mt-1.5 text-sm">Check your connection and try again, or send it on WhatsApp instead.</p>
          <a href="${esc(waLink(v))}" target="_blank" rel="noopener noreferrer" class="mt-3 inline-flex items-center gap-2 text-sm font-semibold underline">${ICON.whatsapp} Send on WhatsApp</a>
        </div>`;
    }
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const v = values();
    const errors = validate(v);
    FIELDS.forEach((k) => (errors[k] ? showError(k, errors[k]) : clearError(k)));
    const first = FIELDS.find((k) => errors[k]);
    if (first) { f(first).focus(); return; }

    if (!FORM_ENDPOINT) { setStatus('whatsapp', v); return; }
    setStatus('sending');
    try {
      const res = await fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(v),
      });
      if (!res.ok) throw new Error(res.status);
      form.reset();
      setStatus('sent');
    } catch {
      setStatus('error', v);
    }
  });
})();
