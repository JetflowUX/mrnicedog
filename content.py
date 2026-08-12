#!/usr/bin/env python3
"""Page content for Mr. Nice Dog. Copy and prices are taken from the
existing mrnicedog.com pages; nothing here is invented."""
from build import (BIZ, ICON, ORIGIN, accordion, cta_band, faq_schema, hours_list,
                   local_business_schema, breadcrumb_schema, service_schema, page,
                   page_head, tel_link)

P = BIZ["phone_e164"]
PD = BIZ["phone_display"]

# ------------------------------------------------------------------ data
GROOM_SERVICES = [
    ("The &ldquo;Nice&rdquo; Brushout", "A full body brush using dry shampoo and conditioner."),
    ("The &ldquo;Nice&rdquo; Bath",
     "A thorough deep cleaning bath using tailored shampoos and conditioners with a thorough dry."),
    ("The &ldquo;Nice&rdquo; Hand-Stripping",
     "Specific to terrier breeds, hand-stripping removes hair from the dog&rsquo;s undercoat and dead hair from "
     "the topcoat. It is an involved longer process that requires the groomer to use specific tools and work "
     "meticulously for the best results."),
    ("The &ldquo;Deluxe Nice&rdquo; Bath",
     "Similar to the &ldquo;Nice&rdquo; Bath with the addition of a nail clip, pad trim, ear and teeth cleaning, "
     "sanitary trim and eyes trim."),
    ("The &ldquo;Premium Nice&rdquo; Bath &amp; Clip",
     "Similar to the &ldquo;Deluxe Nice&rdquo; Bath with a breed specific haircut or your haircut preferences."),
    ("The &ldquo;Nice&rdquo; Puppy Package",
     "A series of 4 visits to introduce your puppy into the world of grooming. The visits gradually expose your "
     "puppy to our full range of services so that they become more comfortable each time — a perfect way to begin "
     "a lifetime of good dog hygiene."),
]

PRICES = [
    ("Very Small Dogs", "1 lb – 12 lbs",
     [("The &ldquo;Nice&rdquo; Brush", 30, 35, 40), ("The &ldquo;Nice&rdquo; Bath", 45, 60, 60),
      ("The &ldquo;Deluxe Nice&rdquo; Bath", 55, 75, 75), ("The &ldquo;Premium Nice&rdquo; Bath &amp; Clip", 80, 95, 95)]),
    ("Small Dogs", "13 lbs – 25 lbs",
     [("The &ldquo;Nice&rdquo; Brush", 40, 45, 50), ("The &ldquo;Nice&rdquo; Bath", 50, 70, 70),
      ("The &ldquo;Deluxe Nice&rdquo; Bath", 65, 85, 85), ("The &ldquo;Premium Nice&rdquo; Bath &amp; Clip", 95, 110, 110)]),
    ("Medium Dogs", "26 lbs – 50 lbs",
     [("The &ldquo;Nice&rdquo; Brush", 50, 55, 60), ("The &ldquo;Nice&rdquo; Bath", 65, 85, 85),
      ("The &ldquo;Deluxe Nice&rdquo; Bath", 75, 100, 100), ("The &ldquo;Premium Nice&rdquo; Bath &amp; Clip", 120, 130, 130)]),
    ("Large Dogs", "51 lbs – 75 lbs",
     [("The &ldquo;Nice&rdquo; Brush", 85, 90, 95), ("The &ldquo;Nice&rdquo; Bath", 120, 140, 140),
      ("The &ldquo;Deluxe Nice&rdquo; Bath", 160, 170, 180), ("The &ldquo;Premium Nice&rdquo; Bath &amp; Clip", 165, 180, 180)]),
]

TRAINING_FEES = [
    ("Pre-Training Consultation / Evaluation", "$25"),
    ("Private Puppy Training Course", "$1,125"),
    ("Group Basic Training Course", "$500"),
    ("Private Basic Training Course", "$1,000"),
    ("Group Advanced Training Course", "$600"),
    ("Private Advanced Training Course", "$1,000"),
    ("Single Session Training", "$125"),
    ("&ldquo;Happy Time&rdquo; Socialization Hour", "$30 / hour"),
]

TEAM = [
    ("Antonio", "Master Groomer &amp; Owner", "img/antonio-torres-master-groomer.webp",
     "Antonio Torres, founder of Mr. Nice Dog, photographed with a standard poodle"),
    ("Billie", "Bather", "img/billie-dog-groomer-natick.webp", "Billie, bather at Mr. Nice Dog, with a standard poodle"),
    ("Megan", "Bather", "img/megan-dog-bather-natick.webp", "Megan, bather at Mr. Nice Dog, with a freshly groomed poodle"),
    ("Faith", "Bather", "img/faith-dog-groomer-natick.webp", "Faith, bather at Mr. Nice Dog, with a goldendoodle"),
]
TEAM_MORE = [("Ana", "Groomer"), ("Lauren", "Front Desk Manager")]

GALLERY = [
    ("img/grooming-stations-natick.webp", "Grooming stations at Mr. Nice Dog in Natick with bright yellow walls"),
    ("img/open-beds-no-crates.webp", "Open beds instead of crates in the Mr. Nice Dog daycare area"),
    ("img/bathing-room.webp", "Stainless steel bathing tubs in the Mr. Nice Dog bathing room"),
    ("img/daycare-gated-park.webp", "Gated indoor dog park with white picket fencing"),
    ("img/daycare-play-park.webp", "Indoor play park at Mr. Nice Dog daycare"),
    ("img/training-room.webp", "Training room with yellow bone wall decals"),
    ("img/daycare-rest-area.webp", "Rest area with dog beds along the daycare fence"),
    ("img/salon-interior-yellow.webp", "Interior of the Mr. Nice Dog salon in Natick, Massachusetts"),
]

REAL_FAQ = [
    ("How often should my dog be groomed?",
     "A lot depends on the pet&rsquo;s lifestyle and living conditions. As a general guide, dogs who have their hair "
     "cut in particular clips &mdash; Poodles, Cockers, Lhasa Apsos, Shih Tzus, Bichons and so on &mdash; should be "
     "groomed every 4&ndash;6 weeks. Bath dogs such as Labradors, Shepherds and Collies should be groomed every "
     "6&ndash;8 weeks."),
    ("How long does grooming take?",
     "When you arrange an appointment with us you are provided with a dedicated pet groomer who will discuss your "
     "dog&rsquo;s grooming requirements. In over 95% of cases we complete the grooming process in 2 hours or less, "
     "giving your pet a positive experience in a modern and spacious facility."),
    ("Do I get the same groomer each time?",
     "Some clients prefer to keep the same groomer. If your dog is nervous, or you have specific requests, we "
     "encourage requesting the same groomer because it fosters a relationship between the client, the groomer "
     "and the dog."),
    ("Do you use crates?",
     "Never. We do not have or use crates in our salon. Dogs rest in individual open beds instead, and we schedule "
     "appointments to minimise the time your dog spends with us."),
    ("What vaccinations does my dog need?",
     "Dogs over 4 months old must have proof of a Rabies vaccine along with Bordetella and Distemper vaccines. "
     "All grooming dogs must be up to date on vaccinations and must show proof of rabies. Dogs must be at least "
     "12 weeks old to receive any of our services."),
    ("Do you take walk-ins?",
     "Walk-ins are welcome to come in, meet us and look around. Grooming itself is by appointment only, so call "
     f"{PD} to book a time."),
]


