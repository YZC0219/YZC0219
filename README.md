<p align="center">
  <img src="assets/intro.gif" width="100%" alt="YZC0219 数据实验室：构建数据链路、核验异常证据、解释分析结果的三幕原创动画" />
</p>

<p align="center">
  <a href="https://github.com/YZC0219/industrial_energy_analysis"><strong>探索 EnergyTrace</strong></a>　✦　
  <a href="https://yzc0219.github.io/industrial_energy_analysis/"><strong>打开在线作品 ↗</strong></a>　✦　
  <a href="https://github.com/YZC0219?tab=repositories">浏览全部仓库</a>
</p>

<p align="center"><sub>DATA ENGINEERING　/　ANALYTICS　/　VISUAL STORYTELLING</sub></p>

## 01 / ABOUT　把问题变成可以验证的答案

你好，我是 **YZC0219**，一名大数据专业学生。现在围绕工业能耗与生产运营场景，把数据清洗、数仓建模、统计分析和交互展示串成完整作品。

我喜欢追问数据背后的细节：**异常来自业务还是清洗？任务成功后，结果真的更新了吗？图表上的结论能否追溯到原始记录？** 这些问题逐渐变成了我的项目习惯：先定义口径，再复现流程，用证据检查结果，最后把结论讲清楚。

开发过程中，我使用 AI 辅助实现，通过提出问题、审查结果、复现和排错逐步理解代码。这里也记录那些让我真正学到东西的错误、修复和未完成事项。

> **目前的关注点：**工业数据链路的可靠性、异常与预测的证据核验，以及数据产品的交互表达。

## 02 / SELECTED WORK　从一个场景持续深入

<a href="https://github.com/YZC0219/industrial_energy_analysis"><img src="assets/energytrace.svg" width="100%" alt="EnergyTrace 能迹：8 个车间、6 种能源、731 天、29 组 SQL 分析；基础数据为模拟数据，卡片图表为视觉示意" /></a>

**能迹 EnergyTrace** 是我目前持续完善的主项目。从主动构造脏数据开始，经过可追溯清洗、MySQL 星型模型与 SQL 分析，交付交互报告，再向分层数仓、时序预测、实时管道和诊断反馈扩展。

| 建立链路 | 核验结果 | 交付洞察 |
|---|---|---|
| 清洗留痕、幂等装载、历史修正 | 29 组查询快照、质量门禁、回归检查 | 能耗 / 单耗 / 费用 / 碳排放分析 |
| Hive / Spark / DataX、Airflow | 三引擎对照、迟到数据修正实验 | 报告、FastAPI、Metabase 与统一指标 |
| Kafka / Flink 与持久化告警 | 故障注入、恢复、重放与对账 | 异常证据问答、人工处置与历史记录 |

