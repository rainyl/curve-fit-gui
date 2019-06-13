from PyQt5.QtWidgets import QWidget, QTextEdit, QHBoxLayout
from src.utils.SSSetter import *
from PyQt5.QtCore import QRect, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from src.config import *


class Ui_HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Help')
        self.setGeometry(QRect(200, 200, 800, 600))
        self.setupUi()

    def setupUi(self):
        html = '''
        <!DOCTYPE html><html><head>
      <title>report</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      
      <link rel="stylesheet" href="file:///.\\katex.min.css">
      <style> 
      /**
 * prism.js Github theme based on GitHub's theme.
 * @author Sam Clarke
 */
code[class*="language-"],
pre[class*="language-"] {
  color: #333;
  background: none;
  font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
  text-align: left;
  white-space: pre;
  word-spacing: normal;
  word-break: normal;
  word-wrap: normal;
  line-height: 1.4;

  -moz-tab-size: 8;
  -o-tab-size: 8;
  tab-size: 8;

  -webkit-hyphens: none;
  -moz-hyphens: none;
  -ms-hyphens: none;
  hyphens: none;
}

/* Code blocks */
pre[class*="language-"] {
  padding: .8em;
  overflow: auto;
  /* border: 1px solid #ddd; */
  border-radius: 3px;
  /* background: #fff; */
  background: #f5f5f5;
}

/* Inline code */
:not(pre) > code[class*="language-"] {
  padding: .1em;
  border-radius: .3em;
  white-space: normal;
  background: #f5f5f5;
}

.token.comment,
.token.blockquote {
  color: #969896;
}

.token.cdata {
  color: #183691;
}

.token.doctype,
.token.punctuation,
.token.variable,
.token.macro.property {
  color: #333;
}

.token.operator,
.token.important,
.token.keyword,
.token.rule,
.token.builtin {
  color: #a71d5d;
}

.token.string,
.token.url,
.token.regex,
.token.attr-value {
  color: #183691;
}

.token.property,
.token.number,
.token.boolean,
.token.entity,
.token.atrule,
.token.constant,
.token.symbol,
.token.command,
.token.code {
  color: #0086b3;
}

.token.tag,
.token.selector,
.token.prolog {
  color: #63a35c;
}

.token.function,
.token.namespace,
.token.pseudo-element,
.token.class,
.token.class-name,
.token.pseudo-class,
.token.id,
.token.url-reference .token.variable,
.token.attr-name {
  color: #795da3;
}

.token.entity {
  cursor: help;
}

.token.title,
.token.title .token.punctuation {
  font-weight: bold;
  color: #1d3e81;
}

.token.list {
  color: #ed6a43;
}

.token.inserted {
  background-color: #eaffea;
  color: #55a532;
}

.token.deleted {
  background-color: #ffecec;
  color: #bd2c00;
}

.token.bold {
  font-weight: bold;
}

.token.italic {
  font-style: italic;
}


/* JSON */
.language-json .token.property {
  color: #183691;
}

.language-markup .token.tag .token.punctuation {
  color: #333;
}

/* CSS */
code.language-css,
.language-css .token.function {
  color: #0086b3;
}

/* YAML */
.language-yaml .token.atrule {
  color: #63a35c;
}

code.language-yaml {
  color: #183691;
}

/* Ruby */
.language-ruby .token.function {
  color: #333;
}

/* Markdown */
.language-markdown .token.url {
  color: #795da3;
}

/* Makefile */
.language-makefile .token.symbol {
  color: #795da3;
}

.language-makefile .token.variable {
  color: #183691;
}

.language-makefile .token.builtin {
  color: #0086b3;
}

/* Bash */
.language-bash .token.keyword {
  color: #0086b3;
}

/* highlight */
pre[data-line] {
  position: relative;
  padding: 1em 0 1em 3em;
}
pre[data-line] .line-highlight-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  background-color: transparent;
  display: block;
  width: 100%;
}

pre[data-line] .line-highlight {
  position: absolute;
  left: 0;
  right: 0;
  padding: inherit 0;
  margin-top: 1em;
  background: hsla(24, 20%, 50%,.08);
  background: linear-gradient(to right, hsla(24, 20%, 50%,.1) 70%, hsla(24, 20%, 50%,0));
  pointer-events: none;
  line-height: inherit;
  white-space: pre;
}

pre[data-line] .line-highlight:before, 
pre[data-line] .line-highlight[data-end]:after {
  content: attr(data-start);
  position: absolute;
  top: .4em;
  left: .6em;
  min-width: 1em;
  padding: 0 .5em;
  background-color: hsla(24, 20%, 50%,.4);
  color: hsl(24, 20%, 95%);
  font: bold 65%/1.5 sans-serif;
  text-align: center;
  vertical-align: .3em;
  border-radius: 999px;
  text-shadow: none;
  box-shadow: 0 1px white;
}

pre[data-line] .line-highlight[data-end]:after {
  content: attr(data-end);
  top: auto;
  bottom: .4em;
}html body{font-family:"Helvetica Neue",Helvetica,"Segoe UI",Arial,freesans,sans-serif;font-size:16px;line-height:1.6;color:#333;background-color:#fff;overflow:initial;box-sizing:border-box;word-wrap:break-word}html body>:first-child{margin-top:0}html body h1,html body h2,html body h3,html body h4,html body h5,html body h6{line-height:1.2;margin-top:1em;margin-bottom:16px;color:#000}html body h1{font-size:2.25em;font-weight:300;padding-bottom:.3em}html body h2{font-size:1.75em;font-weight:400;padding-bottom:.3em}html body h3{font-size:1.5em;font-weight:500}html body h4{font-size:1.25em;font-weight:600}html body h5{font-size:1.1em;font-weight:600}html body h6{font-size:1em;font-weight:600}html body h1,html body h2,html body h3,html body h4,html body h5{font-weight:600}html body h5{font-size:1em}html body h6{color:#5c5c5c}html body strong{color:#000}html body del{color:#5c5c5c}html body a:not([href]){color:inherit;text-decoration:none}html body a{color:#08c;text-decoration:none}html body a:hover{color:#00a3f5;text-decoration:none}html body img{max-width:100%}html body>p{margin-top:0;margin-bottom:16px;word-wrap:break-word}html body>ul,html body>ol{margin-bottom:16px}html body ul,html body ol{padding-left:2em}html body ul.no-list,html body ol.no-list{padding:0;list-style-type:none}html body ul ul,html body ul ol,html body ol ol,html body ol ul{margin-top:0;margin-bottom:0}html body li{margin-bottom:0}html body li.task-list-item{list-style:none}html body li>p{margin-top:0;margin-bottom:0}html body .task-list-item-checkbox{margin:0 .2em .25em -1.8em;vertical-align:middle}html body .task-list-item-checkbox:hover{cursor:pointer}html body blockquote{margin:16px 0;font-size:inherit;padding:0 15px;color:#5c5c5c;border-left:4px solid #d6d6d6}html body blockquote>:first-child{margin-top:0}html body blockquote>:last-child{margin-bottom:0}html body hr{height:4px;margin:32px 0;background-color:#d6d6d6;border:0 none}html body table{margin:10px 0 15px 0;border-collapse:collapse;border-spacing:0;display:block;width:100%;overflow:auto;word-break:normal;word-break:keep-all}html body table th{font-weight:bold;color:#000}html body table td,html body table th{border:1px solid #d6d6d6;padding:6px 13px}html body dl{padding:0}html body dl dt{padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:bold}html body dl dd{padding:0 16px;margin-bottom:16px}html body code{font-family:Menlo,Monaco,Consolas,'Courier New',monospace;font-size:.85em !important;color:#000;background-color:#f0f0f0;border-radius:3px;padding:.2em 0}html body code::before,html body code::after{letter-spacing:-0.2em;content:"\00a0"}html body pre>code{padding:0;margin:0;font-size:.85em !important;word-break:normal;white-space:pre;background:transparent;border:0}html body .highlight{margin-bottom:16px}html body .highlight pre,html body pre{padding:1em;overflow:auto;font-size:.85em !important;line-height:1.45;border:#d6d6d6;border-radius:3px}html body .highlight pre{margin-bottom:0;word-break:normal}html body pre code,html body pre tt{display:inline;max-width:initial;padding:0;margin:0;overflow:initial;line-height:inherit;word-wrap:normal;background-color:transparent;border:0}html body pre code:before,html body pre tt:before,html body pre code:after,html body pre tt:after{content:normal}html body p,html body blockquote,html body ul,html body ol,html body dl,html body pre{margin-top:0;margin-bottom:16px}html body kbd{color:#000;border:1px solid #d6d6d6;border-bottom:2px solid #c7c7c7;padding:2px 4px;background-color:#f0f0f0;border-radius:3px}@media print{html body{background-color:#fff}html body h1,html body h2,html body h3,html body h4,html body h5,html body h6{color:#000;page-break-after:avoid}html body blockquote{color:#5c5c5c}html body pre{page-break-inside:avoid}html body table{display:table}html body img{display:block;max-width:100%;max-height:100%}html body pre,html body code{word-wrap:break-word;white-space:pre}}.markdown-preview{width:100%;height:100%;box-sizing:border-box}.markdown-preview .pagebreak,.markdown-preview .newpage{page-break-before:always}.markdown-preview pre.line-numbers{position:relative;padding-left:3.8em;counter-reset:linenumber}.markdown-preview pre.line-numbers>code{position:relative}.markdown-preview pre.line-numbers .line-numbers-rows{position:absolute;pointer-events:none;top:1em;font-size:100%;left:0;width:3em;letter-spacing:-1px;border-right:1px solid #999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.markdown-preview pre.line-numbers .line-numbers-rows>span{pointer-events:none;display:block;counter-increment:linenumber}.markdown-preview pre.line-numbers .line-numbers-rows>span:before{content:counter(linenumber);color:#999;display:block;padding-right:.8em;text-align:right}.markdown-preview .mathjax-exps .MathJax_Display{text-align:center !important}.markdown-preview:not([for="preview"]) .code-chunk .btn-group{display:none}.markdown-preview:not([for="preview"]) .code-chunk .status{display:none}.markdown-preview:not([for="preview"]) .code-chunk .output-div{margin-bottom:16px}.scrollbar-style::-webkit-scrollbar{width:8px}.scrollbar-style::-webkit-scrollbar-track{border-radius:10px;background-color:transparent}.scrollbar-style::-webkit-scrollbar-thumb{border-radius:5px;background-color:rgba(150,150,150,0.66);border:4px solid rgba(150,150,150,0.66);background-clip:content-box}html body[for="html-export"]:not([data-presentation-mode]){position:relative;width:100%;height:100%;top:0;left:0;margin:0;padding:0;overflow:auto}html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview{position:relative;top:0}@media screen and (min-width:914px){html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview{padding:2em calc(50% - 457px + 2em)}}@media screen and (max-width:914px){html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview{padding:2em}}@media screen and (max-width:450px){html body[for="html-export"]:not([data-presentation-mode]) .markdown-preview{font-size:14px !important;padding:1em}}@media print{html body[for="html-export"]:not([data-presentation-mode]) #sidebar-toc-btn{display:none}}html body[for="html-export"]:not([data-presentation-mode]) #sidebar-toc-btn{position:fixed;bottom:8px;left:8px;font-size:28px;cursor:pointer;color:inherit;z-index:99;width:32px;text-align:center;opacity:.4}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] #sidebar-toc-btn{opacity:1}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc{position:fixed;top:0;left:0;width:300px;height:100%;padding:32px 0 48px 0;font-size:14px;box-shadow:0 0 4px rgba(150,150,150,0.33);box-sizing:border-box;overflow:auto;background-color:inherit}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc::-webkit-scrollbar{width:8px}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc::-webkit-scrollbar-track{border-radius:10px;background-color:transparent}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc::-webkit-scrollbar-thumb{border-radius:5px;background-color:rgba(150,150,150,0.66);border:4px solid rgba(150,150,150,0.66);background-clip:content-box}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc a{text-decoration:none}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc ul{padding:0 1.6em;margin-top:.8em}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc li{margin-bottom:.8em}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .md-sidebar-toc ul{list-style-type:none}html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .markdown-preview{left:300px;width:calc(100% -  300px);padding:2em calc(50% - 457px -  150px);margin:0;box-sizing:border-box}@media screen and (max-width:1274px){html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .markdown-preview{padding:2em}}@media screen and (max-width:450px){html body[for="html-export"]:not([data-presentation-mode])[html-show-sidebar-toc] .markdown-preview{width:100%}}html body[for="html-export"]:not([data-presentation-mode]):not([html-show-sidebar-toc]) .markdown-preview{left:50%;transform:translateX(-50%)}html body[for="html-export"]:not([data-presentation-mode]):not([html-show-sidebar-toc]) .md-sidebar-toc{display:none}
/* Please visit the URL below for more information: */
/*   https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css */
 
      </style>
    </head>
    <body for="html-export">
      <div class="mume markdown-preview  ">
      <h1 class="mume-header" id="%E6%B0%B4%E6%96%87%E9%A2%91%E7%8E%87%E6%9B%B2%E7%BA%BF%E6%8B%9F%E5%90%88%E8%BD%AF%E4%BB%B6%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E">&#x6C34;&#x6587;&#x9891;&#x7387;&#x66F2;&#x7EBF;&#x62DF;&#x5408;&#x8F6F;&#x4EF6;&#x4F7F;&#x7528;&#x8BF4;&#x660E;</h1>

<ul>
<li>&#x4F5C;&#x8005;&#xFF1A;&#x5218;&#x5F66;&#x9F99;</li>
<li>&#x5B66;&#x6821;&#xFF1A;&#x6B66;&#x6C49;&#x5927;&#x5B66;</li>
<li>&#x6307;&#x5BFC;&#x6559;&#x5E08;&#xFF1A;&#x827E;&#x5B66;&#x5C71;&#x3001;&#x4E07;&#x98B7;</li>
</ul>
<ul>
<li><a href="#%E6%B0%B4%E6%96%87%E9%A2%91%E7%8E%87%E6%9B%B2%E7%BA%BF%E6%8B%9F%E5%90%88%E8%BD%AF%E4%BB%B6%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E">&#x6C34;&#x6587;&#x9891;&#x7387;&#x66F2;&#x7EBF;&#x62DF;&#x5408;&#x8F6F;&#x4EF6;&#x4F7F;&#x7528;&#x8BF4;&#x660E;</a>
<ul>
<li><a href="#%E7%AE%80%E4%BB%8B">&#x7B80;&#x4ECB;</a></li>
<li><a href="#%E7%95%8C%E9%9D%A2%E4%BB%8B%E7%BB%8D">&#x754C;&#x9762;&#x4ECB;&#x7ECD;</a></li>
<li><a href="#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95">&#x4F7F;&#x7528;&#x65B9;&#x6CD5;</a>
<ul>
<li><a href="#%E6%95%B0%E6%8D%AE%E8%A6%81%E6%B1%82%E4%B8%8E%E5%AF%BC%E5%85%A5">&#x6570;&#x636E;&#x8981;&#x6C42;&#x4E0E;&#x5BFC;&#x5165;</a></li>
<li><a href="#%E6%89%8B%E5%8A%A8%E5%BE%AE%E8%B0%83">&#x624B;&#x52A8;&#x5FAE;&#x8C03;</a></li>
<li><a href="#%E6%98%BE%E7%A4%BA%E6%8B%9F%E5%90%88%E8%A1%A8%E6%A0%BC">&#x663E;&#x793A;&#x62DF;&#x5408;&#x8868;&#x683C;</a></li>
<li><a href="#%E5%8F%A6%E5%AD%98%E4%B8%BA">&#x53E6;&#x5B58;&#x4E3A;</a></li>
<li><a href="#%E6%B8%85%E9%99%A4">&#x6E05;&#x9664;</a></li>
<li><a href="#%E9%80%80%E5%87%BA">&#x9000;&#x51FA;</a></li>
</ul>
</li>
<li><a href="#%E7%BB%93%E8%AF%AD">&#x7ED3;&#x8BED;</a></li>
</ul>
</li>
</ul>
<h2 class="mume-header" id="%E7%AE%80%E4%BB%8B">&#x7B80;&#x4ECB;</h2>

<p>&#x672C;&#x8F6F;&#x4EF6;&#x53EF;&#x4EE5;&#x5B9E;&#x73B0;&#x6C34;&#x6587;&#x9891;&#x7387;&#x66F2;&#x7EBF;(<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>P</mi><mo>&#x2212;</mo></mrow><annotation encoding="application/x-tex">P-</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="mord mathdefault" style="margin-right:0.13889em;">P</span><span class="mord">&#x2212;</span></span></span></span>)&#x7684;&#x62DF;&#x5408;&#xFF0C;&#x5E76;&#x53EF;&#x4EE5;&#x624B;&#x52A8;&#x8C03;&#x6574;&#xFF0C;&#x5B9E;&#x65F6;&#x663E;&#x793A;&#x62DF;&#x5408;&#x66F2;&#x7EBF;&#x3002;</p>
<p>&#x672C;&#x7A0B;&#x5E8F;&#x91C7;&#x7528;<code>Python</code>&#x7ED3;&#x5408;<code>PyQt5</code>&#x7F16;&#x5199;&#x3002;</p>
<h2 class="mume-header" id="%E7%95%8C%E9%9D%A2%E4%BB%8B%E7%BB%8D">&#x754C;&#x9762;&#x4ECB;&#x7ECD;</h2>

<p><img src="./img/mainwindow.png" alt><br>
&#x4E3B;&#x754C;&#x9762;&#x5305;&#x62EC;&#x83DC;&#x5355;&#x680F;&#x3001;&#x8F93;&#x5165;&#x680F;&#x3001;&#x5E95;&#x90E8;&#x83DC;&#x5355;&#x3001;&#x53F3;&#x4FA7;&#x7ED8;&#x56FE;&#x533A;&#x3002;</p>
<h2 class="mume-header" id="%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95">&#x4F7F;&#x7528;&#x65B9;&#x6CD5;</h2>

<h3 class="mume-header" id="%E6%95%B0%E6%8D%AE%E8%A6%81%E6%B1%82%E4%B8%8E%E5%AF%BC%E5%85%A5">&#x6570;&#x636E;&#x8981;&#x6C42;&#x4E0E;&#x5BFC;&#x5165;</h3>

<p>&#x60A8;&#x53EF;&#x4EE5;&#x9009;&#x62E9;<code>.csv</code>&#x6216;&#x8005;<code>.xls</code>&#x683C;&#x5F0F;&#x6570;&#x636E;&#x5BFC;&#x5165;&#xFF0C;&#x4E0D;&#x8FC7;&#x63A8;&#x8350;&#x4F7F;&#x7528;<code>.csv</code>&#x683C;&#x5F0F;&#x6587;&#x4EF6;&#xFF0C;&#x6570;&#x636E;&#x5305;&#x62EC;&#x4E24;&#x5217;&#xFF0C;&#x7B2C;&#x4E00;&#x5217;&#x4E3A;&#x5E74;&#x4EFD;(&#x6216;&#x8005;&#x60A8;&#x81EA;&#x5DF1;&#x9009;&#x5B9A;&#x7684;&#x65F6;&#x6BB5;)&#xFF0C;&#x7B2C;&#x4E8C;&#x5217;&#x4E3A;&#x6D41;&#x91CF;&#x6570;&#x636E;&#xFF0C;&#x793A;&#x4F8B;&#x6570;&#x636E;&#x53EF;&#x89C1;<code>1.csv</code>&#x3002;<br>
&#x5F53;&#x5BFC;&#x5165;&#x6570;&#x636E;&#x4EE5;&#x540E;&#x7A0B;&#x5E8F;&#x81EA;&#x52A8;&#x5F00;&#x59CB;&#x8BA1;&#x7B97;&#xFF0C;&#x5982;&#x679C;&#x60A8;&#x7684;&#x64CD;&#x4F5C;&#x4E0E;&#x6570;&#x636E;&#x65E0;&#x8BEF;&#xFF0C;&#x6B64;&#x65F6;&#x754C;&#x9762;&#x7ED8;&#x56FE;&#x533A;&#x4F1A;&#x51FA;&#x73B0;&#x62DF;&#x5408;&#x56FE;&#x50CF;&#x3002;&#x5982;&#x4E0B;&#x56FE;:<br>
<img src="./img/plot.png" alt></p>
<h3 class="mume-header" id="%E6%89%8B%E5%8A%A8%E5%BE%AE%E8%B0%83">&#x624B;&#x52A8;&#x5FAE;&#x8C03;</h3>

<p>&#x5F53;&#x5BF9;&#x62DF;&#x5408;&#x7ED3;&#x679C;&#x4E0D;&#x6EE1;&#x610F;&#xFF0C;&#x60A8;&#x53EF;&#x4EE5;&#x9009;&#x62E9;&#x624B;&#x52A8;&#x5FAE;&#x8C03;&#xFF0C;&#x60A8;&#x53EF;&#x4EE5;&#x9009;&#x62E9;&#x8C03;&#x6574;<code>ave&#x3001;Cv&#x3001;fac</code>&#x6765;&#x4F18;&#x5316;&#x62DF;&#x5408;&#x7ED3;&#x679C;&#xFF0C;&#x5176;&#x4E2D;<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi><mi>s</mi><mo>=</mo><mi>f</mi><mi>a</mi><mi>c</mi><mo>&#x2217;</mo><mi>C</mi><mi>v</mi></mrow><annotation encoding="application/x-tex">Cs=fac*Cv</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.07153em;">C</span><span class="mord mathdefault">s</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathdefault" style="margin-right:0.10764em;">f</span><span class="mord mathdefault">a</span><span class="mord mathdefault">c</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">&#x2217;</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathdefault" style="margin-right:0.07153em;">C</span><span class="mord mathdefault" style="margin-right:0.03588em;">v</span></span></span></span>&#xFF0C;&#x4E5F;&#x5C31;&#x662F;&#x8BF4;&#x60A8;&#x4E0D;&#x5FC5;&#x624B;&#x52A8;&#x8C03;&#x6574;<code>Cs</code>&#x3002;</p>
<h3 class="mume-header" id="%E6%98%BE%E7%A4%BA%E6%8B%9F%E5%90%88%E8%A1%A8%E6%A0%BC">&#x663E;&#x793A;&#x62DF;&#x5408;&#x8868;&#x683C;</h3>

<p>&#x5F53;&#x4E0A;&#x8FF0;&#x6570;&#x636E;&#x5BFC;&#x5165;&#x6210;&#x529F;&#x5E76;&#x83B7;&#x5F97;&#x56FE;&#x50CF;&#xFF0C;&#x60A8;&#x53EF;&#x4EE5;&#x70B9;&#x51FB;<code>&#x663E;&#x793A;&#x6570;&#x636E;</code>&#xFF0C;&#x6B64;&#x65F6;&#x4F1A;&#x5F39;&#x51FA;&#x8868;&#x683C;&#x7A97;&#x53E3;&#xFF0C;&#x5DE6;&#x4FA7;&#x4E3A;&#x7ECF;&#x9A8C;&#x9891;&#x7387;&#xFF0C;&#x53F3;&#x4FA7;&#x4E3A;&#x7406;&#x8BBA;&#x9891;&#x7387;&#x3002;<br>
<img src="./img/table.png" alt></p>
<h3 class="mume-header" id="%E5%8F%A6%E5%AD%98%E4%B8%BA">&#x53E6;&#x5B58;&#x4E3A;</h3>

<p>&#x82E5;&#x60A8;&#x60F3;&#x5C06;&#x56FE;&#x50CF;&#x4FDD;&#x5B58;&#xFF0C;&#x53EF;&#x4EE5;&#x70B9;&#x51FB;<code>&#x53E6;&#x5B58;&#x4E3A;</code>&#x6309;&#x94AE;&#x5E76;&#x6839;&#x636E;&#x63D0;&#x793A;&#x64CD;&#x4F5C;&#x3002;</p>
<h3 class="mume-header" id="%E6%B8%85%E9%99%A4">&#x6E05;&#x9664;</h3>

<p>&#x82E5;&#x60A8;&#x60F3;&#x6E05;&#x9664;&#x56FE;&#x50CF;&#xFF0C;&#x8BF7;&#x70B9;&#x51FB;<code>&#x6E05;&#x9664;</code>&#x6309;&#x94AE;&#x3002;</p>
<h3 class="mume-header" id="%E9%80%80%E5%87%BA">&#x9000;&#x51FA;</h3>

<p>&#x70B9;&#x51FB;<code>&#x9000;&#x51FA;</code>&#x6309;&#x94AE;&#x9000;&#x51FA;&#x7A0B;&#x5E8F;&#x3002;</p>
<h2 class="mume-header" id="%E7%BB%93%E8%AF%AD">&#x7ED3;&#x8BED;</h2>

<p>&#x672C;&#x8F6F;&#x4EF6;&#x4E3A;<code>&#x6570;&#x636E;&#x5E93;&#x4E0E;&#x6C34;&#x5229;&#x5E94;&#x7528;&#x5F00;&#x53D1;</code>&#x8BFE;&#x7A0B;&#x7684;&#x4E2A;&#x4EBA;&#x4F5C;&#x54C1;&#xFF0C;&#x611F;&#x8C22;&#x827E;&#x5B66;&#x5C71;&#x8001;&#x5E08;&#x3001;&#x4E07;&#x98B7;&#x8001;&#x5E08;&#x7684;&#x6307;&#x5BFC;&#xFF0C;&#x672C;&#x8F6F;&#x4EF6;&#x4E5F;&#x5728;&#x4E00;&#x5B9A;&#x7A0B;&#x5EA6;&#x4E0A;&#x501F;&#x9274;&#x4E86;&#x4E07;&#x8001;&#x5E08;&#x7684;&#x540C;&#x6B3E;&#x8F6F;&#x4EF6;&#xFF0C;&#x79C9;&#x627F;&#x5F00;&#x6E90;&#x7CBE;&#x795E;&#xFF0C;&#x672C;&#x8F6F;&#x4EF6;&#x5F00;&#x6E90;&#xFF0C;&#x60A8;&#x53EF;&#x4EE5;&#x5728;<a href>&#x8FD9;&#x91CC;</a>&#x627E;&#x5230;&#x672C;&#x8F6F;&#x4EF6;&#x7684;&#x6E90;&#x7801;&#xFF0C;&#x7531;&#x4E8E;&#x521D;&#x6B21;&#x63A5;&#x89E6;&#x754C;&#x9762;&#x5F00;&#x53D1;&#xFF0C;&#x8FD8;&#x6709;&#x8BB8;&#x591A;&#x4E0D;&#x8DB3;&#x4E4B;&#x5904;&#xFF0C;&#x60A8;&#x5982;&#x679C;&#x6709;&#x4EFB;&#x4F55;&#x7684;&#x5EFA;&#x8BAE;&#x53EF;&#x4EE5;&#x524D;&#x5F80;&#x672C;&#x9879;&#x76EE;&#x7684;<code>Github</code>&#x9875;&#x9762;&#x63D0;&#x4EA4;<code>issue</code>.<br>
&#x6700;&#x540E;&#xFF0C;&#x611F;&#x8C22;&#x60A8;&#x7684;&#x4F7F;&#x7528;&#x3002;</p>

      </div>
      
      
    
    
    
    
    
    
    
    
  
    </body></html>
        
        '''
        self.browser = QWebEngineView()
        self.browser.setHtml(html)
        self.browser.load(QUrl('https://github.com/rainyl/curve-fit-gui/blob/master/README.md'))
        # self.txb = QTextEdit()
        # self.txb.setStyleSheet(getEditQSS("#FFFFFF", "#A9A9A9"))
        # self.txb.setText("水文频率曲线拟合软件\n"
        #                  "学校：武汉大学\n"
        #                  "学院：水利水电学院\n"
        #                  "专业：水文与水资源工程\n"
        #                  "学号：2016301580207\n"
        #                  "姓名：刘彦龙\n")
        # self.txb.setDisabled(True)
        #
        layout = QHBoxLayout()
        layout.addWidget(self.browser)
        # layout.addWidget(self.txb)

        self.setLayout(layout)

    def getDoc(self):
        with open(HELP_HTML_PATH) as f:
            data = f.read()
        return data

