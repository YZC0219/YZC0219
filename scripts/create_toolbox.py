"""Maintain an evidence-based, grouped technology wall and local SVG tiles."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEVICON = 'https://cdn.jsdelivr.net/gh/devicons/devicon@v2.17.0/icons/'


def skill(name):
    return 'https://skillicons.dev/icons?i=' + name


def motion(name):
    return f'https://techstack-generator.vercel.app/{name}-icon.svg'


SECTIONS = [
    ('数据分析与建模', [
        ('Python', motion('python')),
        ('pandas', DEVICON+'pandas/pandas-original.svg'),
        ('NumPy', DEVICON+'numpy/numpy-original.svg'),
        ('SciPy', 'assets/icons/scipy.svg'),
        ('MySQL', motion('mysql')),
        ('SQLite', skill('sqlite')),
        ('Scikit-learn', skill('sklearn')),
        ('LightGBM', 'assets/icons/lightgbm.svg'),
        ('PyTorch', skill('pytorch')),
        ('SHAP', 'assets/icons/shap.svg'),
        ('Matplotlib', DEVICON+'matplotlib/matplotlib-original.svg'),
        ('ECharts', 'assets/icons/apacheecharts.svg'),
    ], 'PyTorch 与深度模型按可选依赖启用；ECharts 用于生产运营看板。'),
    ('数仓与实时处理', [
        ('Hadoop', DEVICON+'hadoop/hadoop-original.svg'),
        ('Hive', 'assets/icons/apachehive.svg'),
        ('Spark', DEVICON+'apachespark/apachespark-original.svg'),
        ('DataX', 'assets/icons/datax.svg'),
        ('Airflow', DEVICON+'apacheairflow/apacheairflow-original.svg'),
        ('Kafka', skill('kafka')),
        ('Flink', 'assets/icons/apacheflink.svg'),
        ('Iceberg', 'assets/icons/iceberg.svg'),
        ('ClickHouse', DEVICON+'clickhouse/clickhouse-original.svg'),
        ('Redis', skill('redis')),
        ('Metabase', 'assets/icons/metabase.svg'),
        ('Great Expectations', 'assets/icons/great-expectations.svg'),
    ], '分层数仓、实时处理与湖仓扩展的单节点 / 本机实验；运行方式和验证范围见主项目文档。'),
    ('服务、前端与工程工具', [
        ('FastAPI', skill('fastapi')),
        ('Flask', skill('flask')),
        ('Uvicorn', 'assets/icons/uvicorn.svg'),
        ('PostgreSQL', skill('postgres')),
        ('HTML', skill('html')),
        ('CSS', skill('css')),
        ('JavaScript', motion('js')),
        ('openpyxl', 'assets/icons/openpyxl.svg'),
        ('Docker', motion('docker')),
        ('Linux', skill('linux')),
        ('PowerShell', skill('powershell')),
        ('Git', skill('git')),
        ('GitHub', motion('github')),
        ('GitHub Actions', DEVICON+'githubactions/githubactions-original.svg'),
        ('pytest', DEVICON+'pytest/pytest-original.svg'),
        ('Playwright', DEVICON+'playwright/playwright-original.svg'),
    ], 'PostgreSQL 用于 Airflow 元数据库；openpyxl 支持看板 Excel 导入；pytest / Playwright 用于回归与浏览器验收。'),
]


def write_tiles():
    folder = ROOT/'assets/icons'
    folder.mkdir(exist_ok=True)
    logos = json.loads((ROOT/'scripts/brand_paths.json').read_text(encoding='utf-8'))
    palette = {'scipy':'#8caae6','apachehive':'#f5d45b','apacheflink':'#f0758c','metabase':'#71b9f6','apacheecharts':'#f46d86'}
    for slug, paths in logos.items():
        glyph = ''.join(f'<path d="{escape(path,quote=True)}"/>' for path in paths)
        source = f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" role="img" aria-label="{slug}"><rect width="64" height="64" rx="14" fill="#202938"/><g transform="translate(12 12) scale(1.666667)" fill="{palette[slug]}">{glyph}</g></svg>'
        (folder/f'{slug}.svg').write_text(source,encoding='utf-8')
    tiles = [
        ('lightgbm','LGB','LightGBM','#78dcaa'),
        ('shap','SH','SHAP','#f08ab6'),
        ('datax','DX','DataX','#79baff'),
        ('iceberg','ICE','Apache Iceberg','#91d5f5'),
        ('great-expectations','GX','Great Expectations','#f5b663'),
        ('uvicorn','UV','Uvicorn','#85ddb8'),
        ('openpyxl','XLS','openpyxl','#84d49c'),
    ]
    for filename,label,title,color in tiles:
        source = f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" role="img" aria-label="{escape(title)} abbreviation tile"><rect width="64" height="64" rx="14" fill="#202938"/><path d="M13 49H51" stroke="{color}" stroke-opacity=".4" stroke-width="2"/><text x="32" y="39" text-anchor="middle" fill="{color}" font-family="Segoe UI,Arial,sans-serif" font-size="{22 if len(label)>2 else 26}" font-weight="700">{label}</text></svg>'
        (folder/f'{filename}.svg').write_text(source,encoding='utf-8')


def main():
    write_tiles()
    lines = ['<!-- TOOLBOX:START -->']
    for heading,tools,note in SECTIONS:
        lines.extend([f'### {heading}', '', '<table align="center">'])
        for i in range(0,len(tools),4):
            lines.append('  <tr>')
            for name,url in tools[i:i+4]:
                label = escape(name).replace('Great Expectations','Great<br />Expectations').replace('GitHub Actions','GitHub<br />Actions')
                lines.append(f'    <td align="center" width="140"><img src="{escape(url,quote=True)}" width="48" height="48" alt="{escape(name)}" /><br /><sub>{label}</sub></td>')
            lines.append('  </tr>')
        lines.extend(['</table>', '', note, ''])
    lines.extend(['<p align="center"><sub>图标表示项目涉及的技术与工具，不代表熟练度评级；部分扩展需要独立环境或可选依赖。</sub></p>', '<!-- TOOLBOX:END -->', ''])
    block = '\n'.join(lines)
    p = ROOT/'README.md'
    text = p.read_text(encoding='utf-8')
    if '<!-- TOOLBOX:START -->' in text:
        text = re.sub(r'<!-- TOOLBOX:START -->.*?<!-- TOOLBOX:END -->\n?',lambda _:block,text,flags=re.S)
    else:
        a = text.index('<table',text.index('## 03 / TOOLBOX'))
        b = text.index('<details>',a)
        text = text[:a]+block+'\n'+text[b:]
    text = text.replace('技术图标：[TechStack Generator](https://techstack-generator.vercel.app/) 与 [Skill Icons](https://github.com/tandpfun/skill-icons)。','技术图标：[TechStack Generator](https://techstack-generator.vercel.app/)、[Skill Icons](https://github.com/tandpfun/skill-icons)、[Devicon](https://github.com/devicons/devicon) 与 [Simple Icons](https://github.com/simple-icons/simple-icons)。少数工具使用原创缩写标识；来源见[图标说明](assets/icons/NOTICE.md)。')
    p.write_text(text,encoding='utf-8')
    print('Updated technology wall:',sum(len(tools) for _,tools,_ in SECTIONS),'items in',len(SECTIONS),'groups')


if __name__=='__main__':
    main()
