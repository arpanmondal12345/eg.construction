"""Generates index.html for the static Excellent Great Construction site.
Edit content here (or edit index.html directly after generation)."""
import re, html, pathlib

ROOT = pathlib.Path(__file__).parent
ICON_DIR = pathlib.Path('/home/claude/egc/node_modules/lucide-static/icons')
ICONS = ['phone','instagram','arrow-right','check','menu','x','chevron-left','chevron-right','maximize-2','house',
 'building-2','triangle','layers','brick-wall','columns-3','paint-bucket','grid-3x3','paint-roller','hammer',
 'trending-up','hard-hat','gem','users','clock','ruler','heart-handshake','shield-check','award','thumbs-up',
 'message-circle','clipboard-list','calculator','construction','badge-check','send','info','triangle-alert','mail',
 'map-pin','arrow-up','circle-check','sparkles']

def sprite():
    out = []
    for n in ICONS:
        s = (ICON_DIR / f'{n}.svg').read_text()
        inner = re.search(r'>\s*(.*)</svg>', s, re.S).group(1)
        inner = re.sub(r'\s+', ' ', inner).strip()
        out.append(f'<symbol id="i-{n}" viewBox="0 0 24 24">{inner}</symbol>')
    # WhatsApp brand glyph (filled)
    out.append('<symbol id="i-whatsapp" viewBox="0 0 24 24"><path fill="currentColor" stroke="none" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35M12.05 21.5h-.01a9.4 9.4 0 0 1-4.8-1.32l-.34-.2-3.57.94.95-3.48-.22-.36a9.4 9.4 0 0 1-1.44-5.01c0-5.2 4.23-9.43 9.44-9.43a9.38 9.38 0 0 1 9.43 9.44c0 5.2-4.24 9.42-9.44 9.42m8.02-17.45A11.27 11.27 0 0 0 12.05.75C5.8.75.72 5.83.72 12.08c0 2 .52 3.95 1.52 5.66L.62 23.62l6.02-1.58a11.3 11.3 0 0 0 5.41 1.38h.01c6.24 0 11.33-5.08 11.33-11.33 0-3.03-1.18-5.87-3.32-8.01"/></symbol>')
    return '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + ''.join(out) + '</svg>'

