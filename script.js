/* ============================================================
   MR. NICE DOG — script.js
   Nav, dropdowns, mobile menu, scroll reveal, FAQ accordion,
   and the enquiry forms (which hand off to the visitor's own
   email app — nothing is stored by this site).
   ============================================================ */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var EMAIL = 'info@mrnicedog.com';   /* TODO(confirm): salon's real inbox */

  root.classList.add('reveal');

  /* ---- current year ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---- sticky nav shading + floating call button ---- */
  var nav = document.getElementById('nav');
  var fab = document.getElementById('fab');
  var ticking = false;
  function paint() {
    ticking = false;
    var y = window.scrollY || window.pageYOffset;
    if (nav) nav.classList.toggle('scrolled', y > 8);
    if (fab) fab.classList.toggle('show', y > window.innerHeight * 0.5);
  }
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(paint);
  }, { passive: true });
  paint();

  /* ---- desktop dropdowns ---- */
  var subs = Array.prototype.slice.call(document.querySelectorAll('.has-sub'));
  subs.forEach(function (item) {
    var btn = item.querySelector('button');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = item.classList.contains('open');
      subs.forEach(function (o) {
        o.classList.remove('open');
        var b = o.querySelector('button');
        if (b) b.setAttribute('aria-expanded', 'false');
      });
      if (!open) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });
  document.addEventListener('click', function () {
    subs.forEach(function (o) {
      o.classList.remove('open');
      var b = o.querySelector('button');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    subs.forEach(function (o) {
      o.classList.remove('open');
      var b = o.querySelector('button');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  });

  /* ---- mobile menu ---- */
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('mobileMenu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
  }

  /* ---- scroll reveal ---- */
  var revealables = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
  revealables.forEach(function (el) {
    var d = el.getAttribute('data-reveal-delay');
    if (d) el.style.setProperty('--d', d);
  });
  if (reduce || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---- FAQ / service accordions (one open at a time per group) ---- */
  Array.prototype.slice.call(document.querySelectorAll('.acc')).forEach(function (group) {
    var items = Array.prototype.slice.call(group.querySelectorAll('.acc-item'));
    items.forEach(function (item) {
      var btn = item.querySelector('.acc-q');
      if (!btn) return;
      btn.addEventListener('click', function () {
        var isOpen = item.classList.contains('open');
        items.forEach(function (other) {
          other.classList.remove('open');
          var q = other.querySelector('.acc-q');
          if (q) q.setAttribute('aria-expanded', 'false');
        });
        if (!isOpen) {
          item.classList.add('open');
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });
  });

  /* ---- size tabs on the pricing table (arrow-key navigable) ---- */
  Array.prototype.slice.call(document.querySelectorAll('[role="tablist"]')).forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));

    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    }

    /* panels ship visible for the no-JS case; collapse to the selected one */
    var initial = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0] || tabs[0];
    if (initial) select(initial, false);

    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () { select(tab, false); });
      tab.addEventListener('keydown', function (e) {
        var i = tabs.indexOf(tab);
        var next = e.key === 'ArrowRight' ? i + 1
                 : e.key === 'ArrowLeft'  ? i - 1
                 : e.key === 'Home'       ? 0
                 : e.key === 'End'        ? tabs.length - 1 : null;
        if (next === null) return;
        e.preventDefault();
        select(tabs[(next + tabs.length) % tabs.length], true);
      });
    });
  });

  /* ============================================================
     Enquiry forms -> the visitor's own email client.
     There is no backend, so nothing about anyone's dog is stored
     or transmitted by this site. The visitor sees and sends the
     message themselves.
     ============================================================ */
  Array.prototype.slice.call(document.querySelectorAll('form')).forEach(function (form) {
    var statusEl = form.querySelector('[data-status]');
    if (!statusEl) return;

    function setStatus(msg, bad) {
      statusEl.textContent = msg;
      statusEl.classList.toggle('is-error', !!bad);
    }
    form.addEventListener('input', function (e) {
      if (e.target.classList) e.target.classList.remove('invalid');
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      setStatus('', false);

      var data = new FormData(form);
      var get = function (k) { return (data.get(k) || '').toString().trim(); };
      var name = get('name');
      var phone = get('phone');

      if (name.length < 2) {
        var n = form.querySelector('[name="name"]');
        if (n) { n.classList.add('invalid'); n.focus(); }
        return setStatus('Please add your name so we know who to call back.', true);
      }
      if (phone.replace(/\D/g, '').length < 7) {
        var p = form.querySelector('[name="phone"]');
        if (p) { p.classList.add('invalid'); p.focus(); }
        return setStatus('Please add a phone number we can reach you on.', true);
      }

      var lines = ['Name: ' + name, 'Phone: ' + phone];
      [['dog', 'Dog'], ['breed', 'Breed & weight'], ['service', 'Service'],
       ['date', 'Preferred day'], ['source', 'Heard about us via'], ['notes', 'Notes']
      ].forEach(function (pair) {
        var v = get(pair[0]);
        if (v) lines.push(pair[1] + ': ' + v);
      });

      var subject = 'Website enquiry — ' + (get('service') || 'general') + ' — ' + name;
      var href = 'mailto:' + EMAIL +
                 '?subject=' + encodeURIComponent(subject) +
                 '&body=' + encodeURIComponent(lines.join('\n'));
      window.location.href = href;
      setStatus('Opening your email app — press send and we will get straight back to you.', false);
    });
  });
})();
