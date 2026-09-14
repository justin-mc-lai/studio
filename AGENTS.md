# AGENTS.md — studio

> 项目级 Agent 规约：公开镜像、脱敏、git 忽略、验证命令。
> 本文件会随公开快照一起发布，**禁止**写入真实业务标识/人名/基础设施名。

## 项目定位

`studio` 是 Beacon 驱动的公司运营层控制面（control plane）：portfolio 注册与健康度、
需求池状态机、跨项目需求真相冻结链、双轨执行与全程 trace、知识沉淀。
真相源：`docs/beacon/v0.1.0/features/studio/{truth,tests,tasks,evidence}.md`。

## 验证命令

- 契约测试：`python3 -m pytest tests/ -q`
- 健康看板自检：`python3 scripts/portfolio_health.py --check`
- 健康看板生成：`python3 scripts/portfolio_health.py`
- 真相一致性：`beacon truth-map verify studio --project . --version v0.1.0 --json`
- 真相评审：`beacon truth review studio --project-root . --version v0.1.0 --json`
- 材料完整性：`beacon doctor verify-materials --project-root . --version v0.1.0 --strict`
- 发布预检：`beacon release check v0.1.0 --project-root .`

## 公开镜像与脱敏规范

本项目对外发布**脱敏快照**（非原始仓库）：

- 公开镜像：`github.com/justin-mc-lai/studio`（public）
- 生成/推送：`scripts/publish-public.sh`（从当前 HEAD 生成、脱敏、推送）
- 规则表：`publish/sanitize.map`（**已 gitignore，禁止提交/推送**）
- 规则模板：`publish/sanitize.map.example`

### 脱敏原则

1. **Fail-closed**：脚本对每个文件做原文残留扫描，发现任何未替换的敏感原文立即中止、不推送。
2. **规则顺序敏感**：`sanitize.map` 中更具体/更长的原文在前（如 `<project>-flywheel` 先于 `<project>`）。
3. **规则表不进快照**：生成时删除 `publish/`，规则表本身永不公开。
4. **不写反查表**：公开文件（含本 AGENTS.md）不得出现「原文 → 替换」的真实映射。

### 必须覆盖的脱敏类别

| 类别 | 处理 |
|------|------|
| 业务项目 slug | → 通用 slug（`proj-alpha` 等） |
| 持仓/资产/标的名称 | → `asset-a` … `asset-d`（或移除字段） |
| 人名 | → `Owner` |
| 主机/基础设施名 | → `deploy-host` / `deploy@host` |
| 本地绝对路径 | → `/workspace/<repo>` |
| 业务指标（营收/增长等） | → `metric` |

### 发布流程

```bash
# 1) 确认规则表就绪（首次从模板复制）
cp publish/sanitize.map.example publish/sanitize.map   # 再填入真实值
# 2) 本地验证
python3 -m pytest tests/ -q
# 3) 生成脱敏快照并推送
scripts/publish-public.sh
```

## git 忽略规范

`.gitignore` 覆盖三类，**只提交可复现的源代码与真相文档**：

1. **运行/生成态**（Beacon 由 truth 再生成，不入库）：
   `.beacon/state/`、`.beacon/tasks/`、`.beacon/worktrees/`、`.beacon/traces/`、
   `.beacon/memory/`、`.beacon/locks/`、`.beacon/qa/`、`.beacon/implement/`、
   `.beacon/evidence/auto-test/`、`.beacon/evidence/qa-feature/`、`*.jsonl`
2. **Agent/编排运行态**：`.omc/`
3. **缓存与密钥**：`__pycache__/`、`*.pyc`、`.pytest_cache/`、`.coverage`、
   `publish/sanitize.map`、`*.local.toml`、`.env`、`*.pem`、`*.key`

例外（**必须**提交）：`.beacon/evidence/implement/studio/AC-*.json`、`GATES.json`、
`QA-MATRIX.json`、`.beacon/evidence-manifest.json` —— 它们是可审计的交付证据。

## 安全红线

- 不提交/推送任何密钥、token、私有端点、真实客户/员工数据。
- 公开前必须通过 `scripts/publish-public.sh` 的 fail-closed 扫描。
- 真相冻结后不得静默改写；变更走 `beacon change` → refreeze，并留 revision 记录。
