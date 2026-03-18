'use strict';

function renderEmaily(el) {
  const DEFAULT = `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vulputate lacus id eros consequat tempus. Nam viverra velit sit amet lorem lobortis, at tincidunt nunc ultricies. Duis facilisis ultrices lacus, id tiger123@email.cz auctor massa molestie at. Nunc tristique fringilla congue. Donec ante diam cnn@info.com, dapibus lacinia vulputate vitae, ullamcorper in justo. Maecenas massa purus, ultricies a dictum ut, dapibus vitae massa. Cras abc@gmail.com vel libero felis. In augue elit, porttitor nec molestie quis, auctor a quam. Quisque b2b@money.fr pretium dolor et tempor feugiat. Morbi libero lectus, porttitor eu mi sed, luctus lacinia risus. Maecenas posuere leo sit amet spam@info.cz. elit tincidunt maximus.`;
  const re = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;

  el.innerHTML = `
    ${taskHeader(10)}
    <div class="card card-accent">
      <div class="card-title">Vstupní text (vlož libovolný text s emaily)</div>
      <textarea id="t10-txt" class="data-textarea" rows="6">${DEFAULT}</textarea>
    </div>
    <div id="t10-res"></div>`;

  function compute() {
    const txt = document.getElementById('t10-txt').value;
    const emails = txt.match(re) || [];
    const hl = txt.replace(re, m => `<span class="email-hl">${m}</span>`);
    document.getElementById('t10-res').innerHTML = `
      <div class="card">
        <div class="card-title">Nalezeno ${emails.length} emailových adres</div>
        <div style="margin-bottom:12px">${emails.map(e => `<span class="chip chip-orange">${e}</span>`).join('')}</div>
        <div class="code-output">[${emails.map(e => `'${e}'`).join(', ')}]</div>
      </div>
      <div class="card">
        <div class="card-title">Text se zvýrazněnými emaily</div>
        <div class="email-text">${hl || '<em style="color:var(--text-dim)">Žádný text.</em>'}</div>
      </div>`;
  }

  document.getElementById('t10-txt').addEventListener('input', debounce(compute, 200));
  compute();
}
