# access_control

사용자와 역할별 권한을 JSON으로 관리하고, **역할 기반 접근통제(RBAC)**로 요청을 판정하는 실습 폴더입니다.

사용자 등록 여부만 확인하던 방식에서 재직 여부·역할·요청 권한을 순서대로 검사하도록 확장했습니다. 기존 접속 기록도 같은 규칙으로 다시 판정하고, 기록에서 사용되지 않은 권한을 찾아 최소권한 관점에서 검토했습니다.

## 주요 실습 내용

- 인증과 인가의 차이, 역할별 권한 매트릭스와 최소권한 원칙 이해
- 사용자 정보와 역할별 권한을 JSON 설정 파일로 분리
- `check_permission()` 함수로 허용 여부와 판정 이유 반환
- 미등록 사용자, 퇴사 계정, 정의되지 않은 역할, 권한 없는 요청 거부
- 접속 기록을 재판정하여 전체·사용자별 허용 및 거부 건수 집계
- 역할별 부여 권한과 실제 사용 권한을 비교하여 미사용 권한 확인

## 파일 구성

| 파일 | 역할 |
| --- | --- |
| [config/users.json](./config/users.json) | 사용자별 역할(`role`)과 재직 여부(`employed`) 설정 |
| [config/roles.json](./config/roles.json) | 역할별로 허용하는 `자원:행위` 목록 설정 |
| [rbac.py](./rbac.py) | 설정 파일을 읽고 요청의 허용 여부와 이유를 판정 |
| [day01_6-1_run.py](./day01_6-1_run.py) | 요청 9건을 판정하여 정상 허용과 거부 사유 확인 |
| [access_log.py](./access_log.py) | 권한 점검에 사용하는 조회 기록 15건 |
| [day01_7-1_audit.py](./day01_7-1_audit.py) | 접속 기록 재판정, 사용자별 집계, 미사용 권한 출력 |
| [day01_pm_rbac.md](./day01_pm_rbac.md) | RBAC 개념과 구현 절차를 담은 실습 안내 |
| [day01_pm_report.md](./day01_pm_report.md) | 판정 결과, 검사 순서, 권한 점검과 개선 방향을 정리한 실습 보고서 |

## 권한 구성

권한은 `자원:행위` 형식으로 정의합니다. 자원은 `SALES`(영업 실적), `SETTLE`(정산 내역), `ACCOUNT`(계정)이며, 행위는 `QUERY`(조회)와 `CHANGE`(변경)로 구분합니다.

현재 [roles.json](./config/roles.json)에 저장된 권한은 다음과 같습니다.

| 역할 | SALES 조회 | SALES 변경 | SETTLE 조회 | SETTLE 변경 | ACCOUNT 조회 | ACCOUNT 변경 |
| --- | --- | --- | --- | --- | --- | --- |
| `sales` | 허용 | 허용 | 거부 | 거부 | 거부 | 거부 |
| `account_admin` | 거부 | 거부 | 거부 | 거부 | 허용 | 허용 |
| `finance` | 허용 | 거부 | 허용 | 거부 | 거부 | 거부 |
| `batch` | 거부 | 거부 | 허용 | 거부 | 거부 | 거부 |
| `auditor` | 허용 | 거부 | 허용 | 거부 | 허용 | 거부 |

`tester` 사용자는 `intern` 역할을 갖지만, 역할 파일에는 `intern`이 정의되어 있지 않습니다. 정의되지 않은 역할의 요청을 거부하는지 확인하기 위한 실습 사례입니다.

## 권한 판정 흐름

`check_permission(user, resource, action)`은 다음 순서로 검사하고, 실패한 단계에서 바로 결과를 반환합니다.

| 순서 | 검사 조건 | 조건을 통과하지 못했을 때 반환값 |
| --- | --- | --- |
| 1 | 사용자 파일에 등록된 계정인가? | `(False, "등록되지 않은 사용자")` |
| 2 | 재직 중인 계정인가? | `(False, "퇴사한 계정")` |
| 3 | 사용자의 역할이 역할 파일에 정의되어 있는가? | `(False, "역할이 없음")` |
| 4 | 요청한 `자원:행위`가 해당 역할의 권한 목록에 있는가? | `(False, "권한 없음")` |
| 통과 | 네 가지 조건을 모두 만족하는가? | `(True, "허용")` |

예를 들어 `seoyeon`은 등록된 재직자이고 `sales` 역할도 유효하지만, `SETTLE:QUERY` 권한이 없어 정산 조회 요청은 거부됩니다.

