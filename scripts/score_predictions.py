#!/usr/bin/env python3
"""
AI Power Atlas — Stage 2: Prediction Scorer (Daily) v2-semantic
어제 S08 예측이 오늘 S01에서 몇 개나 실현됐는지 자동 채점.
실행: python3 scripts/score_predictions.py --today YYYY-MM-DD

v2-semantic 변경:
  - 기존 단어 카운팅(kw_hits) → 의미 추론 기반 3축 복합 채점
  - composite = tfidf_similarity×0.45 + entity_overlap×0.35 + layer_concept×0.20
  - 레코드에 scorer_version, composite, breakdown 필드 추가
"""

import os, re, json, glob, argparse
from datetime import datetime, timedelta

# sklearn 없을 경우 graceful fallback (설치 안 된 환경 대비)
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_OK = True
except ImportError:
    SKLEARN_OK = False

APA_ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_DIR    = os.path.join(APA_ROOT, 'references', 'knowledge-base')
REPORTS   = os.path.join(APA_ROOT, 'outputs', 'reports')
LEGACY    = os.path.join(REPORTS, '_legacy_v1')
SCORE_LOG = os.path.join(KB_DIR, 'prediction_scores.jsonl')

SCORER_VERSION = "v2-semantic"

# ── L1~L10 개념 확장 사전 ───────────────────────────────────────────────
LAYER_CONCEPTS = {
    'L1':  ['compute','nvidia','amd','gpu','chip','h100','b200','hardware','tpu','infra',
            'datacenter','watt','power','cooling','fab','wafer','semiconductor'],
    'L2':  ['model','llm','gpt','gemini','claude','qwen','mistral','frontier','benchmark',
            'parameter','token','pretraining','fine-tune','rlhf','reasoning','multimodal'],
    'L3':  ['middleware','api','framework','langchain','inference','deployment','sdk',
            'endpoint','latency','serving','orchestration','agent','workflow'],
    'L4':  ['data','dataset','training','synthetic','licensing','crawl','annotation',
            'copyright','scraping','curation','pipeline','knowledge','retrieval'],
    'L5':  ['platform','azure','aws','gcp','cloud','enterprise','saas','copilot',
            'workspace','productivity','integration','subscription','vertical'],
    'L6':  ['capital','investment','funding','vc','valuation','ipo','acquisition',
            'round','billion','series','revenue','profit','margin','stake'],
    'L7':  ['geopolit','sovereign','government','export','tariff','sanction',
            'regulation policy','national','defense','military','chip act','alliance'],
    'L8':  ['regulation','law','policy','compliance','eu ai act','executive order',
            'liability','audit','transparency','consent','gdpr','copyright law'],
    'L9':  ['labor','talent','layoff','hiring','workforce','job','union','salary',
            'remote','headcount','engineer','researcher','immigration','visa'],
    'L10': ['perception','media','public','narrative','trust','safety','alignment',
            'ethics','bias','risk','harm','safety eval','anthropic','openai safety'],
}

def load_report_text(date_str):
    """날짜 기준으로 리포트 텍스트 로드 (en 우선, v1 폴백)"""
    patterns = [
        os.path.join(REPORTS, f'{date_str}_*_daily-report_en.md'),
        os.path.join(LEGACY,  f'{date_str}_*_daily-report_v1.md'),
    ]
    for p in patterns:
        files = glob.glob(p)
        if files:
            with open(files[0]) as f:
                return f.read()
    return None

def extract_s01_text(report_text):
    """S01 섹션 텍스트만 추출 (tfidf 채점 범위 제한)"""
    m = re.search(r'## S01.*?\n(.*?)(?=\n## S0[2-9]|\Z)', report_text, re.DOTALL)
    return m.group(1) if m else report_text[:3000]

def extract_entities(text):
    """대문자 구문·약어 추출 (2자 이상 연속 대문자 or 단어 첫글자 대문자 시퀀스)"""
    # 약어: 2~6자 연속 대문자 (예: GPT, AWS, RLHF)
    abbrevs = set(re.findall(r'\b[A-Z]{2,6}\b', text))
    # 고유명사 구문: 연속 대문자 단어 (예: OpenAI, Google DeepMind)
    phrases = set(re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b', text))
    # 단일 고유명사: 첫글자 대문자 + 4자 이상
    singles = set(w for w in re.findall(r'\b[A-Z][a-zA-Z]{3,}\b', text)
                  if w not in {'The','This','These','That','With','From','When',
                                'They','Their','After','Also','Such','Some','Into'})
    return abbrevs | phrases | singles

def tfidf_score(signal_text, today_s01_text):
    """TF-IDF 코사인 유사도 (sklearn 없으면 단어 Jaccard로 fallback)"""
    if not today_s01_text.strip():
        return 0.0
    if SKLEARN_OK:
        try:
            vec = TfidfVectorizer(ngram_range=(1, 2), max_features=5000, min_df=1)
            tfidf = vec.fit_transform([signal_text, today_s01_text])
            sim = float(cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0])
            return round(sim, 4)
        except Exception:
            pass
    # fallback: Jaccard
    a = set(signal_text.lower().split())
    b = set(today_s01_text.lower().split())
    inter = a & b
    union = a | b
    return round(len(inter) / len(union), 4) if union else 0.0

