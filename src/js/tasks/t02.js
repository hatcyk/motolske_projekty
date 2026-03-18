'use strict';

function renderPismenoDne(el) {
  const tyden = ['pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle'];
  el.innerHTML = `
    ${taskHeader(2)}
    <div class="card card-accent">
      <div class="form-group">
        <label class="form-label">Den v týdnu</label>
        <select id="t2-den" class="form-input">
          <option value="">— Vyber den —</option>
          ${tyden.map((d, i) => `<option value="${i}">${i + 1} – ${d}</option>`).join('')}
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Zadej první písmeno vybraného dne</label>
        <input type="text" id="t2-p" class="form-input" maxlength="1" placeholder="jedno písmeno">
      </div>
      <button class="btn btn-primary" onclick="t2Check()">Zkontrolovat</button>
      <div id="t2-result"></div>
    </div>`;
  window.t2Check = function () {
    const idx = document.getElementById('t2-den').value;
    const p = document.getElementById('t2-p').value.trim();
    const res = document.getElementById('t2-result');
    if (idx === '') { res.innerHTML = '<div class="result result-error">Vyber nejprve den!</div>'; return; }
    if (!p) { res.innerHTML = '<div class="result result-error">Zadej písmeno!</div>'; return; }
    const den = tyden[parseInt(idx)], ok = den[0];
    res.innerHTML = p === ok
      ? `<div class="result result-success">✓ Správně! „${ok}" je první písmeno dne <strong>${den}</strong>.</div>`
      : `<div class="result result-error">✗ Špatně! Správné písmeno je „${ok}", ty jsi zadal „${p}".</div>`;
  };
  document.getElementById('t2-p').addEventListener('keydown', e => { if (e.key === 'Enter') t2Check(); });
}
