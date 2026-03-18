'use strict';

function renderDlouhaSlova(el) {
  const DEFAULT = `koupelna\nzona\nsyr\nteta\nkriz\nrodina\nnacitani\ncokolada\nasociace\nlavicka\npovrch\nrotace\nzamestnanec\nbalicek\nkomunikace\npopularni\nveta`;

  el.innerHTML = `
    ${taskHeader(12)}
    <div class="card card-accent">
      <div class="row" style="align-items:flex-start">
        <div class="form-group" style="flex:3">
          <label class="form-label">Seznam slov (každé na nový řádek nebo oddělená mezerou)</label>
          <textarea id="t12-words" class="data-textarea" rows="8">${DEFAULT}</textarea>
        </div>
        <div class="form-group" style="flex:1;min-width:100px">
          <label class="form-label">Min. délka</label>
          <input type="number" id="t12-min" class="form-input" value="7" min="1" max="50">
        </div>
      </div>
    </div>
    <div id="t12-res"></div>`;

  function compute() {
    const slova = parseWords(document.getElementById('t12-words').value);
    const min = parseInt(document.getElementById('t12-min').value) || 1;
    const res = document.getElementById('t12-res');
    if (slova.length === 0) { res.innerHTML = '<div class="card"><div class="result result-error">Žádná slova.</div></div>'; return; }
    const dlouha = slova.filter(s => s.length >= min);
    const nejdelsi = slova.reduce((a, b) => a.length >= b.length ? a : b);
    const prumer = (slova.reduce((a, b) => a + b.length, 0) / slova.length).toFixed(1);
    res.innerHTML = `
      <div class="stats-row">
        <div class="stat-card"><div class="stat-value">${slova.length}</div><div class="stat-label">Celkem slov</div></div>
        <div class="stat-card"><div class="stat-value">${dlouha.length}</div><div class="stat-label">Dlouhých (${min}+)</div></div>
        <div class="stat-card"><div class="stat-value">${prumer}</div><div class="stat-label">Prům. délka</div></div>
      </div>
      <div class="card">
        <div class="card-title">Výsledek — zobraz_slova()</div>
        <div class="code-output">${JSON.stringify(dlouha)}</div>
      </div>
      <div class="card">
        <div class="card-title">Všechna slova</div>
        <div style="margin-bottom:10px">
          ${slova.map(s =>
            `<span class="chip ${s.length >= min ? 'chip-orange' : 'chip-dim'}">${s} <small style="opacity:.5">(${s.length})</small></span>`
          ).join('')}
        </div>
        <div style="font-size:11px;color:var(--text-muted)">
          Nejdelší: <strong style="color:var(--orange)">${nejdelsi}</strong> — ${nejdelsi.length} znaků
        </div>
      </div>`;
  }

  document.getElementById('t12-words').addEventListener('input', debounce(compute, 200));
  document.getElementById('t12-min').addEventListener('input', compute);
  compute();
}
