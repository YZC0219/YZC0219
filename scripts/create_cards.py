"""Generate code-native SVG portfolio art. No downloaded media."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]


def svg(name, width, height, body, title):
    source = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0b1423"/><stop offset="1" stop-color="#122a38"/></linearGradient><linearGradient id="accent"><stop stop-color="#6be4c1"/><stop offset="1" stop-color="#87aaff"/></linearGradient></defs>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="18" fill="url(#bg)" stroke="#2b4358"/>
<g font-family="Segoe UI,Arial,Microsoft YaHei,sans-serif">{body}</g></svg>'''
    (ROOT / 'assets' / name).write_text(source, encoding='utf-8')


def main():
    svg('energytrace.svg', 1000, 330, '''
<text x="36" y="43" fill="#6be4c1" font-size="12" letter-spacing="3">01 / FEATURED PROJECT</text>
<text x="32" y="110" fill="#edf4ff" font-size="50" font-weight="700">EnergyTrace <tspan font-size="26" fill="#a8bed0">能迹</tspan></text>
<text x="36" y="153" fill="#edf4ff" font-size="21">工业能耗 · 数据工程 · 可解释分析</text>
<text x="36" y="188" fill="#9bb0c8" font-size="15">清洗 → 数仓 → 分析 → 诊断 → 验证</text>
<g fill="#0b1423" stroke="#2b4358"><rect x="36" y="226" width="105" height="64" rx="8"/><rect x="155" y="226" width="105" height="64" rx="8"/><rect x="274" y="226" width="105" height="64" rx="8"/><rect x="393" y="226" width="105" height="64" rx="8"/></g>
<g fill="#6be4c1" font-size="23" font-weight="600"><text x="52" y="253">8</text><text x="171" y="253">6</text><text x="290" y="253">731</text><text x="409" y="253">29</text></g>
<g fill="#9bb0c8" font-size="11"><text x="52" y="276">WORKSHOPS</text><text x="171" y="276">ENERGIES</text><text x="290" y="276">DAYS</text><text x="409" y="276">SQL QUERIES</text></g>
<rect x="585" y="52" width="374" height="238" rx="12" fill="#0a1421" stroke="#2b4358"/><text x="607" y="79" fill="#9bb0c8" font-size="10" letter-spacing="2">ANALYTICS / VISUAL CONCEPT</text>
<g fill="#182b3e"><rect x="607" y="96" width="97" height="40" rx="6"/><rect x="717" y="96" width="97" height="40" rx="6"/><rect x="827" y="96" width="110" height="40" rx="6"/></g>
<g fill="#6be4c1"><rect x="620" y="108" width="31" height="4" rx="2"/><rect x="730" y="108" width="31" height="4" rx="2"/><rect x="840" y="108" width="31" height="4" rx="2"/></g>
<g stroke="#263c50"><path d="M607 162H937M607 192H937M607 222H937M607 252H937"/></g>
<path d="M607 245L631 220L655 231L679 205L703 214L727 175L751 193L775 163L799 181L823 162L847 197L871 177L895 157L919 174L937 151" fill="none" stroke="url(#accent)" stroke-width="3"/>
<text x="607" y="274" fill="#7995ac" font-size="10">ILLUSTRATION · BASE DATA IS SIMULATED</text>
''', 'EnergyTrace portfolio card. 8 workshops, 6 energy types, 731 days and 29 SQL queries. Chart is an illustration.')
    svg('operations.svg', 490, 270, '''
<text x="27" y="35" fill="#87aaff" font-size="11" letter-spacing="2">02 / OPERATIONS</text><text x="25" y="75" fill="#edf4ff" font-size="27" font-weight="600">生产运营看板</text>
<text x="27" y="105" fill="#9bb0c8" font-size="14">设备 · 排产 · 质量 · 库存</text>
<g stroke="#2b4358" fill="#0b1523"><rect x="27" y="125" width="134" height="63" rx="8"/><rect x="176" y="125" width="134" height="63" rx="8"/><rect x="325" y="125" width="134" height="63" rx="8"/></g>
<g fill="#87aaff"><circle cx="46" cy="143" r="4"/><circle cx="195" cy="143" r="4"/><circle cx="344" cy="143" r="4"/></g><g stroke="#56718b" stroke-width="4"><path d="M40 166H116M189 166H265M338 166H414"/></g>
<text x="27" y="222" fill="#9bb0c8" font-size="12">FLASK / SQLITE / ECHARTS / EXCEL</text><text x="27" y="248" fill="#87aaff" font-size="12">查看项目与验证范围 ↗</text>
''', 'Production operations dashboard: equipment, scheduling, quality and inventory. Flask, SQLite, ECharts and Excel.')
    svg('influenza.svg', 490, 270, '''
<text x="27" y="35" fill="#6be4c1" font-size="11" letter-spacing="2">03 / VISUAL STORYTELLING</text><text x="25" y="75" fill="#edf4ff" font-size="27" font-weight="600">年度流感监测大屏</text>
<text x="27" y="105" fill="#9bb0c8" font-size="14">年份 · 地区 · 年龄组 · 联动筛选</text>
<path d="M28 182H458M28 152H458M28 122H458" stroke="#263c50"/><path d="M28 172L56 162L84 168L112 144L140 153L168 125L196 144L224 151L252 142L280 163L308 156L336 174L364 160L392 167L420 151L458 145" stroke="#6be4c1" stroke-width="3" fill="none"/>
<text x="27" y="222" fill="#9bb0c8" font-size="12">HTML / CSS / JAVASCRIPT · SIMULATED DATA</text><text x="27" y="248" fill="#6be4c1" font-size="12">查看项目与交互设计 ↗</text>
''', 'Annual influenza visualization demo with simulated data. Filter by year, region and age group. Decorative chart.')
    body = '<text x="34" y="39" fill="#6be4c1" font-size="11" letter-spacing="3">THE WAY I CONNECT THINGS</text>'
    for i, (label, chinese, line1, line2) in enumerate([
        ('01 / FOUNDATION','建立数据基础','Python · pandas · SQL','清洗 / 建模 / 指标口径'),
        ('02 / PIPELINE','串起处理链路','MySQL · Airflow','Hive / Spark / DataX'),
        ('03 / INTELLIGENCE','核验模型与证据','时序预测 · 异常检测','滚动验证 / 证据归因'),
        ('04 / EXPERIENCE','把结果交付出去','FastAPI · BI · Web','交互 / 反馈 / 回归检查')]):
        x=34+i*242
        body += f'<rect x="{x}" y="62" width="210" height="149" rx="9" fill="#0b1523" stroke="#2b4358"/><text x="{x+16}" y="88" fill="#87aaff" font-size="11">{label}</text><text x="{x+16}" y="123" fill="#edf4ff" font-size="18" font-weight="600">{chinese}</text><text x="{x+16}" y="160" fill="#9bb0c8" font-size="12">{line1}</text><text x="{x+16}" y="184" fill="#9bb0c8" font-size="12">{line2}</text>'
        if i<3: body += f'<path d="M{x+216} 137H{x+237}M{x+233} 133L{x+237} 137L{x+233} 141" fill="none" stroke="#6be4c1"/>'
    body += '<text x="34" y="242" fill="#7995ac" font-size="11">LEARNING PATH · NOT A SKILL RATING</text>'
    svg('learning-map.svg',1000,264,body,'Learning path from data foundations to pipelines, model evidence and interactive delivery.')


if __name__ == '__main__':
    main()
