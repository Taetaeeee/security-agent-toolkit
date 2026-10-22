# network_zt

네트워크 통신의 기본 구조부터 DNS·VPN·방화벽, 클라우드 구역 설계, **Zero Trust 정책 판단과 로그 점검**, **Docker 서버 실습**까지 진행한 코드와 문서를 모아 둔 폴더입니다.

패킷과 접속 기록을 관찰하고, 규칙을 Python으로 표현해 결과를 비교한 뒤, 근거와 권고를 담은 보고서로 정리했습니다. 실습 기간은 2026년 10월 12일부터 10월 21일까지입니다.

## 학습 영역

| 영역 | 주요 내용 |
| --- | --- |
| 네트워크 기초 | OSI 계층, IP·MAC 주소, TCP·UDP, Wireshark 패킷 분석 |
| 주소·망 설계 | 사설 주소, 서브넷, 스위치·라우터, VLAN과 라우팅 |
| 네트워크 보안 | DNS 구조·캐시·의심 도메인 판정, VPN, 방화벽 규칙과 순서 |
| 클라우드·품질 | 구역 간 허용 포트, 망 구성도, 지연·지터·손실과 품질 판정 |
| Zero Trust | 신원·기기·접속 조건, 위험 점수, PDP·PEP, 세션과 지속 검증 |
| 정책·로그 분석 | 판단과 집행 비교, 오탐·미탐, 거부 후 허용 기록, 점검 보고서 |
| Docker | nginx 서버, 포트 연결, 볼륨, Dockerfile과 이미지 생성·버전 관리 |

## 날짜별 실습 안내와 보고서

| 날짜 | 주제 | 실습 안내 | 보고서·산출물 |
| --- | --- | --- | --- |
| Day 1 · 10/12 | OSI·TCP·패킷 분석 | [OSI 계층](./261012_am_osi_layers.md), [TCP·Wireshark](./261012_pm_tcp_wireshark.md) | [패킷 분석 보고서](./day01_packet_analysis.md) |
| Day 2 · 10/13 | IP·서브넷·VLAN | [IP·서브넷](./261013_am_ip_subnet.md), [스위치·라우터·VLAN](./261013_pm_switch_router_vlan.md) | [서브넷 설계서](./day02_subnet_design.md) |
| Day 3 · 10/14 | DNS·의심 도메인 | [DNS 기초](./day03_am_dns.md), [의심 도메인 판정](./day03_pm_dns_suspicious.md) | [오전 보고서](./day03_am_report.md), [오후 보고서](./day03_pm_report.md) |
| Day 4 · 10/15 | VPN·방화벽 | [VPN](./day04_am_vpn.md), [방화벽](./day04_pm_firewall.md) | [VPN 보고서](./day04_am_report.md), [방화벽 보고서](./day04_pm_report.md) |
| Day 5 · 10/16 | 클라우드 구역·품질 | [망 구성·구역 규칙](./day05_am_cloud_diagram.md), [네트워크 품질](./day05_pm_quality.md) | [오전 보고서](./day05_am_report.md), [오후 보고서](./day05_pm_report.md), [도식](./day05_diagram.md) |
| Day 6 · 10/19 | Zero Trust·Docker 기초 | [Zero Trust](./day06_am_zero_trust.md), [Docker·nginx](./day06_pm_docker_basics.md) | [오전 보고서](./day06_am_report.md), [오후 보고서](./day06_pm_report.md), [A사 적용 방안](./day06_zt_scenario.md) |
| Day 7 · 10/20 | 정책 집행·이미지 관리 | [정책 로그·지속 검증](./day07_am_policy_log.md), [Docker 이미지·버전 관리](./day07_pm_docker_compose.md) | [오전 보고서](./day07_am_report.md), [오후 보고서](./day07_pm_report.md), [정책 로그 점검 결과](./day07_log_summary.md) |
| Day 8 · 10/21 | 서버 점검·로그 상관 분석 | [종합 실습 안내](./day08_am_issue_map.md) | [실습 보고서](./day08_am_report.md), [이슈 도식](./day08_issue_diagram.md), [정산 포털 로그 점검 결과](./day08_customer_report.md) |

## 주요 코드

| 파일 | 역할 |
| --- | --- |
| [addr_kind.py](./addr_kind.py) | 구분자와 항목 수를 이용해 IP·MAC 형태를 구분하는 기초 실습 |
| [ping_check.py](./ping_check.py) | 코드 안에 준비한 응답 시간으로 정상·느림·실패 분류 |
| [warmup_7_1.py](./warmup_7_1.py) 등 `warmup*.py` | IP·서브넷 계산과 조건문·반복문 복습 |
| [day03_7-1_judge_new.py](./day03_7-1_judge_new.py) | 도메인 길이·최상위 도메인·NXDOMAIN 조건으로 점수 계산 |
| [day03_7-2_my_logs.py](./day03_7-2_my_logs.py) | 직접 구성한 DNS 기록을 이용한 의심 판정 실습 |
| [day04_7-1_my_rules.py](./day04_7-1_my_rules.py), [day04_7-2_rules_admin.py](./day04_7-2_rules_admin.py) | 출발지·목적지 대역, 포트, 규칙 순서에 따른 허용·차단 판정 |
| [day05_4-1_zone_rules.py](./day05_4-1_zone_rules.py), [day05_4-2_allowed_ports.py](./day05_4-2_allowed_ports.py) | outside·DMZ·inside 구역 규칙과 허용 포트 확인 |
| [day05_6-1_measure.py](./day05_6-1_measure.py), [day05_6-2_judge.py](./day05_6-2_judge.py) | 예제 응답 시간에서 지연·지터·손실을 계산하고 회선 적합성 판정 |
| [day06_3-1_decide_admin.py](./day06_3-1_decide_admin.py), [day06_3-2_batch_decide.py](./day06_3-2_batch_decide.py) | 계정·기기·요청 조건을 검사해 허용·추가확인·거부 판정 |
| [day06_4-1_zt_score.py](./day06_4-1_zt_score.py) | MFA·기기·최소권한·세그멘테이션·위험 기반 인증을 실습 기준으로 점수화 |
| [day07_2-1_session_state.py](./day07_2-1_session_state.py) | 자원별 세션 유지 시간에 따라 유지·재인증·종료 판정 |
| [day07_3-1_enforcement_check.py](./day07_3-1_enforcement_check.py) | 요청 ID로 정책 결정과 앱 응답을 비교해 집행 누락·과집행·정책 기록 부재 확인 |
| [day07_4-1_rule_tuning.py](./day07_4-1_rule_tuning.py) | 현재 규칙과 조정안 A·B·C의 오탐·미탐 비교 |
| [day08_3-1_deny_then_allow.py](./day08_3-1_deny_then_allow.py) | JSON 문자열 로그에서 같은 사용자의 10분 이내 거부 후 허용 기록과 거부 이유별 건수 출력 |

