'use strict';

function parseSeq(str) {
  return str.split(',').map(s => s.trim()).filter(s => s !== '').map(Number).filter(n => !isNaN(n));
}
function parseWords(str) {
  return str.split(/[\s\n\r,]+/).map(w => w.trim()).filter(w => w.length > 0);
}
function parseSetInput(str) {
  return new Set(str.split(',').map(s => s.trim()).filter(s => s !== '').map(Number).filter(n => !isNaN(n)));
}
function fmtSet(s) {
  return '{' + [...s].sort((a, b) => a - b).join(', ') + '}';
}
function debounce(fn, ms = 300) {
  let t; return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), ms); };
}
