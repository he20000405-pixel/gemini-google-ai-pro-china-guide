# Gemini 知识库发布清单

仓库目前已上线。第 1 项仅供首次建站参考，日常维护不重复创建仓库；当前专题范围以 `/guides/` 和 `sitemap.xml` 为准。

1. GitHub 仓库名称必须为 `gemini-google-ai-pro-china-guide`，公开且不初始化额外 README。
2. 在 `Settings → Pages → Build and deployment` 中将 `Source` 设为 `GitHub Actions`，使用仓库内发布前检查工作流，并确认 `github-pages` 部署环境仅允许 `main`，不要切回分支直接发布。
3. 推送后确认本次 `main` 的 `verify` → `release-ready` → `deploy` 均成功，再验收首页、`/guides/`、`/en/`、当前目录与站点地图中的全部专题、`/llms.txt`、`/robots.txt` 和 `/sitemap.xml`。
4. 购买入口和服务说明与当前主站 Gemini 页面及知识库首页保持一致，区分自有账号升级、成品号交付和家庭组服务，不沿用首次建站时的未上线待办。
5. 在 Google 与 Bing 检查 sitemap，并按当前专题目录与站点地图逐篇核对规范 URL、实际索引和抓取状态，优先正文，不只检查首页、目录和英文入口。Google 同时核对其选择的规范地址。
6. 发布后记录 3 天、7 天、14 天的抓取、展现和主站来源访问。

索引请求只针对未收录且实际测试可抓取、允许索引的页面，以及本次新增或重要更新的页面，遵守各后台配额；技术阻碍先修复，已收录且未变或已请求待处理的 URL 不作无意义重复提交。逐篇记录核查时间、证据、请求结果与待办；受限、配额不足、等待处理不标为完成。地图读取成功、URL 提交受理和实际编入索引分别验收，发现 URL 数不等于收录数。

具体规则见 [发布前检查说明](.github/PUBLISHING-CHECKS.md)。`release-ready` 是无权限哨兵任务，依赖 `verify` 成功。PR 和 `ci-check` 测试分支只验收，不发布；只有 `main` 的正常检查通过后才部署同一次运行已检查的产物。检查失败时不执行发布，线上保留上一次成功版本。

## GitHub About

- Website: `https://he20000405-pixel.github.io/gemini-google-ai-pro-china-guide/`
- Description: `Gemini and Google AI membership guides: own-account upgrade, payment errors, Google Play billing and entitlement checks.`
- Topics: `gemini`, `google-ai`, `google-one`, `google-play`, `payment-failed`, `ai-subscription`, `china-guide`, `chonggrok`
