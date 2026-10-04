"""Daily GitHub contribution calendar and curated project activity. Stdlib only."""
from collections import Counter
from datetime import datetime, timezone, timedelta
from html import escape
import json,os,re,subprocess,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
USER="YZC0219"
TZ=timezone(timedelta(hours=8))
FEATURED={"industrial_energy_analysis":"EnergyTrace · 能迹","production-operations-dashboard":"生产运营看板","annual-influenza-dashboard":"流感监测大屏"}

def api(path,data=None):
    headers={"Accept":"application/vnd.github+json","User-Agent":"YZC0219-profile"}
    token=os.environ.get("GH_TOKEN")
    if token:headers["Authorization"]=f"Bearer {token}"
    if data:headers["Content-Type"]="application/json"
    req=urllib.request.Request("https://api.github.com/"+path,headers=headers,data=json.dumps(data).encode() if data else None)
    with urllib.request.urlopen(req,timeout=30) as response:return json.load(response)

def calendar():
    query='query { user(login:"YZC0219") { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } } } }'
    if os.environ.get("GH_TOKEN"):payload=api("graphql",{"query":query})
    else:payload=json.loads(subprocess.check_output(["gh","api","graphql","-f","query="+query],text=True,encoding="utf-8"))
    if payload.get("errors"):raise RuntimeError(str(payload["errors"]))
    return payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]

def svg(body,height,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img" aria-label="{escape(title)}"><rect x=".5" y=".5" width="999" height="{height-1}" rx="16" fill="#0b1523" stroke="#2b4358"/><g font-family="Segoe UI,Arial,Microsoft YaHei,sans-serif">{body}</g></svg>'

def text(x,y,value,size=12,fill="#9bb0c8",weight="400"):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}">{escape(str(value))}</text>'

def main():
    user=api(f"users/{USER}")
    repos=[]
    for page in range(1,101):
        batch=api(f"users/{USER}/repos?type=owner&amp;per_page=100&amp;page={page}".replace("&amp;","&"))
        repos.extend(r for r in batch if not r["fork"] and not r["private"])
        if len(batch)<100:break
    cal=calendar()
    days=[d for w in cal["weeks"] for d in w["contributionDays"]]
    date=datetime.now(TZ).strftime("%Y-%m-%d")
    active=sum(d["contributionCount"]>0 for d in days[-30:])
    body=text(34,36,"PUBLIC BUILD LOG / 公开开发节奏",13,"#6be4c1")+text(787,36,date+" · UTC+8",12)
    values=[("YEAR CONTRIBUTIONS",cal["totalContributions"]),("ACTIVE DAYS / LAST 30",active),("PUBLIC REPOS",len(repos)),("TOTAL STARS",sum(r["stargazers_count"] for r in repos))]
    for i,(label,value) in enumerate(values):
        x=34+i*242
        body+=text(x,76,label,10)+text(x,117,value,32,"#edf4ff","600")
        if i<3:body+=f'<path d="M{x+217} 60V119" stroke="#2b4358"/>'
    colors=["#17293b","#23515a","#327d7c","#4bb9a5","#6be4c1"]
    months=set()
    for wi,week in enumerate(cal["weeks"]):
        for day in week["contributionDays"]:
            parsed=datetime.fromisoformat(day["date"])
            x=80+wi*16;y=175+((parsed.weekday()+1)%7)*16
            count=day["contributionCount"]
            level=0 if count==0 else 1 if count<3 else 2 if count<7 else 3 if count<15 else 4
            body+=f'<rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="{colors[level]}"><title>{day["date"]}: {count} GitHub contributions</title></rect>'
            month=parsed.strftime("%Y-%m")
            if month not in months:
                months.add(month)
                if wi<51:body+=text(x,157,parsed.strftime("%b"),10)
    for label,row in [("MON",1),("WED",3),("FRI",5)]:body+=text(34,184+row*16,label,9)
    body+=text(34,320,"GitHub 原生贡献日历 · "+days[0]["date"]+" → "+days[-1]["date"],11)
    body+=text(787,319,"LESS",9)
    for i,c in enumerate(colors):body+=f'<rect x="{820+i*17}" y="309" width="12" height="12" rx="2" fill="{c}"/>'
    body+=text(911,319,"MORE",9)
    languages=Counter(r["language"] for r in repos if r["language"])
    body+=text(34,354,"REPO LANGUAGES / "+" · ".join(f"{name} {count}" for name,count in languages.most_common(4)),11)
    activity=svg(body,380,f"GitHub contribution calendar: {cal['totalContributions']} contributions over the past year, {active} active days in the last 30, {len(repos)} public non-fork repositories. Updated {date}.")
    recent=sorted((r for r in repos if r["name"] in FEATURED),key=lambda r:r["pushed_at"] or "",reverse=True)
    body=text(34,35,"PROJECT SIGNALS / 作品更新",13,"#87aaff")+text(802,35,date+" · UTC+8",11)
    lines=[f"<!-- ACTIVITY:START -->\n最近刷新：**{date} · Asia/Shanghai**。贡献日历与作品更新每天自动同步。\n"]
    for i,repo in enumerate(recent):
        x=24+i*326
        pushed=datetime.fromisoformat(repo["pushed_at"].replace("Z","+00:00")).astimezone(TZ).strftime("%Y-%m-%d")
        commit=api(f"repos/{USER}/{repo['name']}/commits?per_page=1")[0]
        message=commit["commit"]["message"].splitlines()[0]
        body+=f'<a href="{escape(repo["html_url"],quote=True)}"><rect x="{x}" y="58" width="304" height="135" rx="9" fill="#101e2d" stroke="#2b4358"/>'
        body+=text(x+16,86,FEATURED[repo["name"]],17,"#edf4ff","600")+text(x+16,112,"最近推送 / "+pushed,11)
        # Short line wrap keeps long commit subjects inside their card.
        words=message.split();chunks=[];current=""
        for word in words:
            if len(current)+len(word)>35 and current:chunks.append(current);current=word
            else:current+=(" " if current else "")+word
        if current:chunks.append(current)
        for j,line in enumerate(chunks[:2]):body+=text(x+16,143+j*19,line[:36]+("…" if j==1 and len(chunks)>2 else ""),11,"#b1c4d7")
        body+='</a>'
        title=message.replace("[","\\[").replace("]","\\]")
        lines.append(f"- [{FEATURED[repo['name']]}]({repo['html_url']}) · {pushed} · [{title}]({commit['html_url']})")
    lines.append("<!-- ACTIVITY:END -->")
    readme=ROOT/"README.md";source=readme.read_text(encoding="utf-8")
    source,count=re.subn(r"<!-- ACTIVITY:START -->.*?<!-- ACTIVITY:END -->",lambda _:"\n".join(lines),source,flags=re.S)
    if count!=1:raise ValueError("Exactly one activity marker pair required")
    # Only save after all remote reads and rendering succeed.
    (ROOT/"assets/activity.svg").write_text(activity,encoding="utf-8")
    (ROOT/"assets/recent-projects.svg").write_text(svg(body,215,"Curated project updates and latest commit subjects, refreshed "+date),encoding="utf-8")
    readme.write_text(source,encoding="utf-8")
    print(f"Updated calendar ({cal['totalContributions']} contributions), {len(recent)} project cards, {date}")
if __name__=="__main__":main()
