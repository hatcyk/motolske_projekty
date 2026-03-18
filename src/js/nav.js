'use strict';

let currentTaskId = null;

function navigateTo(id) {
  if (window._timer) { clearInterval(window._timer); window._timer = null; }
  currentTaskId = id;
  updateSidebar();
  const content = document.getElementById('content');
  content.innerHTML = '';
  const map = {
    1: renderTrojuhelnik, 2: renderPismenoDne, 3: renderSety,
    4: renderData, 5: renderKalkulacka, 6: renderBullsCows,
    7: renderTicTacToe, 8: renderPrumer, 9: renderOS,
    10: renderEmaily, 11: renderFormatovani,
    12: renderDlouhaSlova, 13: renderCsv, 14: renderJson,
  };
  if (map[id]) map[id](content);
}

function navigateToMenu() {
  if (window._timer) { clearInterval(window._timer); window._timer = null; }
  currentTaskId = null;
  updateSidebar();
  renderMenu();
}

function updateSidebar() {
  document.querySelectorAll('.task-item[data-id]').forEach(el => {
    el.classList.toggle('active', parseInt(el.dataset.id) === currentTaskId);
  });
}
