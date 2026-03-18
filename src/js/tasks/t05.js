'use strict';

function renderKalkulacka(el) {
  let op = '+', tab = 'kalk', slova = [];
  el.innerHTML = `
    ${taskHeader(5)}
    <div class="card">
      <div class="tabs">
        <button class="tab active" onclick="t5Tab('kalk')">Kalkulačka</button>
        <button class="tab" onclick="t5Tab('ovoce')">Výběr ovoce</button>
        <button class="tab" onclick="t5Tab('slova')">Sbírání slov</button>
      </div>
      <div id="t5-c"></div>
    </div>`;

  function render() {
    const c = document.getElementById('t5-c');
    if (tab === 'kalk') {
      c.innerHTML = `
        <div class="op-buttons">
          ${['+','-','*','/'].map(o => `<button class="op-btn ${o===op?'selected':''}" onclick="t5Op('${o}')">${o}</button>`).join('')}
        </div>
        <div class="row">
          <div class="form-group">
            <label class="form-label">První číslo</label>
            <input type="number" id="t5-n1" class="form-input" placeholder="0" step="any">
          </div>
          <div class="form-group">
            <label class="form-label">Druhé číslo</label>
            <input type="number" id="t5-n2" class="form-input" placeholder="0" step="any">
          </div>
        </div>
        <button class="btn btn-primary" onclick="t5Calc()">Vypočítat</button>
        <div id="t5-r"></div>`;
    } else if (tab === 'ovoce') {
      c.innerHTML = `
        <p style="font-size:12px;color:var(--text-muted);margin-bottom:12px">Dostupné ovoce:</p>
        <div class="fruit-grid">
          ${['🍎 jablko','🍌 banán','🍋 citron','🍊 pomeranč'].map(o =>
            `<button class="fruit-btn" onclick="t5Ovoce('${o.replace(/.*\s/, '')}')">${o}</button>`
          ).join('')}
        </div>
        <div id="t5-r"></div>`;
    } else {
      const done = slova.length >= 3;
      c.innerHTML = `
        <p style="font-size:12px;color:var(--text-muted);margin-bottom:12px">
          Zadej 3 unikátní slova přesně se 4 znaky &nbsp;
          <span class="status-badge sb-info">${slova.length}/3</span>
        </p>
        <div style="margin-bottom:12px;min-height:26px">
          ${slova.map(s => `<span class="chip chip-orange">${s}</span>`).join('')}
        </div>
        ${done
          ? `<div class="result result-success">✓ Hotovo! Uložená slova: <strong>${slova.join(', ')}</strong></div>`
          : `<div class="row">
               <div class="form-group">
                 <input type="text" id="t5-s" class="form-input" maxlength="4" placeholder="4 znaky">
               </div>
               <button class="btn btn-primary btn-sm" onclick="t5AddSlovo()">Přidat</button>
             </div>
             <div id="t5-r"></div>`}`;
    }
  }

  window.t5Tab = function (t) {
    tab = t;
    document.querySelectorAll('#content .tab').forEach((b, i) =>
      b.classList.toggle('active', ['kalk', 'ovoce', 'slova'][i] === t));
    render();
  };
  window.t5Op = function (o) {
    op = o;
    document.querySelectorAll('.op-btn').forEach(b => b.classList.toggle('selected', b.textContent === o));
  };
  window.t5Calc = function () {
    const n1 = parseFloat(document.getElementById('t5-n1').value);
    const n2 = parseFloat(document.getElementById('t5-n2').value);
    const res = document.getElementById('t5-r');
    if (isNaN(n1) || isNaN(n2)) { res.innerHTML = '<div class="result result-error">Zadej platná čísla!</div>'; return; }
    let v;
    if (op === '+') v = n1 + n2; else if (op === '-') v = n1 - n2;
    else if (op === '*') v = n1 * n2;
    else { if (n2 === 0) { res.innerHTML = '<div class="result result-error">Dělení nulou!</div>'; return; } v = n1 / n2; }
    res.innerHTML = `<div class="result result-success">${n1} ${op} ${n2} = <strong>${v}</strong></div>`;
  };
  window.t5Ovoce = function (o) {
    document.getElementById('t5-r').innerHTML = `<div class="result result-success">✓ Vybral/a sis „${o}".</div>`;
  };
  window.t5AddSlovo = function () {
    const inp = document.getElementById('t5-s');
    const s = inp.value.trim();
    const res = document.getElementById('t5-r');
    if (s.length !== 4) { res.innerHTML = `<div class="result result-error">✗ Slovo „${s}" nemá 4 znaky (má ${s.length})!</div>`; return; }
    if (slova.includes(s)) { res.innerHTML = `<div class="result result-error">✗ Slovo „${s}" už je uložené!</div>`; return; }
    slova.push(s); render();
  };
  render();
}