def ico(name, cls='ico'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def pic(name, alt, sizes='100vw', cls='', eager=False, w=1440, h=1080):
    return (f'<img src="images/{name}-1440.webp" srcset="images/{name}-720.webp 720w, images/{name}-1440.webp 1440w" '
            f'sizes="{sizes}" alt="{html.escape(alt)}" width="{w}" height="{h}" '
            f'{"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async"' + (f' class="{cls}"' if cls else '') + '>')

LOGO_MARK = '''<svg class="logo-mark" viewBox="0 0 60 36" aria-hidden="true"><defs><linearGradient id="lg-gold" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#FFC233"/><stop offset="1" stop-color="#FF9A00"/></linearGradient></defs><polygon points="0,24 19,6 38,24 31,24 19,13 7,24" fill="url(#lg-gold)"/><polygon points="20,20 39,1 58,20 51,20 39,8 27,20" fill="#FF7900"/><g fill="url(#lg-gold)"><rect x="14.5" y="21" width="4" height="4"/><rect x="19.5" y="21" width="4" height="4"/><rect x="14.5" y="26" width="4" height="4"/><rect x="19.5" y="26" width="4" height="4"/></g><g fill="#FF7900"><rect x="34.5" y="17" width="4" height="4"/><rect x="39.5" y="17" width="4" height="4"/><rect x="34.5" y="22" width="4" height="4"/><rect x="39.5" y="22" width="4" height="4"/></g></svg>'''

def logo(extra=''):
    return f'''<span class="logo {extra}">{LOGO_MARK}<span class="logo-text"><span class="logo-name">Excellent <b>Great</b></span><span class="logo-sub">Construction</span></span></span>'''

PHONE = '+1 876-434-5647'
TEL = 'tel:+18764345647'
WA = 'https://wa.me/18764345647'
IG = 'https://www.instagram.com/eg.construction/'
IGH = '@eg.construction'

NAV = [('Home','home'),('About Us','about'),('Services','services'),('Our Projects','projects'),('Gallery','gallery'),('Contact Us','contact')]

SERVICES = [
 ('Residential Construction','house','block-structure-formwork','Complete homes built from the ground up, from setting out and foundations to the final coat.','Homes'),
 ('Commercial Construction','building-2',None,'Shops, offices and business premises built to a clear plan, schedule and budget.','Commercial'),
 ('Roofing & Roof Installation','triangle','roof-trusses','Timber truss roofs, concrete roof decks and metal roofing, installed to keep the weather out.','Roofing'),
 ('Concrete Work & Foundation','layers','foundation-rebar-columns','Footings, reinforced columns, slabs and decking poured on properly prepared steel and formwork.','Groundwork'),
 ('Block Work & Masonry','brick-wall','mason-block-laying','Straight, level block walls laid to the line, with steel and fill where the structure needs it.','Masonry'),
 ('Structural Construction','columns-3','column-formwork-pour','Columns, beams and ring beams framed, reinforced and cast to carry the building safely.','Structure'),
 ('Plastering & Wall Finishing','paint-bucket','wall-plastering','Smooth, even rendering inside and out, ready for paint or a textured finish.','Finishing'),
 ('Tiling & Flooring','grid-3x3',None,'Floor and wall tiling for kitchens, bathrooms, living areas and patios, set flat and true.','Finishing'),
 ('Painting & Finishing','paint-roller',None,'Interior and exterior painting and the finishing touches that complete your property.','Finishing'),
 ('Renovation & Remodeling','hammer',None,'Extensions, upgrades and repairs that bring an existing home or building up to date.','Renovation'),
 ('Staircase Construction','trending-up','staircase-concrete','Reinforced concrete staircases formed and poured on site, with even risers and solid treads.','Structure'),
 ('General Construction Services','hard-hat',None,'Windows, doors, fencing and the many other jobs that come up on a building project.','General'),
]

CATS = [('all','All Work'),('foundation','Foundation Work'),('concrete','Concrete Pouring'),('masonry','Block & Masonry Work'),
 ('roofing','Roofing'),('structural','Structural Work'),('staircase','Staircase Construction'),('plastering','Wall Plastering'),('finishing','Building Finishing')]
CATL = dict(CATS)

PROJECTS = [
 ('site-supervisor-blockwork','Block structure with slab formwork',['structural','masonry'],True),
 ('foundation-rebar-columns','Foundation footings and column steel',['foundation'],False),
 ('slab-concrete-pour','Pouring and screeding a concrete slab',['concrete'],False),
 ('roof-trusses','Timber roof truss installation',['roofing'],False),
 ('staircase-concrete','Reinforced concrete staircase',['staircase','concrete'],True),
 ('mason-block-laying','Laying block walls to the line',['masonry'],False),
 ('column-formwork-pour','Column formwork and concrete pour',['structural','concrete'],False),
 ('wall-plastering','Exterior wall plastering',['plastering','finishing'],False),
 ('roof-deck-steel','Steel reinforcement for a concrete roof deck',['structural','roofing'],False),
 ('block-wall-on-foundation','Block walls rising from the foundation',['masonry','foundation'],False),
 ('slab-pour-power-float','Concrete deck pour and power floating',['concrete','roofing'],False),
 ('block-structure-formwork','Block and column structure in progress',['structural','masonry'],False),
]

WHY = [
 ('gem','Quality Materials & Workmanship','Proper steel, sound concrete and careful hands on every stage of the build.'),
 ('users','Skilled Construction Team','Masons, steel fixers, carpenters and finishers who know their trade.'),
 ('clock','Reliable Project Delivery','We show up, keep you updated and work steadily toward your handover.'),
 ('ruler','Attention to Every Detail','Level lines, plumb walls and clean finishes, checked as we go.'),
 ('heart-handshake','Customer-Focused Approach','Your plans, budget and questions come first, from the first call to the last day.'),
 ('shield-check','Professional Construction Solutions','One team for groundwork, structure, roofing and finishing.'),
]

PROCESS = [
 ('message-circle','Consultation','Tell us what you want to build. We look at the site, your drawings and your ideas.'),
 ('calculator','Planning & Estimation','We work out the scope, materials and schedule, and give you a clear quote.'),
 ('construction','Construction & Execution','Our crew builds stage by stage, from foundation to roof, keeping you updated.'),
 ('badge-check','Final Inspection & Delivery','We walk the finished work with you, fix any snags and hand over your property.'),
]

def wa_service(title):
    from urllib.parse import quote
    return f'{WA}?text=' + quote(f"Hello Excellent Great Construction, I'd like a quote for {title}.")

def section_head(eyebrow, title, intro='', align='center'):
    return f'''<div class="section-head {align}"><p class="eyebrow">{eyebrow}</p><h2>{title}</h2>{f'<p class="section-intro">{intro}</p>' if intro else ''}</div>'''

# ---------------- sections ----------------
def header():
    links = ''.join(f'<li><a class="nav-link" href="#{i}">{l}</a></li>' for l, i in NAV)
    return f'''
<header class="site-header" id="siteHeader">
  <div class="container header-inner">
    <a href="#home" class="brand" aria-label="Excellent Great Construction, back to top">{logo()}</a>
    <nav class="primary-nav" id="primaryNav" aria-label="Main">
      <ul>{links}</ul>
      <div class="nav-mobile-extra">
        <a class="btn btn-primary btn-block" href="#contact">{ico('send')} Get a Free Quote</a>
        <a class="btn btn-whatsapp btn-block" href="{WA}" target="_blank" rel="noopener">{ico('whatsapp')} WhatsApp Us</a>
        <a class="nav-phone" href="{TEL}">{ico('phone')} {PHONE}</a>
      </div>
    </nav>
    <div class="header-actions">
      <a class="header-phone" href="{TEL}" aria-label="Call {PHONE}">{ico('phone')}<span>{PHONE}</span></a>
      <a class="btn btn-primary btn-sm header-cta" href="#contact">Free Quote</a>
      <button class="nav-toggle" id="navToggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="primaryNav"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''

def hero():
    checks = ''.join(f'<li>{ico("circle-check")}{t}</li>' for t in ['Foundation to finishing','Skilled, uniformed crew','Free quotes on WhatsApp'])
    return f'''
<section id="home" class="hero" aria-labelledby="hero-title">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="container hero-inner">
    <div class="hero-copy">
      <p class="eyebrow eyebrow-left">Building a strong foundation, one project at a time</p>
      <h1 id="hero-title">Building Your Vision. <span class="hl">Creating Your Future.</span></h1>
      <p class="hero-lead">From strong foundations to beautiful finishing touches, Excellent Great Construction delivers quality craftsmanship, reliable service, and exceptional construction solutions.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary btn-lg" href="#contact">Get a Free Quote {ico('arrow-right')}</a>
        <a class="btn btn-outline btn-lg" href="#projects">Explore Our Projects</a>
      </div>
      <ul class="hero-checks">{checks}</ul>
    </div>
    <div class="hero-visual">
      <figure class="hero-photo">
        {pic('site-supervisor-blockwork','Excellent Great Construction supervisor reviewing plans while the crew builds a block house', '(min-width: 1000px) 560px, 100vw', eager=True)}
        <figcaption class="photo-tag">{ico('hard-hat')} On site with our crew</figcaption>
      </figure>
      <figure class="hero-photo-sm">
        {pic('slab-pour-power-float','Crew pouring and finishing a concrete deck','240px')}
      </figure>
      <div class="hero-badge">
        {LOGO_MARK}
        <div><strong>Excellent Great Construction</strong><span>Call / WhatsApp <a href="{TEL}">{PHONE}</a></span></div>
      </div>
    </div>
  </div>
  <div class="container">
    <ul class="trust-bar">
      <li>{ico('layers')}<div><strong>Foundations & Concrete</strong><span>Footings, columns, slabs</span></div></li>
      <li>{ico('brick-wall')}<div><strong>Block Work & Structure</strong><span>Walls, beams, formwork</span></div></li>
      <li>{ico('triangle')}<div><strong>Roofing & Staircases</strong><span>Trusses, decks, stairs</span></div></li>
      <li>{ico('paint-roller')}<div><strong>Plastering & Finishing</strong><span>Render, tiles, paint</span></div></li>
    </ul>
  </div>
</section>'''

def about():
    cards = [('award','Quality Craftsmanship','Every block, bar and pour is set out carefully and checked before we move on.'),
             ('users','Professional Team','A uniformed, safety-minded crew of masons, steel fixers, carpenters and finishers.'),
             ('thumbs-up','Customer Satisfaction','Clear communication and honest workmanship, so you always know where your project stands.')]
    c = ''.join(f'<article class="value-card reveal">{ico(i)}<h3>{t}</h3><p>{d}</p></article>' for i, t, d in cards)
    return f'''
<section id="about" class="section about" aria-labelledby="about-title">
  <div class="container about-grid">
    <div class="about-media reveal">
      <figure class="about-main">{pic('mason-block-laying','Excellent Great Construction mason laying concrete blocks to a string line','(min-width: 1000px) 520px, 100vw')}</figure>
      <figure class="about-inset">{pic('foundation-rebar-columns','Crew tying column steel on new foundations','260px')}</figure>
      <div class="about-chip">{ico('hard-hat')}<span><strong>Groundwork to finish</strong>One crew, every stage</span></div>
    </div>
    <div class="about-copy">
      <p class="eyebrow eyebrow-left">About us</p>
      <h2 id="about-title">Building Excellence. <span class="hl">Delivering Trust.</span></h2>
      <p class="lead">Excellent Great Construction is a hands-on building company committed to quality construction, reliable workmanship and customer satisfaction.</p>
      <p>We take projects from the first excavation and foundation through block work, structure and roofing, and on to plastering and finishing. Every job, large or small, gets the same attention to detail: proper reinforcement, level lines, solid concrete and clean finishes. We keep our clients informed at every stage, because a strong building starts with a strong working relationship.</p>
      <div class="value-grid">{c}</div>
      <div class="about-actions">
        <a class="btn btn-dark" href="#process">Learn More {ico('arrow-right')}</a>
        <a class="link-arrow" href="{TEL}">{ico('phone')} {PHONE}</a>
      </div>
    </div>
  </div>
</section>'''

def services():
    cards = []
    for i, (t, ic, photo, d, tag) in enumerate(SERVICES):
        media = (pic(photo, f'{t} by Excellent Great Construction', '(min-width: 1000px) 380px, (min-width: 640px) 50vw, 100vw') if photo
                 else f'<div class="svc-illus">{ico(ic, "ico svc-illus-ico")}</div>')
        cards.append(f'''<article class="svc-card reveal">
  <div class="svc-media">{media}<span class="pill pill-dark">{tag}</span><span class="svc-icon">{ico(ic)}</span></div>
  <div class="svc-body">
    <h3>{t}</h3><p>{d}</p>
    <div class="svc-actions">
      <a class="btn btn-ghost btn-sm" href="#contact" data-service="{html.escape(t)}">Learn More</a>
      <a class="btn btn-whatsapp btn-sm" href="{html.escape(wa_service(t))}" target="_blank" rel="noopener">{ico('whatsapp')} Enquire</a>
    </div>
  </div>
</article>''')
    return f'''
<section id="services" class="section section-tint" aria-labelledby="services-title">
  <div class="container">
    <div class="section-head split">
      <div><p class="eyebrow eyebrow-left">Our services</p><h2 id="services-title">Every stage of the build, <span class="hl">one trusted crew</span></h2></div>
      <p class="section-intro">From the first footing to the final coat of paint, we handle the work in-house. Tap <b>Enquire</b> to ask about a service on WhatsApp.</p>
    </div>
    <div class="svc-grid">{''.join(cards)}</div>
  </div>
</section>
<section class="promo-wrap section-tint" aria-labelledby="promo-title">
  <div class="container">
    <div class="promo">
      <div class="promo-copy">
        <p class="eyebrow eyebrow-left eyebrow-light">Free quote</p>
        <h2 id="promo-title">Need a price for your project?</h2>
        <p>Every job is different. Send us a few details or photos of your site on WhatsApp and we’ll talk you through the scope, materials and cost.</p>
        <a class="btn btn-primary" href="{WA}" target="_blank" rel="noopener">{ico('whatsapp')} Ask for a quote on WhatsApp</a>
      </div>
      <ul class="promo-list">
        <li>{ico('sparkles')} Quotes based on your plans and site</li>
        <li>{ico('sparkles')} Clear explanation of what is included</li>
        <li>{ico('sparkles')} No pressure. Ask any questions you have</li>
      </ul>
    </div>
  </div>
</section>'''

def projects():
    counts = {c: (len(PROJECTS) if c == 'all' else sum(c in p[2] for p in PROJECTS)) for c, _ in CATS}
    pills = ''.join(f'<button type="button" class="filter{" is-active" if c=="all" else ""}" data-filter="{c}" aria-pressed="{"true" if c=="all" else "false"}">{l} <span>{counts[c]}</span></button>' for c, l in CATS)
    items = []
    for i, (photo, title, cats, feat) in enumerate(PROJECTS):
        items.append(f'''<li class="g-item{" is-feature" if feat else ""}" data-cats="{" ".join(cats)}">
  <button type="button" class="g-btn" data-index="{i}" data-full="images/{photo}-1440.webp" data-title="{html.escape(title)}" data-label="{html.escape(" · ".join(CATL[c] for c in cats))}" aria-label="View photo: {html.escape(title)}">
    {pic(photo, title, "(min-width: 1000px) 600px, (min-width: 640px) 50vw, 100vw" if feat else "(min-width: 1000px) 300px, 50vw")}
    <span class="g-cap"><span class="g-label">{CATL[cats[0]]}</span><span class="g-title">{title}</span></span>
    <span class="g-zoom">{ico('maximize-2')}</span>
  </button>
</li>''')
    items.append(f'''<li class="g-item g-cta" data-cats="all-only"><a href="{IG}" target="_blank" rel="noopener">{ico('instagram','ico ico-lg')}<span><strong>More of our work on Instagram</strong>Follow {IGH} for new site updates.</span><span class="link-arrow">Follow us {ico('arrow-right')}</span></a></li>''')
    return f'''
<section id="projects" class="section" aria-labelledby="projects-title">
  <div class="container">
    {section_head('Our projects', 'Real sites. Real crews. <span class="hl">Real work.</span>', 'Photos straight from our job sites, from steel and footings to the final coat of plaster. Filter by type of work and tap any photo to view it larger.')}
    <div class="filters" role="group" aria-label="Filter projects by category">{pills}</div>
    <ul class="gallery" id="gallery-grid">{''.join(items)}</ul>
    <p class="gallery-empty" id="galleryEmpty" hidden>More photos for this category are coming soon.</p>
  </div>
</section>'''

def why():
    items = ''.join(f'<li class="why-item reveal"><span class="why-ico">{ico(i)}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in WHY)
    return f'''
<section id="why" class="section section-dark why" aria-labelledby="why-title">
  <div class="container why-grid">
    <div class="why-intro">
      <p class="eyebrow eyebrow-left eyebrow-light">Why choose us</p>
      <h2 id="why-title">Why choose <span class="hl-orange">Excellent Great</span> Construction?</h2>
      <p>A building is only as good as the work you can no longer see. We do the hidden work properly, so the finished result stands strong.</p>
      <figure class="why-photo">{pic('column-formwork-pour','Crew pouring concrete into a column formwork','(min-width: 1000px) 460px, 100vw')}</figure>
    </div>
    <ul class="why-list">{items}</ul>
  </div>
</section>'''

def process():
    steps = ''.join(f'''<li class="step reveal"><span class="step-ico">{ico(i)}<span class="step-num">{n:02d}</span></span><h3>{t}</h3><p>{d}</p></li>''' for n, (i, t, d) in enumerate(PROCESS, 1))
    return f'''
<section id="process" class="section section-tint" aria-labelledby="process-title">
  <div class="container">
    {section_head('Our work process', 'Four steps from first call to <span class="hl">handover</span>', 'A clear process, so you always know what happens next.')}
    <ol class="steps">{steps}</ol>
    <div class="center"><a class="btn btn-dark" href="#contact">Start with Step 1 {ico('arrow-right')}</a></div>
  </div>
</section>'''

def cta():
    return f'''
<section class="cta" aria-labelledby="cta-title">
  {pic('slab-concrete-pour','', '100vw', cls='cta-bg')}
  <div class="container cta-inner">
    <div>
      <h2 id="cta-title">Ready to Build <span class="hl-orange">Something Great?</span></h2>
      <p>Let's turn your construction vision into reality. Contact our team today and let's discuss your next project.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary btn-lg" href="#contact">Request a Quote {ico('arrow-right')}</a>
      <a class="btn btn-light btn-lg" href="{TEL}">{ico('phone')} Call Us Today</a>
      <span class="cta-phone">{PHONE}</span>
    </div>
  </div>
</section>'''

def instagram():
    tiles = [('roof-deck-steel','Steel fixing for a concrete roof deck'),('staircase-concrete','Concrete staircase in progress'),
             ('wall-plastering','Plastering a block wall'),('roof-trusses','Roof truss installation')]
    t = ''.join(f'<a class="ig-tile ig-{k}" href="{IG}" target="_blank" rel="noopener" aria-label="{a}, see more on Instagram">{pic(n,a,"(min-width: 1000px) 280px, 45vw")}<span>{ico("instagram")}</span></a>' for k, (n, a) in enumerate(tiles))
    return f'''
<section id="gallery" class="section ig" aria-labelledby="ig-title">
  <div class="container ig-grid">
    <div class="ig-copy">
      <p class="eyebrow eyebrow-left">Gallery & Instagram</p>
      <h2 id="ig-title">Follow the build on <span class="hl-orange">Instagram</span></h2>
      <p>We share step-by-step photos and videos from our sites, from decking preparation and steel fixing to the finished roof. Follow along for new projects.</p>
      <div class="ig-actions">
        <a class="btn btn-instagram" href="{IG}" target="_blank" rel="noopener">{ico('instagram')} Follow Us on Instagram</a>
        <a class="btn btn-ghost" href="#projects">View project gallery</a>
      </div>
      <p class="ig-handle">{ico('instagram')} {IGH}</p>
    </div>
    <div class="ig-collage">{t}</div>
  </div>
</section>'''

def contact():
    opts = ''.join(f'<option>{html.escape(s[0])}</option>' for s in SERVICES) + '<option>Other / Not sure yet</option>'
    return f'''
<section id="contact" class="section contact" aria-labelledby="contact-title">
  <div class="container contact-grid">
    <div class="contact-copy">
      <p class="eyebrow eyebrow-left">Contact us</p>
      <h2 id="contact-title">Let’s talk about <span class="hl">your project</span></h2>
      <p class="section-intro">Share a few details and we’ll get back to you to talk through your plans, timeline and budget. No obligation.</p>
      <ul class="methods">
        <li><a class="method" href="{WA}" target="_blank" rel="noopener"><span class="method-ico wa">{ico('whatsapp')}</span><span><strong>WhatsApp</strong><small>The fastest way to reach us. Tap to start a chat.</small></span></a></li>
        <li><a class="method" href="{TEL}"><span class="method-ico">{ico('phone')}</span><span><strong>Call us</strong><small class="num">{PHONE}</small></span></a></li>
        <li><a class="method" href="{IG}" target="_blank" rel="noopener"><span class="method-ico ig">{ico('instagram')}</span><span><strong>Instagram</strong><small>{IGH}</small></span></a></li>
        <li data-config="email" hidden><a class="method" href="#"><span class="method-ico">{ico('mail')}</span><span><strong>Email</strong><small data-value></small></span></a></li>
        <li data-config="address" hidden><div class="method"><span class="method-ico">{ico('map-pin')}</span><span><strong>Address</strong><small data-value></small></span></div></li>
        <li data-config="hours" hidden><div class="method"><span class="method-ico">{ico('clock')}</span><span><strong>Working hours</strong><small data-value></small></span></div></li>
      </ul>
    </div>
    <form class="form-card" id="quoteForm" novalidate>
      <h3>Request a free quote</h3>
      <p class="form-note-top">Fields marked <span class="req">*</span> are required.</p>
      <div class="form-grid">
        <div class="field"><label for="f-name">Full Name <span class="req">*</span></label><input id="f-name" name="name" autocomplete="name" placeholder="Your full name"><p class="err" id="e-name"></p></div>
        <div class="field"><label for="f-phone">Phone Number <span class="req">*</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" placeholder="+1 876 000 0000"><p class="err" id="e-phone"></p></div>
        <div class="field"><label for="f-email">Email Address <span class="opt">(optional)</span></label><input id="f-email" name="email" type="email" autocomplete="email" placeholder="you@example.com"><p class="err" id="e-email"></p></div>
        <div class="field"><label for="f-service">Service Required <span class="req">*</span></label><select id="f-service" name="service"><option value="">Choose a service</option>{opts}</select><p class="err" id="e-service"></p></div>
        <div class="field full"><label for="f-details">Project Details <span class="req">*</span></label><textarea id="f-details" name="details" rows="5" placeholder="What are you building? Location, size, timeline, and whether you have drawings."></textarea><p class="err" id="e-details"></p></div>
      </div>
      <div class="form-notice" id="formNotice">{ico('info')}<p>Submitting opens <b>WhatsApp</b> with your details filled in. Press <b>Send</b> in WhatsApp to deliver your request. This website does not store your information.</p></div>
      <button class="btn btn-whatsapp btn-block btn-lg" type="submit" id="submitBtn">{ico('whatsapp')} <span>Submit Request</span></button>
      <div class="form-status" id="formStatus" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>'''

def footer():
    links = ''.join(f'<li><a href="#{i}">{l}</a></li>' for l, i in NAV)
    svc = ''.join(f'<li><a href="#services">{s[0]}</a></li>' for s in SERVICES[:7])
    return f'''
<footer class="footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      {logo('logo-light')}
      <p class="footer-tag">Building a Strong Foundation, One Project at a Time.</p>
      <p>Foundations, concrete, block work, roofing, staircases, plastering and finishing, built by one dedicated crew.</p>
      <div class="socials">
        <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ico('whatsapp')}</a>
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ico('instagram')}</a>
        <a href="{TEL}" aria-label="Call {PHONE}">{ico('phone')}</a>
      </div>
    </div>
    <div><h3>Explore</h3><ul>{links}</ul></div>
    <div><h3>Services</h3><ul>{svc}<li><a href="#services" class="more">All services {ico('arrow-right')}</a></li></ul></div>
    <div><h3>Get in touch</h3>
      <ul class="footer-contact">
        <li>{ico('phone')}<span><small>Phone</small><a href="{TEL}">{PHONE}</a></span></li>
        <li>{ico('whatsapp')}<span><small>WhatsApp</small><a href="{WA}" target="_blank" rel="noopener">Message us on WhatsApp</a></span></li>
        <li>{ico('instagram')}<span><small>Instagram</small><a href="{IG}" target="_blank" rel="noopener">{IGH}</a></span></li>
      </ul>
      <a class="btn btn-primary btn-sm" href="#contact">Get a Free Quote</a>
    </div>
  </div>
  <div class="footer-bottom"><div class="container footer-bottom-inner"><p>© 2026 Excellent Great Construction. All Rights Reserved.</p><a href="#home" class="to-top-link">Back to top {ico('arrow-up')}</a></div></div>