def entity_overlap_score(signal_text, today_text):
    """entity 교집합 비율"""
    sig_ents   = extract_entities(signal_text)
    today_ents = extract_entities(today_text)
    if not sig_ents:
        return 0.0
    overlap = sig_ents & today_ents
    return round(len(overlap) / len(sig_ents), 4)

def layer_concept_score(signal_text, today_text):
    """L1~L10 개념 사전 기반 레이어 공간 일치"""
    signal_lower = signal_text.lower()
    today_lower  = today_text.lower()

    sig_layers, today_layers = set(), set()
    for layer, concepts in LAYER_CONCEPTS.items():
        if any(c in signal_lower for c in concepts):
            sig_layers.add(layer)
        if any(c in today_lower for c in concepts):
            today_layers.add(layer)

    if not sig_layers:
        return 0.0
    overlap = sig_layers & today_layers
    return round(len(overlap) / len(sig_layers), 4)

def composite_score(signal_text, today_s01_text, today_full_text):
    """3축 복합 채점 → composite (0~1) + 세부 breakdown 반환"""
    tfidf   = tfidf_score(signal_text, today_s01_text)
    entity  = entity_overlap_score(signal_text, today_full_text)
    layer   = layer_concept_score(signal_text, today_full_text)

    composite = round(tfidf * 0.45 + entity * 0.35 + layer * 0.20, 4)

    breakdown = {
        'tfidf':  tfidf,
        'entity': entity,
        'layer':  layer,
    }
    return composite, breakdown

def score_to_label(composite):
    """composite → 점수(0~3) + 레이블"""
    if composite >= 0.35: return 3, '실현'
    if composite >= 0.20: return 2, '부분실현'
    if composite >= 0.08: return 1, '연관'
    return 0, '미실현'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--today', default=datetime.now().strftime('%Y-%m-%d'))
    args = parser.parse_args()

    today_str     = args.today
    yesterday_str = (datetime.strptime(today_str, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')

    today_full     = load_report_text(today_str)
    yesterday_text = load_report_text(yesterday_str)

    if not today_full:
        print(f"⚠️  오늘({today_str}) 리포트 없음 — 스킵")
        return
    if not yesterday_text:
        print(f"⚠️  어제({yesterday_str}) 리포트 없음 — S08 예측 기준 없음")
        return

    today_s01 = extract_s01_text(today_full)

    # 어제 S08 추출
    s08_m = re.search(r'## S08.*?\n(.*?)(?=\n## |\Z)', yesterday_text, re.DOTALL)
    if not s08_m:
        print("⚠️  어제 S08 섹션 없음")
        return

    watchlist = []
    for m in re.finditer(r'\d+\.\s+\*\*(.+?)\*\*\s*[—-]\s*(.+?)(?=\n\d+\.|\Z)',
                          s08_m.group(1), re.DOTALL):
        watchlist.append({'signal': m.group(1).strip(), 'detail': m.group(2).strip()[:200]})

    if not watchlist:
        print("⚠️  어제 S08 예측 항목 없음")
        return

    # 채점
    scores = []
    for w in watchlist:
        combined = w['signal'] + ' ' + w['detail']
        comp, breakdown = composite_score(combined, today_s01, today_full)
        score, label = score_to_label(comp)
        scores.append({
            'signal':    w['signal'],
            'score':     score,
            'label':     label,
            'composite': comp,
            'breakdown': breakdown,
        })

    total    = len(scores)
    realized = sum(1 for s in scores if s['score'] >= 2)
    accuracy = round(realized / total * 100) if total else 0

    record = {
        'date':            today_str,
        'prediction_date': yesterday_str,
        'scorer_version':  SCORER_VERSION,
        'total_signals':   total,
        'realized':        realized,
        'accuracy_pct':    accuracy,
        'scores':          scores,
        'scored_at':       datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    }

    os.makedirs(KB_DIR, exist_ok=True)
    with open(SCORE_LOG, 'a') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

    sklearn_note = '' if SKLEARN_OK else ' [sklearn 미설치 — Jaccard fallback]'
    print(f"Stage 2 채점 완료 ({SCORER_VERSION}){sklearn_note} — {today_str}")
    print(f"예측 정확도: {accuracy}% ({realized}/{total} 실현)")
    for s in scores:
        icon = '✅' if s['score'] >= 2 else ('🔶' if s['score'] == 1 else '❌')
        comp_str = f"composite={s['composite']:.3f} (tfidf={s['breakdown']['tfidf']:.2f}, entity={s['breakdown']['entity']:.2f}, layer={s['breakdown']['layer']:.2f})"
        print(f"  {icon} [{s['label']}] {s['signal'][:50]} — {comp_str}")

if __name__ == '__main__':
    main()
