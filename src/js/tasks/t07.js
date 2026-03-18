'use strict';

function renderTicTacToe(el) {
  let plocha = Array(9).fill(''), hrac = 'O', bezi = true, vitezne = [];
  const kombs = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  function checkWin(p, h) { for (const k of kombs) if (k.every(i => p[i] === h)) return k; return null; }
  function renderGrid() {
    document.getElementById('ttt-g').innerHTML = plocha.map((v, i) => `
      <div class="ttt-cell ${v} ${v?'taken':''} ${vitezne.includes(i)?'winning':''}" onclick="tttClick(${i})">${v}</div>`).join('');
    const s = document.getElementById('ttt-s');
    if (!bezi) {
      s.innerHTML = vitezne.length
        ? `<span class="status-badge sb-win">🏆 Hráč ${hrac} vyhrál!</span>`
        : `<span class="status-badge sb-info">🤝 Remíza!</span>`;
    } else {
      const col = hrac === 'O' ? 'var(--orange)' : 'var(--blue)';
      s.innerHTML = `Na tahu: <strong style="color:${col}">${hrac}</strong>`;
    }
  }
  el.innerHTML = `
    ${taskHeader(7)}
    <div class="card card-accent">
      <div class="ttt-wrap">
        <div id="ttt-s" class="ttt-status"></div>
        <div id="ttt-g" class="ttt-grid"></div>
        <button class="btn btn-ghost" onclick="tttNew()" style="margin-top:14px">Nová hra</button>
      </div>
    </div>
    <div class="card">
      <div class="card-title">Pravidla</div>
      <p style="font-size:12.5px;color:var(--text-muted);line-height:1.75">
        Hráči střídavě umísťují <strong style="color:var(--orange)">O</strong> a <strong style="color:var(--blue)">X</strong> na plochu 3×3.<br>
        Vyhrává ten, kdo jako první obsadí celou řadu — horizontálně, vertikálně nebo diagonálně.
      </p>
    </div>`;
  window.tttClick = function (pos) {
    if (!bezi || plocha[pos]) return;
    plocha[pos] = hrac;
    const v = checkWin(plocha, hrac);
    if (v) { vitezne = v; bezi = false; }
    else if (plocha.every(c => c)) { bezi = false; }
    else { hrac = hrac === 'O' ? 'X' : 'O'; }
    renderGrid();
  };
  window.tttNew = function () {
    plocha = Array(9).fill(''); hrac = 'O'; bezi = true; vitezne = []; renderGrid();
  };
  renderGrid();
}
