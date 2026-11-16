(() => {
  const menuButton = document.querySelector('[data-menu-button]');
  const navLinks = document.querySelector('[data-nav-links]');
  if (menuButton && navLinks) {
    menuButton.addEventListener('click', () => {
      const expanded = menuButton.getAttribute('aria-expanded') === 'true';
      menuButton.setAttribute('aria-expanded', String(!expanded));
      navLinks.classList.toggle('open', !expanded);
    });
  }

  const input = document.querySelector('[data-search]');
  if (input) {
    const cards = [...document.querySelectorAll('[data-search-item]')];
    const count = document.querySelector('[data-search-count]');
    const empty = document.querySelector('[data-empty]');
    input.addEventListener('input', () => {
      const query = input.value.trim().toLocaleLowerCase();
      let shown = 0;
      cards.forEach(card => {
        const match = (card.dataset.searchItem || '').toLocaleLowerCase().includes(query);
        card.hidden = !match;
        if (match) shown++;
      });
      if (count) count.textContent = `${shown} 筆內容`;
      if (empty) empty.classList.toggle('show', shown === 0);
    });
  }

  const headings = [...document.querySelectorAll('.prose h2[id], .prose h3[id]')];
  const toc = document.querySelector('[data-toc]');
  if (toc && headings.length) {
    headings.forEach(h => {
      const a = document.createElement('a');
      a.href = `#${h.id}`;
      a.textContent = h.textContent;
      if (h.tagName === 'H3') a.classList.add('toc-sub');
      toc.append(a);
    });
    if ('IntersectionObserver' in window) {
      const links = [...toc.querySelectorAll('a')];
      const obs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            links.forEach(a => a.classList.toggle('active', a.hash === `#${entry.target.id}`));
          }
        });
      }, {rootMargin:'-18% 0px -68% 0px'});
      headings.forEach(h => obs.observe(h));
    }
  }

  const progress = document.querySelector('[data-progress]');
  if (progress) {
    const update = () => {
      const size = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = size > 0 ? `${Math.min(100, Math.max(0, scrollY / size * 100))}%` : '0%';
    };
    window.addEventListener('scroll', update, {passive:true});
    update();
  }

  const lightbox = document.querySelector('[data-lightbox]');
  if (lightbox) {
    const enlarged = lightbox.querySelector('img');
    const caption = lightbox.querySelector('[data-lightbox-caption]');
    const close = () => { lightbox.classList.remove('open'); lightbox.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; };
    document.querySelectorAll('.prose figure img').forEach(img => {
      img.setAttribute('tabindex', '0');
      img.setAttribute('role', 'button');
      img.setAttribute('aria-label', `放大圖片：${img.alt || '圖片'}`);
      const open = () => { enlarged.src = img.src; enlarged.alt = img.alt; caption.textContent = img.alt; lightbox.classList.add('open'); lightbox.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; };
      img.addEventListener('click', open);
      img.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
    });
    lightbox.addEventListener('click', e => { if (e.target === lightbox || e.target.closest('[data-lightbox-close]')) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }
})();
