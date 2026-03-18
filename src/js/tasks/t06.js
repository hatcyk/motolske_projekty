'use strict';

function renderBullsCows(el) {
  let tajne, pokusy, start, bezi, history;

  function gen() {
    const p = Math.floor(Math.random() * 9) + 1;
    const d = [0,1,2,3,4,5,6,7,8,9].filter(x => x !== p);
    for (let i = d.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i+1)); [d[i],d[j]]=[d[j],d[i]]; }
    return '' + p + d[0] + d[1] + d[2];
  }
  function vyhodnot(t, tip) {
    let b = 0, c = 0;
    for (let i = 0; i < 4; i++) { if (tip[i]===t[i]) b++; else if (t.includes(tip[i])) c++; }
    return { b, c };
  }
  function fmtT(s) { return s < 60 ? `${s}s` : `${Math.floor(s/60)}m ${s%60}s`; }
  function hodnoceni(p) {
    if (p <= 4) return 'úžasné! 🏆'; if (p <= 7) return 'průměrné'; if (p <= 10) return 'mohlo být lepší'; return 'zkus to příště';
  }
  function renderHistory() {
    const h = document.getElementById('bc-hist');
    if (!h) return;
    h.innerHTML = [...history].reverse().map((g, i) => `
      <div class="bc-guess-row">
        <span class="bc-guess-num">${g.tip}</span>
        <div class="bc-badges">
          <span class="badge badge-bull">🐂 ${g.b} bulls</span>
          <span class="badge badge-cow">🐄 ${g.c} cows</span>
        </div>
        <span class="bc-guess-idx">#${history.length - i}</span>
      </div>`).join('');
  }
  function startGame() {
    tajne = gen(); pokusy = 0; history = []; bezi = true; start = Date.now();
    if (window._timer) clearInterval(window._timer);
    window._timer = setInterval(() => {
      const t = document.getElementById('bc-timer');
      if (t) t.textContent = fmtT(Math.floor((Date.now() - start) / 1000));
    }, 1000);
    renderGame();
  }
  function renderGame() {
    el.innerHTML = `
      ${taskHeader(6)}
      <div class="card card-accent">
        <div class="bc-top">
          <span class="status-badge sb-orange" id="bc-att">Pokus #1</span>
          <div style="display:flex;gap:14px;align-items:center">
            <span style="font-size:12px;color:var(--text-muted)">⏱ <span id="bc-timer">0s</span></span>
            <button class="btn btn-ghost btn-sm" onclick="bcNew()">Nová hra</button>
          </div>
        </div>
        <div class="bc-input-row">
          <div class="form-group" style="flex:1">
            <input type="text" id="bc-in" class="form-input bc-big-input" maxlength="4" placeholder="· · · ·">
          </div>
          <button class="btn btn-primary" onclick="bcGuess()" style="margin-bottom:14px;height:44px">Hádat</button>
        </div>
        <div id="bc-res" style="min-height:4px"></div>
      </div>
      <div class="card" id="bc-hist-card" style="display:none">
        <div class="card-title">Historie tipů</div>
        <div id="bc-hist"></div>
      </div>`;
    document.getElementById('bc-in').addEventListener('keydown', e => { if (e.key === 'Enter') bcGuess(); });
    document.getElementById('bc-in').focus();
  }
  window.bcGuess = function () {
    if (!bezi) return;
    const inp = document.getElementById('bc-in');
    const tip = inp.value.trim(), res = document.getElementById('bc-res');
    if (tip.length !== 4) { res.innerHTML = '<div class="result result-error">Zadej přesně 4 číslice!</div>'; return; }
    if (!/^\d+$/.test(tip)) { res.innerHTML = '<div class="result result-error">Zadej pouze čísla!</div>'; return; }
    if (tip[0] === '0') { res.innerHTML = '<div class="result result-error">Číslo nesmí začínat nulou!</div>'; return; }
    if (new Set(tip).size !== 4) { res.innerHTML = '<div class="result result-error">Číslo nesmí obsahovat duplicity!</div>'; return; }
    pokusy++;
    const { b, c } = vyhodnot(tajne, tip);
    history.push({ tip, b, c });
    inp.value = '';
    const att = document.getElementById('bc-att');
    if (att) att.textContent = `Pokus #${pokusy + 1}`;
    const hCard = document.getElementById('bc-hist-card');
    if (hCard) hCard.style.display = 'block';
    if (b === 4) {
      bezi = false; clearInterval(window._timer); window._timer = null;
      const cas = fmtT(Math.floor((Date.now() - start) / 1000));
      res.innerHTML = `
        <div class="result result-success">
          🎉 Správně! Číslo bylo <strong>${tajne}</strong><br>
          Na <strong>${pokusy}</strong> ${pokusy===1?'pokus':'pokusů'} &nbsp;·&nbsp; ${hodnoceni(pokusy)} &nbsp;·&nbsp; ${cas}<br><br>
          <button class="btn btn-primary btn-sm" onclick="bcNew()">Hrát znovu</button>
        </div>`;
    } else {
      res.innerHTML = '';
      if (document.getElementById('bc-in')) document.getElementById('bc-in').focus();
    }
    renderHistory();
  };
  window.bcNew = function () { startGame(); };
  startGame();
}
