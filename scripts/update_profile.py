"""Refresh only public GitHub metadata; Python standard library only."""
from collections import Counter
from datetime import datetime, timezone, timedelta
from html import escape
import json
import os
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
USER = "YZC0219"


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "YZC0219-profile"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com/" + path, headers=headers), timeout=30) as response:
        return json.load(response)


def main():
    user = api(f"users/{USER}")
    repositories = []
    for page in range(1, 101):
        batch = api(f"users/{USER}/repos?type=owner&per_page=100&page={page}")
        repositories.extend(r for r in batch if not r["fork"] and not r["private"])
        if len(batch) < 100:
            break
    date = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    languages = Counter(r["language"] for r in repositories if r["language"])
    stars = sum(r["stargazers_count"] for r in repositories)
    values = [("PUBLIC REPOS", len(repositories)), ("TOTAL STARS", stars), ("FOLLOWERS", user["followers"])]
    fragments = []
    for index, (label, value) in enumerate(values):
        x = 42 + index * 230
        fragments.append(f'<text x="{x}" y="76" fill="#8da5b5" font-size="12" letter-spacing="2">{label}</text><text x="{x}" y="127" fill="#eff7fc" font-size="40" font-weight="600">{value}</text>')
    language_text = " / ".join(f"{name} {count}" for name, count in languages.most_common(4)) or "No language data yet"
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="212" viewBox="0 0 1000 212" role="img" aria-labelledby="title desc">
<title id="title">Public GitHub activity for {USER}</title><desc id="desc">{len(repositories)} public non-fork repositories, {stars} stars, {user['followers']} followers. Languages by repository count: {escape(language_text)}. Updated {date}.</desc>
<rect width="1000" height="212" rx="16" fill="#0b1722"/><path d="M272 56V137M502 56V137M731 40V172" stroke="#284252"/>
<g font-family="Segoe UI,Arial,sans-serif">{''.join(fragments)}<text x="764" y="72" fill="#57e2c0" font-size="12" letter-spacing="2">PUBLIC SNAPSHOT</text><text x="764" y="110" fill="#eff7fc" font-size="22">{date}</text><text x="764" y="138" fill="#8da5b5" font-size="12">Asia/Shanghai</text><text x="42" y="179" fill="#8da5b5" font-size="13">REPO LANGUAGES · {escape(language_text)}</text></g></svg>'''
    (ROOT / "assets/activity.svg").write_text(svg, encoding="utf-8")
    recent = sorted((r for r in repositories if r["name"] != USER), key=lambda r: r["pushed_at"] or "", reverse=True)[:3]
    lines = [f"<!-- ACTIVITY:START -->\n最后刷新：**{date} · Asia/Shanghai**\n", "| 最近有推送的项目 | 推送日期（上海时间） |", "|---|---|"]
    for repo in recent:
        pushed = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00")).astimezone(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
        name = repo["name"].replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")
        lines.append(f"| [{name}]({repo['html_url']}) | {pushed} |")
    lines.append("<!-- ACTIVITY:END -->")
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    text, count = re.subn(r"<!-- ACTIVITY:START -->.*?<!-- ACTIVITY:END -->", lambda _: "\n".join(lines), text, flags=re.S)
    if count != 1:
        raise ValueError("Exactly one activity marker pair is required")
    readme.write_text(text, encoding="utf-8")
    print(f"Updated public metadata: {len(repositories)} repositories, {date}")


if __name__ == "__main__":
    main()