</footer>'''

def extras():
    return f'''
<a href="{WA}" class="fab-wa" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{ico('whatsapp')}<span>Chat with us</span></a>
<button class="fab-top" id="backToTop" type="button" aria-label="Back to top">{ico('arrow-up')}</button>
<div class="mobile-bar" aria-label="Quick contact">
  <a href="{TEL}">{ico('phone')}Call</a>
  <a href="{WA}" target="_blank" rel="noopener">{ico('whatsapp')}WhatsApp</a>
  <a href="#contact" class="mb-primary">Free Quote</a>
</div>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Project photo viewer" hidden>
  <div class="lb-top"><span class="lb-count" id="lbCount"></span><button class="lb-btn" id="lbClose" type="button" aria-label="Close photo viewer">{ico('x')}</button></div>
  <div class="lb-stage" id="lbStage">
    <button class="lb-btn lb-prev" id="lbPrev" type="button" aria-label="Previous photo">{ico('chevron-left')}</button>
    <img id="lbImg" src="" alt="">
    <button class="lb-btn lb-next" id="lbNext" type="button" aria-label="Next photo">{ico('chevron-right')}</button>
  </div>
  <div class="lb-info"><span class="lb-label" id="lbLabel"></span><span class="lb-title" id="lbTitle"></span><div class="lb-thumbs" id="lbThumbs"></div></div>
