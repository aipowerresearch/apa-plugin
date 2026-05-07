# APA Plugin Installer for Windows
# Usage: .\install.ps1 [-WorkDir <path>] [-RegisterTasks]

param(
    [string]$WorkDir = "$env:USERPROFILE\Downloads\apa",
    [switch]$RegisterTasks = $false
)

Write-Host "===== APA Plugin Installer v2.0.0 =====" -ForegroundColor Cyan
Write-Host ""

# 1. 작업 폴더 검증·생성
if (-not (Test-Path $WorkDir)) {
    Write-Host "[1/4] 작업 폴더 신설: $WorkDir" -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $WorkDir -Force | Out-Null
}
foreach ($sub in @("outputs", "web", "ssh", "_archive")) {
    $p = Join-Path $WorkDir $sub
    if (-not (Test-Path $p)) {
        New-Item -ItemType Directory -Path $p -Force | Out-Null
    }
}
foreach ($lang in @("en", "ko")) {
    foreach ($category in @("sources", "reports", "blog", "newsletters")) {
        New-Item -ItemType Directory -Path "$WorkDir\outputs\$category\$lang" -Force | Out-Null
    }
}
foreach ($pdfLang in @("en", "ko", "en-ko")) {
    New-Item -ItemType Directory -Path "$WorkDir\outputs\pdf\$pdfLang" -Force | Out-Null
}
foreach ($extra in @("analysis", "_logs")) {
    New-Item -ItemType Directory -Path "$WorkDir\outputs\$extra" -Force | Out-Null
}
foreach ($webExtra in @("analysis")) {
    New-Item -ItemType Directory -Path "$WorkDir\web\$webExtra" -Force | Out-Null
}

Write-Host "[1/4] 작업 폴더 구조 OK: $WorkDir" -ForegroundColor Green

# 2. 슬림 CLAUDE.md 배치
$claudeMd = Join-Path $WorkDir "CLAUDE.md"
$pluginRoot = Split-Path $PSScriptRoot -Parent
if (-not (Test-Path $claudeMd)) {
    Copy-Item "$PSScriptRoot\docs\CLAUDE.slim.md" $claudeMd
    Write-Host "[2/4] 슬림 CLAUDE.md 배치 완료" -ForegroundColor Green
} else {
    Write-Host "[2/4] CLAUDE.md 이미 존재 — 건너뜀 (수동 갱신 필요 시 docs\CLAUDE.slim.md 참조)" -ForegroundColor Yellow
}

# 3. 예약 작업 자동 등록 (Cowork)
if ($RegisterTasks) {
    Write-Host "[3/4] 예약 작업 자동 등록 시도..." -ForegroundColor Yellow
    Write-Host "      (Cowork API 연동 필요 — 현재는 SKILL.md만 OneDrive로 복사)" -ForegroundColor Yellow
    $oneDriveScheduled = "$env:USERPROFILE\OneDrive\Documents\Claude\Scheduled"
    if (Test-Path $oneDriveScheduled) {
        foreach ($task in @("apa-daily", "apa-weekly", "apa-kb-daily", "apa-kb-weekly")) {
            $taskDir = Join-Path $oneDriveScheduled $task
            New-Item -ItemType Directory -Path $taskDir -Force | Out-Null
            Copy-Item "$PSScriptRoot\scheduled-tasks\$task\SKILL.md" $taskDir -Force
        }
        Write-Host "[3/4] 4개 SKILL.md 배포 완료 → $oneDriveScheduled" -ForegroundColor Green
        Write-Host "      → Cowork UI에서 cron 스케줄 활성화 필요" -ForegroundColor Yellow
    } else {
        Write-Host "[3/4] OneDrive Scheduled 폴더 없음 — Cowork이 자동 감지 후 등록" -ForegroundColor Yellow
    }
} else {
    Write-Host "[3/4] 예약 작업 등록 건너뜀 (-RegisterTasks 옵션 필요)" -ForegroundColor Yellow
}

# 4. 안내
Write-Host ""
Write-Host "[4/4] 설치 완료" -ForegroundColor Green
Write-Host ""
Write-Host "다음 단계:" -ForegroundColor Cyan
Write-Host "  1. SSH 키를 $WorkDir\ssh\id_rsa 에 배치 (FastComet 업로드용)"
Write-Host "  2. Claude/Cowork 새 세션 시작 → 자동으로 CLAUDE.md 로드됨"
Write-Host "  3. 테스트: /apa:daily --test-mode (산출물 발행 없이 검증)"
Write-Host ""
