'use strict';

function renderOS(el) {
  const platform = process.platform;
  const isWin = platform === 'win32';
  const names = { win32: 'Windows', darwin: 'macOS', linux: 'Linux' };
  const icons = { win32: '🪟', darwin: '🍎', linux: '🐧' };
  el.innerHTML = `
    ${taskHeader(9)}
    <div class="card card-accent" style="text-align:center;padding:40px 24px">
      <div style="font-size:72px;margin-bottom:16px;line-height:1">${icons[platform] || '💻'}</div>
      <div style="font-size:24px;font-weight:800;margin-bottom:8px">${names[platform] || platform}</div>
      <div style="font-family:'Courier New',monospace;font-size:12px;color:var(--text-muted);margin-bottom:24px">
        process.platform = <span style="color:var(--orange)">"${platform}"</span>
      </div>
      <div class="result ${isWin ? 'result-success' : 'result-info'}" style="display:inline-block;margin:0;font-family:'Courier New',monospace">
        je_os_windows() → <strong>${isWin}</strong>
      </div>
    </div>`;
}
