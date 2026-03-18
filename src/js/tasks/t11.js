'use strict';

function renderFormatovani(el) {
  el.innerHTML = `
    ${taskHeader(11)}
    <div class="card card-accent">
      <div class="card-title">Vstupní hodnoty</div>
      <div class="row">
        <div class="form-group">
          <label class="form-label">Číslo — kombinace s $</label>
          <input type="number" id="t11-komb" class="form-input" value="1.234" step="any">
        </div>
        <div class="form-group">
          <label class="form-label">String — oříznutí</label>
          <input type="text" id="t11-str" class="form-input" value="Hello">
        </div>
      </div>
      <div class="row">
        <div class="form-group">
          <label class="form-label">Číslo — přesnost (2e | 1f | 2f)</label>
          <input type="number" id="t11-cislo" class="form-input" value="123.4567" step="any">
        </div>
        <div class="form-group">
          <label class="form-label">Max znaků pro oříznutí</label>
          <input type="number" id="t11-max" class="form-input" value="4" min="0" max="100">
        </div>
      </div>
    </div>
    <div id="t11-res"></div>`;

  function compute() {
    const komb  = parseFloat(document.getElementById('t11-komb').value);
    const str   = document.getElementById('t11-str').value;
    const cislo = parseFloat(document.getElementById('t11-cislo').value);
    const max   = parseInt(document.getElementById('t11-max').value) || 0;
    const res   = document.getElementById('t11-res');
    if (isNaN(komb) || isNaN(cislo)) { res.innerHTML = '<div class="card"><div class="result result-error">Zadej platná čísla.</div></div>'; return; }
    const fP = `|${cislo.toExponential(2)}|${cislo.toFixed(1)}|${cislo.toFixed(2)}|`;
    const fK = `|${komb}$|`;
    const fS = `|${str.slice(0, max)}|`;
    res.innerHTML = `
      <div class="card">
        <div class="card-title">Výsledky formátování</div>
        <table class="data-table">
          <thead><tr><th>Typ</th><th>Vstup</th><th>Výstup</th></tr></thead>
          <tbody>
            <tr><td>Přesnost (2e | 1f | 2f)</td><td><code>${cislo}</code></td><td><code>${fP}</code></td></tr>
            <tr><td>Kombinace s $</td><td><code>${komb}</code></td><td><code>${fK}</code></td></tr>
            <tr><td>Oříznutí (max ${max})</td><td><code>${str}</code></td><td><code>${fS}</code></td></tr>
          </tbody>
        </table>
      </div>
      <div class="card">
        <div class="card-title">Obsah souboru vysledek.txt</div>
        <div class="code-output">${fP}
${fK}
${fS}</div>
      </div>`;
  }

  ['t11-komb','t11-str','t11-cislo','t11-max'].forEach(id => {
    document.getElementById(id).addEventListener('input', compute);
  });
  compute();
}
