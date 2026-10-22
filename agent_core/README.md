# agent_core

Python 기초부터 보안 로그 처리, 탐지 규칙, API·Webhook, LLM 분석, 보고서·알림 자동화까지 단계적으로 학습한 **노트북과 실행 코드**를 모아 둔 폴더입니다.

날짜별 노트북에는 개념 설명, 예제, 실습 코드와 출력 결과가 포함되어 있습니다. 실습 중 별도 파일로 저장한 코드와 보고서도 함께 정리했습니다.

## 학습 흐름

| 단계 | 학습 내용 | 적용한 작업 |
| --- | --- | --- |
| Python 기초 | 변수, 자료형, 리스트·딕셔너리, 조건문·반복문, 함수 | 로그 저장·조회, 로그인 실패 집계, 파일 입출력 |
| 로그 처리·탐지 | 예외 처리, Logging, JSON, 정규표현식 | 로그 정규화, 로그인 실패·의심 접속 탐지 |
| 외부 연동·자동화 | HTTP, Requests, Flask, CLI, schedule | API 조회, 경보 수신, 중복 처리 방지, 주기적 점검 |
| LLM·도구 호출 | Gemini API, 프롬프트, JSON 응답, Tool Router | 경보 분석, 도구 선택·실행, 승인 게이트 실습 |
| 보고서·검증 | 배치 요약, 위험도 정렬, Markdown, 설정 분리, assert | 관제 보고서 생성, 확인 대상 집계·알림, 테스트·디버깅 |

## 날짜별 학습 노트북

| 날짜 | 실습 파일 | 주요 활동 |
| --- | --- | --- |
| `2026-09-22` | [`260922_variables_and_lists.ipynb`](./260922_variables_and_lists.ipynb) | Python 변수와 자료형을 익히고, 리스트·딕셔너리에 보안 로그 데이터를 저장하고 조회하는 기초 실습을 진행 |
| `2026-09-23` | [`260923_am_conditions_loops_counting.ipynb`](./260923_am_conditions_loops_counting.ipynb) | 조건문과 반복문을 이용해 로그인 성공·실패 로그를 판별하고 계정별 실패 횟수를 집계 |
| `2026-09-23` | [`260923_extra_challenges.ipynb`](./260923_extra_challenges.ipynb) | 앞에서 학습한 Python 문법을 활용한 추가 문제와 응용 실습 진행 |
| `2026-09-23` | [`260923_pm_functions_files_csv.ipynb`](./260923_pm_functions_files_csv.ipynb) | 반복되는 로그 처리 코드를 함수로 분리하고, 파일에서 로그 데이터를 읽고 저장하는 방법을 실습 |
| `2026-09-28` | [`260928_am_exceptions_logging.ipynb`](./260928_am_exceptions_logging.ipynb) | `try / except`와 Logging을 이용해 잘못된 로그가 포함되어 있어도 중단되지 않는 로그 파서 구현 |
| `2026-09-28` | [`260928_pm_nested_json.ipynb`](./260928_pm_nested_json.ipynb) | 중첩 리스트·딕셔너리와 JSON을 다루고, 서로 다른 형식의 로그를 하나의 구조로 정규화 |
| `2026-09-29` | [`260929_am_regex_detection_rules.ipynb`](./260929_am_regex_detection_rules.ipynb) | 정규표현식으로 서버 로그에서 계정·IP·이벤트 정보를 추출하고 브루트포스 및 의심 IP 탐지 규칙 적용 |
| `2026-09-29` | [`260929_pm_rules_api.ipynb`](./260929_pm_rules_api.ipynb) | 심야 로그인 성공 등 추가 탐지 규칙을 만들고 URL, HTTP Method, 상태 코드, 인증 방식 등 API 기초 학습 |
| `2026-09-30` | [`260930_am_requests_api_client.ipynb`](./260930_am_requests_api_client.ipynb) | `requests`로 외부 API를 호출하고 `timeout`, 상태 코드 확인, 재시도, `.env`를 이용한 API 요청 처리 |
| `2026-10-02` | [`261002_am_webhook_cli.ipynb`](./261002_am_webhook_cli.ipynb) | Flask로 Webhook 수신 서버를 만들고 `curl`과 CLI를 이용해 실제 HTTP 요청을 보내고 수신하는 과정 실습 |
| `2026-10-02` | [`261002_pm_trigger_scheduler.ipynb`](./261002_pm_trigger_scheduler.ipynb) | Trigger → Condition → Action 구조를 이해하고 중복 경보 방지와 Scheduler를 이용한 자동 실행 구현 |
| `2026-10-06` | [`261006_am_llm_prompt.ipynb`](./261006_am_llm_prompt.ipynb) | Gemini API를 호출해 보안 로그를 자연어로 분석하고, 프롬프트를 구성해 JSON 형태의 응답을 받도록 구현 |
| `2026-10-06` | [`261006_pm_agent_tools.ipynb`](./261006_pm_agent_tools.ipynb) | LLM이 필요한 도구를 선택하게 하고 Tool Router를 통해 실제 함수를 실행하며 위험 작업에는 승인 절차 적용 |
| `2026-10-07` | [`261007_am_report_summary.ipynb`](./261007_am_report_summary.ipynb) | 여러 보안 경보를 묶음으로 LLM에 전달해 요약하고 `high / medium / low` 위험도로 분류·정렬 |
| `2026-10-07` | [`261007_pm_report_generator.ipynb`](./261007_pm_report_generator.ipynb) | 경보 전체의 총평을 생성하고 경보 건수, 조건부 경고, 건별 내역을 포함한 Markdown 보안 관제 보고서 구현 |
| `2026-10-08` | [`261008_am_config_pipeline.ipynb`](./261008_am_config_pipeline.ipynb) | 모델·정책·알림 주소를 `config.json`으로 분리하고 보고서 생성과 알림 기능을 `pipeline.py`로 통합 |
| `2026-10-08` | [`261008_pm_review_debug_retro.ipynb`](./261008_pm_review_debug_retro.ipynb) | `assert` 기반 테스트, 코드 리뷰, 문법·실행·논리 오류 디버깅을 진행하고 전체 파이프라인 동작을 최종 점검 |