def img(src, alt, w=None, h=None, cls="", lazy=True, sizes=None):
    a = f' width="{w}"' if w else ""
    b = f' height="{h}"' if h else ""
    c = f' class="{cls}"' if cls else ""
    s = f' sizes="{sizes}"' if sizes else ""
    ld = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="{src}" alt="{alt}"{a}{b}{c}{s}{ld}>'


def ticks(items):
    li = "".join(f'<li>{ICON["check"]}<span>{t}</span></li>' for t in items)
    return f'<ul class="ticks">{li}</ul>'


def gallery_grid(items, limit=None):
    figs = "".join(f'<figure>{img(s, a)}</figure>' for s, a in (items[:limit] if limit else items))
    return f'<div class="gallery">{figs}</div>'


# ------------------------------------------------------------------ pages
def build():
    # ---------------------------------------------------------------- HOME
    home_faq = REAL_FAQ[:3]
    marquee = ["Poodles", "Doodles", "Terriers &amp; hand-stripping", "Labs &amp; shepherds",
               "Puppy packages", "Nail &amp; pad trims", "Ear &amp; teeth cleaning",
               "De-matting", "Breed-specific clips", "Puppy socialisation"]
    mset = "".join(f"<span>{m}</span>" for m in marquee)

    body = f'''<section class="hero">
  <div class="wrap hero-in">
    <div>
      <h1>Your dog waits in an open bed. <em>Never a crate.</em></h1>
      <p class="lede">Grooming, daycare and training on Worcester Street in Natick,
        run by a Westminster Best&nbsp;of&nbsp;Breed groomer. Bright rooms, gentle hands,
        and the shortest stay we can manage.</p>
      <div class="hero-cta">
        <a class="btn btn-lg btn-primary" href="tel:{P}">{ICON['phone']} Call {PD}</a>
        <a class="btn btn-lg btn-ghost" href="grooming.html">See grooming prices {ICON['arrow']}</a>
      </div>
    </div>
    <div class="hero-media">
      {img("img/groomer-with-standard-poodle.webp",
           "A Mr. Nice Dog groomer with a freshly groomed white standard poodle in the Natick salon",
           1210, 1301, lazy=False)}
      <div class="stamp" aria-hidden="true">No crates.<span>Ever.</span></div>
    </div>
  </div>
  <div class="wrap">
    <ul class="trust">
      <li>{ICON['door']}<b>Walk-ins welcome</b><span>Come and look around any time. Grooming itself is by appointment.</span></li>
      <li>{ICON['bed']}<b>No crates, ever</b><span>Individual open beds in a climate-controlled room.</span></li>
      <li>{ICON['shield']}<b>Fully insured</b><span>Every service, every dog, every day.</span></li>
      <li>{ICON['years']}<b>Since 2007</b><span>A family trade Antonio grew up in.</span></li>
    </ul>
  </div>
</section>

<section class="marquee" aria-hidden="true">
  <div class="marquee-track"><div class="marquee-set">{mset}</div><div class="marquee-set">{mset}</div></div>
</section>

<section class="sec sec-lg">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <span class="eyebrow-rule" aria-hidden="true"></span>
      <h2>Three services, one dog-loving community</h2>
      <p>Grooming is what we are named for. Daycare and training run alongside it,
         in the same building, with the same people.</p>
    </div>
    <div class="svc">
      <article class="card svc-lead" data-reveal>
        {img("img/grooming-stations-natick.webp",
             "Dog grooming stations with yellow walls at Mr. Nice Dog in Natick, MA", 800, 500)}
        <div class="card-body">
          <h3>Dog Grooming</h3>
          <p class="price-from">From $30</p>
          <p>Baths, breed-specific clips, hand-stripping, nails, ears and teeth, using gentle
             hypoallergenic products suited to every skin type. You are given a dedicated groomer
             who talks through your dog&rsquo;s coat before anything starts.</p>
          <a class="go" href="grooming.html">Grooming &amp; full price list {ICON['arrow']}</a>
        </div>
      </article>
      <div class="svc-side" data-reveal data-reveal-delay="1">
        <article class="card">
          {img("img/daycare-play-park.webp", "Indoor dog daycare play park at Mr. Nice Dog in Natick", 800, 600)}
          <div class="card-body">
            <h3>Dog Daycare</h3>
            <p class="price-from">$30 half day &middot; $45 full day</p>
            <p>An indoor play park with an attendant on duty all day.</p>
            <a class="go" href="daycare.html">Daycare &amp; rates {ICON['arrow']}</a>
          </div>
        </article>
      </div>
      <div class="svc-side" data-reveal data-reveal-delay="2">
        <article class="card">
          {img("img/dog-training-natick-ma.webp",
               "A golden retriever sitting at heel during a training session at Mr. Nice Dog", 900, 850)}
          <div class="card-body">
            <h3>Dog Training</h3>
            <p class="price-from">From $125 a session</p>
            <p>Puppy, basic and advanced courses, private or in groups of 3&ndash;6.</p>
            <a class="go" href="training.html">Training &amp; courses {ICON['arrow']}</a>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>

<section class="promise">
  <div class="promise-media">
    {img("img/band-indoor-park.webp",
         "The crate-free indoor dog park at Mr. Nice Dog, with white picket fencing and yellow walls",
         2000, 959)}
    <div class="promise-head"><div class="in">
      <h2>No crates. Ever.</h2>
      <p>It is the first thing people ask, so here is the room it happens in.</p>
    </div></div>
  </div>
  <div class="promise-panel">
    <div class="wrap" style="padding-top:clamp(1.8rem,3.5vw,3rem)">
      <div class="compare" data-reveal>
        <div class="them">
          <h3>What usually happens</h3>
          <p>Between the bath and the blow-dry, most salons put your dog in a holding crate
             and move on to the next one.</p>
        </div>
        <div class="us">
          <h3>What happens here</h3>
          <p>An individual open bed in a climate-controlled room, with a designated attendant
             on duty, and appointments spaced so the wait is short.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-lg">
  <div class="wrap cred">
    <div data-reveal>
      {img("img/antonio-torres-master-groomer.webp",
           "Antonio Torres, master groomer and founder of Mr. Nice Dog, with a black standard poodle",
           900, 1125)}
    </div>
    <div data-reveal data-reveal-delay="1">
      <blockquote>
        <p>&ldquo;Nothing is better than hearing someone call the work I do
          <em style="font-style:normal;color:var(--purple-ink)">nice</em>.&rdquo;</p>
      </blockquote>
      <div class="who"><b>Antonio Torres</b>Founder, master groomer and trainer</div>
      <div class="cred-facts">
        <div><b>Westminster</b><span>Best of Breed &amp; Group Placement, multiple times</span></div>
        <div><b>22 years</b><span>Apprenticed to a New England breeder-groomer</span></div>
        <div><b>Since 1993</b><span>Working with dogs in New England</span></div>
      </div>
      <p style="margin-top:1.6rem"><a class="btn btn-ghost" href="about.html">Read Antonio&rsquo;s story {ICON['arrow']}</a></p>
    </div>
  </div>
</section>

<section class="sec sec-white">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <span class="eyebrow-rule" aria-hidden="true"></span>
      <h2>Inside the salon</h2>
      <p>Bright yellow walls, white picket fencing and a lot of room to run.</p>
    </div>
    <div data-reveal>
      <div class="gallery">
        <figure class="wide"><img src="img/grooming-stations-natick.webp" alt="Row of grooming stations with yellow walls at Mr. Nice Dog in Natick" loading="lazy" decoding="async"><figcaption>The grooming floor</figcaption></figure>
        <figure><img src="img/open-beds-no-crates.webp" alt="Open dog beds along the fence instead of crates" loading="lazy" decoding="async"><figcaption>Open beds, no crates</figcaption></figure>
        <figure><img src="img/bathing-room.webp" alt="Stainless steel bathing tubs at Mr. Nice Dog" loading="lazy" decoding="async"><figcaption>The bathing suite</figcaption></figure>
        <figure><img src="img/sq-play-park.webp" alt="Indoor play park with toys at Mr. Nice Dog daycare" loading="lazy" decoding="async"><figcaption>The indoor park</figcaption></figure>
        <figure class="wide pos-high"><img src="img/groomed-doodles-natick.webp" alt="Three freshly groomed doodles at Mr. Nice Dog in Natick" loading="lazy" decoding="async"><figcaption>Wednesday afternoon</figcaption></figure>
        <figure><img src="img/hero-doodle-portrait.webp" alt="A groomed apricot doodle in front of the Mr. Nice Dog sign" loading="lazy" decoding="async"><figcaption>Freshly finished</figcaption></figure>
      </div>
    </div>
    <p style="margin-top:1.8rem"><a class="btn btn-ghost" href="salon.html">See the whole salon {ICON['arrow']}</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap wrap-narrow">
    <div class="sec-head" data-reveal>
      <span class="eyebrow-rule" aria-hidden="true"></span>
      <h2>Frequently asked</h2>
    </div>
    {accordion(home_faq)}
    <p style="margin-top:1.8rem"><a class="btn btn-ghost" href="faq.html">All questions {ICON['arrow']}</a></p>
  </div>
</section>

<section class="sec sec-cream2">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <span class="eyebrow-rule" aria-hidden="true"></span>
      <h2>Find us in Natick</h2>
      <p>On Worcester Street, minutes from Framingham, Wellesley and Wayland.</p>
    </div>
    <div class="info-grid" style="margin-bottom:1.6rem">
      <div class="info-card" data-reveal>
        <h3>{ICON['pin']} Address</h3>
        <p>{BIZ['street']}<br>{BIZ['city']}, {BIZ['region']} {BIZ['zip']}</p>
        <p><a href="{BIZ['place']}" target="_blank" rel="noopener">Get directions</a></p>
      </div>
      <div class="info-card" data-reveal data-reveal-delay="1">
        <h3>{ICON['phone']} Phone</h3>
        <p><a href="tel:{P}">{PD}</a></p>
        <p><a href="tel:{BIZ['phone2_e164']}">{BIZ['phone2_display']}</a></p>
      </div>
      <div class="info-card" data-reveal data-reveal-delay="2">
        <h3>{ICON['clock']} Hours</h3>
        {hours_list()}
      </div>
    </div>
    <div class="map" data-reveal>
      <iframe src="{BIZ['map_embed']}" title="Map showing Mr. Nice Dog Grooming Salon at 42 Worcester Street, Natick, MA"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>

{cta_band()}'''
    page("index.html",
         "Dog Grooming, Daycare & Training in Natick MA | Mr. Nice Dog",
         "No-crate dog grooming, daycare and training in Natick MA. Grooming from $30, daycare from $30 a "
         f"half day. Walk-ins welcome. Call {PD}.",
         body, schema=(local_business_schema(), faq_schema(home_faq)),
         preload="img/groomer-with-standard-poodle.webp")

    # ------------------------------------------------------------ GROOMING
    svc = "".join(f'<div class="acc-item"><button class="acc-q" type="button" aria-expanded="false">'
                  f'<span>{n}</span><span class="acc-ico" aria-hidden="true"></span></button>'
                  f'<div class="acc-a"><div><p>{d}</p></div></div></div>' for n, d in GROOM_SERVICES)
    # four stacked full-width tables were unreadable; one table at a time,
    # switched by real buttons, keeps name and price in the same eye-span
    tabs, panels = "", ""
    for i, (name, weight, rows) in enumerate(PRICES):
        sel = "true" if i == 0 else "false"
        tabs += (f'<button class="tab" role="tab" id="tab-{i}" aria-controls="panel-{i}" '
                 f'aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{name}</button>')
        trs = "".join(f'<tr><th scope="row">{r[0]}</th><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td></tr>'
                      for r in rows)
        panels += (f'<div class="tab-panel" role="tabpanel" id="panel-{i}" aria-labelledby="tab-{i}"'
                   f'><div class="table-scroll"><table class="ptable">'
                   f'<caption>{name} &middot; {weight}</caption>'
                   f'<thead><tr><th scope="col">Service</th><th scope="col">Short coat</th>'
                   f'<th scope="col">Medium coat</th><th scope="col">Long coat</th></tr></thead>'
                   f'<tbody>{trs}</tbody></table></div></div>')
    tables = (f'<div class="tabs" role="tablist" aria-label="Dog size">{tabs}</div>{panels}')

    body = f'''{page_head("Dog Grooming in Natick, MA",
        "Baths, breed-specific clips, hand-stripping and full spa services &mdash; in a salon that never uses crates.",
        "Dog Grooming", image="img/groomer-with-goldendoodle.webp",
        alt="A Mr. Nice Dog groomer with a freshly groomed goldendoodle")}

<section class="sec">
  <div class="wrap split">
    <div data-reveal>
      <h2>What makes us different</h2>
      <p class="lede">Our grooming is based on a holistic approach, to create a stress-free
        environment for your dog. The mental and social wellbeing of your pet is our top priority.</p>
      <p>We do not have or use crates in our salon, and we schedule appointments to minimise the
        time your dog spends here. We use the finest shampoos, conditioners and products &mdash;
        gentle, hypoallergenic and suited to all skin types: normal, dry and oily.</p>
      <p>When checking in, we analyse your dog&rsquo;s skin and coat and talk through any concerns.
        Dogs sometimes arrive unexpectedly matted; when that happens we may have to focus the
        day&rsquo;s service on removing the mats before anything else.</p>
      <div class="note"><strong>Before you book:</strong> all pets must be up to date on their rabies
        vaccination. When booking a service, please attach your pet&rsquo;s vaccination certificate.</div>
    </div>
    <div class="split-media" data-reveal data-reveal-delay="1">
      {img("img/groomer-with-standard-poodle.webp", "A Mr. Nice Dog groomer with a freshly groomed white standard poodle", 1200, 1224)}
    </div>
  </div>
</section>

<section class="sec sec-white">
  <div class="wrap wrap-narrow">
    <div class="sec-head" data-reveal><h2>Our grooming services</h2>
      <p>Choose the level of service your dog needs, from a refreshing brushout to a full clip.</p></div>
    <div class="acc" data-reveal>{svc}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head" data-reveal><span class="eyebrow-rule" aria-hidden="true"></span><h2>Grooming prices</h2>
      <p>Pick your dog&rsquo;s size. Pricing is based on weight and the length of their coat.</p></div>
    <div class="pricing-wrap" data-reveal>{tables}</div>
    <div class="note warn" style="margin-top:1.6rem" data-reveal>
      <strong>Extra large and super large dogs:</strong> for dogs over 75 lbs
      (76&ndash;100 lbs and 101 lbs +) we quote individually &mdash; please call {tel_link("", PD)}.
      All prices are subject to change based on your dog&rsquo;s weight, size, coat length and
      condition at the intake evaluation.
    </div>
  </div>
</section>

{cta_band("Book your dog's grooming appointment",
          "Grooming is by appointment only so every dog gets a dedicated groomer and the shortest possible stay.")}'''
    page("grooming.html",
         "Dog Grooming Natick MA — Prices & Services | Mr. Nice Dog",
         "Dog grooming in Natick MA from $30. Baths, breed-specific clips, hand-stripping, nails and "
         "teeth. No crates. Full price list by size and coat.",
         body, schema=(local_business_schema(), breadcrumb_schema("Dog Grooming", "grooming"),
                       service_schema("Dog grooming",
                                      "Dog baths, breed-specific haircuts, hand-stripping, nail trimming, "
                                      "ear and teeth cleaning in Natick, Massachusetts.", "grooming",
                                      [("The Nice Brush", "30"), ("The Nice Bath", "45"),
                                       ("The Deluxe Nice Bath", "55"), ("The Premium Nice Bath & Clip", "80")])),
         og_image="img/grooming-stations-natick.webp")

    # ------------------------------------------------------------- DAYCARE
    body = f'''{page_head("Dog Daycare in Natick, MA",
        "An indoor dog park, a designated attendant on duty, and open beds instead of crates.", "Dog Daycare",
        image="img/daycare-gated-park.webp", alt="The gated indoor dog park at Mr. Nice Dog in Natick")}

<section class="sec">
  <div class="wrap split">
    <div data-reveal>
      <h2>Daycare at Mr. Nice Dog</h2>
      <p class="lede">For pet parents needing daycare, we are happy to offer this service during our
        business hours &mdash; a morning, an afternoon, or a full day.</p>
      <p>Our facility has a state-of-the-art indoor play &ldquo;park&rdquo; with an automatic cleaning
        system to keep areas tidy and clean. There is always a designated daycare attendant on duty
        who monitors and watches over all the dogs in attendance.</p>
      <p>Daycare involves a combination of play time, socialisation and relaxation periods with the
        other dogs attending. We do not use holding crates in our facility &mdash; we use individual
        open beds for your dog&rsquo;s comfort.</p>
      <p>Pet parents are encouraged to bring snacks and food if needed. We offer snacks at no cost,
        though there is an additional fee for any food we provide. You must inform us of your
        dog&rsquo;s food-related restrictions, sensitivities and allergies.</p>
    </div>
    <div class="split-media" data-reveal data-reveal-delay="1">
      {img("img/indoor-dog-park-turf.webp", "Indoor artificial-turf dog park with toys at Mr. Nice Dog daycare", 900, 1490)}
    </div>
  </div>
</section>

<section class="sec sec-white">
  <div class="wrap">
    <div class="cards cards-2">
      <div data-reveal>
        <h2>Daycare rates</h2>
        <p class="lede" style="margin-bottom:1.4rem">Book a morning, an afternoon or the full day.</p>
        <ul class="rate-list">
          <li><span>Full day</span><b>$45</b></li>
          <li><span>Half day</span><b>$30</b></li>
          <li><span>Behavioural evaluation (first visit)</span><b>$25</b></li>
        </ul>
        <div class="note" style="margin-top:1.2rem">
          <strong>Before the first visit:</strong> we meet with you to understand your dog&rsquo;s
          temperament and behaviour around both people and dogs, so their experience is stress-free
          and fun. This evaluation fee is $25.
        </div>
      </div>
      <div data-reveal data-reveal-delay="1">
        <h2>Daycare hours</h2>
        <p class="lede" style="margin-bottom:1.4rem">Separate from salon hours &mdash; please note the times.</p>
        <ul class="rate-list is-hours">
          <li><span>Monday to Friday</span><b>8:00am – 5:30pm</b></li>
          <li><span>Saturday</span><b>9:00am – 4:30pm</b></li>
          <li><span>Morning daycare</span><b>8:00am – 12:30pm</b></li>
          <li><span>Afternoon daycare</span><b>1:00pm – 5:30pm</b></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-purple">
  <div class="wrap split rev">
    <div class="split-media" data-reveal>
      {img("img/daycare-gated-park.webp", "Gated indoor dog park with white picket fencing at Mr. Nice Dog", 800, 600)}
    </div>
    <div data-reveal data-reveal-delay="1">
      <h2>Stay, play, learn</h2>
      <p class="lede">The coolest indoor dog park in Natick. When working with us, you can rest
        assured that your dog is in good hands.</p>
      {ticks(["Automatic cleaning system keeps the park tidy",
              "A designated attendant on duty at all times",
              "Play, socialisation and proper rest periods",
              "Individual open beds — we never use holding crates"])}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap wrap-narrow">
    <div class="callout" data-reveal>
      <div>
        <h3>Booking daycare</h3>
        <p>To book a daycare spot for your companion, please give us a bark at {PD}.
           Our team will help you schedule a day of play, pampering and all-around happiness.</p>
      </div>
      <a class="btn btn-lg btn-primary" href="tel:{P}">{ICON['phone']} Call to book</a>
    </div>
  </div>
</section>

{cta_band("Come and try a day with us",
          "Bring your best friend to Mr. Nice Dog and let them have some fun — don't leave them bored at home.")}'''
    page("daycare.html",
         "Dog Daycare in Natick MA — $30 Half Day, $45 Full Day",
         "Crate-free dog daycare in Natick MA. Indoor play park, attendant always on duty, open beds "
         f"instead of crates. $30 half day, $45 full day. Call {PD}.",
         body, schema=(local_business_schema(), breadcrumb_schema("Dog Daycare", "daycare"),
                       service_schema("Dog daycare",
                                      "Crate-free dog daycare with an indoor play park in Natick, Massachusetts.",
                                      "daycare", [("Full day", "45"), ("Half day", "30"),
                                                  ("Behavioural evaluation", "25")])),
         og_image="img/indoor-dog-park-natick-ma.webp")

    # ------------------------------------------------------------ TRAINING
    fees = "".join(f'<li><span>{n}</span><b>{p}</b></li>' for n, p in TRAINING_FEES)
    courses = [
        ("Puppy Training Course", "Puppies 3 to 6 months &middot; 5 weeks &middot; 10 sessions",
         "Each session runs for 1 hour. For consistent, impactful training we suggest at least twice per week. "
         "This course requires a pet parent to be present.",
         ["Crate basic training", "Common puppy problems: chewing, jumping, play and biting", "Walking manners",
          "Socialisation with foreign objects, people and dogs", "Acceptance of collar", "Walking with leash"]),
        ("Basic Training Course", "Dogs 6 months and older &middot; 5 weeks &middot; 10 sessions",
         "Each session runs for 1 hour. We will accommodate your personal schedule and adjust the training "
         "schedule to meet your requirements.",
         ["Commands &mdash; sit, come, down, stay", "Leash acceptance", "Socialisation with dogs",
          "Socialisation with people", "Calming and agitation management",
          "Leash walking and heel without pulling", "Jumping control"]),
        ("Advanced Training Course", "Dogs with basic skills &middot; 8 sessions",
         "For dogs that come to us already having the skill set outlined in the Basic Training Course.",
         ["Off-leash commands &mdash; stay, sit, down, heel", "Off-leash recall", "Confidence building"]),
    ]
    course_html = ""
    for title, meta, intro, skills in courses:
        course_html += f'''<article class="card" data-reveal><div class="card-body">
        <h3>{title}</h3>
        <p class="price-from">{meta}</p>
        <p>{intro}</p>
        {ticks(skills)}
      </div></article>'''

    body = f'''{page_head("Dog Training in Natick, MA",
        "Puppy, basic and advanced courses in private or small group settings, run by experienced trainers.",
        "Dog Training", image="img/dog-training-natick-ma.webp",
        alt="A golden retriever sitting at heel during training at Mr. Nice Dog")}

<section class="sec">
  <div class="wrap split">
    <div data-reveal>
      <h2>Professional dog training</h2>
      <p class="lede">Mr. Nice Dog offers training classes for your dog in both private and group
        settings: a Basic Training Course, an Advanced Training Course and a Puppy Training Course.
        Each course consists of between 8 and 10 sessions.</p>
      <p>We also provide a Private Single Training Session for pet parents with specific, targeted
        needs &mdash; a new skill, or a review and fine-tune of skills your dog already has.</p>
      <p>Our &ldquo;Happy Time Socialization Hour&rdquo; is a great way for your dog to meet and play
        with others. It is essential that dogs interact, acquire socialisation skills and build confidence.</p>
      <p>Our trainers are experienced, competent professionals who have trained all breeds for many
        years. Prior to enrolment we conduct an evaluation meeting to assess your dog&rsquo;s needs
        and the best approach to reach the targeted goals.</p>
      <div class="note"><strong>Group class size:</strong> a minimum of 3 dogs and a maximum of 6.</div>
    </div>
    <div class="split-media" data-reveal data-reveal-delay="1">
      {img("img/dog-training-natick-ma.webp", "Dog training at Mr. Nice Dog in Natick, Massachusetts", 900, 1207)}
    </div>
  </div>
</section>

<section class="sec sec-white">
  <div class="wrap">
    <div class="sec-head" data-reveal><h2>Our courses</h2>
      <p>Every course is flexible and built around your schedule.</p></div>
    <div class="cards cards-3">{course_html}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap wrap-narrow">
    <div class="sec-head" data-reveal><h2>Training fees</h2>
      <p>All courses begin with a pre-training consultation and evaluation.</p></div>
    <ul class="rate-list" data-reveal>{fees}</ul>
  </div>
</section>

{cta_band("Start with an evaluation",
          "A $25 consultation tells us what your dog needs and which course will get you there fastest.")}'''
    page("training.html",
         "Dog Training in Natick MA — Puppy, Basic & Advanced",
         "Dog training in Natick MA. Puppy, basic and advanced courses, private or small groups of 3-6, "
         "plus single sessions from $125.",
         body, schema=(local_business_schema(), breadcrumb_schema("Dog Training", "training"),
                       service_schema("Dog training",
                                      "Puppy, basic and advanced dog obedience training in Natick, Massachusetts.",
                                      "training", [("Single Session Training", "125"),
                                                   ("Group Basic Training Course", "500"),
                                                   ("Group Advanced Training Course", "600")])),
         og_image="img/dog-training-natick-ma.webp")

    # --------------------------------------------------------------- ABOUT
    body = f'''{page_head("About Mr. Nice Dog",
        "Pride and commitment to the art of dog care &mdash; from a family that has bred and trained dogs for generations.",
        "About", image="img/groomer-with-standard-poodle.webp",
        alt="A Mr. Nice Dog groomer with a white standard poodle")}

<section class="sec">
  <div class="wrap split">
    <div class="split-media" data-reveal>
      {img("img/antonio-torres-master-groomer.webp",
           "Antonio Torres, founder and master groomer at Mr. Nice Dog, with a black standard poodle", 900, 1200)}
    </div>
    <div data-reveal data-reveal-delay="1">
      <h2>Pride and commitment to the art of dog care</h2>
      <p>It has always been my dream to open a full-service dog salon ever since I was a young adult.
        At a very early age I was surrounded by animals because my parents and grandparents bred and
        trained dogs for their livelihood. When I was around 9 years old I realised my love and passion
        for dogs whenever I was in their presence. I began helping and working alongside my family when
        I was not attending school. As a teenager I took on more responsibilities within my family&rsquo;s
        business to expand my knowledge in every aspect of dog care.</p>
      <p>To further develop my skills, I moved to the US in 1993 to work alongside a well-renowned dog
        breeder and groomer based right here in New England. I apprenticed and worked there for 22 years,
        becoming a master trainer. During this time I competed at numerous dog shows throughout the
        country and won several awards in the &ldquo;Best of Breed&rdquo; category. I also competed at
        the prestigious Westminster Kennel Club Dog Show in New York, where I won &ldquo;Best of
        Breed&rdquo; and &ldquo;Group Placement&rdquo; awards multiple times.</p>
      <p>I moved to Massachusetts in 2006 to further develop my dog grooming abilities. Over the years
        I worked for notable dog salons in and around Boston as a means to refine my grooming skills
        and techniques.</p>
      <p>It is so exciting to now open my full-service dog salon that offers the best there is in dog
        grooming, training and daycare services. I welcome you to come by, check us out and take a tour
        of our salon.</p>
      <p><strong>Antonio Torres</strong><br><span style="color:var(--ink-3)">Founder &amp; Owner</span></p>
    </div>
  </div>
</section>

<section class="sec sec-yellow">
  <div class="wrap wrap-narrow">
    <div data-reveal>
      <h2>The naming of my business</h2>
      <p>When it came to choosing a name for my new business, I tossed around several ideas. What came
        to mind was how my clients would often say to me how wonderful and &ldquo;nice&rdquo; their dog
        looked after being groomed and cared for. I was so pleased that they appreciated and liked my
        work. For me, nothing is better than hearing someone call the work I do &ldquo;nice&rdquo;!
        I knew that &ldquo;Mr. Nice Dog Grooming and Spa&rdquo; was a perfect name for my business.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <h2>A best-in-class dog spa</h2>
      <p>&ldquo;Offering grooming, daycare and training services with our commitment to provide
         exceptional service.&rdquo;</p>
    </div>
    <div data-reveal>{gallery_grid(GALLERY, 4)}</div>
  </div>
</section>

{cta_band()}'''
    page("about.html",
         "About Mr. Nice Dog — Natick's No-Crate Dog Salon",
         "Meet Antonio Torres, master groomer and founder of Mr. Nice Dog in Natick MA. Westminster "
         "Best of Breed winner and a lifetime around dogs.",
         body, schema=(local_business_schema(), breadcrumb_schema("About", "about")),
         og_image="img/antonio-torres-master-groomer.webp")

    # ---------------------------------------------------------------- TEAM
    cards = "".join(f'''<figure data-reveal>{img(s, a, 560, 560)}
      <figcaption><b>{n}</b><span>{r}</span></figcaption></figure>''' for n, r, s, a in TEAM)
    more = "".join(f'<li><b>{n}</b><span>{r}</span></li>' for n, r in TEAM_MORE)
    body = f'''{page_head("Meet the team",
        "The people who will be looking after your dog &mdash; groomers, bathers and the friendliest front desk in Natick.",
        "Our Team", image="img/mr-nice-dog-full-team.webp",
        alt="The Mr. Nice Dog Grooming Salon team in Natick, Massachusetts")}

<section class="sec">
  <div class="wrap">
    <div class="team">{cards}</div>
    <div class="wrap-narrow" style="padding:0;margin-top:2.5rem">
      <ul class="rate-list" data-reveal>{more}</ul>
    </div>
  </div>
</section>

<section class="sec sec-white">
  <div class="wrap split">
    <div class="split-media" data-reveal>
      {img("img/mr-nice-dog-full-team.webp", "The full Mr. Nice Dog Grooming Salon team in Natick, MA", 1200, 900)}
    </div>
    <div data-reveal data-reveal-delay="1">
      <h2>One dedicated groomer per dog</h2>
      <p class="lede">When you arrange an appointment you are provided with a dedicated pet groomer who
        will discuss your dog&rsquo;s grooming requirements.</p>
      <p>If your dog is nervous, or you have specific requests, we encourage requesting the same groomer
        each visit &mdash; it fosters a relationship between the client, the groomer and the dog.</p>
      <a class="btn btn-primary" href="booking.html">Book with us {ICON['arrow']}</a>
    </div>
  </div>
</section>

{cta_band()}'''
    page("team.html",
         "Meet the Team — Dog Groomers in Natick, MA | Mr. Nice Dog",
         "Meet the groomers, bathers and front desk team at Mr. Nice Dog Grooming Salon in Natick, Massachusetts. "
         "One dedicated groomer per dog, every visit.",
         body, schema=(local_business_schema(), breadcrumb_schema("Our Team", "team")),
         og_image="img/mr-nice-dog-full-team.webp")

    # --------------------------------------------------------------- SALON
    extra = GALLERY + [
        ("img/groomer-with-poodle-2.webp", "A Mr. Nice Dog groomer with a groomed standard poodle"),
        ("img/groomer-with-goldendoodle.webp", "A Mr. Nice Dog team member with a goldendoodle"),
        ("img/daycare-play-area.webp", "The daycare play area at Mr. Nice Dog"),
        ("img/salon-detail.webp", "Detail of the Mr. Nice Dog salon interior"),
    ]
    body = f'''{page_head("Our salon",
        "The new concept for your best friend has arrived in Natick &mdash; bright, climate-controlled and crate-free.",
        "Our Salon", image="img/salon-interior-yellow.webp",
        alt="The bright yellow interior of the Mr. Nice Dog salon in Natick")}

<section class="sec">
  <div class="wrap">
    <div class="split" style="margin-bottom:clamp(2.5rem,5vw,4rem)">
      <div data-reveal>
        <h2>Built around the dog, not the schedule</h2>
        <p class="lede">A climate-controlled facility with state-of-the-art equipment, bright colours
          and a lot of room to move.</p>
        <p>Grooming stations sit along one wall, the bathing room is fitted with stainless steel tubs,
          and the indoor park runs the length of the building behind white picket fencing. Dogs rest
          in individual open beds. There is not a crate in the building.</p>
        {ticks(["Climate-controlled throughout",
                "Indoor play park with an automatic cleaning system",
                "Stainless steel bathing suite",
                "Fully insured"])}
      </div>
      <div class="split-media" data-reveal data-reveal-delay="1">
        {img("img/indoor-dog-park-natick-ma.webp", "The crate-free indoor dog park at Mr. Nice Dog in Natick", 1800, 1440)}
      </div>
    </div>
    <div data-reveal>{gallery_grid(extra)}</div>
  </div>
</section>

{cta_band("Come and take a tour",
          "Walk in during opening hours, meet the team and see the salon for yourself. No appointment needed just to look around.")}'''
    page("salon.html",
         "Inside Our Dog Grooming Salon in Natick MA | Mr. Nice Dog",
         "Look inside Mr. Nice Dog in Natick MA: grooming stations, a stainless steel bathing suite "
         "and a crate-free indoor dog park.",
         body, schema=(local_business_schema(), breadcrumb_schema("Our Salon", "salon")),
         og_image="img/salon-interior-yellow.webp")

    # ------------------------------------------------------------- BOOKING
    body = f'''{page_head("Booking",
        "Grooming is by appointment, daycare is booked by phone. Here is exactly how it works.", "Booking")}

<section class="sec">
  <div class="wrap">
    <div class="cards cards-2">
      <div class="form-card" data-reveal>
        <h2 style="margin-bottom:.6rem">Grooming appointments</h2>
        <p>Grooming services are by appointment only. Call us and we will match your dog with a
          dedicated groomer and a time that keeps their stay as short as possible.</p>
        <p>Grooming service prices are subject to change due to your pet&rsquo;s weight, size and hair
          length during our intake evaluation.</p>
        <div class="note"><strong>All grooming dogs must be up to date on vaccinations</strong> and must
          show proof of rabies.</div>
        <p style="margin-top:1.2rem"><a class="btn btn-primary btn-block" href="tel:{P}">{ICON['phone']} Call {PD}</a></p>
      </div>
      <div class="form-card" data-reveal data-reveal-delay="1">
        <h2 style="margin-bottom:.6rem">Daycare bookings</h2>
        <p>To book a daycare spot for your adorable companion, please give us a bark at {PD}.
          Our friendly team is ready to help you schedule a day filled with play, pampering and
          all-around happiness for your pet.</p>
        <p>Before a first visit we run a behavioural evaluation ($25) so we understand your dog&rsquo;s
          temperament around both people and dogs.</p>
        <p style="margin-top:1.2rem"><a class="btn btn-ghost btn-block" href="daycare.html">Daycare rates &amp; hours {ICON['arrow']}</a></p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-white">
  <div class="wrap wrap-narrow">
    <div class="note warn" data-reveal>
      <h3 style="margin-bottom:.5rem">Important: confirming your grooming booking</h3>
      <p style="margin:0">Please be cautious of any communication claiming to represent Mr. Nice Dog
        outside of our official channels. To ensure the authenticity of your grooming appointment,
        kindly verify directly with our team on {PD}.</p>
    </div>
    <div style="margin-top:1.6rem" class="note" data-reveal>
      <h3 style="margin-bottom:.5rem">About the card pre-authorisation</h3>
      <p style="margin:0">In order to save your credit card information for payment after your grooming
        service is completed, we run a pre-authorisation charge on your card. This charge is solely for
        verifying your card information and will not be the final charge for your grooming service.
        Once the service is completed we will charge the full amount to your saved card. If you have any
        questions about this process, please don&rsquo;t hesitate to contact us.</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap wrap-narrow">
    <div class="sec-head" data-reveal><h2>Send us a booking enquiry</h2>
      <p>Prefer to write? Fill this in and it opens a pre-written email to the salon &mdash;
         you can check it before it sends.</p></div>
    <div class="form-card" data-reveal>
      <form id="enquiry" novalidate>
        <div class="f-row">
          <label class="field"><span>Your name</span>
            <input type="text" name="name" autocomplete="name" placeholder="Jane Smith" required></label>
          <label class="field"><span>Phone number</span>
            <input type="tel" name="phone" autocomplete="tel" placeholder="(508) 000-0000" required></label>
        </div>
        <div class="f-row">
          <label class="field"><span>Dog&rsquo;s name</span>
            <input type="text" name="dog" placeholder="Charlie"></label>
          <label class="field"><span>Breed &amp; approximate weight</span>
            <input type="text" name="breed" placeholder="Goldendoodle, 45 lbs"></label>
        </div>
        <label class="field"><span>Service</span>
          <select name="service">
            <option>Grooming — not sure which, please advise</option>
            <option>The “Nice” Brushout</option>
            <option>The “Nice” Bath</option>
            <option>The “Deluxe Nice” Bath</option>
            <option>The “Premium Nice” Bath &amp; Clip</option>
            <option>Hand-stripping</option>
            <option>The “Nice” Puppy Package</option>
            <option>Daycare</option>
            <option>Training</option>
          </select></label>
        <label class="field"><span>Preferred day <em>optional</em></span>
          <input type="date" name="date"></label>
        <label class="field"><span>Anything we should know? <em>optional</em></span>
          <textarea name="notes" rows="3" placeholder="Nervous with clippers, matting behind the ears, vaccination dates…"></textarea></label>
        <button class="btn btn-primary btn-lg btn-block" type="submit">Open email to the salon</button>
        <p class="f-status" data-status role="status" aria-live="polite"></p>
        <p class="f-fine">This opens your own email app with the details filled in. Nothing is stored
          on this website. For the fastest answer, call {PD}.</p>
      </form>
    </div>
  </div>
</section>

{cta_band()}'''
    page("booking.html",
         "Book Dog Grooming or Daycare in Natick, MA | Mr. Nice Dog",
         f"Book grooming or daycare at Mr. Nice Dog in Natick MA. Grooming is by appointment — call {PD}. "
         "Daycare bookings by phone. Vaccination proof required.",
         body, schema=(local_business_schema(), breadcrumb_schema("Booking", "booking")))

    # ------------------------------------------------------------- CONTACT
    body = f'''{page_head("Contact us",
        "Questions about grooming, daycare or training? Call the salon or send us a note.", "Contact")}

<section class="sec">
  <div class="wrap">
    <div class="info-grid">
      <div class="info-card" data-reveal>
        <h3>{ICON['phone']} Phone</h3>
        <p>Questions? Call us.</p>
        <p><a href="tel:{P}"><strong>{PD}</strong></a></p>
        <p><a href="tel:{BIZ['phone2_e164']}">{BIZ['phone2_display']}</a></p>
      </div>
      <div class="info-card" data-reveal data-reveal-delay="1">
        <h3>{ICON['pin']} Address</h3>
        <p>{BIZ['street']}<br>{BIZ['city']}, {BIZ['region']} {BIZ['zip']}</p>
        <p><a href="{BIZ['place']}" target="_blank" rel="noopener">Open in Google Maps</a></p>
      </div>
      <div class="info-card" data-reveal data-reveal-delay="2">
        <h3>{ICON['clock']} Business hours</h3>
        {hours_list()}
      </div>
    </div>
  </div>
</section>

<section class="sec sec-white">
  <div class="wrap">
    <div class="cards cards-2">
      <div data-reveal>
        <h2>Get in touch</h2>
        <p class="lede">Tell us about your dog and we&rsquo;ll come back to you. For same-day answers,
          calling is always fastest.</p>
        <div class="map" style="margin-top:1.6rem">
          <iframe src="{BIZ['map_embed']}" title="Map showing Mr. Nice Dog Grooming Salon at 42 Worcester Street, Natick, MA"
                  loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
      </div>
      <div class="form-card" data-reveal data-reveal-delay="1">
        <form id="contactForm" novalidate>
          <div class="f-row">
            <label class="field"><span>Your name</span>
              <input type="text" name="name" autocomplete="name" required></label>
            <label class="field"><span>Phone</span>
              <input type="tel" name="phone" autocomplete="tel" required></label>
          </div>
          <label class="field"><span>Service</span>
            <select name="service">
              <option>Dog Grooming</option><option>Daycare</option>
              <option>Training</option><option>Other</option>
            </select></label>
          <label class="field"><span>Where did you hear about us? <em>optional</em></span>
            <select name="source">
              <option>Google</option><option>Yelp</option><option>Social media</option>
              <option>Referral</option><option>Newspaper</option><option>Other</option>
            </select></label>
          <label class="field"><span>Message</span>
            <textarea name="notes" rows="4" placeholder="How can we help?"></textarea></label>
          <button class="btn btn-primary btn-lg btn-block" type="submit">Open email to the salon</button>
          <p class="f-status" data-status role="status" aria-live="polite"></p>
          <p class="f-fine">Opens your email app with the details filled in. Nothing is stored on this website.</p>
        </form>
      </div>
    </div>
  </div>
</section>

{cta_band()}'''
    page("contact.html",
         "Contact Mr. Nice Dog — Natick MA | (508) 545-1046",
         f"Contact Mr. Nice Dog Grooming Salon at 42 Worcester Street, Natick MA 01760. Call {PD}. "
         "Open Tuesday to Friday 7:30am–6pm and Saturday 7:30am–5pm.",
         body, schema=(local_business_schema(), breadcrumb_schema("Contact", "contact")))

    # ----------------------------------------------------------------- FAQ
    body = f'''{page_head("Frequently asked questions",
        "Grooming frequency, appointment length, vaccinations and what happens on the day.", "FAQ")}

<section class="sec">
  <div class="wrap wrap-narrow">
    {accordion(REAL_FAQ)}
    <div class="callout" style="margin-top:2.5rem" data-reveal>
      <div><h3>Still have questions?</h3>
        <p>If your question hasn&rsquo;t been answered here, call the salon and we&rsquo;ll talk it through.</p></div>
      <a class="btn btn-lg btn-primary" href="tel:{P}">{ICON['phone']} Call {PD}</a>
    </div>
  </div>
</section>

{cta_band()}'''
    page("faq.html",
         "Dog Grooming FAQ — Natick, MA | Mr. Nice Dog",
         "How often should a dog be groomed? How long does it take? What vaccinations are needed? "
         "Answers from Mr. Nice Dog Grooming Salon in Natick, Massachusetts.",
         body, schema=(local_business_schema(), breadcrumb_schema("FAQ", "faq"), faq_schema(REAL_FAQ)))

    # ------------------------------------------------------------ POLICIES
    sections = [
        ("Pet health", [
            "<strong>Health:</strong> Dogs that have age-related or any general health issues might not be suitable "
            "for our services. We will consult with you regarding the health of your pet prior to the start of any "
            "service. We require all up-to-date, relevant information about your pet&rsquo;s current health status. "
            "If your pet is under the care of a veterinarian for a specific illness, ailment or condition this must "
            "be communicated to us. We have the right to refuse a service if we deem that your pet cannot be "
            "properly serviced due to any existing health conditions.",
            "<strong>Vaccines:</strong> Dogs over 4 months old must have proof of a Rabies vaccine along with "
            "Bordetella and Distemper vaccines.",
            "<strong>Sterilisation:</strong> Dogs over the age of 9 months must be neutered or spayed.",
            "<strong>Fleas &amp; ticks:</strong> We maintain a tick and flea free environment. We reserve the right "
            "to stop or refuse a service if it is determined that your pet has fleas or ticks. If this is determined "
            "while a service is underway, your pet will be treated to remove them and you will be responsible for "
            "the cost of that treatment.",
            "<strong>Mats:</strong> If your pet arrives matted, additional de-matting fees will apply. Depending on "
            "severity, de-matting might take precedence over all other grooming. If the booked service cannot be "
            "completed during the scheduled appointment as a result, we will require a future visit to complete it.",
            "<strong>Age:</strong> Dogs must be at least 12 weeks old to receive any of our services."]),
        ("Pet behaviour", [
            "Our approach is gentle, loving and holistic, and we want your pet to have the best experience possible. "
            "Due to the nature of the grooming process, or a pet&rsquo;s tolerance for stress, strangers and "
            "handling, some pets can become anxious or reactive. When a dog demonstrates aggressive or "
            "uncontrollable behaviour they might not be suitable for our services. If inappropriate behaviour is "
            "demonstrated while your pet is already in our facility, we may discontinue the service if we determine "
            "that continuing presents a threat to your dog&rsquo;s emotional or physical health, or to the safety of "
            "the groomer. Service fees will be pro-rated when a service is stopped."]),
        ("Payment &amp; pricing", [
            "Published prices are subject to change due to your pet&rsquo;s size, weight, coat length and condition, "
            "behaviour and requested haircut style.",
            "When a grooming service requires more time than originally outlined, we will contact you immediately "
            "before continuing to inform you of potential additional costs.",
            "Full payment is due when a service is completed.",
            "We accept cash and credit cards (Amex, Discover, MasterCard, Visa)."]),
        ("Grooming appointment cancellations", [
            "If you cancel within 24 hours of your scheduled appointment time you will be charged the full cost of "
            "the service, which will be charged automatically to the credit card on file.",
            "An appointment rescheduled within 24 hours will not be charged if a future appointment is made. If that "
            "future appointment is then cancelled, you will incur the full cost of the service. In this case we will "
            "require all future bookings to be paid in advance."]),
        ("Daycare and training cancellations", [
            "Cancellations within 24 hours of the scheduled appointment time will incur the full cost of the service "
            "and be charged automatically to the credit card on file."]),
        ("Late fees", [
            "Appointments arriving 15 minutes past the scheduled service time may have to be rescheduled. If you are "
            "running late, please call us. If you have not arrived within the 15-minute window, the booked service "
            "will be considered a no-show and charged in full.",
            "At the beginning of all grooming services we communicate the approximate pick-up time. You will receive "
            "a call or text 15 minutes before completion. If you are not on site 15 minutes after the confirmed "
            "pick-up time, a pet holding fee of $1 per minute applies."]),
        ("No shows", [
            "&ldquo;No call / no show&rdquo; appointments will be charged automatically to the credit card on file."]),
        ("Communication", [
            "There might be times when we have to speak with you regarding the service being provided to your pet. "
            "We ask that you are readily available while your pet is in our care."]),
    ]
    blocks = ""
    for title, items in sections:
        lis = "".join(f'<li>{ICON["check"]}<span>{t}</span></li>' for t in items)
        blocks += f'<div data-reveal style="margin-bottom:2.5rem"><h2>{title}</h2><ul class="ticks">{lis}</ul></div>'
    body = f'''{page_head("Policies",
        "Grooming, daycare and training policies &mdash; health, behaviour, payment and cancellations.", "Policies")}
<section class="sec"><div class="wrap wrap-narrow">{blocks}</div></section>
{cta_band()}'''
    page("policies.html",
         "Policies — Grooming, Daycare & Training | Mr. Nice Dog",
         "Mr. Nice Dog policies for grooming, daycare and training in Natick MA: vaccination requirements, "
         "behaviour, payment, cancellations, late fees and no-shows.",
         body, schema=(local_business_schema(), breadcrumb_schema("Policies", "policies")))

    _write_sitemap()


def _write_sitemap():
    from build import OUT
    pages = [("", "1.0", "weekly"), ("grooming", "0.9", "monthly"), ("daycare", "0.9", "monthly"),
             ("training", "0.9", "monthly"), ("booking", "0.8", "monthly"), ("contact", "0.8", "monthly"),
             ("about", "0.7", "yearly"), ("team", "0.6", "yearly"), ("salon", "0.6", "yearly"),
             ("faq", "0.7", "yearly"), ("policies", "0.4", "yearly")]
    urls = "".join(
        f'\n  <url><loc>{ORIGIN}/{s}</loc><changefreq>{c}</changefreq><priority>{p}</priority></url>'
        for s, p, c in pages)
    OUT.mkdir(exist_ok=True)
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}\n</urlset>\n', encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n", encoding="utf-8")