## 실행 방법

Python 3와 표준 라이브러리만 사용하므로 별도 패키지 설치는 필요하지 않습니다. 저장소 루트에서 다음과 같이 실행합니다.

```bash
cd access_control
python day01_6-1_run.py
python day01_7-1_audit.py
```

설정 파일 경로가 현재 작업 폴더 기준인 `config/roles.json`, `config/users.json`으로 지정되어 있어 `access_control` 폴더 안에서 실행해야 합니다. 설정은 `rbac.py`를 불러올 때 읽으므로 JSON을 수정한 뒤에는 스크립트를 다시 실행하여 결과를 확인합니다.

### 요청 9건 판정

`day01_6-1_run.py`의 실행 결과입니다.

| 사용자 | 자원 | 행위 | 허용 여부 | 이유 |
| --- | --- | --- | --- | --- |
| `seoyeon` | `SALES` | `QUERY` | `True` | 허용 |
| `seoyeon` | `SETTLE` | `QUERY` | `False` | 권한 없음 |
| `junho` | `SETTLE` | `QUERY` | `True` | 허용 |
| `junho` | `SALES` | `CHANGE` | `False` | 권한 없음 |
| `dami` | `SALES` | `QUERY` | `False` | 퇴사한 계정 |
| `minsu` | `SALES` | `QUERY` | `False` | 등록되지 않은 사용자 |
| `gaeun` | `ACCOUNT` | `CHANGE` | `True` | 허용 |
| `batch-night` | `SETTLE` | `QUERY` | `True` | 허용 |
| `tester` | `SALES` | `QUERY` | `False` | 역할이 없음 |

### 접속 기록 15건 재판정

`day01_7-1_audit.py`는 [access_log.py](./access_log.py)의 기록을 재판정합니다.

| 사용자 | 허용 | 거부 |
| --- | --- | --- |
| `batch-night` | 1건 | 0건 |
| `junho` | 3건 | 0건 |
| `seoyeon` | 3건 | 8건 |
| **합계** | **7건** | **8건** |

거부된 기록 번호는 `3, 4, 5, 12, 14, 15, 16, 17`이며, 모두 `seoyeon`의 `SETTLE:QUERY` 요청입니다. 이 결과는 저장된 실습 기록을 새 권한 규칙으로 재판정한 결과입니다.

## 미사용 권한 점검

재판정에서 허용된 요청의 권한을 역할별로 모은 뒤, 부여된 권한 목록과 비교합니다. 현재 기록에서 사용되지 않은 권한은 다음과 같습니다.

| 역할 | 기록에서 사용되지 않은 권한 |
| --- | --- |
| `sales` | `SALES:CHANGE` |
| `account_admin` | `ACCOUNT:QUERY`, `ACCOUNT:CHANGE` |
| `finance` | `SALES:QUERY` |
| `auditor` | `SALES:QUERY`, `SETTLE:QUERY`, `ACCOUNT:QUERY` |

미사용 권한은 회수 여부를 검토할 후보입니다. 이번 자료는 하루치 조회 기록이므로 변경 업무나 정기 감사에 필요한 권한은 사용되지 않은 것으로 나올 수 있습니다. 실제 업무와 더 긴 기간의 기록을 함께 확인한 뒤 유지·회수를 판단하도록 정리했습니다.

## 학습한 점

- 정상 계정으로 접속했더라도 요청한 업무 권한이 있는지는 별도로 확인해야 합니다.
- 위험 점수 기반 실습과 RBAC 실습은 판단에 사용하는 정보가 다릅니다. 시간·기기 조건이 정상이어도 역할에 정산 조회 권한이 없다면 RBAC에서 거부할 수 있습니다.
- 검사 순서가 바뀌면 같은 거부 결과라도 기록되는 이유가 달라질 수 있어, 원인 분석에 필요한 순서를 고려해야 합니다.
- 재직 정보와 권한 설정이 실제 상태를 반영해야 올바르게 판정할 수 있습니다.
- 현재 함수는 사용자·재직·역할·권한을 검사합니다. 시간, 기기, MFA 조건은 별도 확장 항목으로 검토했습니다.

## 관련 자료

- [전체 저장소 안내](../README.md)
- [네트워크·Zero Trust 실습](../network_zt/)
- [Zero Trust 적용 방안](../network_zt/day06_zt_scenario.md)
- [RBAC 실습 보고서](./day01_pm_report.md)
