'use strict';

function initSidebar() {
  const nav = document.getElementById('taskNav');
  const cats = [...new Set(TASKS.map(t => t.cat))];
  let html = `
    <div class="task-item nav-home" onclick="navigateToMenu()">
      <div class="task-item-icon">⌂</div>
      <span>Domovská stránka</span>
    </div>
  `;
  for (const cat of cats) {
    html += `<div class="nav-section-label">${cat}</div>`;
    for (const t of TASKS.filter(x => x.cat === cat)) {
      html += `
        <div class="task-item" data-id="${t.id}" onclick="navigateTo(${t.id})">
          <div class="task-item-icon">${t.icon}</div>
          <span style="flex:1">${t.name}</span>
          <span class="task-item-num">${String(t.id).padStart(2, '0')}</span>
        </div>`;
    }
  }
  nav.innerHTML = html;
}

function breadcrumb(taskId) {
  const t = TASKS.find(x => x.id === taskId);
  return `
    <div class="task-breadcrumb">
      <a onclick="navigateToMenu()">Domů</a>
      <span class="sep">/</span>
      <span style="color:var(--text-muted)">${t.cat}</span>
      <span class="sep">/</span>
      <span class="current">Úkol ${taskId}</span>
    </div>`;
}

function taskHeader(id) {
  const t = TASKS.find(x => x.id === id);
  return `
    ${breadcrumb(id)}
    <div class="task-header">
      <div class="task-header-inner">
        <div class="task-header-icon">${t.icon}</div>
        <h2>${t.name}</h2>
      </div>
      <div class="task-subtitle">Úkol č. ${id} &nbsp;·&nbsp; ${t.cat}</div>
    </div>`;
}

function renderMenu() {
  document.getElementById('content').innerHTML = `
    <div class="welcome-header">
      <div class="school-banner">
        <h1>Domácí úkoly z <span>Pythonu</span></h1>
        <p>Střední průmyslová škola dopravní, Praha</p>
        <div class="author-line">
          <span class="author-chip">👤 Štefan Barát</span>
          <span class="author-chip">🏫 SPŠD Praha</span>
          <span class="author-chip">📦 ${TASKS.length} úkolů</span>
        </div>
      </div>
      <div class="section-title">Všechny úkoly</div>
      <div class="task-grid">
        ${TASKS.map(t => `
          <div class="task-card-welcome" onclick="navigateTo(${t.id})">
            <div class="tcw-num">${String(t.id).padStart(2, '0')}</div>
            <span class="tcw-icon">${t.icon}</span>
            <div class="tcw-name">${t.name}</div>
            <div class="tcw-cat">${t.cat}</div>
          </div>`).join('')}
      </div>
    </div>`;
}
