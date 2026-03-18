'use strict';

function renderCsv(el) {
  const DEFAULT = `10,a1,1\n12,a2,3\n14,a3,5\n16,a4,7\n18,a5,9`;

  el.innerHTML = `
    ${taskHeader(13)}
    <div class="card card-accent">
      <div class="card-title">CSV data (uprav nebo vlož vlastní)</div>
      <textarea id="t13-csv" class="data-textarea" rows="8" style="font-family:'Courier New',monospace">${DEFAULT}</textarea>
    </div>
    <div id="t13-res"></div>`;

  function compute() {
    const raw = document.getElementById('t13-csv').value.trim();
    const res = document.getElementById('t13-res');
    if (!raw) { res.innerHTML = '<div class="card"><div class="result result-error">Žádná data.</div></div>'; return; }
    const rows = raw.split('\n').filter(r => r.trim()).map(r => r.split(',').map(c => c.trim()));
    const cols = Math.max(...rows.map(r => r.length));
    res.innerHTML = `
      <div class="card">
        <div class="card-title">Tabulka (${rows.length} řádků, ${cols} sloupců)</div>
        <table class="data-table">
          <thead><tr>${Array.from({length:cols},(_,i)=>`<th>Sloupec ${i+1}</th>`).join('')}</tr></thead>
          <tbody>${rows.map(r =>
            `<tr>${Array.from({length:cols},(_,i)=>`<td>${r[i]??''}</td>`).join('')}</tr>`
          ).join('')}</tbody>
        </table>
      </div>
      <div class="card">
        <div class="card-title">Raw CSV výstup</div>
        <div class="code-output">${raw}</div>
      </div>`;
  }

  document.getElementById('t13-csv').addEventListener('input', debounce(compute, 200));
  compute();
}
