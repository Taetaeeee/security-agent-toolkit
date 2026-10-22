# artifacts

`artifacts`는 Security Agent Toolkit 실습 과정에서 생성한 코드, 테스트 데이터, JSON 결과, 보안 관제 보고서 등의 산출물을 모아 둔 폴더입니다.

`agent_core`에서 구현하고 실행한 기능들이 실제로 어떤 데이터를 입력받고 어떤 결과를 만들어 냈는지 확인할 수 있습니다.

## 산출물 확인 순서

| 단계 | 확인할 파일 | 내용 |
| --- | --- | --- |
| 로그·탐지 | [raw_logs.txt](./raw_logs.txt), [normalized_logs.json](./normalized_logs.json), [scheduler_job.py](./scheduler_job.py) | 로그 구조와 탐지 규칙, 중복 처리 방지 |
| API·경보 수신 | [api_result.json](./api_result.json), [received_alerts.json](./received_alerts.json) | 외부 조회 결과와 Webhook 수신 기록 |
| LLM 분석 | [events_1007.json](./events_1007.json), [events_1008.json](./events_1008.json), [event_summaries.json](./event_summaries.json) | 분석에 사용한 경보와 위험도·요약 결과 |
| 보고서·알림 | [sorted_summaries.json](./sorted_summaries.json), `daily_report_*.md`, [pipeline.py](./pipeline.py) | 위험도 정렬, 보고서 생성, 확인 대상 집계와 알림 |

각 파일은 단계별 실습에서 생성한 산출물입니다. 현재 [pipeline.py](./pipeline.py)는 [events_1008.json](./events_1008.json)을 직접 읽어 요약·보고서·알림을 실행하며, 앞선 로그 정규화·탐지·Webhook 수신까지 자동으로 연결하는 코드는 아닙니다.

## 주요 데이터 및 결과

| 파일 | 내용 |
| --- | --- |
| [raw_logs.txt](./raw_logs.txt) | 정규표현식과 탐지 룰 실습에 사용한 원본 서버 로그 |
| [normalized_logs.json](./normalized_logs.json) | 원본 로그에서 시간, 등급, 사용자, IP 등을 추출해 공통 형식으로 정규화한 결과 |
| [api_result.json](./api_result.json) | 의심 IP를 외부 API로 조회한 국가 및 ISP 정보 |
| [received_alerts.json](./received_alerts.json) | Flask Webhook 서버가 실제로 수신한 경보 기록 |
| [processed_ids.json](./processed_ids.json) | Scheduler 실행 시 이미 처리한 경보를 기록하여 중복 처리를 방지하기 위한 데이터 |
| [events_1007.json](./events_1007.json) | 10/7 LLM 분석 및 보고서 생성에 사용한 경보 18건 |
| [events_1008.json](./events_1008.json) | 파이프라인 입력으로 사용하는 경보 6건 |
| [event_summaries.json](./event_summaries.json) | 경보 18건에 대해 저장한 `id`, `risk_level`, `summary` 결과 |
| [sorted_summaries.json](./sorted_summaries.json) | 경보 요약 18건을 `high → medium → low` 순으로 정렬한 결과 |
| [agent_result.json](./agent_result.json) | AI Agent가 선택한 도구와 실행 결과, 승인 대기 결과를 저장한 파일 |

## 보안 관제 보고서

| 파일 | 내용 |
| --- | --- |
| [daily_report_20261007.md](./daily_report_20261007.md) | 경보 18건을 분석해 생성한 10/7 야간 보안 관제 보고서 |
| [daily_report_20261008.md](./daily_report_20261008.md) | 처리한 경보 6건·high 1건을 정리한 10/8 관제 보고서 |
| [daily_report_20261009.md](./daily_report_20261009.md) | 처리한 경보 6건·high 1건을 정리한 10/9 관제 보고서 |
| [daily_report_2026-10-08.md](./daily_report_2026-10-08.md) | 현재 제목만 저장된 보고서 초안 |
| [report_test.md](./report_test.md) | 보안 경보를 Markdown 보고서 형태로 변환하는 과정에서 사용한 테스트 파일 |

완성된 [daily_report_20261007.md](./daily_report_20261007.md), [daily_report_20261008.md](./daily_report_20261008.md), [daily_report_20261009.md](./daily_report_20261009.md)에는 다음 정보가 포함됩니다.

- 처리한 전체 경보 수
- `high` 위험도 경보 수
- high 경보가 3건 이상일 때 표시하는 조건부 경고
- LLM이 작성한 전체 경보 총평
- `HIGH → MEDIUM → LOW` 순으로 정렬한 건별 내역

