// ミチノサキ アクセス計測（GA4）。計測IDはここ1か所だけ。
// 流入元はURLのutm_source／utm_medium／utm_campaignをGA4が自動で読む。
(function () {
  var MEASUREMENT_ID = 'G-3S63V58CRV'; // GA4の測定ID（ミチノサキ公式サイト）
  if (MEASUREMENT_ID === 'G-XXXXXXXXXX' || !/^G-[A-Z0-9]{8,}$/.test(MEASUREMENT_ID)) return; // 未設定の間は何も送らない
  if (window.__michinosakiGa) return; // 二重読み込み防止
  window.__michinosakiGa = true;

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  gtag('js', new Date());
  gtag('config', MEASUREMENT_ID);

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + MEASUREMENT_ID;
  document.head.appendChild(s);

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var name = null;
    if (href.indexOf('lin.ee/') !== -1) name = 'line_click';
    else if (href.indexOf('mailto:') === 0) name = 'mail_click';
    if (!name) return;
    var place = a.closest('footer') ? 'footer' : a.closest('.mobile-cta') ? 'sticky' : 'body';
    gtag('event', name, { link_location: place, page_path: location.pathname });
  });
})();
