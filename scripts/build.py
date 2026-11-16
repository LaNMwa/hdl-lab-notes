"""Build HDL Lab Notes. Python 3 + mistune 3, no frontend build tooling required.

Usage: pip install -r requirements.txt && python scripts/build.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path
import mistune

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = json.loads((ROOT / 'data/articles.json').read_text(encoding='utf-8'))
MD = mistune.create_markdown(plugins=['table', 'strikethrough'])


def escape(value):
    return html.escape(str(value), quote=True)


def url(a):
    return f"{a['category']}/{a['slug']}.html"


def tags_html(tags):
    return '<div class="tags">' + ''.join(f'<span>{escape(tag)}</span>' for tag in tags) + '</div>'


def header(inner=False, current='home'):
    p = '../' if inner else ''
    return f'''<header class="site-header"><div class="wrap nav">
      <a class="brand" href="{p}index.html" aria-label="HDL Lab Notes 首頁"><span class="brand-icon" aria-hidden="true">⌁</span><span>HDL <b>Lab Notes</b></span><small>DESIGN JOURNAL</small></a>
      <nav class="nav-links" id="main-nav" data-nav-links aria-label="主要導覽">
        <a href="{p}index.html" {'aria-current="page"' if current == 'home' else ''}>首頁</a>
        <a href="{p}index.html#assignments" {'aria-current="page"' if current == 'assignments' else ''}>作業紀錄</a>
        <a href="{p}index.html#notes" {'aria-current="page"' if current == 'notes' else ''}>技術筆記</a>
        <a href="{p}index.html#workflow">設計流程</a>
      </nav>
      <a class="nav-cta" href="{p}index.html#assignments">Explore <span aria-hidden="true">↗</span></a>
      <button class="menu-toggle" type="button" data-menu-button aria-controls="main-nav" aria-expanded="false" aria-label="開啟選單">☰</button>
    </div></header>'''


def footer(inner=False):
    p = '../' if inner else ''
    return f'''<footer class="footer"><div class="wrap footer-inner"><p>© 2026 HDL Lab Notes · Hardware Description Language / Learning Journal</p><div class="utility-links"><a href="{p}index.html">回到首頁</a><a href="{p}AGENTS.md" target="_blank" rel="noopener">AI 開發規範 ↗</a></div></div></footer>'''


def doc(title, description, body, inner=False, current='home'):
    p = '../' if inner else ''
    return f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
    <meta name="description" content="{escape(description)}"/><meta name="theme-color" content="#080d13"/>
    <title>{escape(title)} · HDL Lab Notes</title><link rel="stylesheet" href="{p}assets/css/styles.css"/>
    <script defer src="{p}assets/js/site.js"></script></head><body>{'<div class="reading-progress" data-progress></div>' if inner else ''}{header(inner,current)}{body}{footer(inner)}</body></html>'''


def assignment_card(a):
    text = ' '.join([a['title'], a['subtitle'], a['description'], *a['tags']])
    return f'''<a href="{url(a)}" class="card" data-search-item="{escape(text)}"><div class="card-media"><img src="assets/images/{escape(a['cover'])}" alt="{escape(a['title'])} 實作截圖" loading="lazy"/><span class="card-index">{escape(a['number'])}</span></div><div class="card-body">
      <p class="card-subtitle">{escape(a['subtitle'])}</p><h3>{escape(a['title'])}</h3><p>{escape(a['description'])}</p>{tags_html(a['tags'])}
      <div class="card-bottom"><span class="card-date">{escape(a['date'])}</span><span class="card-arrow">閱讀實驗紀錄 <span aria-hidden="true">↗</span></span></div></div></a>'''


def note_card(a):
    text = ' '.join([a['title'], a['subtitle'], a['description'], *a['tags']])
    return f'''<a href="{url(a)}" class="note-card" data-search-item="{escape(text)}"><div class="note-top"><span>{escape(a['number'])}</span><b aria-hidden="true">↗</b></div><h3>{escape(a['title'])}</h3><p>{escape(a['description'])}</p><small>{escape(' / '.join(a['tags']))}</small></a>'''


def home():
    assignments = [a for a in ARTICLES if a['category'] == 'assignments']
    notes = [a for a in ARTICLES if a['category'] == 'notes']
    pipeline = [('01','RTL','Design'),('02','SIM','Verify'),('03','DC','Synthesis'),('04','PT','Timing'),('05','APR','Physical'),('06','LVS','Signoff')]
    flow = ''.join(f'<div class="flow-cell"><span>STAGE / {n}</span><h4>{short}</h4><p>{meaning}</p></div>' for n, short, meaning in pipeline)
    body = f'''<main>
      <section class="hero wrap"><div class="hero-copy"><div class="eyebrow"><span class="status-ping"></span> HARDWARE DESIGN · 2026 LAB ARCHIVE</div>
       <h1>從 Verilog 到<br/><em>實體晶片。</em><br/>每一步都記錄。</h1>
       <p class="intro">這是我的 HDL 實驗筆記：整理 RTL 設計、模擬波形、PPA 分析與實體設計成果，把每次 Debug 變成下一次設計的參考。</p>
       <div class="hero-actions"><a class="btn btn-primary" href="#assignments">查看作業紀錄 <span>↗</span></a><a class="btn btn-outline" href="#notes">探索技術筆記 <span>→</span></a></div>
       <p class="hero-caption"><span>●</span> PROJECTS / 由真實作業報告整理 · 持續更新</p></div>
       <div class="visual" aria-label="四級 CPU Pipeline 示意"><div class="visual-top"><div class="window-dots"><i></i><i></i><i></i></div><span>rtl / thumb_cpu.v</span><span>● ACTIVE</span></div>
        <div class="visual-core"><div class="schematic-title"><span>ARCHITECTURE VIEW</span><span>4-STAGE PIPELINE</span></div>
        <div class="chip-box"><div class="chip-kicker">THUMB / CPU CORE</div><div class="pipeline">
           <div class="stage"><span>STAGE 01</span><strong>IF</strong><small>Fetch</small></div><div class="stage"><span>STAGE 02</span><strong>ID</strong><small>Decode</small></div><div class="stage"><span>STAGE 03</span><strong>EX</strong><small>Execute</small></div><div class="stage"><span>STAGE 04</span><strong>WB</strong><small>Writeback</small></div>
         </div><div class="signal"><span>CLK <i>▰▰▱▰▰</i></span><span>RESET <i>LOW</i></span><span>DATA <i>READY</i></span></div></div>
        <div class="terminal"><div><span class="prompt">$</span> run_design_flow --hw3</div><div><span class="pass">✓</span> RTL &amp; gate simulation</div><div><span class="pass">✓</span> APR setup / hold</div><div><span class="pass">✓</span> DRC: 0 violations</div><div><span class="pass">✓</span> LVS: CORRECT</div></div></div>
        <div class="visual-foot"><span>PROJECT / 003</span><span>POST-ROUTE VERIFIED</span></div></div></section>
      <div class="stats-strip"><div class="wrap stats"><div class="stat"><strong>{len(assignments):02d}</strong><span>份作業實驗紀錄</span></div><div class="stat"><strong>{len(notes):02d}</strong><span>篇技術重點筆記</span></div><div class="stat"><strong>04</strong><span>Stage THUMB CPU</span></div></div></div>
      <section id="assignments" class="section wrap"><div class="section-header"><div><span class="section-number">01 / THE PROJECTS</span><h2>把實驗過程留下來。</h2><p>從 Verilog 寫法比較到完整的 CPU APR 流程，附上原始作業成果截圖。</p></div><span class="section-aside">SORTED BY / NEWEST FIRST</span></div>
        <div class="search-area"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg><input data-search type="search" aria-label="搜尋實驗與技術筆記" placeholder="搜尋 Pipeline、Clock Gating、LVS、APR..."/><small data-search-count>{len(ARTICLES)} 筆內容</small></div>
        <div class="card-grid">{''.join(assignment_card(a) for a in assignments)}</div></section>
      <section id="notes" class="section wrap"><div class="section-header"><div><span class="section-number">02 / KNOWLEDGE BASE</span><h2>實驗之外，整理核心觀念。</h2><p>每篇內容都有對應的 Markdown 原始檔，後續可以依照 AGENTS.md 持續擴充。</p></div><span class="section-aside">MARKDOWN-FIRST NOTES</span></div>
        <div class="notes-grid">{''.join(note_card(a) for a in notes)}</div><div class="empty-state" data-empty>找不到符合的筆記，試試其他關鍵字。</div></section>
      <section id="workflow" class="section wrap flow-section"><div class="section-header"><div><span class="section-number">03 / THE PROCESS</span><h2>我的數位 IC 設計流程。</h2><p>把做過的工具與驗證階段串成一條清楚的學習路徑。</p></div></div>
        <div class="flow-grid">{flow}</div></section>
      <section class="guide-band"><div class="wrap guide-row"><div><span class="section-number">04 / KEEP BUILDING</span><h2>一份規範，讓網站可以一直寫下去。</h2><p>每次把作業報告、自己寫的課程筆記整理成 Markdown，再讓 AI 遵守 AGENTS.md 的命名、引用與排版規則新增文章。</p></div>
        <div class="guide-steps"><div><span>STEP / 01</span><strong>整理資料</strong><small>課堂內容、實驗報告、截圖</small></div><div><span>STEP / 02</span><strong>新增 Markdown</strong><small>沿用固定文章結構</small></div><div><span>STEP / 03</span><strong>更新網站</strong><small>執行 build.py 並推送 GitHub</small></div></div></div></section>
    </main>'''
    return doc('首頁', 'HDL Lab Notes：Verilog、Pipeline、Clock Gating 與 Pipelined THUMB CPU 的硬體設計學習紀錄。', body)


def render_markdown(source):
    # The page title comes from article metadata to avoid duplicate H1.
    md = re.sub(r'^# .+\n', '', source, count=1)
    out = MD(md)
    index = 0
    def add_heading(m):
        nonlocal index
        level = m.group(1)
        index += 1
        return f'<h{level} id="section-{index}">{m.group(2)}</h{level}>'
    out = re.sub(r'<h([23])>(.*?)</h\1>', add_heading, out, flags=re.S)
    out = re.sub(r'<p><img src="([^"]+)" alt="([^"]*)"\s*/?></p>',
                 lambda m: f'<figure><img loading="lazy" src="{m.group(1)}" alt="{m.group(2)}"/><figcaption>{m.group(2)}</figcaption></figure>', out)
    out = out.replace('<table>', '<div class="table-scroller"><table>').replace('</table>', '</table></div>')
    return out


def article(a):
    source_file = ROOT / 'content' / f"{a['slug']}.md"
    if not source_file.exists():
        raise FileNotFoundError(source_file)
    parsed = render_markdown(source_file.read_text(encoding='utf-8'))
    category = '作業紀錄' if a['category'] == 'assignments' else '技術筆記'
    body = f'''<main><section class="article-head"><div class="wrap"><div class="crumbs"><a href="../index.html">首頁</a><span>/</span><a href="../index.html#{a['category']}">{category}</a><span>/</span><span>{escape(a['title'])}</span></div>
        <div class="article-label">{escape(a['number'])} / {escape(category)}</div><h1>{escape(a['title'])}</h1><p class="article-deck">{escape(a['subtitle'])}。{escape(a['description'])}</p>
        <div class="article-meta"><span>{escape(a['date'])}</span><span>◷ {escape(a['reading'])}</span>{tags_html(a['tags'])}</div></div></section>
        <div class="wrap article-grid"><article class="prose">{parsed}<nav class="article-prevnext" aria-label="文章導覽"><a href="../index.html#{a['category']}">← 回到文章列表</a><a href="#">↑ 回到頂端</a></nav></article>
         <aside class="article-aside"><div class="toc-title">ON THIS PAGE / 文章目錄</div><nav class="toc" data-toc aria-label="本篇目錄"></nav><div class="aside-bottom"><a href="../index.html#assignments">↗ 全部作業紀錄</a><a href="../index.html#notes">↗ 全部技術筆記</a></div></aside></div></main>
      <div class="lightbox" data-lightbox role="dialog" aria-modal="true" aria-label="圖片放大預覽" aria-hidden="true"><button class="lightbox-close" data-lightbox-close aria-label="關閉圖片">×</button><img alt="放大圖片"/><div class="lightbox-caption" data-lightbox-caption></div></div>'''
    return doc(a['title'], a['description'], body, inner=True, current=a['category'])


def build():
    valid_categories = {'assignments', 'notes'}
    seen = set()
    for a in ARTICLES:
        if a['category'] not in valid_categories or not re.fullmatch(r'[a-z0-9-]+', a['slug']):
            raise ValueError('Invalid category/slug: '+str(a))
        if a['slug'] in seen:
            raise ValueError('Duplicate slug '+a['slug'])
        seen.add(a['slug'])
        target = ROOT / url(a)
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(article(a),encoding='utf-8')
        print('built',target.relative_to(ROOT))
    (ROOT / 'index.html').write_text(home(),encoding='utf-8')
    print('built index.html')


if __name__ == '__main__':
    build()
