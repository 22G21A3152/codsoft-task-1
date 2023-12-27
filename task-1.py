<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>Movie_Rating_Prediction_With_Python_Task2_CodSoft</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Movie_Rating_Prediction_With_Python">Movie_Rating_Prediction_With_Python<a class="anchor-link" href="#Movie_Rating_Prediction_With_Python">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Importing-Libraries">Importing Libraries<a class="anchor-link" href="#Importing-Libraries">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="k">import</span> <span class="n">train_test_split</span>
<span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="k">import</span> <span class="n">mean_absolute_error</span><span class="p">,</span> <span class="n">mean_squared_error</span><span class="p">,</span> <span class="n">r2_score</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="k">import</span> <span class="n">SGDRegressor</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="k">import</span> <span class="n">StandardScaler</span>
<span class="kn">from</span> <span class="nn">sklearn.pipeline</span> <span class="k">import</span> <span class="n">Pipeline</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;E:\DATA SCIENCE(GRASS)\DATA SCIENCE-Projects\IMDb Movies India.csv\IMDb Movies India.csv&quot;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;ISO-8859-1&#39;</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[4]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Year</th>
      <th>Duration</th>
      <th>Genre</th>
      <th>Rating</th>
      <th>Votes</th>
      <th>Director</th>
      <th>Actor 1</th>
      <th>Actor 2</th>
      <th>Actor 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Drama</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>J.S. Randhawa</td>
      <td>Manmauji</td>
      <td>Birbal</td>
      <td>Rajendra Bhatia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>#Gadhvi (He thought he was Gandhi)</td>
      <td>(2019)</td>
      <td>109 min</td>
      <td>Drama</td>
      <td>7.0</td>
      <td>8</td>
      <td>Gaurav Bakshi</td>
      <td>Rasika Dugal</td>
      <td>Vivek Ghamande</td>
      <td>Arvind Jangid</td>
    </tr>
    <tr>
      <th>2</th>
      <td>#Homecoming</td>
      <td>(2021)</td>
      <td>90 min</td>
      <td>Drama, Musical</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Soumyajit Majumdar</td>
      <td>Sayani Gupta</td>
      <td>Plabita Borthakur</td>
      <td>Roy Angana</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#Yaaram</td>
      <td>(2019)</td>
      <td>110 min</td>
      <td>Comedy, Romance</td>
      <td>4.4</td>
      <td>35</td>
      <td>Ovais Khan</td>
      <td>Prateik</td>
      <td>Ishita Raj</td>
      <td>Siddhant Kapoor</td>
    </tr>
    <tr>
      <th>4</th>
      <td>...And Once Again</td>
      <td>(2010)</td>
      <td>105 min</td>
      <td>Drama</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Amol Palekar</td>
      <td>Rajat Kapoor</td>
      <td>Rituparna Sengupta</td>
      <td>Antara Mali</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Data-Preprocessing:">Data Preprocessing:<a class="anchor-link" href="#Data-Preprocessing:">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">dataoverview</span> <span class="p">(</span><span class="n">df</span><span class="p">,</span><span class="n">message</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="s1">&#39;</span><span class="si">{message}</span><span class="s1">:</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Rows:&quot;</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Number of features:&quot;</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Features:&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">tolist</span><span class="p">())</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Missing values:&quot;</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="o">.</span><span class="n">sum</span><span class="p">())</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Unique values:&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">nunique</span><span class="p">())</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataoverview</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="s1">&#39;Overview of the training dataset&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Overview of the training dataset:

Rows: 15509

Number of features: 10