</div>'''

HEAD = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="claude:viewport-fit-sides" content="cover">
  <title>Excellent Great Construction</title>
  <meta name="description" content="Excellent Great Construction delivers foundations, concrete work, block masonry, roofing, staircases, plastering and finishing. Call or WhatsApp {PHONE} for a free quote.">
  <meta name="theme-color" content="#101D35">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Excellent Great Construction">
  <meta property="og:title" content="Excellent Great Construction | Building a Strong Foundation, One Project at a Time">
  <meta property="og:description" content="Foundations, concrete, block work, roofing, staircases, plastering and finishing. Call or WhatsApp {PHONE}.">
  <!-- TODO after deployment: replace with the full absolute URL of og-image.jpg -->
  <meta property="og:image" content="images/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="preload" as="image" href="images/site-supervisor-blockwork-1440.webp" imagesrcset="images/site-supervisor-blockwork-720.webp 720w, images/site-supervisor-blockwork-1440.webp 1440w" imagesizes="(min-width: 1000px) 560px, 100vw">
  <link rel="stylesheet" href="css/style.css">
  <!-- Structured data: verified details only (no address, hours or ratings) -->
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"GeneralContractor","name":"Excellent Great Construction","slogan":"Building a Strong Foundation, One Project at a Time.","telephone":"+1-876-434-5647","sameAs":["{IG}"]}}
  </script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
'''

doc = (HEAD + sprite() + header() + '\n<main id="main">' + hero() + about() + services() + projects() + why() + process()
       + cta() + instagram() + contact() + '\n</main>' + footer() + extras()
       + '\n<script src="js/config.js"></script>\n<script src="js/main.js"></script>\n</body>\n</html>\n')
(ROOT / 'site' / 'index.html').write_text(doc)
print('index.html', len(doc))
