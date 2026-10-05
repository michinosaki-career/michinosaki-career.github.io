// 無料枠の残り表示。slots.json（毎朝、フォームの申込数から更新）を読んで、バッジの文言を差し替える。
// 読み込みに失敗したときは、HTMLに書いてある文言のまま表示する。
(function () {
  fetch('slots.json', { cache: 'no-cache' })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) {
      if (!d || typeof d.limit !== 'number' || typeof d.used !== 'number') return;
      var left = Math.max(0, d.limit - d.used);
      var text = left > 0
        ? 'サービス改善期間｜無料受付中・残り' + left + '名（先着' + d.limit + '名）'
        : 'サービス改善期間｜無料枠は満員になりました';
      document.querySelectorAll('.offer-badge').forEach(function (el) {
        var dot = el.querySelector('span');
        el.textContent = '';
        if (dot) el.appendChild(dot);
        el.appendChild(document.createTextNode(text));
      });
    })
    .catch(function () {});
})();
