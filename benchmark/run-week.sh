#!/bin/bash
# ponytail: 1 周对比，不另起炉灶
set -e
echo "Day 1: 发 3 需求"
for req in "quant-alpha 修数据" "Q3 路线图" "抽重复代码"; do
  ssh deploy@host "docker exec brain-loop bash -c \"chat send --from owner '$req'\" 2>&1 | head -1"
done
echo "等 7 天后看 trajectory 中 learn/recall"
echo "Day 7: grep -c learn trajectory | mem search 命中率"
