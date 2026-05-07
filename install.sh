#!/usr/bin/env bash
# APA Plugin Installer for macOS/Linux
# Usage: ./install.sh [WORK_DIR]

set -e

WORK_DIR="${1:-$HOME/Downloads/apa}"
PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "===== APA Plugin Installer v2.0.0 ====="
echo ""

# 1. 작업 폴더 구조
mkdir -p "$WORK_DIR"/{outputs,web,ssh,_archive}
for category in sources reports blog newsletters; do
    mkdir -p "$WORK_DIR/outputs/$category"/{en,ko}
done
for lang in en ko en-ko; do
    mkdir -p "$WORK_DIR/outputs/pdf/$lang"
done
for extra in analysis _logs; do
    mkdir -p "$WORK_DIR/outputs/$extra"
done
mkdir -p "$WORK_DIR/web/analysis"

echo "[1/4] 작업 폴더 구조 OK: $WORK_DIR"

# 2. 슬림 CLAUDE.md
if [ ! -f "$WORK_DIR/CLAUDE.md" ]; then
    cp "$PLUGIN_DIR/docs/CLAUDE.slim.md" "$WORK_DIR/CLAUDE.md"
    echo "[2/4] 슬림 CLAUDE.md 배치 완료"
else
    echo "[2/4] CLAUDE.md 이미 존재 — 건너뜀"
fi

# 3. 예약 작업 (macOS는 ~/Library/CloudStorage/OneDrive-*, Linux는 미사용)
SCHEDULED_DIR=""
if [ -d "$HOME/Library/CloudStorage" ]; then
    SCHEDULED_DIR=$(find "$HOME/Library/CloudStorage" -maxdepth 4 -type d -name "Scheduled" -path "*Claude*" 2>/dev/null | head -1)
fi
if [ -n "$SCHEDULED_DIR" ]; then
    for task in apa-daily apa-weekly apa-kb-daily apa-kb-weekly; do
        mkdir -p "$SCHEDULED_DIR/$task"
        cp "$PLUGIN_DIR/scheduled-tasks/$task/SKILL.md" "$SCHEDULED_DIR/$task/"
    done
    echo "[3/4] 4개 SKILL.md 배포 완료 → $SCHEDULED_DIR"
else
    echo "[3/4] Scheduled 폴더 자동 탐지 실패 — Cowork이 자동 감지 후 등록"
fi

# 4. SSH 키 권한
if [ -f "$WORK_DIR/ssh/id_rsa" ]; then
    chmod 600 "$WORK_DIR/ssh/id_rsa"
fi

echo ""
echo "[4/4] 설치 완료"
echo ""
echo "다음 단계:"
echo "  1. SSH 키를 $WORK_DIR/ssh/id_rsa 에 배치"
echo "  2. Claude/Cowork 새 세션 시작"
echo "  3. 테스트: /apa:daily --test-mode"
