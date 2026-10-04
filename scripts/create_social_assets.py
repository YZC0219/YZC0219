"""Original animated conversation and typing SVGs, with light/dark themes."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]


def conversation(dark):
    bg = '#0b1523' if dark else '#f6f8fc'
    border = '#2b4358' if dark else '#d8e3ed'
    ink = '#edf4ff' if dark else '#182d42'
    muted = '#9bb0c8' if dark else '#61758b'
    bubble = '#152b3b' if dark else '#e8f0f6'
    accent = '#6be4c1' if dark else '#087e72'
    outgoing = '#293956' if dark else '#e6edff'
    rows = [
        (32, 84, 350, '嗨，我是 YZC0219 👋', .6, False),
        (32, 146, 620, '大数据专业学生，正在把问题变成作品。', 2.8, False),
        (604, 208, 264, '最近在做什么？', 5.2, True),
        (32, 270, 705, '能迹 EnergyTrace · 工业能耗分析与可视化', 7.5, False),
        (32, 332, 625, 'AI 辅助实现，用证据核验，持续学习。', 10.0, False),
    ]
    styles = []
    groups = []
    for i, (x, y, width, value, onset, right) in enumerate(rows):
        start = onset / 16 * 100
        styles.append(f'@keyframes m{i} {{ 0%,{start:.2f}% {{opacity:0;transform:translateY(6px)}} {start+2:.2f}%,88% {{opacity:1;transform:translateY(0)}} 97%,100% {{opacity:0;transform:translateY(0)}} }} .m{i} {{opacity:0;animation:m{i} 16s linear infinite}}')
        a, b = max(0, start-9), max(1, start-1)
        styles.append(f'@keyframes t{i} {{0% {{opacity:0}} {a:.2f}%,{b:.2f}% {{opacity:1}} {start:.2f}%,100% {{opacity:0}} }} .t{i} {{opacity:0;animation:t{i} 16s linear infinite}}')
        color = outgoing if right else bubble
        tail = f'M{x+width-14} {y+39}l14 13v-18' if right else f'M{x+14} {y+39}l-14 13v-18'
        groups.append(f'<g class="m{i}"><path d="{tail}" fill="{color}"/><rect x="{x}" y="{y}" width="{width}" height="49" rx="17" fill="{color}"/><text x="{x+21}" y="{y+32}" fill="{ink}" font-size="23">{escape(value)}</text></g>')
        groups.append(f'<g class="t{i}"><rect x="{x}" y="{y}" width="104" height="49" rx="17" fill="{color}"/>' + ''.join(f'<circle class="dot d{j}" cx="{x+30+j*22}" cy="{y+25}" r="5" fill="{muted}"/>' for j in range(3)) + '</g>')
    styles.append('@keyframes pulse {0%,100%{opacity:.35}50%{opacity:1}} .dot{animation:pulse .8s ease-in-out infinite}.d1{animation-delay:.15s}.d2{animation-delay:.3s}')
    styles.append('@media (prefers-reduced-motion:reduce){[class^="m"]{animation:none;opacity:1}[class^="t"]{display:none}.dot{animation:none}}')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="437" viewBox="0 0 900 437" role="img" aria-labelledby="title desc">
<title id="title">Hi, I'm YZC0219</title><desc id="desc">Animated introduction: big data student, building EnergyTrace, using AI assistance and checking results with evidence.</desc>
<style>{''.join(styles)}</style><rect x=".5" y=".5" width="899" height="436" rx="20" fill="{bg}" stroke="{border}"/>
<g font-family="Segoe UI,Arial,Microsoft YaHei,sans-serif"><circle cx="48" cy="39" r="16" fill="{accent}"/><text x="40" y="46" fill="{bg}" font-size="20" font-weight="600">Y</text><text x="76" y="36" fill="{ink}" font-size="17" font-weight="600">YZC0219</text><text x="76" y="55" fill="{muted}" font-size="11">LET'S TALK DATA</text><circle cx="731" cy="36" r="4" fill="{accent}"/><text x="745" y="40" fill="{muted}" font-size="12">Learning in public</text>
{''.join(groups)}<path d="M32 398H868" stroke="{border}"/><text x="32" y="422" fill="{accent}" font-size="11" letter-spacing="2">ASK · BUILD · VERIFY</text><text x="681" y="422" fill="{muted}" font-size="11">ORIGINAL LOOP / 16s</text></g></svg>'''


def typing(dark):
    ink = '#6be4c1' if dark else '#087e72'
    phrases = ['DATA ENGINEERING', 'ANALYTICS & VISUALIZATION', 'LEARNING IN PUBLIC', 'BUILD WITH AI. VERIFY WITH EVIDENCE.']
    styles, clips, lines = [], [], []
    for i, phrase in enumerate(phrases):
        start, end = i*25, i*25+24
        if i == 0:
            rule = '0%,24%{opacity:1}25%,100%{opacity:0}'
        elif i == 3:
            rule = '0%,74%{opacity:0}75%,99%{opacity:1}100%{opacity:0}'
        else:
            rule = f'0%,{start-1}%{{opacity:0}}{start}%,{end}%{{opacity:1}}{end+1}%,100%{{opacity:0}}'
        styles.append(f'@keyframes l{i}{{{rule}}}.l{i}{{opacity:0;animation:l{i} 16s linear infinite}}')
        width = len(phrase)*15.7
        x = (900-width)/2
        clips.append(f'<clipPath id="c{i}"><rect x="{x}" y="0" width="0" height="65"><animate attributeName="width" values="0;0;{width};{width};0;0" keyTimes="0;.02;.16;.21;.249;1" begin="{i*4}s" dur="16s" repeatCount="indefinite"/></rect></clipPath>')
        lines.append(f'<g class="l{i}"><text clip-path="url(#c{i})" x="{x}" y="40" font-size="26" fill="{ink}" font-family="Consolas,DejaVu Sans Mono,monospace">{escape(phrase)}</text><rect x="{x}" y="18" width="2" height="27" fill="{ink}"><animate attributeName="x" values="{x};{x};{x+width};{x+width};{x};{x}" keyTimes="0;.02;.16;.21;.249;1" begin="{i*4}s" dur="16s" repeatCount="indefinite"/></rect></g>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="65" viewBox="0 0 900 65" role="img" aria-label="Data engineering, analytics and visualization, learning in public, building with AI and verifying with evidence"><defs>{"".join(clips)}</defs><style>{"".join(styles)}</style>{"".join(lines)}</svg>'


def main():
    for theme, dark in [('dark', True), ('light', False)]:
        (ROOT / f'assets/chat-{theme}.svg').write_text(conversation(dark), encoding='utf-8')
        (ROOT / f'assets/typing-{theme}.svg').write_text(typing(dark), encoding='utf-8')
    print('Created original animated conversation and typing assets, both themes')


if __name__ == '__main__':
    main()
