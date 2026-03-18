'use strict';

function renderPrumer(el) {
  const DEFAULT = '35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30';

  el.innerHTML = `
    ${taskHeader(8)}
    <div class="card card-accent">
      <div class="card-title">Vstupní sekvence (čísla oddělená čárkou)</div>
      <input type="text" id="t8-seq" class="form-input" value="${DEFAULT}" style="font-family:'Courier New',monospace">
    </div>
    <div id="t8-res"></div>`;

  function compute() {
    const seq = parseSeq(document.getElementById('t8-seq').value);
    const res = document.getElementById('t8-res');
    if (seq.length === 0) { res.innerHTML = '<div class="card"><div class="result result-error">Žádná platná čísla.</div></div>'; return; }
    const suma = seq.reduce((a, b) => a + b, 0);
    const prumer = suma / seq.length;
    const min = Math.min(...seq), max = Math.max(...seq);
    res.innerHTML = `
      <div class="stats-row">
        <div class="stat-card"><div class="stat-value">${seq.length}</div><div class="stat-label">Počet čísel</div></div>
        <div class="stat-card"><div class="stat-value">${suma}</div><div class="stat-label">Součet</div></div>
        <div class="stat-card"><div class="stat-value">${prumer.toFixed(4)}</div><div class="stat-label">Průměr</div></div>
      </div>
      <div class="card">
        <div class="card-title">Výsledek</div>
        <div class="code-output">spocitej_prumer([${seq.join(', ')}])

→ <span class="hl">${prumer}</span>

min: ${min} &nbsp;·&nbsp; max: ${max} &nbsp;·&nbsp; rozsah: ${max - min}</div>
      </div>`;
  }

  document.getElementById('t8-seq').addEventListener('input', compute);
  compute();
}