## 분석 및 자동화 코드

| 파일 | 역할 |
| --- | --- |
| [api_client.py](./api_client.py) | 외부 API를 이용한 IP 정보 조회 및 재시도 처리 |
| [llm_client.py](./llm_client.py) | Gemini API 호출 및 JSON 응답 처리 |
| [tool_router.py](./tool_router.py) | `count_failed_logins`, `lookup_ip` 도구 이름을 실제 함수와 연결 |
| [event_summarizer.py](./event_summarizer.py) | 여러 보안 경보를 묶음으로 요약하고 위험도순으로 정렬 |
| [report_generator.py](./report_generator.py) | LLM 총평과 경보 데이터를 이용해 Markdown 관제 보고서 생성 |
| [notifier.py](./notifier.py) | 설정을 확인하고 사람의 확인이 필요한 경보를 판정한 뒤 알림 전송 |
| [pipeline.py](./pipeline.py) | 경보 분석 → 보고서 생성 → 승인 대상 판정 → 알림을 하나의 흐름으로 연결 |
| [scheduler_job.py](./scheduler_job.py) | 로그인 실패·IP별 사용자 수·심야 성공 조건을 점검하고 신규 경보 ID 출력·기록 |
| [test_agent_core.py](./test_agent_core.py) | 보고서 행 생성, 사람 확인 대상 판정, JSON 응답 처리를 `assert` 9개로 검증 |

## Webhook 관련 산출물

| 파일 | 역할 |
| --- | --- |
| [webhook_server.py](./webhook_server.py) | 포트를 인자로 받는 `POST /webhook` 서버, 수신 목록을 JSON에 저장 |
| [webhook_server_pm.py](./webhook_server_pm.py) | 스케줄 실습에서 사용한 `POST /webhook` 수신·저장 서버 |
| [alert_server.py](./alert_server.py) | 5001번 포트의 `POST /alert`에서 보고서 알림을 받아 콘솔에 출력 |
| [hello_server.py](./hello_server.py) | 기본적인 Flask Webhook 수신 실습 |
| [echo_server.py](./echo_server.py) | 받은 요청의 값을 응답으로 돌려주는 Webhook 실습 |
| [count_server.py](./count_server.py) | 수신한 경보 개수를 누적하여 반환하는 서버 |
| [save_server.py](./save_server.py) | 수신한 경보를 [received_alerts.json](./received_alerts.json)에 저장하는 서버 |
| [test_webhook.sh](./test_webhook.sh) | `curl`을 이용해 탐지 경보를 Webhook 서버로 전송하는 테스트 스크립트 |
| [demo_test.sh](./demo_test.sh) | Webhook 요청 전송을 확인하기 위한 간단한 테스트 스크립트 |

## 설정 파일

| 파일 | 용도 |
| --- | --- |
| [config.json](./config.json) | 기본 모델, 사람 확인 기준, 보고서 폴더 항목, 알림 주소 설정 |
| [config_low.json](./config_low.json) | 승인 기준을 `low`로 변경한 테스트 설정 |
| [config_medium.json](./config_medium.json) | 승인 기준을 `medium`으로 변경한 테스트 설정 |
| [config_off.json](./config_off.json) | 알림 주소를 로컬 5999번 포트로 바꿔 연결 실패 상황을 확인하는 설정 |
| [config_broken.json](./config_broken.json) | `report_folder`, `webhook_url`이 빠졌을 때 설정 검사를 확인하는 파일 |

설정 파일을 분리하여 Python 코드를 직접 수정하지 않고도 승인 기준이나 알림 주소 등의 동작을 변경할 수 있도록 실습했습니다.

## 실습 및 테스트 파일

| 파일 | 내용 |
| --- | --- |
| [port_demo.py](./port_demo.py) | `argparse`를 이용해 CLI에서 포트 번호를 전달하는 실습 |
| [notype_demo.py](./notype_demo.py) | CLI 인자의 자료형 지정 여부에 따른 차이 확인 |
| [rule_demo.py](./rule_demo.py) | 포트와 탐지 룰을 CLI 인자로 전달하는 실습 |
| [demo_ids.json](./demo_ids.json) | 중복 처리 로직을 확인하기 위한 테스트 ID 데이터 |
| [test.md](./test.md) | Markdown 파일 생성 실습 |
| [alert_failures.log](./alert_failures.log) | 현재 보고서 저장 메시지가 기록된 로그로, 실패 예외 내역은 포함되어 있지 않음 |

