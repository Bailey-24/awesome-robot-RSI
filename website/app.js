'use strict';

(() => {
  const input = document.querySelector('#search');
  const codeOnly = document.querySelector('#code-only');
  const sort = document.querySelector('#sort');
  const container = document.querySelector('#paper-cards');
  const cards = [...container.querySelectorAll('.paper-card')];
  const buttons = [...document.querySelectorAll('.category-nav button')];
  const searchText = new Map(cards.map(card => [card, card.textContent.toLowerCase()]));
  let category = 'all';

  function update() {
    const terms = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const card of cards) {
      const matches = (category === 'all' || card.dataset.category === category)
        && (!codeOnly.checked || card.dataset.code === 'true')
        && terms.every(term => searchText.get(card).includes(term));
      card.hidden = !matches;
      if (matches) visible++;
    }
    container.append(...[...cards].sort((a, b) => sort.value === 'oldest'
      ? a.dataset.date.localeCompare(b.dataset.date)
      : b.dataset.date.localeCompare(a.dataset.date)));
    for (const button of buttons) button.setAttribute('aria-pressed', String(button.dataset.category === category));
    document.querySelector('#result-count').textContent = `${visible} ${visible === 1 ? 'paper' : 'papers'} · ${category === 'all' ? 'all research areas' : category}`;
    document.querySelector('#empty').hidden = visible !== 0;
  }

  function reset() {
    category = 'all';
    input.value = '';
    codeOnly.checked = false;
    sort.value = 'newest';
    update();
  }

  input.addEventListener('input', update);
  codeOnly.addEventListener('change', update);
  sort.addEventListener('change', update);
  document.querySelector('#reset').addEventListener('click', reset);
  for (const button of buttons) button.addEventListener('click', () => {
    category = button.dataset.category;
    update();
  });
  document.addEventListener('keydown', event => {
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey
        && !event.target.closest('input, textarea, select, [contenteditable="true"]')) {
      event.preventDefault();
      input.focus();
    }
    if (event.key === 'Escape' && document.activeElement === input) {
      input.value = '';
      update();
      input.blur();
    }
  });
  document.querySelectorAll('.enhanced-control').forEach(control => { control.hidden = false; });
  update();
})();