[源码与运行说明 →](https://github.com/YZC0219/industrial_energy_analysis)　[交互报告 ↗](https://yzc0219.github.io/industrial_energy_analysis/)　[工程复盘 →](https://github.com/YZC0219/industrial_energy_analysis/blob/main/docs/问题发现与工程复盘.md)

<p>
  <a href="https://github.com/YZC0219/production-operations-dashboard"><img src="assets/operations.svg" width="49%" alt="生产运营看板：设备、排产、质量与库存；Flask、SQLite、ECharts、Excel" /></a>
  <a href="https://github.com/YZC0219/annual-influenza-dashboard"><img src="assets/influenza.svg" width="49%" alt="年度流感监测大屏：年份、地区、年龄组联动筛选；模拟数据展示" /></a>
</p>

- **生产运营看板**：围绕设备、排产、质量和库存，加入 Excel 导入校验、角色权限、告警与运行维护入口。功能与实机验证范围以仓库说明为准。
- **年度流感监测大屏**：探索月度趋势、地区分布、年龄组对比与联动筛选；数值为模拟数据，用于展示设计和交互。

## 03 / TOOLBOX　我正在连接的技术

<img src="assets/learning-map.svg" width="100%" alt="学习路线：数据基础、处理链路、模型证据、交互交付。学习方向不代表技能熟练度评级。" />

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&amp;logo=pandas&amp;logoColor=white" alt="pandas" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&amp;logo=mysql&amp;logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Spark-E25A1C?style=flat-square&amp;logo=apachespark&amp;logoColor=white" alt="Spark" />
  <img src="https://img.shields.io/badge/Kafka-25364A?style=flat-square&amp;logo=apachekafka&amp;logoColor=white" alt="Kafka" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&amp;logo=fastapi&amp;logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/JavaScript-DCC35B?style=flat-square&amp;logo=javascript&amp;logoColor=142D3A" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&amp;logo=docker&amp;logoColor=white" alt="Docker" />
</p>

<details>
<summary><strong>展开我的实践方向与下一步</strong></summary>

| 方向 | 已在项目中尝试 | 接下来想做 |
|---|---|---|
| 数据工程 | 星型模型、分层数仓、增量修正、CDC 与调度 | 更完整的独立复现、故障恢复和运行保障 |
| 模型与证据 | 滚动时序验证、异常检测、证据归因 | 接入真实事件标签，检查跨数据场景的适用性 |
| 数据产品 | 网页报告、BI、诊断工作台与反馈 | 完善筛选语义、交互体验和处置流程 |

这些是学习与实践方向。单节点实验、模拟结果、真实数据案例都有各自适用范围；生产部署、真实节能效果与多节点高可用尚需进一步验证。

</details>

## 04 / FIELD NOTES　错误也是项目的一部分

**01 · 一次清洗修复。** 删除离群值整行，让 34 个“车间 × 日期”缺少能源品种，随后产生假异常。改为异常单元格置空再插补，缺失品种的车间日降到 0，并用回归测试固化。

**02 · 一次链路排查。** 新数据进入事实表，报告却没变：日期维表未覆盖新增日期，`INNER JOIN` 过滤了记录。这个问题让我学会同时检查任务状态、数据覆盖与最终结果。

[完整工程复盘 →](https://github.com/YZC0219/industrial_energy_analysis/blob/main/docs/问题发现与工程复盘.md)　[两个月学习计划 →](https://github.com/YZC0219/industrial_energy_analysis/blob/main/docs/两个月项目学习计划.md)

## 05 / BUILD LOG　让持续投入看得见

<img src="assets/activity.svg" width="100%" alt="过去一年 GitHub 贡献热力图、近 30 日活跃天数、公开仓库与 Stars；每日自动刷新" />

<img src="assets/recent-projects.svg" width="100%" alt="三个代表项目的最近推送日期与最新提交主题；每日自动刷新" />

<details>
<summary>查看最新提交与统计说明</summary>

<!-- ACTIVITY:START -->
最近刷新：**2026-10-04 · Asia/Shanghai**。贡献日历与作品更新每天自动同步。

- [EnergyTrace · 能迹](https://github.com/YZC0219/industrial_energy_analysis) · 2026-10-04 · [Deploy visualization report to GitHub Pages](https://github.com/YZC0219/industrial_energy_analysis/commit/4a79a5be4c556b6f7005b038df09480859baedfa)
- [生产运营看板](https://github.com/YZC0219/production-operations-dashboard) · 2026-09-22 · [feat: add device configuration alarms OEE backups and Windows service](https://github.com/YZC0219/production-operations-dashboard/commit/fc717abab31017fb149fc3b3b399c8e37e263734)
- [流感监测大屏](https://github.com/YZC0219/annual-influenza-dashboard) · 2026-09-16 · [Fix regional comparisons and responsive layout](https://github.com/YZC0219/annual-influenza-dashboard/commit/2b04b47e2378c8705b38af365e5d658ace48485d)
<!-- ACTIVITY:END -->

贡献热力图来自 GitHub 原生贡献日历，覆盖过去一年；贡献并不等同于提交次数。仓库统计覆盖公开、非 Fork 仓库，语言按仓库主要语言计数。作品卡片展示精选项目的推送日期与最新提交主题。

页面每日通过 GitHub Actions 刷新，也支持手动触发。顶部 GIF 与作品卡图表是原创视觉设计；统计区使用真实 API 数据，更新失败时保留之前版本。[查看刷新记录](https://github.com/YZC0219/YZC0219/actions/workflows/refresh-profile.yml) · [查看生成脚本](scripts/update_profile.py)

</details>

---

<p align="center"><strong>从数据出发，让每一个结论有据可查。</strong><br /><sub>ASK BETTER QUESTIONS. BUILD THOUGHTFULLY. KEEP LEARNING.</sub></p>
