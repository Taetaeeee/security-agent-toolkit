# Security Agent Toolkit

Python과 LLM을 활용한 **보안 로그 분석·관제 자동화**, 네트워크와 **Zero Trust**, **역할 기반 접근통제(RBAC)**를 학습하고 구현한 실습 저장소입니다.

로그를 정리하고 탐지 규칙을 적용하는 과정부터 경보 요약, 보고서 생성, 접근 정책 판단과 권한 점검까지 단계별 코드와 결과를 기록했습니다.

## 학습 영역

| 영역 | 주요 내용 | 관련 폴더 |
| --- | --- | --- |
| 보안 로그 분석·관제 자동화 | Python 기초, 로그 파싱·정규화, 탐지 규칙, API·Webhook, LLM 분석, 보고서·알림 | [agent_core](./agent_core/), [artifacts](./artifacts/) |
| 네트워크·Zero Trust | OSI·TCP/IP, 패킷 분석, 서브넷·VLAN, DNS, VPN·방화벽, 접근 정책, Docker | [network_zt](./network_zt/) |
| 접근통제 자동화 | 사용자·역할·권한 관리, RBAC 판정, 접속 기록 재판정, 미사용 권한 점검 | [access_control](./access_control/) |
| 학습 기록·회고 | 날짜별 학습 내용, 사용한 명령어, 오류와 해결 과정, 추가 확인 사항 | [docs](./docs/) |

각 영역은 과목별 실습으로 구성되어 있습니다. 보안 경보의 요약·보고서·알림은 파이프라인으로 연결했으며, 네트워크·Zero Trust와 RBAC 실습은 별도 코드와 문서로 정리했습니다.

## 폴더 구성

| 폴더 | 역할 | 주요 파일 |
| --- | --- | --- |
| [access_control](./access_control/) | RBAC 구현과 권한 점검 | `rbac.py`, `config/roles.json`, `config/users.json`, `day01_7-1_audit.py` |
| [agent_core](./agent_core/) | Python·보안 자동화 학습 노트북과 일부 실행 코드 | 날짜별 `.ipynb`, `pipeline.py`, `webhook_server.py` |
| [artifacts](./artifacts/) | 실습에서 만든 실행 코드, 입력 데이터, 분석 결과와 보고서 | `llm_client.py`, `event_summarizer.py`, `report_generator.py`, `pipeline.py`, `daily_report_*.md` |
| [docs](./docs/) | 날짜별 학습 기록과 과목 회고 | 날짜별 `.md`, `day08_retrospective.md` |
| [network_zt](./network_zt/) | 네트워크·Zero Trust 실습 코드와 보고서, Docker 실습 자료 | `day*_*.py`, `day*_report.md`, `day06_docker/`, `day07_docker/` |

`agent_core`에는 학습 과정을 담은 노트북이 있고, `artifacts`에는 실습 중 저장한 모듈과 데이터가 모여 있습니다. 경보 요약과 보고서 생성에 필요한 관련 모듈은 `artifacts`에서 함께 확인할 수 있습니다.

## 주요 구현 및 실습

### 1. 보안 로그 분석·관제 자동화

- Python의 리스트·딕셔너리, 조건문·반복문, 함수와 파일 입출력을 활용한 로그 처리
- 예외 처리와 Logging을 이용한 오류 확인, JSON 형식의 로그 정규화
- 정규표현식과 규칙을 활용한 로그인 실패·의심 접속 탐지
- Requests 기반 외부 API 조회와 Flask Webhook 경보 수신
- 처리한 경보 ID를 기록하는 중복 처리 방지와 스케줄 실행
- Gemini API를 이용한 경보 요약과 `high / medium / low` 위험도 분류
- 위험도순 정렬, Markdown 관제 보고서 생성, 확인 대상 경보 건수와 알림 연동
- 설정 파일 분리, `assert` 기반 결과 검증과 디버깅

관련 자료: [학습 노트북](./agent_core/) · [실행 코드와 산출물](./artifacts/) · [1과목 회고](./docs/day08_retrospective.md)

### 2. 네트워크·Zero Trust

