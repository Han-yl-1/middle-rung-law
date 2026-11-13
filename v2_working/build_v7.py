#!/usr/bin/env python3
"""
v7 合并版出稿：
  第一、二部分 = 原 v6 HTML（一字不改，只给元素表加表头重复）
  第三部分     = 母方程（Z-Model）全文，修订14，Markdown → pandoc --mathml
  第四部分     = 2026-11-12 补编（原 III.1–III.4 改号 IV.1–IV.4）
用法：python3 build_v7.py   （在 v2_working 里跑；产出 *_v7.html 与 *_v7.pdf）
"""
import re, subprocess, pathlib

HERE = pathlib.Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

LANG = {
    'zh': dict(
        base='中间级定律_预注册与公式全集_中文版.html',
        md='母方程_Z-Model_修订14_论文合并用.md',
        out='中间级定律与母方程_预注册与公式全集_中文版_v7',
        p3_head='第三部分　母方程（Z-Model）：基于 ΔN = −1 拓扑破缺的跨尺度时空阻抗框架',
        p3_note='本部分为母方程论文全文（修订14），§ 编号自成一套，文中「§N」均指本部分。'
                'Z-Model 是第一作者的扩展框架，不代表第二作者观点；它不改动第一、二部分的任何预言与数字。'
                '锁相周期 T<sub>lock</sub> = 232 as 取自 Jiang 等（Phys. Rev. Lett. 133, 163201, 2024）的含时薛定谔方程数值计算，为理论计算值，不是实验测量值。',
        p4_old='第三部分　补编', p4_new='第四部分　补编',
        p4_note_old='本部分由第一作者补写，不改动第一、二部分的任何预言与数字',
        p4_note_new='本部分由第一作者补写，是第三部分与第一、二部分的接口，不改动第一、二部分的任何预言与数字',
        old_credit='<span class="n">本中文版与英文原件同步编排，供张祥前老师及中文读者使用；归一化方程 4π²r³c²/(T²Ghν)=1 由张祥前老师于 2026 年 3 月 3 日写出。</span>',
        credit='''<div class="credit"><b>作者分工</b>　张祥前提供一个静态方程，即归一化方程（2026 年 3 月 3 日写出）：
<div class="eq">4π² r³ c² ⁄ ( T² G h ν ) = 1</div>
其余内容，包括以太频率写法、预言 P1–P6.2、公式全集、元素表、母方程（Z-Model）框架及其推演与诠释，均由第一作者完成，文责由第一作者承担。第三、四部分不代表第二作者观点。<br>
<span class="n">本中文版与英文版同步编排。</span></div>''',
        old_date='<b>版本日期：</b>2026 年 11 月 6 日（首版预注册：2026 年 11 月 5 日）',
        date='<b>版本：</b>第七版，2026 年 11 月 13 日（首版预注册：2026 年 11 月 5 日；第七版并入母方程全文与 11 月 12 日补编，第一、二部分不变）',
        title_old='<h1>中间级定律：三级频率阶梯的预言与公式全集</h1>',
        title='<h1>中间级定律：三级频率阶梯的预言与公式全集<br><span class="sub">附母方程（Z-Model）全文</span></h1>',
    ),
    'en': dict(
        base='Middle-Rung_Law_formula_compendium.html',
        md='Z-Model_rev14_merged_en.md',
        out='Middle-Rung_Law_and_Mother_Equation_compendium_v7',
        p3_head='Part III — The Mother Equation (Z-Model): A Cross-Scale Spacetime-Impedance Framework from ΔN = −1 Topological Breaking',
        p3_note='This part is the full text of the mother-equation paper (revision 14). Its § numbers are self-contained; every “§N” in this part refers to this part. '
                'The Z-Model is the first author’s extension framework and does not represent the second author’s views; it does not alter any prediction or number in Parts I–II. '
                'The phase-lock period T<sub>lock</sub> = 232 as is taken from a time-dependent Schrödinger-equation calculation by Jiang et al. (Phys. Rev. Lett. 133, 163201, 2024); it is a theoretical, numerically computed value, not an experimental measurement.',
        p4_old='Part III — Addendum', p4_new='Part IV — Addendum',
        p4_note_old=None, p4_note_new=None,
        old_credit='<span class="n">Normalization relation 4π²r³c²/(T²Ghν)=1 written by Zhang Xiangqian (2026-03-03). All numerical values use CODATA 2018 constants.</span>',
        credit='''<div class="credit"><b>Author contributions.</b> Zhang Xiangqian contributed one static equation, the normalization relation (written 3 March 2026):
<div class="eq">4π² r³ c² ⁄ ( T² G h ν ) = 1</div>
Everything else, including the ether-frequency formulation, predictions P1–P6.2, the formula compendium, the element table, and the mother-equation (Z-Model) framework with its derivations and interpretations, is the work and responsibility of the first author. Parts III–IV do not represent the second author’s views.<br>
<span class="n">All numerical values use CODATA 2018 constants.</span></div>''',
        old_date='<b>Edition date:</b> 2026-11-06 (Initial preregistration: 2026-11-05)',
        date='<b>Edition:</b> v7, 2026-11-13 (initial preregistration 2026-11-05; v7 adds the full mother-equation paper and the 12 November addendum; Parts I–II unchanged)',
        title_old='<h1>Middle-Rung Law: Predictions of a Three-Rung Frequency Ladder and Formula Compendium</h1>',
        title='<h1>Middle-Rung Law: Predictions of a Three-Rung Frequency Ladder and Formula Compendium<br><span class="sub">with the full text of the Mother Equation (Z-Model)</span></h1>',
    ),
}