## 실행 코드와 데이터

| 파일 | 역할 |
| --- | --- |
| [webhook_server.py](./webhook_server.py) | Flask의 `POST /webhook`으로 경보를 받고, 수신 목록을 `received_alerts.json`에 저장 |
| [test_webhook.sh](./test_webhook.sh) | 로컬 서버의 5001번 포트로 경보 3종을 보내 HTTP 응답 코드 확인 |
| [scheduler_job.py](./scheduler_job.py) | 로그인 실패 횟수를 점검하고, 처음 처리한 경보 ID를 출력·기록하는 스케줄 실습 |
| [processed_ids.json](./processed_ids.json) | 중복 처리를 방지하기 위한 처리 완료 ID 목록 |
| [config.json](./config.json) | 모델 이름, 사람 확인 기준, 보고서 폴더 항목, 알림 주소 설정 |
| [notifier.py](./notifier.py) | 필수 설정 키 확인, 위험도에 따른 사람 확인 대상 판정, HTTP 알림 전송 |
| [pipeline.py](./pipeline.py) | 경보 요약·위험도 정렬·보고서 저장·확인 대상 집계·알림을 연결 |
| [test_agent_core.py](./test_agent_core.py) | 보고서 행 생성, 확인 대상 판정, LLM JSON 응답 처리에 대한 `assert` 9개 |
| [reports/daily_report_20261008.md](./reports/daily_report_20261008.md) | 경보 6건을 정리한 관제 보고서 산출물 |

## 노트북 확인 방법

