'use strict';

function renderSety(el) {
  const DEFAULT_S1 = '1, 2, 3, 4';
  const DEFAULT_S2 = '3, 4, 5, 6';
  let pokusy = 3;

  el.innerHTML = `
    ${taskHeader(3)}
    <div class="card card-accent">
      <div class="card-title">Vstupní data — sety</div>
      <div class="row">
        <div class="form-group">
          <label class="form-label">Set 1 (čísla oddělená čárkou)</label>
          <input type="text" id="t3-s1" class="form-input" value="${DEFAULT_S1}" placeholder="1, 2, 3, 4">
        </div>
        <div class="form-group">
          <label class="form-label">Set 2 (čísla oddělená čárkou)</label>
          <input type="text" id="t3-s2" class="form-input" value="${DEFAULT_S2}" placeholder="3, 4, 5, 6">
        </div>
      </div>
    </div>
    <div id="t3-set-result"></div>
    <div class="card">
      <div class="card-title">Úloha 3 — Ověření hesla &nbsp;<span style="font-weight:400;color:var(--text-dim)">(3 pokusy)</span></div>
      <div class="form-group">
        <label class="form-label">Heslo</label>
        <input type="password" id="t3-h" class="form-input" placeholder="zadej heslo">
      </div>
      <div style="display:flex;gap:10px;align-items:center;">
        <button class="btn btn-primary" id="t3-btn" onclick="t3Login()">Přihlásit</button>
        <span id="t3-att" style="font-size:11px;color:var(--text-muted)">Zbývá ${pokusy} pokusy</span>
      </div>
      <div id="t3-login-res"></div>
    </div>`;

  function computeSets() {
    const s1 = parseSetInput(document.getElementById('t3-s1').value);
    const s2 = parseSetInput(document.getElementById('t3-s2').value);
    const rozdil = new Set([...s1].filter(x => !s2.has(x)));
    const sjed   = new Set([...s1, ...s2]);
    document.getElementById('t3-set-result').innerHTML = `
      <div class="card">
        <div class="card-title">Úloha 1 — Rozdíl (Set 1 − Set 2)</div>
        <div class="code-output">Set 1: ${fmtSet(s1)}
Set 2: ${fmtSet(s2)}
Rozdíl: <span class="hl">${fmtSet(rozdil)}</span></div>
      </div>
      <div class="card">
        <div class="card-title">Úloha 2 — Sjednocení (Set 1 ∪ Set 2)</div>
        <div class="code-output">Sjednocení: <span class="hl">${fmtSet(sjed)}</span></div>
      </div>`;
  }

  document.getElementById('t3-s1').addEventListener('input', computeSets);
  document.getElementById('t3-s2').addEventListener('input', computeSets);
  computeSets();

  window.t3Login = function () {
    if (pokusy <= 0) return;
    const h = document.getElementById('t3-h').value;
    const res = document.getElementById('t3-login-res');
    if (h === 'tajne123') {
      res.innerHTML = '<div class="result result-success">✓ Heslo je správné! Jsi přihlášen/a.</div>';
      pokusy = 0;
      document.getElementById('t3-h').disabled = true;
      document.getElementById('t3-btn').disabled = true;
      document.getElementById('t3-att').textContent = '';
    } else {
      pokusy--;
      document.getElementById('t3-att').textContent = `Zbývá ${pokusy} pokusů`;
      res.innerHTML = pokusy > 0
        ? `<div class="result result-error">✗ Špatné heslo! Zbývá ${pokusy} pokus/pokusů.</div>`
        : '<div class="result result-error">✗ Vyčerpali jsi všechny pokusy!</div>';
      if (pokusy === 0) {
        document.getElementById('t3-h').disabled = true;
        document.getElementById('t3-btn').disabled = true;
      }
    }
  };
  document.getElementById('t3-h').addEventListener('keydown', e => { if (e.key === 'Enter') t3Login(); });
}
