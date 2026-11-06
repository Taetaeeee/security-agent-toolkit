# 4과목 Day 5 도커 컴포즈로 서버 두 대 켜기 · 웹 서버 로그 만들기 · 오후 (이름 · 2026-11-06(금))

> **쓰는 법**
> - 문제를 풀 때마다 그 문제 제목 아래 질문에 답합니다.
> - 질문마다 `쓸 내용:` 에 무엇을 쓰면 되는지 적혀 있습니다. 그대로 `답:` 뒤에 씁니다.
> - 출력이나 코드를 붙여 넣는 질문은 `답:` 아래 빈 코드 상자에 붙여 넣고, 설명은 `답:` 뒤에 씁니다.
> - 「왜」를 묻는 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 이 교시에서 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다. 🔍 가 없는 질문도 못 적으면 같은 말을 씁니다.

---

## 5교시 · 도커 복습 · 컴포즈로 서버 두 대 한 번에 켜기

### 문제 5-1 · 서버 한 대를 복습하고 컴포즈로 두 대 켜기

- (가) 5교시 순서의 서버 켜기 · 확인 명령(`docker images` 부터 `curl` 까지)과 그 결과를 친 순서대로 붙여 넣고, 서비스 이름 두 개와 각 서비스의 포트를 적어 주세요.
  - 쓸 내용: ① 명령과 결과를 친 순서대로(코드 상자에 붙여 넣기): `docker images` · `docker run` · `docker ps` · `docker stop` · `docker compose up -d` · `docker compose ps` · `curl` 두 개 (`docker pull` 은 받았을 때만, `pwd` · `touch` · `ls` 는 붙이지 않아도 됩니다) ② 서비스 이름 두 개 ③ 각 서비스의 포트
  - 답: ② 서비스 이름 두 개 : web1, web2
  ③ 각 서비스의 포트 : web1의 포트 0.0.0.0:8080->80/tcp
                      web2의 포트 0.0.0.0:8081->80/tcp

```
docker images nginx:1.28
                                                                                                                                                                                                                        i Info →   U  In Use
IMAGE        ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:1.28   146adea4768b        240MB         65.8MB    U 


docker run -d --rm -p 8080:80 --name web-run nginx:1.28
643e7f136e455c0535b365261574755c64173542787bb1d4c55547c217719413


docker ps
CONTAINER ID   IMAGE        COMMAND                   CREATED         STATUS         PORTS                                     NAMES
643e7f136e45   nginx:1.28   "/docker-entrypoint.…"   6 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-run


docker stop web-run
web-run


docker compose up -d
[+] up 3/3
 ✔ Network anomaly_detection_default  Created                                                                                                                                                                                            0.0s
 ✔ Container anomaly_detection-web1-1 Started                                                                                                                                                                                            0.4s
 ✔ Container anomaly_detection-web2-1 Started


docker compose ps
NAME                       IMAGE        COMMAND                   SERVICE   CREATED          STATUS         PORTS
anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      10 seconds ago   Up 8 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      10 seconds ago   Up 8 seconds   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp


curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080
200


curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8081
200
```

- (나) 🔍 서버 두 대를 `docker run` 으로 켜는 것과 `compose.yaml` 과 `docker compose up -d` 로 켜는 것을 비교해, 컴포즈가 더 나은 점을 두 가지 적어 주세요.
  - 쓸 내용: ① 컴포즈가 더 나은 점 두 가지
  - 답: ① 컴포즈가 더 나은 점 두 가지 : 
  첫째, docker run으로 서버 두 대를 켜려면 각각 명령어를 입력해야 하지만, Docker Compose는 compose.yaml에 설정을 미리 작성해 두고 docker compose up -d 명령 한 번으로 실행할 수 있어 간편하다.
  둘째, 이미지 버전과 포트, 재시작 설정 등을 파일에 저장할 수 있으므로 다른 사람이 서버를 실행할 때도 같은 설정을 사용할 수 있다. 또한 설정을 확인하거나 수정하기도 편리하다.

