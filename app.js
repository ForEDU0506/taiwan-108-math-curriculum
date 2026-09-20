const sidebar = document.querySelector('#sidebar');
const toggle = document.querySelector('#sidebarToggle');
const close = document.querySelector('#sidebarClose');
const gradeFilter = document.querySelector('#gradeFilter');
const themeFilter = document.querySelector('#themeFilter');
const searchInput = document.querySelector('#searchInput');
const searchButton = document.querySelector('#searchButton');
const resultMessage = document.querySelector('#resultMessage');

function setSidebar(open) {
  sidebar.classList.toggle('collapsed', !open);
  toggle.setAttribute('aria-expanded', String(open));
}

toggle.addEventListener('click', () => setSidebar(sidebar.classList.contains('collapsed')));
close.addEventListener('click', () => setSidebar(false));

function applyFilters() {
  const grade = gradeFilter.value;
  const theme = themeFilter.value;
  const keyword = searchInput.value.trim().toLowerCase();
  const cards = [...document.querySelectorAll('[data-search]')];
  let visible = 0;

  cards.forEach((card) => {
    const gradeMatches = grade === 'all' || card.dataset.grade === grade;
    const themeMatches = theme === 'all' || card.dataset.theme === theme;
    const textMatches = !keyword || card.dataset.search.toLowerCase().includes(keyword);
    const show = gradeMatches && themeMatches && textMatches;
    card.hidden = !show;
    if (show) visible += 1;
  });

  resultMessage.textContent = grade === 'all' && theme === 'all' && !keyword
    ? ''
    : `目前顯示 ${visible} 筆相關內容`;
}

gradeFilter.addEventListener('change', applyFilters);
themeFilter.addEventListener('change', applyFilters);
searchButton.addEventListener('click', applyFilters);
searchInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') applyFilters();
});

document.querySelectorAll('.top-nav a, .index-links a').forEach((link) => {
  link.addEventListener('click', () => {
    if (window.innerWidth <= 700) setSidebar(false);
  });
});