1. 날짜순으로 노트북을 열어 개념과 실습 내용을 확인합니다. GitHub에서는 저장된 코드와 출력 결과를 볼 수 있습니다.
2. 직접 실습할 때는 각 노트북의 시작하기·환경 준비 셀을 먼저 확인합니다. 일부 노트북에는 Google Colab·Drive 연결이나 실습 경로를 설정하는 코드가 포함되어 있습니다.
3. 앞선 셀에서 만든 변수·함수·입력 파일을 뒤에서 사용하는 경우가 있어, 준비 셀부터 순서대로 진행합니다. `%%writefile` 셀은 별도 Python 파일을 생성하거나 덮어씁니다.

### 실행 파일과 artifacts의 관계

현재 이 폴더에는 실습 과정에서 저장한 일부 실행 파일이 있습니다. 파이프라인과 테스트가 참조하는 다음 모듈·입력 데이터는 [artifacts](../artifacts/)에 모여 있습니다.

| 참조하는 코드 | 필요한 모듈·입력 데이터 | 저장 위치 |
| --- | --- | --- |
| `pipeline.py` | `llm_client.py`, `event_summarizer.py`, `report_generator.py`, `events_1008.json` | [artifacts](../artifacts/) |
| `test_agent_core.py` | `llm_client.py`, `report_generator.py` | [artifacts](../artifacts/) |
| `scheduler_job.py` | `normalized_logs.json` | [정규화된 로그](../artifacts/normalized_logs.json) |

따라서 현재 `agent_core` 폴더만으로 파이프라인·테스트·스케줄러를 바로 실행하려면 필요한 모듈과 입력 파일을 먼저 준비해야 합니다. 구현 과정은 이 폴더의 노트북에서, 저장된 모듈과 데이터는 `artifacts`에서 함께 확인합니다.

### Webhook 수신 실습

Python 환경에 Flask가 설치되어 있다면, 저장소 루트에서 다음 명령으로 서버를 실행할 수 있습니다.

```bash
cd agent_core
python webhook_server.py --port 5001
```

다른 터미널에서도 `agent_core` 폴더로 이동한 뒤 요청을 보냅니다. 아래 스크립트는 Bash와 curl을 사용합니다.

```bash
bash test_webhook.sh
```

스크립트가 보내는 경보는 `brute_force`, `password_spraying`, `night_login`이며, 정상적으로 수신하면 각각 HTTP `200`을 반환합니다. 서버는 받은 데이터를 현재 작업 폴더의 `received_alerts.json`에 저장합니다.

## 구현에서 확인할 점

- **스케줄 실행:** 현재 `scheduler_job.py`는 점검 루프를 4회 확인하는 실습 코드입니다. 신규 경보는 콘솔에 출력하고 처리 완료 ID를 파일에 저장합니다.
- **LLM과 코드의 역할:** 경보별 요약·위험도와 보고서 총평은 LLM이 생성하고, 위험도 정렬·건수 집계·보고서 틀은 Python 코드로 처리합니다.
- **승인 처리:** 도구 호출 노트북에서는 위험 도구의 실행 전 승인 게이트를 실습합니다. 보고서 파이프라인의 `needs_approval()`은 사람 확인이 필요한 경보를 판정하고 건수를 알림에 포함합니다.
- **설정과 저장 경로:** `report_folder`는 설정 파일과 필수 키 검사에 포함되어 있으나, 현재 `artifacts/report_generator.py`의 `save_report()`는 보고서를 실행한 작업 폴더에 저장합니다.
- **테스트 범위:** `test_agent_core.py`는 문자열·판정·JSON 처리 결과를 확인합니다. 외부 API나 전체 파이프라인의 정상 동작 여부는 별도 실행으로 확인해야 합니다.

## 관련 자료

- [전체 저장소 안내](../README.md)
- [실행 코드·입력 데이터·분석 산출물](../artifacts/)
- [날짜별 학습 기록](../docs/)
- [1과목 회고](../docs/day08_retrospective.md)