Features:
[&#39;Name&#39;, &#39;Year&#39;, &#39;Duration&#39;, &#39;Genre&#39;, &#39;Rating&#39;, &#39;Votes&#39;, &#39;Director&#39;, &#39;Actor 1&#39;, &#39;Actor 2&#39;, &#39;Actor 3&#39;]

Missing values: 33523

Unique values:
Name        13838
Year          102
Duration      182
Genre         485
Rating         84
Votes        2034
Director     5938
Actor 1      4718
Actor 2      4891
Actor 3      4820
dtype: int64
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[10]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Name           0
Year         528
Duration    8269
Genre       1877
Rating      7590
Votes       7589
Director     525
Actor 1     1617
Actor 2     2384
Actor 3     3144
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 15509 entries, 0 to 15508
Data columns (total 10 columns):
Name        15509 non-null object
Year        14981 non-null object
Duration    7240 non-null object
Genre       13632 non-null object
Rating      7919 non-null float64
Votes       7920 non-null object
Director    14984 non-null object
Actor 1     13892 non-null object
Actor 2     13125 non-null object
Actor 3     12365 non-null object
dtypes: float64(1), object(9)
memory usage: 666.4+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#genre, director, and actors values counts</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Genre&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[12]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Drama                           2780
Action                          1289
Thriller                         779
Romance                          708
Drama, Romance                   524
Comedy                           495
Action, Crime, Drama             455
Drama, Family                    418
Horror                           322
Action, Drama                    316
Documentary                      283
Comedy, Drama                    264
Comedy, Drama, Romance           224
Fantasy                          170
Action, Comedy, Drama            149
Action, Thriller                 142
Comedy, Romance                  140
Action, Drama, Romance           134
Family                           112
Drama, Musical, Romance          108
Action, Comedy, Crime             95
Drama, Thriller                   94
Mystery                           92
Crime                             91
Comedy, Drama, Family             82
Crime, Drama                      81
Action, Drama, Thriller           81
Animation                         74
Crime, Drama, Thriller            72
Action, Adventure, Drama          69
                                ... 
Adventure, Romance, Thriller       1
Drama, Action, Family              1
Action, Fantasy, Musical           1
Comedy, Crime, Horror              1
Comedy, Drama, Sci-Fi              1
Romance, Action, Crime             1
Action, Crime, War                 1
Action, Crime, Horror              1
History, Musical, Romance          1
Mystery, Musical, Romance          1
Comedy, Horror, Thriller           1
Comedy, History                    1
Fantasy, Sci-Fi                    1
History, Romance                   1
Drama, Family, Horror              1
Drama, Crime, Family               1
Documentary, Sport                 1
Horror, Drama, Mystery             1
Action, Crime, Fantasy             1
Fantasy, Mystery, Romance          1
Crime, Fantasy, Mystery            1
Biography, History, War            1
Crime, Musical, Romance            1
Horror, Musical                    1
Action, Family, Thriller           1
Drama, Family, Adventure           1
Action, Romance, Western           1
Drama, Action, Musical             1
Adventure, Horror                  1
Action, Drama, Western             1
Name: Genre, Length: 485, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Director&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Jayant Desai               58
Kanti Shah                 57
Babubhai Mistry            50
Mahesh Bhatt               48
Master Bhagwan             47
Dhirubhai Desai            46
Nanabhai Bhatt             46
David Dhawan               44
Mohammed Hussain           44
B.R. Ishara                44
Hrishikesh Mukherjee       42
Ram Gopal Varma            39
Shakti Samanta             39
Basu Chatterjee            36
Rama Rao Tatineni          36
Shibu Mitra                36
Kedar Kapoor               35
Raj N. Sippy               34
K. Raghavendra Rao         34
Vikram Bhatt               33
Kishan Shah                33
Phani Majumdar             32
Priyadarshan               32
K. Bapaiah                 32
Dwarka Khosla              32
Jagatrai Pesumal Advani    32
Aspi Irani                 32
Mohan Sinha                32
Nanubhai Vakil             32
Abdul Rashid Kardar        31
                           ..
Ganpati Bohra               1
S.N. Azhar                  1
Anita Udeep                 1
Narugopal Mandal            1
Ram Kumar                   1
Sadiq Nizami                1
Satish Shah                 1
Spencer Mathew              1
Sakthi Chidambaram          1
Victor Mukherjee            1
M.D. Baig                   1
Gauravv K. Chawla           1
Rajkannu                    1
Nandamuri Balakrishna       1
Ashwin Rai Shetty           1
Neville Shah                1
Prasenjit Chatterjee        1
Prashant Sehgal             1
Lakshmi Musari              1
Premji                      1
Pradeep R. Sharma           1
Jai Tank                    1
Shashikant Doiphode         1
Ravi Khanna                 1
Prabhuraj                   1
K. Kant                     1
S. Rai                      1
Poonam Balan                1
B.N. Chowhan                1
Jehangir Surti              1
Name: Director, Length: 5938, dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[14]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Year</th>
      <th>Duration</th>
      <th>Genre</th>
      <th>Rating</th>
      <th>Votes</th>
      <th>Director</th>
      <th>Actor 1</th>
      <th>Actor 2</th>
      <th>Actor 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Drama</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>J.S. Randhawa</td>
      <td>Manmauji</td>
      <td>Birbal</td>
      <td>Rajendra Bhatia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>#Gadhvi (He thought he was Gandhi)</td>
      <td>(2019)</td>
      <td>109 min</td>
      <td>Drama</td>
      <td>7.0</td>
      <td>8</td>
      <td>Gaurav Bakshi</td>
      <td>Rasika Dugal</td>
      <td>Vivek Ghamande</td>
      <td>Arvind Jangid</td>
    </tr>
    <tr>
      <th>2</th>
      <td>#Homecoming</td>
      <td>(2021)</td>
      <td>90 min</td>
      <td>Drama, Musical</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Soumyajit Majumdar</td>
      <td>Sayani Gupta</td>
      <td>Plabita Borthakur</td>
      <td>Roy Angana</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#Yaaram</td>
      <td>(2019)</td>
      <td>110 min</td>
      <td>Comedy, Romance</td>
      <td>4.4</td>
      <td>35</td>
      <td>Ovais Khan</td>
      <td>Prateik</td>
      <td>Ishita Raj</td>
      <td>Siddhant Kapoor</td>
    </tr>
    <tr>
      <th>4</th>
      <td>...And Once Again</td>
      <td>(2010)</td>
      <td>105 min</td>
      <td>Drama</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Amol Palekar</td>
      <td>Rajat Kapoor</td>
      <td>Rituparna Sengupta</td>
      <td>Antara Mali</td>
    </tr>
    <tr>
      <th>5</th>
      <td>...Aur Pyaar Ho Gaya</td>
      <td>(1997)</td>
      <td>147 min</td>
      <td>Comedy, Drama, Musical</td>
      <td>4.7</td>
      <td>827</td>
      <td>Rahul Rawail</td>
      <td>Bobby Deol</td>
      <td>Aishwarya Rai Bachchan</td>
      <td>Shammi Kapoor</td>
    </tr>
    <tr>
      <th>6</th>
      <td>...Yahaan</td>
      <td>(2005)</td>
      <td>142 min</td>
      <td>Drama, Romance, War</td>
      <td>7.4</td>
      <td>1,086</td>
      <td>Shoojit Sircar</td>
      <td>Jimmy Sheirgill</td>
      <td>Minissha Lamba</td>
      <td>Yashpal Sharma</td>
    </tr>
    <tr>
      <th>7</th>
      <td>.in for Motion</td>
      <td>(2008)</td>
      <td>59 min</td>
      <td>Documentary</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Anirban Datta</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>?: A Question Mark</td>
      <td>(2012)</td>
      <td>82 min</td>
      <td>Horror, Mystery, Thriller</td>
      <td>5.6</td>
      <td>326</td>
      <td>Allyson Patel</td>
      <td>Yash Dave</td>
      <td>Muntazir Ahmad</td>
      <td>Kiran Bhatia</td>
    </tr>
    <tr>
      <th>9</th>
      <td>@Andheri</td>
      <td>(2014)</td>
      <td>116 min</td>
      <td>Action, Crime, Thriller</td>
      <td>4.0</td>
      <td>11</td>
      <td>Biju Bhaskar Nair</td>
      <td>Augustine</td>
      <td>Fathima Babu</td>
      <td>Byon</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># As we are going to predict movie ratings based on fdf.dropna(subset=[&#39;Name&#39;,&#39;Year&#39;,&#39;Duration&#39;,&#39;Votes&#39;,&#39;Rating&#39;],inplace=True)eatures, we need to remove null values from features that can directly influence the results.</span>
<span class="n">df</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">subset</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span><span class="s1">&#39;Year&#39;</span><span class="p">,</span><span class="s1">&#39;Duration&#39;</span><span class="p">,</span><span class="s1">&#39;Votes&#39;</span><span class="p">,</span><span class="s1">&#39;Rating&#39;</span><span class="p">],</span><span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[15]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Name          0
Year          0
Duration      0
Genre        31
Rating        0
Votes         0
Director      1
Actor 1      75
Actor 2     117
Actor 3     163
dtype: int64</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Remove parentheses from &#39;Year&#39; column and convert to integer</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Year&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Year&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">&#39;()&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Remove commas from &#39;Votes&#39; column and convert to integer</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Votes&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Votes&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Remove min from &#39;Duration&#39; column andDurationonvert to integer</span>
<span class="n">df</span><span class="p">[</span><span class="s1">&#39;Duration&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Duration&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;min&#39;</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
Int64Index: 5851 entries, 1 to 15508
Data columns (total 10 columns):
Name        5851 non-null object
Year        5851 non-null int32
Duration    5851 non-null int32
Genre       5820 non-null object
Rating      5851 non-null float64
Votes       5851 non-null int32
Director    5850 non-null object
Actor 1     5776 non-null object
Actor 2     5734 non-null object
Actor 3     5688 non-null object
dtypes: float64(1), int32(3), object(6)
memory usage: 297.1+ KB
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Duration</th>
      <th>Rating</th>
      <th>Votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5851.000000</td>
      <td>5851.000000</td>
      <td>5851.000000</td>
      <td>5851.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1996.416852</td>
      <td>132.294480</td>
      <td>5.931875</td>
      <td>2611.273116</td>
    </tr>
    <tr>
      <th>std</th>
      <td>19.914640</td>
      <td>26.555826</td>
      <td>1.389942</td>
      <td>13433.828528</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1931.000000</td>
      <td>21.000000</td>
      <td>1.100000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1983.000000</td>
      <td>117.000000</td>
      <td>5.000000</td>
      <td>28.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2002.000000</td>
      <td>134.000000</td>
      <td>6.100000</td>
      <td>119.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2013.000000</td>
      <td>150.000000</td>
      <td>7.000000</td>
      <td>862.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2021.000000</td>
      <td>321.000000</td>
      <td>10.000000</td>
      <td>591417.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Drop Genre column </span>
<span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s1">&#39;Genre&#39;</span><span class="p">,</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Year</th>
      <th>Duration</th>
      <th>Rating</th>
      <th>Votes</th>
      <th>Director</th>
      <th>Actor 1</th>
      <th>Actor 2</th>
      <th>Actor 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>#Gadhvi (He thought he was Gandhi)</td>
      <td>2019</td>
      <td>109</td>
      <td>7.0</td>
      <td>8</td>
      <td>Gaurav Bakshi</td>
      <td>Rasika Dugal</td>
      <td>Vivek Ghamande</td>
      <td>Arvind Jangid</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#Yaaram</td>
      <td>2019</td>
      <td>110</td>
      <td>4.4</td>
      <td>35</td>
      <td>Ovais Khan</td>
      <td>Prateik</td>
      <td>Ishita Raj</td>
      <td>Siddhant Kapoor</td>
    </tr>
    <tr>
      <th>5</th>
      <td>...Aur Pyaar Ho Gaya</td>
      <td>1997</td>
      <td>147</td>
      <td>4.7</td>
      <td>827</td>
      <td>Rahul Rawail</td>
      <td>Bobby Deol</td>
      <td>Aishwarya Rai Bachchan</td>
      <td>Shammi Kapoor</td>
    </tr>
    <tr>
      <th>6</th>
      <td>...Yahaan</td>
      <td>2005</td>
      <td>142</td>
      <td>7.4</td>
      <td>1086</td>
      <td>Shoojit Sircar</td>
      <td>Jimmy Sheirgill</td>
      <td>Minissha Lamba</td>
      <td>Yashpal Sharma</td>
    </tr>
    <tr>
      <th>8</th>
      <td>?: A Question Mark</td>
      <td>2012</td>
      <td>82</td>
      <td>5.6</td>
      <td>326</td>
      <td>Allyson Patel</td>
      <td>Yash Dave</td>
      <td>Muntazir Ahmad</td>
      <td>Kiran Bhatia</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Exploratory-Data-Analysis">Exploratory Data Analysis<a class="anchor-link" href="#Exploratory-Data-Analysis">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">14</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="n">sns</span><span class="o">.</span><span class="n">boxplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">&#39;Votes&#39;</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">df</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
<span class="n">sns</span><span class="o">.</span><span class="n">distplot</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Year&#39;</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;g&#39;</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
<span class="n">sns</span><span class="o">.</span><span class="n">distplot</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Rating&#39;</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;g&#39;</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
<span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Duration&#39;</span><span class="p">],</span> <span class="n">y</span><span class="o">=</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Rating&#39;</span><span class="p">],</span> <span class="n">data</span><span class="o">=</span><span class="n">df</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>D:\Anaconda\Ana\lib\site-packages\scipy\stats\stats.py:1713: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
  return np.add.reduce(sorted[indexer] * weights, axis=axis) / sumval
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">30</span><span class="p">,</span><span class="mi">15</span><span class="p">))</span>
<span class="kc">None</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Heatmap</span>
<span class="n">corrmat</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">corr</span><span class="p">()</span>
<span class="n">fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span>

<span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">corrmat</span><span class="p">,</span> <span class="n">vmax</span><span class="o">=.</span><span class="mi">8</span><span class="p">,</span> <span class="n">square</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[26]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Year</th>
      <th>Duration</th>
      <th>Rating</th>
      <th>Votes</th>
      <th>Director</th>
      <th>Actor 1</th>
      <th>Actor 2</th>
      <th>Actor 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>#Gadhvi (He thought he was Gandhi)</td>
      <td>2019</td>
      <td>109</td>
      <td>7.0</td>
      <td>8</td>
      <td>Gaurav Bakshi</td>
      <td>Rasika Dugal</td>
      <td>Vivek Ghamande</td>
      <td>Arvind Jangid</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#Yaaram</td>
      <td>2019</td>
      <td>110</td>
      <td>4.4</td>
      <td>35</td>
      <td>Ovais Khan</td>
      <td>Prateik</td>
      <td>Ishita Raj</td>
      <td>Siddhant Kapoor</td>
    </tr>
    <tr>
      <th>5</th>
      <td>...Aur Pyaar Ho Gaya</td>
      <td>1997</td>
      <td>147</td>
      <td>4.7</td>
      <td>827</td>
      <td>Rahul Rawail</td>
      <td>Bobby Deol</td>
      <td>Aishwarya Rai Bachchan</td>
      <td>Shammi Kapoor</td>
    </tr>
    <tr>
      <th>6</th>
      <td>...Yahaan</td>
      <td>2005</td>
      <td>142</td>
      <td>7.4</td>
      <td>1086</td>
      <td>Shoojit Sircar</td>
      <td>Jimmy Sheirgill</td>
      <td>Minissha Lamba</td>
      <td>Yashpal Sharma</td>
    </tr>
    <tr>
      <th>8</th>
      <td>?: A Question Mark</td>
      <td>2012</td>
      <td>82</td>
      <td>5.6</td>
      <td>326</td>
      <td>Allyson Patel</td>
      <td>Yash Dave</td>
      <td>Muntazir Ahmad</td>
      <td>Kiran Bhatia</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Feature-Engineering:">Feature Engineering:<a class="anchor-link" href="#Feature-Engineering:">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span><span class="s1">&#39;Director&#39;</span><span class="p">,</span><span class="s1">&#39;Actor 1&#39;</span><span class="p">,</span><span class="s1">&#39;Actor 2&#39;</span><span class="p">,</span><span class="s1">&#39;Actor 3&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[27]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Duration</th>
      <th>Rating</th>
      <th>Votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2019</td>
      <td>109</td>
      <td>7.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2019</td>
      <td>110</td>
      <td>4.4</td>
      <td>35</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1997</td>
      <td>147</td>
      <td>4.7</td>
      <td>827</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2005</td>
      <td>142</td>
      <td>7.4</td>
      <td>1086</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2012</td>
      <td>82</td>
      <td>5.6</td>
      <td>326</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">X</span> <span class="o">=</span> <span class="n">df</span><span class="p">[[</span><span class="s1">&#39;Year&#39;</span><span class="p">,</span><span class="s1">&#39;Duration&#39;</span><span class="p">,</span><span class="s1">&#39;Votes&#39;</span><span class="p">]]</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Rating&#39;</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Split the data into training and testing sets</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span><span class="n">random_state</span><span class="o">=</span><span class="mi">1000</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Model-Buiding:">Model Buiding:<a class="anchor-link" href="#Model-Buiding:">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Create a pipeline with standard scaling and SGD regression</span>
<span class="n">pipeline</span> <span class="o">=</span> <span class="n">Pipeline</span><span class="p">([</span>
    <span class="p">(</span><span class="s1">&#39;scaler&#39;</span><span class="p">,</span> <span class="n">StandardScaler</span><span class="p">()),</span>
    <span class="p">(</span><span class="s1">&#39;sgd&#39;</span><span class="p">,</span> <span class="n">SGDRegressor</span><span class="p">(</span><span class="n">max_iter</span><span class="o">=</span><span class="mi">10000</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">1000</span><span class="p">))</span>
<span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pipeline</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[34]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Pipeline(memory=None,
     steps=[(&#39;scaler&#39;, StandardScaler(copy=True, with_mean=True, with_std=True)), (&#39;sgd&#39;, SGDRegressor(alpha=0.0001, average=False, epsilon=0.1, eta0=0.01,
       fit_intercept=True, l1_ratio=0.15, learning_rate=&#39;invscaling&#39;,
       loss=&#39;squared_loss&#39;, max_iter=10000, n_iter=None, penalty=&#39;l2&#39;,
       power_t=0.25, random_state=1000, shuffle=True, tol=None, verbose=0,
       warm_start=False))])</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Predict ratings on the test set</span>
<span class="n">y_pred_pipeline</span> <span class="o">=</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Model-Evaluation:">Model Evaluation:<a class="anchor-link" href="#Model-Evaluation:">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[36]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Evaluation Metrics for the Pipeline</span>
<span class="n">mae_pipeline</span> <span class="o">=</span> <span class="n">mean_absolute_error</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">y_pred_pipeline</span><span class="p">)</span>
<span class="n">mse_pipeline</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">y_pred_pipeline</span><span class="p">)</span>
<span class="n">r2_pipeline</span> <span class="o">=</span> <span class="n">r2_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">y_pred_pipeline</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[37]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Pipeline Mean Absolute Error:&quot;</span><span class="p">,</span> <span class="n">mae_pipeline</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Pipeline Mean Squared Error:&quot;</span><span class="p">,</span> <span class="n">mse_pipeline</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Pipeline R-squared:&quot;</span><span class="p">,</span> <span class="n">r2_pipeline</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Pipeline Mean Absolute Error: 1.0398241948647298
Pipeline Mean Squared Error: 1.7897862935710085
Pipeline R-squared: 0.019359484203190114
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Model-Deployment:">Model Deployment:<a class="anchor-link" href="#Model-Deployment:">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[38]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Take new user input for prediction</span>
<span class="n">new_input</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">({</span>
    <span class="s1">&#39;Year&#39;</span><span class="p">:</span> <span class="p">[</span><span class="mi">2023</span><span class="p">],</span>          <span class="c1"># Replace with the desired year</span>
    <span class="s1">&#39;Duration&#39;</span><span class="p">:</span> <span class="p">[</span><span class="mi">120</span><span class="p">],</span>       <span class="c1"># Replace with the desired duration in minutes</span>
    <span class="s1">&#39;Votes&#39;</span><span class="p">:</span> <span class="p">[</span><span class="mi">10000</span><span class="p">],</span>        <span class="c1"># Replace with the desired number of votes</span>
<span class="p">})</span>

<span class="c1"># Use the trained pipeline to make predictions on the input</span>
<span class="n">predicted_rating</span> <span class="o">=</span> <span class="n">pipeline</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">new_input</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Predicted Rating:&quot;</span><span class="p">,</span> <span class="n">predicted_rating</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Predicted Rating: [5.71243533]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Thank-You!!!">Thank You!!!<a class="anchor-link" href="#Thank-You!!!">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="GitHub:-https://github.com/anujtiwari21?tab=repositories">GitHub: <a href="https://github.com/anujtiwari21?tab=repositories">https://github.com/anujtiwari21?tab=repositories</a><a class="anchor-link" href="#GitHub:-https://github.com/anujtiwari21?tab=repositories">&#182;</a></h3>
</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>