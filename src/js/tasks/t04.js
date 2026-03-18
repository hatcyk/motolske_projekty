'use strict';

function renderData(el) {
  const DEFAULT_SEQ = '1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2';
  const DEFAULT_VET = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu';
  const SAMS = 'aeiouyáěíóů';
  let tab = 1;

  function computeSeq(str) {
    const seq = parseSeq(str);
    if (seq.length === 0) return '<div class="result result-error">Žádná platná čísla.</div>';
    const counts = {};
    for (const n of seq) counts[n] = (counts[n] || 0) + 1;
    const sorted = Object.entries(counts).sort(([a], [b]) => Number(a) - Number(b));
    return `
      <div style="font-size:11px;color:var(--text-muted);margin-bottom:10px;font-family:'Courier New',monospace">[${seq.join(', ')}]</div>
      <table class="data-table">
        <thead><tr><th>Číslo</th><th>Výskytů</th><th>Graf</th></tr></thead>
        <tbody>${sorted.map(([k, v]) => `
          <tr><td><code>${k}</code></td><td><strong>${v}×</strong></td>
          <td><div style="width:${Math.min(v * 22, 160)}px;height:6px;background:var(--orange);border-radius:3px;"></div></td></tr>`
        ).join('')}</tbody>
      </table>`;
  }

  function computeVeta(str) {
    if (!str.trim()) return '<div class="result result-error">Zadej text.</div>';
    let sam = 0, souh = 0;
    for (const z of str.toLowerCase()) {
      if (!/[a-záčďéěíňóřšťúůýž]/i.test(z)) continue;
      SAMS.includes(z) ? sam++ : souh++;
    }
    const tot = sam + souh;
    return `<div class="code-output">Souhlásky: <span class="hl">${souh}</span>  (${tot ? (souh/tot*100).toFixed(1) : 0} %)
Samohlásky: <span class="ok">${sam}</span>  (${tot ? (sam/tot*100).toFixed(1) : 0} %)
Celkem písmen: ${tot}</div>`;
  }

  function renderTab() {
    const c = document.getElementById('t4-c');
    if (tab === 1) {
      c.innerHTML = `
        <div class="form-group">
          <label class="form-label">Vstupní seznam (čísla oddělená čárkou)</label>
          <input type="text" id="t4-seq" class="form-input" value="${DEFAULT_SEQ}">
        </div>
        <div id="t4-seq-res"></div>`;
      const compute = () => document.getElementById('t4-seq-res').innerHTML = computeSeq(document.getElementById('t4-seq').value);
      document.getElementById('t4-seq').addEventListener('input', compute);
      compute();
    } else {
      c.innerHTML = `
        <div class="form-group">
          <label class="form-label">Vstupní text</label>
          <textarea id="t4-vet" class="data-textarea" rows="3">${DEFAULT_VET}</textarea>
        </div>
        <div id="t4-vet-res"></div>`;
      const compute = () => document.getElementById('t4-vet-res').innerHTML = computeVeta(document.getElementById('t4-vet').value);
      document.getElementById('t4-vet').addEventListener('input', compute);
      compute();
    }
  }

  el.innerHTML = `
    ${taskHeader(4)}
    <div class="card">
      <div class="tabs">
        <button class="tab active" id="t4-t1" onclick="t4Tab(1)">Výskyty v seznamu</button>
        <button class="tab" id="t4-t2" onclick="t4Tab(2)">Samohlásky &amp; souhlásky</button>
      </div>
      <div id="t4-c"></div>
    </div>`;
  window.t4Tab = function (n) {
    tab = n;
    document.getElementById('t4-t1').classList.toggle('active', n === 1);
    document.getElementById('t4-t2').classList.toggle('active', n === 2);
    renderTab();
  };
  renderTab();
}