## 실행 방법

Python 3 환경에서 저장소 루트의 `artifacts` 폴더로 이동하고, 실행할 실습에 필요한 패키지를 설치합니다.

```bash
cd artifacts
python -m pip install requests flask schedule
```

### 기존 테스트 확인

```bash
python test_agent_core.py
```

성공하면 `[테스트 통과] 9건 모두`를 출력합니다. 이 테스트는 외부 API를 호출하지 않고 보고서 문자열, 위험도 판정, JSON 변환 결과를 확인합니다.

### 경보 수신 실습

첫 번째 터미널에서 서버를 실행합니다.

```bash
python webhook_server.py --port 5001
```

다른 터미널에서도 `artifacts` 폴더로 이동한 뒤 요청을 보냅니다. 스크립트 실행에는 Bash와 curl이 필요합니다.

```bash
bash test_webhook.sh
```

경보 3종을 `POST /webhook`으로 전송하고, 정상 수신 시 각각 HTTP `200`을 출력합니다. 수신 목록은 현재 작업 폴더의 `received_alerts.json`에 저장됩니다.

### 보고서·알림 파이프라인

LLM 호출에는 `.env`의 `GEMINI_API_KEY`가 필요합니다. `llm_client.py`는 현재 작업 폴더부터 상위 경로를 탐색해 `.env`를 찾으며, 모델 이름은 `config.json`의 `model` 값을 사용합니다.

보고서 알림 수신 서버를 먼저 실행합니다.

```bash
python alert_server.py
```

다른 터미널의 `artifacts` 폴더에서 실행합니다.

```bash
python pipeline.py
```

`events_1008.json`의 경보를 요약·정렬하고 총평과 보고서를 생성한 뒤, 사람 확인이 필요한 경보 건수를 알림으로 보냅니다. 보고서 파일은 실행일 기준 `daily_report_YYYYMMDD.md` 이름으로 저장되며, 같은 이름의 파일이 있으면 덮어씁니다.

경보 수신 서버와 보고서 알림 서버의 기본 예제는 모두 5001번 포트를 사용하므로, 위 두 실습은 서버를 종료한 뒤 바꾸어 실행하거나 포트를 구분하여 실행합니다.

| 구분 | 경보 수신 | 보고서 알림 |
| --- | --- | --- |
| 서버 | `webhook_server.py` | `alert_server.py` |
| 경로 | `POST /webhook` | `POST /alert` |
| 입력 예시 | `{"rule": "brute_force"}` | `{"text": "보고서 저장 안내"}` |
| 처리 | 수신 목록을 JSON 파일에 저장 | 메시지를 콘솔에 출력 |

## 구현과 결과를 읽을 때

- `pipeline.py`의 입력은 현재 `events_1008.json`으로 고정되어 있습니다. 보고서 날짜를 바꾸더라도 입력 파일이 자동으로 다른 날짜의 경보로 바뀌지는 않습니다.
- 경보 요약은 한 번에 최대 6건씩 LLM에 전달하고, 총평 생성에도 별도 호출을 사용합니다.
- `report_folder`는 필수 설정 키이지만, 현재 `report_generator.py`의 `save_report()`는 보고서를 실행한 작업 폴더에 저장합니다.
- `needs_approval()`은 기준 위험도 이상의 경보를 판정합니다. 보고서 파이프라인에서는 확인 대상 건수를 집계해 알리며, 승인 응답을 기다리는 기능은 포함되어 있지 않습니다.
- `agent_result.json`에는 `lock_account`가 승인 대기(`held`)로 남은 결과가 있습니다. 현재 `tool_router.py`에 등록된 도구는 로그인 실패 집계와 IP 조회 두 가지입니다.
- `scheduler_job.py`는 점검 루프를 4회 확인하는 실습 코드이며, 신규 경보를 콘솔에 출력하고 처리한 ID를 저장합니다. 해당 코드에서 Webhook 요청을 보내지는 않습니다.
- `notifier.py`는 알림 요청 중 발생한 예외를 출력하고 `False`를 반환합니다. 현재 코드는 HTTP 오류 상태 코드를 별도로 검사하거나 `alert_failures.log`에 실패를 저장하지 않습니다.

## 관련 폴더

실제 구현 과정과 학습 코드는 [`agent_core`](../agent_core)에서 확인할 수 있습니다.

날짜별 학습 내용과 회고는 [`docs`](../docs)에서 확인할 수 있습니다.

[전체 저장소 안내](../README.md) · [1과목 회고](../docs/day08_retrospective.md)
