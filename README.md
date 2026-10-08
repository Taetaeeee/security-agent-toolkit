# Security Agent Toolkit

Python과 LLM을 활용해 보안 로그와 경보를 분석하고,  
결과를 요약·정리하여 보안 관제 보고서로 만드는 과정을 실습하는 프로젝트입니다.

---

## 주요 내용

- 보안 로그 파싱 및 JSON 데이터 처리
- 탐지된 보안 경보 정리
- Flask Webhook을 이용한 경보 수신
- Gemini API를 활용한 경보 요약
- `high / medium / low` 위험도 분류 및 정렬
- Markdown 형식의 보안 관제 보고서 생성

---

## 📁 Main Files

| 파일 | 설명 |
| --- | --- |
| `llm_client.py` | Gemini API 호출 및 응답 처리 |
| `event_summarizer.py` | 경보 요약 및 위험도 정렬 |
| `report_generator.py` | 보안 관제 보고서 생성 |

---

## 📚 Learning Log

| 날짜 | 학습 내용 |
| --- | --- |
| `2026-09-22` | Python 변수, 자료형, 리스트, f-string |
| `2026-09-23` | 조건문, 반복문, 데이터 집계, 함수 및 파일 처리 |
| `2026-09-28` | 예외처리, Logging, JSON, 로그 정규화 |
| `2026-09-29` | 정규표현식, 보안 탐지 룰, API·HTTP 기초 |
| `2026-09-30` | Requests를 이용한 API 호출, 예외·재시도 처리 |
| `2026-10-02` | Flask Webhook, 트리거, 중복 처리, 스케줄러 |
| `2026-10-06` | Gemini API, 프롬프트, AI 도구 호출 |
| `2026-10-07` | 경보 묶음 요약, 위험도 정렬, 관제 보고서 생성 |
