# Mr. Nice Dog Grooming Salon — website

An 11-page static rebuild of [mrnicedog.com](https://www.mrnicedog.com/) for the dog
grooming, daycare and training salon at 42 Worcester Street, Natick MA.

Their palette, their photographs, their copy and their prices — rebuilt as fast,
crawlable static HTML with a proper local-SEO layer.

```
index.html …  11 generated pages
build.py      shell: head, nav, footer, schema helpers
content.py    every page's copy and prices
styles.css    design tokens + components
script.js     nav, dropdowns, accordions, reveal, enquiry forms
img/          27 optimised webp images (1.7 MB total)
fonts/        Gabarito + Instrument Sans, self-hosted
sitemap.xml   generated
robots.txt    generated
```

## Run it

```bash
npm run dev        # builds, then serves on http://localhost:5173
python3 build.py   # regenerate the HTML after editing content.py
```

Deploy with `vercel`, or drop the folder on any static host. Nothing runs at
request time.

**Edit content in `content.py`, not in the `.html` files** — the HTML is generated
and will be overwritten. Nav links, address, phone and hours live once in
`build.py` (`BIZ`, `NAV`, `HOURS`) and propagate everywhere.

## Design

**The salon's walls are the ground, not an accent.** The single biggest choice
here: the page background is a cream pulled off the yellow those walls are
actually painted, so the photographs sit *inside* the room instead of being cut
out and pasted onto white. White is reserved for raised surfaces — cards, tables,
forms. Purple stays the accent it should be: buttons, links, one conviction band.

| Token | Value | Where it came from |
| --- | --- | --- |
| `--cream` / `--cream-2` | `#FDF5E2` / `#F8EACA` | derived from the salon wall yellow |
| `--yellow` | `#EDCE58` | sampled directly from their own photos |
| `--purple` | `#B146D2` | the purple already in their CSS (595 uses) |
| `--purple-fill` / `--purple-ink` / `--purple-deep` | `#A340C1` / `#7E3196` / `#5F2571` | see contrast note |
| `--line-ui` | `#8C8171` | control boundaries, held to 3:1 for WCAG 1.4.11 |
| `--ink` | `#16121A` | body text |

Their brand purple `#B146D2` is **4.49:1** on white — a hair under AA. It is kept
for large shapes; the deeper steps carry text and button fills. Don't collapse
them into one.

`--line` is decorative hairlines only. Anything that is the *sole* visible
boundary of a control — form inputs, ghost buttons — uses `--line-ui`, because
WCAG 1.4.11 holds those to 3:1 and a 1.27:1 hairline fails it.

Type is self-hosted **Gabarito** (display) + **Instrument Sans** (text), two woff2
files totalling 64 KB, no external requests. Body copy is 17px; `--t-meta` (15px)
is for metadata and must not be used for paragraphs.

### The structure is built around what this business actually owns

Rather than the generic hero → three-equal-cards → alternating-splits sequence:

- **The hero leads with the promise**, not a slogan: *"Your dog waits in an open
  bed. Never a crate."*
- **Grooming gets the big tile.** It is in the business's name, so the services
  block is a 7/5 bento with grooming at double size — not three equal cards
  asserting that grooming, daycare and training are the same size of thing.
- **"No crates. Ever." is a section, not a badge.** Full-bleed photograph of the
  actual room, then an honest two-column comparison: what usually happens between
  the bath and the blow-dry versus what happens here. It shows the claim instead
  of asserting it four times.
- **Antonio's Westminster record is on the homepage.** Best of Breed and Group
  Placement, 22 years apprenticed — the highest-trust asset the business has, and
  it was buried in paragraph two of an essay.
- **The gallery is a captioned bento**, with wide tiles and named rooms, on a
  fixed row height so tiles never leave holes.
- **Grooming prices are one table with size tabs**, not four stacked full-width
  tables where the name and its price were 400px apart. Arrow-key navigable, and
  without JavaScript all four tables render normally.
- **The logo is drawn, not photographed.** It was a 42px crop of a photo of their
  sign — a muddy dark square at the top of every page. It is now an inline SVG paw
  mark that stays crisp at any size and costs no request. The same paw tiles
  faintly across the band that closes every page.
- **The hero photo sits on an offset yellow panel** with a typographic stamp on the
  exposed corner — the sticker device their own salon photos already use. The
  previous hero repeated the sign, so the brand name appeared three times above
  the fold.
- **The marquee earns its place.** It used to repeat three of the four trust items
  sitting directly above it; it now lists breeds and services instead.

Light theme only — the brand is bright yellow and purple and the audience is pet
owners on phones in daylight.

## SEO

This is the part that should move the needle, because the old site was a single
weak funnel.

**Each page targets its own intent.** The old site's homepage tried to rank for
everything; now `grooming.html` owns "dog grooming Natick MA", `daycare.html`
owns "dog daycare Natick MA", `training.html` owns "puppy training Natick MA".
Every page has its own title (≤60 chars), description (≤160) and canonical.

**Structured data** on every page:

- `LocalBusiness` with the real NAP, geo coordinates, per-day opening hours,
  `areaServed` for Natick, Framingham, Wellesley, Sherborn, Wayland, Ashland and
  Dover, and an offer catalogue.
- `Service` + `BreadcrumbList` on the three service pages, with prices.
- `FAQPage` on the homepage and FAQ page — this is the one most likely to win a
  rich result, since the questions are genuine.

The geo coordinates (`42.3037897, -71.3283709`) were lifted from the Google Maps
embed on their own contact page, so they point at the real building.

**Performance**, which is a ranking factor and was the old site's weakest point:
their images totalled 5.9 MB, with a single 2.2 MB PNG. The same images are now
1.7 MB of webp — **69% smaller** — correctly sized, lazy-loaded below the fold,
with `width`/`height` set to prevent layout shift. The hero image is preloaded
with `fetchpriority="high"`. Fonts are preloaded and self-hosted.

**Also included:** `sitemap.xml`, `robots.txt`, semantic image filenames,
descriptive alt text on all 27 images, one `<h1>` per page, and internal linking
between every service page.

## Verified

Measured on the built pages, not assumed:

- **0 WCAG AA text-contrast failures** across all 11 pages (~1,000 text nodes),
  using a self-testing checker that scores each node against its real composited
  background.
- **UI boundaries pass 1.4.11** — form and button borders measure 3.2–3.8:1.
- **Focus rings pass on both grounds** — 8.3:1 on cream, and a yellow ring inside
  purple bands where the purple ring measured 1.74:1.
- 0 console errors, 0 failed requests, 0 horizontal overflow at 390 / 768 / 1200 /
  1440px, and no nav wrapping at any of them.
- One `<h1>` per page; every image has alt text; all JSON-LD parses.
- Reduced-motion renders a complete static page; without JavaScript nothing is
  hidden and all four price tables are reachable.
- Pricing tabs verified with mouse, click and arrow keys.

## ⚠ Confirm before going live

Everything on the site is taken from their existing pages. These few items still
need the owner's input:

| Item | Where | Currently |
| --- | --- | --- |
| **Email address** | `script.js` (`EMAIL`) | `info@mrnicedog.com` — **a guess.** The enquiry forms open the visitor's email app addressed to it. Replace with the real inbox or the forms misfire. |
| Extra-large / super-large grooming prices | `grooming.html` | Their site lists the 76–100 lb and 101 lb+ size bands but publishes no prices, so those say "call for a quote". |
| Team roles | `team.html` | Antonio (Master Groomer), Ana (Groomer), Megan, Billie and Faith (Bathers), Lauren (Front Desk Manager) — as listed on their page. Photos exist for four of the six; Ana and Lauren are listed without one. |
| Reviews | — | Their reviews page says "No reviews available now", so there are **no testimonials anywhere on this site.** See below. |
| Vimeo daycare video | — | Not carried over. The original embeds `vimeo.com/1027971418`; add it back if wanted. |
| Instagram feed | — | Their old site embedded a live Instagram feed via a WordPress plugin. Not reproduced — it needs a third-party script. |

Nothing has been invented: no fake reviews, no fake credentials, no made-up
prices, no stock photography. Every image is one of theirs and every price is
copied from their published tables.

## The biggest SEO win available, which I could not do for them

**Get reviews.** For a local service business, review count and rating are among
the strongest local-pack ranking factors, and this business currently shows none
on its own site. Google Business Profile reviews matter most. Once there are
genuine reviews, add `AggregateRating` to the `LocalBusiness` schema in
`build.py` and a testimonials section — but only with real, attributable ones.

Two other things worth doing that are outside a website rebuild:

1. **Claim and complete the Google Business Profile** with these exact NAP
   details, the same photos, and service categories matching the three pages.
   Consistency between the site and the profile is what local ranking rewards.
2. **Point the three service pages at Google Business Profile services** so the
   profile and site reinforce each other.