- (다) 🔍 보안 사고가 난 뒤 감사팀이 「사고 당시와 같은 구성으로 서버를 다시 켜 보라」고 요청했습니다. 팀원 한 명은 3주 전에 긴 `docker run` 명령을 직접 쳐서 서버를 켰는데 그 명령을 기억하지 못합니다. 다른 팀은 `compose.yaml` 을 깃허브에 올려 두었습니다. 두 팀이 같은 구성을 다시 켤 수 있는지 비교하고, 파일에 `nginx:1.28` 처럼 버전을 적어 두는 것이 이런 재현에 왜 중요한지 적어 주세요.
  - 쓸 내용: ① 두 팀의 차이 ② 버전을 적어 두는 것이 재현에 중요한 이유
  - 답: ① 두 팀의 차이 : docker run 명령을 직접 입력한 팀은 당시 사용했던 명령어를 기록하지 않았다면 포트나 실행 옵션 등을 정확하게 기억하기 어려워 사고 당시와 같은 구성으로 서버를 다시 실행하기 어렵다.반면 compose.yaml을 GitHub에 저장한 팀은 당시 작성한 설정을 확인할 수 있으므로 같은 이미지와 포트, 실행 옵션을 사용해 서버를 다시 실행하기 쉽다.
  ② 버전을 적어 두는 것이 재현에 중요한 이유 : 이미지 버전을 명시하지 않으면 나중에 서버를 다시 실행할 때 사고 당시와 다른 버전의 프로그램을 사용할 수 있기 때문이다. 버전이 달라지면 프로그램의 동작이나 설정이 달라질 수도 있으므로, nginx:1.28처럼 사용한 버전을 기록해 두어야 사고 당시 환경을 재현하기 쉽다.

- (라) 🔍 팀원 세 명이 같은 `compose.yaml` 로 서버를 켰는데 한 명의 PC 에서만 `8081` 번 포트를 다른 프로그램이 쓰고 있어서 `web2` 가 켜지지 않았습니다. 이 사람이 파일의 어느 줄을 어떻게 바꾸면 되는지 적고, 바꿔도 서버 안에서는 여전히 `80` 번 포트로 동작하는 이유를 적어 주세요. 이 사람이 `curl` 로 확인할 때 달라지는 점도 적어 주세요.
  - 쓸 내용: ① 바꿀 줄과 바꾼 모양 ② 서버 안은 그대로 80 인 이유 ③ curl 주소의 달라지는 점
  - 답: ① 바꿀 줄과 바꾼 모양 : services의 web2 안에 ports 설정을 기존 "8081:80"에서 "8082:80"으로 바꾼다.
  ② 서버 안은 그대로 80 인 이유 : "8082:80"에서 앞의 8082는 내 컴퓨터에서 사용하는 포트이고, 뒤의 80은 컨테이너 내부에서 사용하는 포트이다. 내 컴퓨터의 포트만 8082로 변경한 것이므로 컨테이너 안의 Nginx는 기존과 동일하게 80번 포트로 동작한다.
  ③ curl 주소의 달라지는 점 : 기존에는 http://localhost:8081로 확인했지만, 변경한 후에는 http://localhost:8082로 확인해야 한다. 명령어는 다음과 같다.
  curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8082

## 6교시 · 서버마다 접속 범위 정하기 · 설정 바꿔 적용하기

### 문제 6-1 · 서버마다 접속 범위를 정해 컴포즈 파일로 적용하기

- (가) 1번과 5번의 `docker compose ps` 출력을 붙여 넣고, 접속 범위가 바뀐 기존 서비스와 새로 추가된 서비스를 따로 적어 주세요.
  - 쓸 내용: ① 1번 출력(코드 상자에 붙여 넣기) ② 5번 출력(코드 상자에 붙여 넣기) ③ 접속 범위가 바뀐 기존 서비스 ④ 새로 추가된 서비스
  - 답: ③ 접속 범위가 바뀐 기존 서비스 : web2
  ④ 새로 추가된 서비스 : web3

