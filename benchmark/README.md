# 1周对比：Headlong vs Headlong+Letta

同一批 3 需求，看 learn/recall 命中率

**3 需求（已写入 requirements/pool.md）：**
- REQ-A 单项目：quant-alpha 修数据 bug
- REQ-B 跨项目：Q3 路线图优先级
- REQ-C 技术债：抽 3 项目重复代码

**怎么跑：**
- Day 1: 各发一次，看 Headlong 是否 learn
- Day 7: 发相似需求，看 recall 命中率
- 指标：`grep -c "learn" trajectory` vs `mem search` 命中

**当前：** Letta wrapper 是 grep，LangGraph 是 dict。跑 1 周后看 recall <50% 再换真实现。