EXTRA_CSS = (
    'thead{display:table-header-group}tr{break-inside:avoid;page-break-inside:avoid}'
    'h1 .sub{font-size:11pt;font-weight:normal;color:#333}'
    '.credit{border:1px solid #888;background:#f7f7f7;padding:5pt 8pt;margin:6pt 0}'
    '.credit .eq{text-align:center;font-size:12.5pt;margin:4pt 0;font-family:"Times New Roman","STIX Two Math",serif}'
    '.zm math[display=block]{margin:5pt 0;font-size:108%}.zm math{font-family:"STIX Two Math","Latin Modern Math",serif}'
    '.zm blockquote{border-left:3px solid #999;margin:5pt 0;padding:1pt 8pt;color:#222}'
    '.zm h4{font-size:10pt;margin:6pt 0 2pt}.zm table{margin:5pt 0}'
    'h2,h3,h4{break-after:avoid;page-break-after:avoid}'
)


def add_thead(html):
    """把每张表第一行的 <tr><th>… 包进 <thead>，跨页时表头重复。"""
    return re.sub(r'<table>(<tr>(?:<th>.*?</th>)+</tr>)', r'<table><thead>\1</thead>', html)


def md_to_html(md_path):
    md = pathlib.Path(md_path).read_text(encoding='utf-8')
    md = re.sub(r'\A#\s+.*\n', '', md)          # 标题由外层 h2 接管
    r = subprocess.run(['pandoc', '-f', 'markdown+lists_without_preceding_blankline', '-t', 'html', '--mathml',
                        '--shift-heading-level-by=1', '--wrap=none'],
                       input=md, capture_output=True, text=True, check=True)
    return r.stdout


def build(lang):
    c = LANG[lang]
    html = (HERE / c['base']).read_text(encoding='utf-8')
    for k_old, k_new in (('title_old', 'title'), ('old_date', 'date'), ('old_credit', 'credit')):
        assert html.count(c[k_old]) == 1, (lang, k_old)
        html = html.replace(c[k_old], c[k_new])
    html = html.replace('</style>', EXTRA_CSS + '</style>', 1)
    html = add_thead(html)

    head, sep, tail = html.partition('<h2 class="pb">' + c['p4_old'])
    assert sep, lang
    addendum = sep.replace(c['p4_old'], c['p4_new']) + tail
    addendum = re.sub(r'\bIII\.([1-9])', r'IV.\1', addendum)
    if c['p4_note_old']:
        assert addendum.count(c['p4_note_old']) == 1
        addendum = addendum.replace(c['p4_note_old'], c['p4_note_new'])

    zm = md_to_html(HERE / c['md'])
    zm = add_thead(zm)
    part3 = (f'<h2 class="pb">{c["p3_head"]}</h2>\n<p class="n">{c["p3_note"]}</p>\n'
             f'<div class="zm">\n{zm}\n</div>\n')
    out_html = head + part3 + addendum
    out = HERE / (c['out'] + '.html')
    out.write_text(out_html, encoding='utf-8')
    pdf = HERE / (c['out'] + '.pdf')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                    f'--print-to-pdf={pdf}', out.as_uri()], check=True,
                   capture_output=True)
    print(lang, out.name, pdf.name)


if __name__ == '__main__':
    import sys
    for lang in (sys.argv[1:] or ['zh', 'en']):
        build(lang)