`day03_*.py`, `day04_*.py` 등은 같은 주제를 조건·임계값별로 나누어 확인한 실습 파일입니다. [sample.log](./sample.log)는 로그 검색 연습에 사용하는 예제 파일입니다.

## Docker 실습 자료

| 위치 | 내용 |
| --- | --- |
| [day06_docker/site-one](./day06_docker/site-one/), [site-two](./day06_docker/site-two/) | nginx 서버와 연결해 확인하는 HTML 페이지 |
| [day07_docker/Dockerfile](./day07_docker/Dockerfile) | `nginx:1.28` 이미지를 기반으로 `site-three/index.html`을 복사하는 이미지 정의 |
| [day07_docker/site-three](./day07_docker/site-three/), [site-four](./day07_docker/site-four/) | 서버별 페이지와 이미지·파일 변경 실습에 사용하는 HTML |

[day07_pm_docker_compose.md](./day07_pm_docker_compose.md)는 파일명과 달리 Dockerfile, 이미지 생성과 버전 관리 실습을 담고 있습니다. 현재 폴더에는 Compose 설정 파일이 포함되어 있지 않습니다.

## 실행 방법

아래 예제는 Python 3와 표준 라이브러리만 사용하며, 코드에 포함된 실습 데이터로 결과를 출력합니다. 저장소 루트에서 실행합니다.

```bash
cd network_zt
python day04_7-1_my_rules.py
python day06_4-1_zt_score.py
python day07_3-1_enforcement_check.py
python day07_4-1_rule_tuning.py
python day08_3-1_deny_then_allow.py
```

| 실행 파일 | 현재 실습 데이터의 결과 |
| --- | --- |
| `day04_7-1_my_rules.py` | 요청 8건 모두 기대한 허용·차단 결과와 일치 (`점수: 8 / 8`) |
| `day06_4-1_zt_score.py` | MFA 10점, 기기 5점, 최소권한 15점, 나머지 0점으로 총 30/100점 |
| `day07_3-1_enforcement_check.py` | 집행 누락 2건, 과집행 1건, 정책 로그에 없는 요청 1건 |
| `day07_4-1_rule_tuning.py` | 현재 규칙 오탐 6·미탐 0, A안 0·1, B안 0·2, C안 0·2 |
| `day08_3-1_deny_then_allow.py` | 10분 이내 거부 후 허용 2건, 거부 이유별 건수 2·4·1·1 |

DNS 조회 예제는 실제 이름 해석을 사용하며, Wireshark 패킷 캡처와 Docker 서버 실습은 해당 도구와 실행 환경이 필요합니다. 환경 준비와 상세 명령은 날짜별 실습 안내에서 확인합니다.

## 결과를 해석할 때

- **정책 판단과 실제 집행을 구분합니다.** Python의 허용·거부 출력은 실습 데이터에 대한 판정이며, 실제 방화벽이나 접근 게이트웨이의 차단을 실행하는 코드는 아닙니다.
- **점수와 임계값은 실습 기준입니다.** Zero Trust 점수와 DNS 판정 규칙은 예제 조건에 따른 결과로, 운영 환경의 공통 기준으로 사용하려면 별도 검토가 필요합니다.
- **기록 부재와 우회를 구분합니다.** 정책 로그 없이 앱에서 처리된 요청은 코드에서 `[우회]`로 출력되지만, 실제 우회인지 정책 로그 누락인지는 추가 근거로 확인해야 합니다.
- **오탐을 줄이는 조정의 미탐도 비교합니다.** A안은 예제의 오탐을 줄이지만, 위험 요청 1건을 거부하지 못합니다. 이 실습에서는 정상 요청의 불필요한 제한을 오탐, 위험 요청을 거부하지 못한 경우를 미탐으로 집계합니다.
- **분석 시간 범위에 따라 결과가 달라집니다.** 현재 상관 분석 코드는 10분 기준입니다. [정산 포털 로그 점검 결과](./day08_customer_report.md)에는 60분으로 넓혔을 때 추가된 사례와 확인할 사항을 함께 기록했습니다.

## 관련 자료

- [전체 저장소 안내](../README.md)
- [날짜별 학습 기록](../docs/)
- [역할 기반 접근통제 실습](../access_control/)
- [보안 자동화 학습 노트북](../agent_core/)
- [경보 분석·보고서 산출물](../artifacts/)
