'use strict';

function renderJson(el) {
  const DEFAULT_JSON = JSON.stringify([
    { id: 1, jmeno: 'Marek', barva: ['červená', 'zelená'] },
    { id: 2, jmeno: 'Bob',   barva: ['růžová',  'žlutá']  },
  ], null, 2);

  el.innerHTML = `
    ${taskHeader(14)}
    <div class="card card-accent">
      <div class="row" style="align-items:flex-start">
        <div class="form-group" style="flex:3">
          <label class="form-label">JSON data (uprav nebo vlož vlastní)</label>
          <textarea id="t14-json" class="data-textarea" rows="10" style="font-family:'Courier New',monospace">${DEFAULT_JSON}</textarea>
        </div>
        <div class="form-group" style="flex:1;min-width:120px">
          <label class="form-label">Hledaný klíč</label>
          <input type="text" id="t14-key" class="form-input" value="jmeno" placeholder="jmeno">
        </div>
      </div>
    </div>
    <div id="t14-res"></div>`;

  function hlJson(json) {
    return json
      .replace(/("([^"]+)")\s*:/g, '<span class="json-k">$1</span>:')
      .replace(/:\s*("([^"]+)")/g, ': <span class="json-s">$1</span>')
      .replace(/:\s*(\d+)/g, ': <span class="json-n">$1</span>');
  }

  function compute() {
    const raw = document.getElementById('t14-json').value;
    const key = document.getElementById('t14-key').value.trim();
    const res = document.getElementById('t14-res');
    let data;
    try {
      data = JSON.parse(raw);
    } catch (e) {
      res.innerHTML = `<div class="card"><div class="result result-error">Neplatný JSON: ${e.message}</div></div>`;
      return;
    }
    const arr = Array.isArray(data) ? data : [data];
    const values = arr.filter(d => typeof d === 'object' && d !== null && key in d).map(d => d[key]);
    res.innerHTML = `
      <div class="card">
        <div class="card-title">Nalezené hodnoty klíče "${key}" (${values.length})</div>
        <div class="code-output">[${values.map(v => JSON.stringify(v)).join(', ')}]</div>
        <div style="margin-top:10px">
          ${values.map(v => `<span class="chip chip-orange">${typeof v === 'object' ? JSON.stringify(v) : v}</span>`).join('')}
        </div>
      </div>
      <div class="card">
        <div class="card-title">JSON data (zvýrazněná syntaxe)</div>
        <div class="code-output">${hlJson(JSON.stringify(data, null, 2))}</div>
      </div>`;
  }

  document.getElementById('t14-json').addEventListener('input', debounce(compute, 300));
  document.getElementById('t14-key').addEventListener('input', debounce(compute, 200));
  compute();
}
