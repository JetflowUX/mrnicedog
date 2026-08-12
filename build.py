#!/usr/bin/env python3
"""
Static site generator for Mr. Nice Dog Grooming Salon.

Every page shares one shell (head, nav, footer) so the navigation and NAP
details are defined once. Run `python3 build.py` after editing to regenerate
the HTML. The output is plain static files with no runtime dependency.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
ORIGIN = "https://www.mrnicedog.com"

# ---------------------------------------------------------------- business
BIZ = {
    "name": "Mr. Nice Dog Grooming Salon",
    "street": "42 Worcester Street",
    "city": "Natick",
    "region": "MA",
    "zip": "01760",
    "phone_display": "(508) 545-1046",
    "phone_e164": "+15085451046",
    "phone2_display": "(857) 214-0119",
    "phone2_e164": "+18572140119",
    # taken from the Google Maps embed on their own contact page
    "lat": 42.3037897,
    "lng": -71.3283709,
    "place": "https://maps.google.com/?q=42+Worcester+St,+Natick,+MA+01760",
    "facebook": "https://www.facebook.com/mrnicedog",
    "instagram": "https://www.instagram.com/mrnicedog/",
    "map_embed": ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2950.816080248581"
                  "!2d-71.3283709!3d42.30378969999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1"
                  "!3m3!1m2!1s0x89e3868ca4e2301f%3A0xa3e16110e6cecf62"
                  "!2s42%20Worcester%20St%2C%20Natick%2C%20MA%2001760!5e0!3m2!1sen!2sus"
                  "!4v1673475241821!5m2!1sen!2sus"),
}
HOURS = [("Monday", None), ("Tuesday", ("07:30", "18:00")), ("Wednesday", ("07:30", "18:00")),
         ("Thursday", ("07:30", "18:00")), ("Friday", ("07:30", "18:00")),
         ("Saturday", ("07:30", "17:00")), ("Sunday", None)]

NAV = [
    ("Home", "index.html", None),
    ("Services", None, [("Dog Grooming", "grooming.html"),
                        ("Dog Daycare", "daycare.html"),
                        ("Dog Training", "training.html")]),
    ("Our Salon", "salon.html", None),
    ("About", None, [("Our Story", "about.html"),
                     ("Meet the Team", "team.html"),
                     ("FAQ", "faq.html"),
                     ("Policies", "policies.html")]),
    ("Booking", "booking.html", None),
    ("Contact", "contact.html", None),
]

ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6.6 3.5h2.7l1.5 4-2 1.4a11.8 11.8 0 0 0 6.3 6.3l1.4-2 4 1.5v2.7a2 2 0 0 1-2.2 2A17.5 17.5 0 0 1 4.6 5.7a2 2 0 0 1 2-2.2Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6" stroke="currentColor" stroke-width="1.8"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.8"/><path d="M12 7.3V12l3.4 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="currentColor" opacity=".14"/><path d="M8 12.4l2.7 2.7L16.3 9" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "chev": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 9.5 12 15l6-5.5" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "bed": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 17v-4.2A2.8 2.8 0 0 1 5.8 10h12.4A2.8 2.8 0 0 1 21 12.8V17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M3 17h18M6.5 10V8.2A1.7 1.7 0 0 1 8.2 6.5h7.6A1.7 1.7 0 0 1 17.5 8.2V10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 3.4 19.4 6.6v5.2c0 4.2-3 7-7.4 8.2-4.4-1.2-7.4-4-7.4-8.2V6.6L12 3.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9.2 12.2l2 2 3.6-3.8" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "door": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M14 3.5H6.2v17H14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M11 12h9m0 0-3.2-3.2M20 12l-3.2 3.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "years": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="9.6" r="5.6" stroke="currentColor" stroke-width="1.8"/><path d="M8.4 14.4 7 21l5-2.4L17 21l-1.4-6.6" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 12h13m0 0-5.2-5.2M18 12l-5.2 5.2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}


MARK = ('<svg class="mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
        '<rect width="64" height="64" rx="16" fill="var(--purple-fill)"/>'
        '<g fill="#fff">'
        '<ellipse cx="32" cy="41" rx="12.5" ry="9.8"/>'
        '<ellipse cx="17.8" cy="27.5" rx="5.5" ry="6.9"/>'
        '<ellipse cx="27.2" cy="20.6" rx="5.5" ry="7.3"/>'
        '<ellipse cx="36.8" cy="20.6" rx="5.5" ry="7.3"/>'
        '<ellipse cx="46.2" cy="27.5" rx="5.5" ry="6.9"/>'
        '</g></svg>')

def tel_link(cls="", label=None):
    return (f'<a class="{cls}" href="tel:{BIZ["phone_e164"]}">{ICON["phone"]}'
            f'{label or BIZ["phone_display"]}</a>')


# ---------------------------------------------------------------- schema
def local_business_schema():
    spec = []
    for day, hrs in HOURS:
        if hrs:
            spec.append({"@type": "OpeningHoursSpecification", "dayOfWeek": f"https://schema.org/{day}",
                         "opens": hrs[0], "closes": hrs[1]})
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": f"{ORIGIN}/#business",
        "name": BIZ["name"],
        "description": ("No-crate dog grooming, daycare and training salon in Natick, Massachusetts. "
                        "Walk-ins welcome for grooming enquiries; grooming by appointment."),
        "url": ORIGIN + "/",
        "telephone": BIZ["phone_e164"],
        "priceRange": "$$",
        "image": f"{ORIGIN}/img/groomed-doodles-natick.webp",
        "logo": f"{ORIGIN}/img/mr-nice-dog-logo.webp",
        "address": {"@type": "PostalAddress", "streetAddress": BIZ["street"], "addressLocality": BIZ["city"],
                    "addressRegion": BIZ["region"], "postalCode": BIZ["zip"], "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": BIZ["lat"], "longitude": BIZ["lng"]},
        "hasMap": BIZ["place"],
        "openingHoursSpecification": spec,
        "sameAs": [BIZ["facebook"], BIZ["instagram"]],
        "areaServed": [{"@type": "City", "name": n} for n in
                       ["Natick", "Framingham", "Wellesley", "Sherborn", "Wayland", "Ashland", "Dover"]],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Dog care services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Dog grooming"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Dog daycare"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Dog training"}},
            ],
        },
    }


def breadcrumb_schema(title, slug):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"},
        {"@type": "ListItem", "position": 2, "name": title, "item": f"{ORIGIN}/{slug}"},
    ]}


def service_schema(name, desc, slug, offers=None):
    d = {"@context": "https://schema.org", "@type": "Service", "serviceType": name, "name": name,
         "description": desc, "url": f"{ORIGIN}/{slug}",
         "provider": {"@id": f"{ORIGIN}/#business"},
         "areaServed": {"@type": "City", "name": "Natick, MA"}}
    if offers:
        d["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": f"{name} options", "itemListElement": [
            {"@type": "Offer", "name": n, "price": p, "priceCurrency": "USD"} for n, p in offers]}
    return d


def faq_schema(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in pairs]}


import json


def jsonld(*objs):
    return "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(o, separators=(",", ":"))
        for o in objs)


# ---------------------------------------------------------------- shell
def nav_html(active):
    items = []
    for label, href, sub in NAV:
        if sub:
            links = "".join(
                f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{l}</a></li>'
                for l, h in sub)
            items.append(f'<li class="has-sub"><button type="button" aria-expanded="false">{label}'
                         f'{ICON["chev"]}</button><ul class="sub">{links}</ul></li>')
        else:
            cur = ' aria-current="page"' if href == active else ""
            items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')

    mob = []
    for label, href, sub in NAV:
        if sub:
            mob.append(f'<a href="{sub[0][1]}">{label}</a>')
            mob += [f'<a class="sub-item" href="{h}">{l}</a>' for l, h in sub]
        else:
            mob.append(f'<a href="{href}">{label}</a>')

    return f'''<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="index.html" aria-label="{BIZ['name']} — home">
      {MARK}
      <span class="brand-txt"><b>Mr. Nice Dog</b><span>Grooming Salon</span></span>
    </a>
    <nav aria-label="Primary"><ul class="nav-links">{''.join(items)}</ul></nav>
    <div class="nav-act">
      {tel_link("nav-tel")}
      <a class="btn btn-primary" href="booking.html">Book a visit</a>
      <button class="burger" id="navToggle" type="button" aria-expanded="false"
              aria-controls="mobileMenu" aria-label="Open menu"><span></span><span></span><span></span></button>
    </div>
  </div>
  <div class="mobile-menu" id="mobileMenu">
    <div class="mobile-menu-in">{''.join(mob)}
      <a class="btn btn-primary btn-block" href="tel:{BIZ['phone_e164']}">Call {BIZ['phone_display']}</a>
    </div>
  </div>
</header>'''


def hours_list(cls="hours"):
    out = []
    for day, hrs in HOURS:
        if hrs:
            a = f'{int(hrs[0][:2]) % 12 or 12}:{hrs[0][3:]}am'
            hh = int(hrs[1][:2]); b = f'{hh % 12 or 12}:{hrs[1][3:]}pm'
            out.append(f'<li><span>{day}</span><span>{a} – {b}</span></li>')
        else:
            out.append(f'<li class="closed"><span>{day}</span><span>Closed</span></li>')
    return f'<ul class="{cls}">{"".join(out)}</ul>'


def footer_html():
    quick = [("Dog Grooming", "grooming.html"), ("Dog Daycare", "daycare.html"),
             ("Dog Training", "training.html"), ("Booking", "booking.html"), ("Our Salon", "salon.html")]
    more = [("About Us", "about.html"), ("Meet the Team", "team.html"), ("FAQ", "faq.html"),
            ("Policies", "policies.html"), ("Contact", "contact.html")]
    l1 = "".join(f'<a href="{h}">{t}</a>' for t, h in quick)
    l2 = "".join(f'<a href="{h}">{t}</a>' for t, h in more)
    return f'''<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-brand">
      <a class="brand" href="index.html">
        {MARK}
        <span class="brand-txt"><b>Mr. Nice Dog</b><span>Grooming Salon</span></span>
      </a>
      <p>A no-crate dog spa in Natick, Massachusetts offering grooming, daycare
         and training. Come by, check us out and become part of our dog-loving community.</p>
    </div>
    <div><h4>Services</h4><nav class="foot-nav" aria-label="Services">{l1}</nav></div>
    <div><h4>Salon</h4><nav class="foot-nav" aria-label="More">{l2}</nav></div>
    <div>
      <h4>Visit us</h4>
      <div class="foot-contact">
        <a href="tel:{BIZ['phone_e164']}"><strong>{BIZ['phone_display']}</strong></a>
        <div>{BIZ['street']}<br>{BIZ['city']}, {BIZ['region']} {BIZ['zip']}</div>
        <div>Tue–Fri 7:30am – 6pm<br>Sat 7:30am – 5pm</div>
        <div><a href="{BIZ['facebook']}" target="_blank" rel="noopener">Facebook</a> ·
             <a href="{BIZ['instagram']}" target="_blank" rel="noopener">Instagram</a></div>
      </div>
    </div>
  </div>
  <div class="wrap foot-bot">
    <p>© <span data-year>2026</span> {BIZ['name']}. All rights reserved.</p>
    <p>No Crates. Ever.</p>
  </div>
</footer>
<a class="fab" id="fab" href="tel:{BIZ['phone_e164']}">{ICON['phone']} Call the salon</a>'''


def page(slug, title, desc, body, active=None, schema=(), og_image="img/groomed-doodles-natick.webp",
         preload=None):
    active = active or slug
    canonical = ORIGIN + "/" if slug == "index.html" else f"{ORIGIN}/{slug.replace('.html','')}"
    pre = f'<link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ""
    doc = f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#B146D2">
<meta name="geo.region" content="US-MA">
<meta name="geo.placename" content="Natick, Massachusetts">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{BIZ['name']}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ORIGIN}/{og_image}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{ORIGIN}/{og_image}">

<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="img/mr-nice-dog-logo.webp">
<link rel="preload" as="font" type="font/woff2" href="fonts/gabarito.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/instrument-sans.woff2" crossorigin>
{pre}
<link rel="stylesheet" href="styles.css">
{jsonld(*schema)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{nav_html(active)}
<main id="main">
{body}
</main>
{footer_html()}
<script src="script.js" defer></script>
</body>
</html>
'''
    (ROOT / slug).write_text(doc, encoding="utf-8")
    return slug


def crumb(title):
    return (f'<nav class="crumb" aria-label="Breadcrumb"><a href="index.html">Home</a>'
            f'{ICON["chev"]}<span>{title}</span></nav>')


def page_head(title, sub, crumb_title=None, image=None, alt=""):
    media = (f'<div><img src="{image}" alt="{alt}" width="900" height="562" '
             f'loading="eager" fetchpriority="high"></div>') if image else ""
    return f'''<section class="page-head">
  <div class="wrap page-head-in">
    <div>{crumb(crumb_title or title)}
      <h1>{title}</h1>
      <p>{sub}</p>
    </div>
    {media}
  </div>
</section>'''


def cta_band(heading="Ready to spoil your best friend?",
             text="Grooming is by appointment. Give us a call and we'll find a time that suits you and your dog."):
    return f'''<section class="sec cta-band">
  <div class="wrap">
    <h2>{heading}</h2>
    <p>{text}</p>
    <div class="btn-row">
      <a class="btn btn-lg btn-yellow" href="tel:{BIZ['phone_e164']}">{ICON['phone']} Call {BIZ['phone_display']}</a>
      <a class="btn btn-lg btn-white" href="booking.html">Booking info {ICON['arrow']}</a>
    </div>
  </div>
</section>'''


def accordion(pairs, reveal=True):
    items = []
    for q, a in pairs:
        items.append(f'''<div class="acc-item">
      <button class="acc-q" type="button" aria-expanded="false"><span>{q}</span><span class="acc-ico" aria-hidden="true"></span></button>
      <div class="acc-a"><div><p>{a}</p></div></div>
    </div>''')
    r = ' data-reveal' if reveal else ''
    return f'<div class="acc"{r}>{"".join(items)}</div>'


if __name__ == "__main__":
    import content
    content.build()
    print("built", len(list(ROOT.glob("*.html"))), "pages")
