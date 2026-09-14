#!/usr/bin/env bash
# 发布脱敏公开快照：从当前 HEAD 生成脱敏副本并推送到 GitHub 公开镜像。
#
# 规范见 AGENTS.md「公开镜像与脱敏规范」。规则表：publish/sanitize.map（gitignored）。
# 用法： scripts/publish-public.sh
# 环境变量： PUBLIC_REPO=owner/name  PUBLIC_REMOTE=origin
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MAP="$ROOT/publish/sanitize.map"
OUT="${TMPDIR:-/tmp}/studio-public"
REPO="${PUBLIC_REPO:-justin-mc-lai/studio}"
REMOTE="${PUBLIC_REMOTE:-origin}"

[ -f "$MAP" ] || { echo "ABORT: 缺少 $MAP（从 publish/sanitize.map.example 复制并填真实值）"; exit 1; }

rm -rf "$OUT"; mkdir -p "$OUT"
git -C "$ROOT" archive HEAD | tar -x -C "$OUT"
rm -rf "$OUT/publish"          # 规则表绝不进入公开快照

python3 - "$OUT" "$MAP" <<'PY'
import sys
from pathlib import Path
out, mapf = Path(sys.argv[1]), Path(sys.argv[2])
rules = []
for line in mapf.read_text(encoding="utf-8").splitlines():
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    a, b = line.split("\t", 1)
    rules.append((a, b))
for p in out.rglob("*"):
    if not p.is_file():
        continue
    try:
        t = p.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    n = t
    for a, b in rules:
        n = n.replace(a, b)
    if n != t:
        p.write_text(n, encoding="utf-8")

# fail-closed：任何原文残留即中止，不推送
bad = []
for p in out.rglob("*"):
    if not p.is_file():
        continue
    try:
        t = p.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    for a, _ in rules:
        if a in t:
            bad.append(f"{p.relative_to(out)}: {a}")
if bad:
    print("ABORT: 脱敏后仍残留敏感原文：")
    for item in bad[:20]:
        print(" -", item)
    sys.exit(1)
print("sanitize ok")
PY

# 脱敏改了 truth 内容，重建 .machine 投影让公开快照自洽（best-effort）
if command -v beacon >/dev/null 2>&1; then
  ( cd "$OUT" && beacon truth-map rebuild-machine studio --project . --version v0.1.0 --json >/dev/null 2>&1 || true )
fi

cd "$OUT"
git init -q -b main
git add -A
git -c user.name=owner -c user.email=owner@example.com commit -q \
  -m "sanitized snapshot of $(git -C "$ROOT" rev-parse --short HEAD)"
if git remote get-url "$REMOTE" >/dev/null 2>&1; then
  git push -f "$REMOTE" main
elif gh repo view "$REPO" >/dev/null 2>&1; then
  git remote add origin "$(gh repo view "$REPO" --json sshUrl -q .sshUrl 2>/dev/null || echo "https://github.com/$REPO.git")"
  git push -f origin main
else
  gh repo create "$REPO" --public --source=. --remote=origin --push
fi
echo "published -> $REPO (from $(git -C "$ROOT" rev-parse --short HEAD))"