- OSI 계층, TCP 통신과 Wireshark 패킷 분석
- IP 주소·서브넷 설계, 스위치·라우터·VLAN 개념 정리
- DNS 구조와 의심 도메인 판정, VPN·방화벽 규칙 실습
- 클라우드 네트워크 구역 구성과 지연·손실 등 품질 지표 확인
- 사용자·기기·접속 조건에 따른 접근 정책 판단
- PDP의 정책 결정과 PEP의 집행 결과 비교, 세션 상태와 오탐·미탐 점검
- Docker와 nginx를 이용한 서버 실행, 포트 연결, 볼륨, 이미지 생성·버전 관리
- 정책 로그와 접속 기록을 비교한 이슈 분석 및 점검 보고서 작성

관련 자료: [네트워크·Zero Trust 실습](./network_zt/) · [정책 로그 점검 결과](./network_zt/day07_log_summary.md) · [정산 포털 로그 점검 결과](./network_zt/day08_customer_report.md)

### 3. 역할 기반 접근통제(RBAC)

- 사용자 정보와 역할별 권한을 JSON 파일로 분리
- 사용자 등록 여부 → 재직 여부 → 역할 존재 여부 → 요청 권한 순서로 검사
- 허용 목록에 없는 요청은 기본 거부하고 판정 이유 반환
- 기존 접속 기록을 RBAC 규칙으로 다시 판정하여 허용·거부 내역 집계
- 역할별 사용 권한을 비교해 미사용 권한과 회수 검토 대상 확인

관련 자료: [권한 판정 함수](./access_control/rbac.py) · [접속 기록 재판정 코드](./access_control/day01_7-1_audit.py) · [RBAC 실습 보고서](./access_control/day01_pm_report.md)

## 대표 산출물

| 산출물 | 확인할 내용 |
| --- | --- |
| [보안 경보 입력 데이터](./artifacts/events_1008.json) | LLM 분석과 보고서 생성에 사용한 경보 목록 |
| [경보 요약 결과](./artifacts/event_summaries.json) | 경보별 위험도와 한국어 요약 |
| [위험도순 정렬 결과](./artifacts/sorted_summaries.json) | `high → medium → low` 순으로 정리한 경보 |
| [보안 관제 보고서](./artifacts/daily_report_20261008.md) | 처리 건수, 위험 경보, 총평과 건별 내역 |
| [보고서·알림 파이프라인](./artifacts/pipeline.py) | 경보 요약부터 보고서 저장·확인 대상 집계·알림까지 연결한 코드 |
| [Zero Trust 적용 방안](./network_zt/day06_zt_scenario.md) | 신원·기기·네트워크·애플리케이션·정책 관점의 개선 방안 |
| [정책 로그 점검 결과](./network_zt/day07_log_summary.md) | 판단과 집행의 불일치, 규칙 조정에 따른 오탐·미탐 비교 |
| [RBAC 실습 보고서](./access_control/day01_pm_report.md) | 권한 매트릭스, 요청 판정 결과, 미사용 권한 검토 |

## 사용 기술·도구

| 구분 | 기술·도구 |
| --- | --- |
| 언어·학습 환경 | Python, Jupyter Notebook |
| 데이터·로그 처리 | JSON, CSV, 정규표현식, Logging |
| API·자동화 | Requests, Flask, schedule, curl |
| LLM | Gemini API, 프롬프트 구성, JSON 응답 처리 |
| 네트워크·서버 | Wireshark, Docker, nginx |
| 기록·버전 관리 | Git, GitHub, Markdown, Mermaid |

## 저장소 살펴보기

1. **구현 과정**은 [agent_core](./agent_core/)의 날짜별 노트북에서 확인합니다.
2. **입력 데이터·분석 결과·보고서**는 [artifacts](./artifacts/)에서 비교합니다.
3. **네트워크와 접근 정책 분석**은 [network_zt](./network_zt/)의 코드와 보고서에서 확인합니다.
4. **권한 판정과 점검 과정**은 [access_control](./access_control/)에서 확인합니다.
5. **문제 해결 과정과 회고**는 [docs](./docs/)에서 확인합니다.
