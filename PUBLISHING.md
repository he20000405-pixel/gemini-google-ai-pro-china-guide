# Gemini 知识库发布清单

1. GitHub 仓库名称必须为 `gemini-google-ai-pro-china-guide`，公开且不初始化额外 README。
2. 在 `Settings → Pages → Build and deployment` 中将 `Source` 设为 `GitHub Actions`，使用仓库内发布前检查工作流，并确认 `github-pages` 部署环境仅允许 `main`，不要切回分支直接发布。
3. 推送后确认本次 `main` 的 `verify` → `release-ready` → `deploy` 均成功，再验收首页、`/guides/`、`/en/`、7 个专题、`/llms.txt`、`/robots.txt` 和 `/sitemap.xml`。
4. 主站 Gemini 页面完成“仅用户自有账号”文案修正前，不增加购买 CTA。
5. Google 与 Bing 各提交一次 sitemap、首页、专题目录和英文入口，不重复请求。
6. 发布后记录 3 天、7 天、14 天的抓取、展现和主站来源访问。

具体规则见 [发布前检查说明](.github/PUBLISHING-CHECKS.md)。`release-ready` 是无权限哨兵任务，依赖 `verify` 成功。PR 和 `ci-check` 测试分支只验收，不发布；只有 `main` 的正常检查通过后才部署同一次运行已检查的产物。检查失败时不执行发布，线上保留上一次成功版本。

## GitHub About

- Website: `https://he20000405-pixel.github.io/gemini-google-ai-pro-china-guide/`
- Description: `Gemini and Google AI membership guides: own-account upgrade, payment errors, Google Play billing and entitlement checks.`
- Topics: `gemini`, `google-ai`, `google-one`, `google-play`, `payment-failed`, `ai-subscription`, `china-guide`, `chonggrok`