```
$ docker compose ps
NAME                       IMAGE        COMMAND                   SERVICE   CREATED             STATUS             PORTS
anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      About an hour ago   Up About an hour   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      About an hour ago   Up About an hour   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp


$ docker compose -f compose.secure.yaml ps
NAME                       IMAGE        COMMAND                   SERVICE   CREATED             STATUS             PORTS
anomaly_detection-web1-1   nginx:1.28   "/docker-entrypoint.…"   web1      About an hour ago   Up About an hour   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
anomaly_detection-web2-1   nginx:1.28   "/docker-entrypoint.…"   web2      17 seconds ago      Up 15 seconds      127.0.0.1:8081->80/tcp
anomaly_detection-web3-1   nginx:1.28   "/docker-entrypoint.…"   web3      17 seconds ago      Up 16 seconds      127.0.0.1:8082->80/tcp
```

- (나) 🔍 `"8081:80"` 과 `"127.0.0.1:8081:80"` 은 누가 접속할 수 있는지가 어떻게 다른가요? 관리 화면이나 데이터베이스 서버를 이렇게 설정하는 이유도 적어 주세요.
  - 쓸 내용: ① 두 포트 줄에서 누가 접속할 수 있는지의 차이 ② 관리 화면 · 데이터베이스를 이렇게 설정하는 이유
  - 답: ① 두 포트 줄에서 누가 접속할 수 있는지의 차이 : "8081:80"은 내 PC의 8081번 포트를 모든 네트워크 인터페이스에 연결하므로, 네트워크와 방화벽 설정에 따라 다른 PC에서도 접속할 수 있다. 반면 "127.0.0.1:8081:80"은 내 PC의 루프백 주소로 접속 범위를 제한하므로 다른 PC에서는 직접 접속할 수 없고, 내 PC에서만 접속할 수 있다.
  ② 관리 화면 · 데이터베이스를 이렇게 설정하는 이유 : 관리 화면이나 데이터베이스는 외부에 공개할 필요가 없는 경우가 많기 때문이다. 접속 범위를 내 PC로 제한하면 다른 PC에서 직접 접근하는 것을 막아 불필요한 접근 시도를 줄일 수 있다.

- (다) 🔍 `up -d` 의 출력에서 `web1` 은 `Running`, `web2` 는 `Recreated`, `web3` 은 `Created` 였습니다. 서버마다 출력이 다른 이유와, 운영 중인 서비스의 설정을 바꿀 때 이것이 왜 도움이 되는지 적어 주세요.
  - 쓸 내용: ① 서버마다 출력이 다른 이유 ② 서버를 끊지 않고 바꿀 수 있는 것의 쓸모
  - 답: ① 서버마다 출력이 다른 이유 : 
  web1은 기존 설정과 새 설정이 같기 때문에 컨테이너를 다시 만들지 않고 계속 실행되어 Running으로 표시되었다.
  web2는 접속 범위를 기존 "8081:80"에서 "127.0.0.1:8081:80"으로 변경했기 때문에 기존 컨테이너를 새 설정으로 다시 만들어 Recreated로 표시되었다.
  web3은 새로 추가한 서비스이므로 새로운 컨테이너가 만들어져 Created로 표시되었다.
  ② 서버를 끊지 않고 바꿀 수 있는 것의 쓸모 : 설정이 변경되지 않은 서버는 계속 실행하고, 설정이 바뀐 서버만 다시 만들 수 있기 때문이다. 따라서 web2의 접속 범위를 수정하거나 web3을 새로 추가하더라도 web1은 중단하지 않고 계속 운영할 수 있다. 이렇게 하면 설정 변경으로 영향을 받는 서버를 줄이고, 정상적으로 실행 중인 서비스의 불필요한 중단을 방지할 수 있다.

### 마무리 · 오늘 만든 것을 깃허브에 올리기

- (가) `git status` 를 쳤을 때 `.env` 나 `.venv` 가 보였는지, 보였다면 어떻게 했는지 적어 주세요.
  - 쓸 내용: ① `.env` · `.venv` 가 보였는지 ② 보였다면 한 조치
  - 답: 없다.
