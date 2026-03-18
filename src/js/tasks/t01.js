'use strict';

function renderTrojuhelnik(el) {
  el.innerHTML = `
    ${taskHeader(1)}
    <div class="card card-accent">
      <div class="card-title">Vstupní hodnoty</div>
      <div class="row">
        <div class="form-group">
          <label class="form-label">Základna</label>
          <input type="number" id="t1-z" class="form-input" placeholder="např. 10" step="any">
        </div>
        <div class="form-group">
          <label class="form-label">Výška</label>
          <input type="number" id="t1-v" class="form-input" placeholder="např. 5" step="any">
        </div>
      </div>
      <button class="btn btn-primary" onclick="t1Calc()">Vypočítat plochu</button>
      <div id="t1-result"></div>
    </div>
    <div class="card">
      <div class="card-title">Vzorec</div>
      <div class="code-output">P = (základna × výška) / 2</div>
    </div>`;
  window.t1Calc = function () {
    const z = parseFloat(document.getElementById('t1-z').value);
    const v = parseFloat(document.getElementById('t1-v').value);
    const res = document.getElementById('t1-result');
    if (isNaN(z) || isNaN(v)) { res.innerHTML = '<div class="result result-error">Zadej platné číslo!</div>'; return; }
    res.innerHTML = `<div class="result result-success">Plocha trojúhelníku = (${z} × ${v}) / 2 = <strong>${(z * v) / 2}</strong></div>`;
  };
  document.getElementById('t1-v').addEventListener('keydown', e => { if (e.key === 'Enter') t1Calc(); });
}
