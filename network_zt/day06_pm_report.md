# Day 6 Docker ① · nginx 서버 · 오후 (이름 · 2026-10-19)

> **쓰는 법**
> - 문제를 하나 풀 때마다 그 문제 제목 아래를 채웁니다.
> - 질문마다 `쓸 내용:` 에 **무엇을 쓰면 되는지** 적혀 있습니다. 그 내용대로 `답:` 뒤에 씁니다.
> - 「왜 그럴까요?」 같은 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 그 교시에 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다.

---

## 5교시 · 왜 도커인가 · 이미지와 컨테이너 · 같이 설치하기

### 문제 5-1 · 설치를 확인하고 첫 컨테이너 실행하기

- (가) `docker --version` 으로 나온 값을 적어 주세요.
  - 쓸 내용: 「Docker version … build …」 한 줄
  - 답: Docker version 29.8.2, build 7fc2dff
- (나) 🔍 `docker run hello-world` 출력이 말하는 일의 순서를 5.5 그림의 번호(① ~ ④)에 맞춰 설명해 주세요.
  - 쓸 내용: ① ~ ④ 번호마다 한 일 (클라이언트 · 엔진 · Docker Hub · 컨테이너)
  - 답: ① The Docker client contacted the Docker daemon.
          Docker 클라이언트가 Docker 엔진에 실행을 요청한다
        ② The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
          Docker 엔진이 로컬에 이미지가 없으면 Docker Hub에서 hello-world 이미지를 다운로드한다.
        ③ The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
          Docker 엔진이 다운로드한 이미지로 컨테이너를 생성하고 실행한다.
        ④ The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
          컨테이너에서 출력된 결과가 Docker 엔진과 클라이언트를 거쳐 터미널에 표시된다.
- (다) 🔍 `docker images` 에 보인 것과 `docker ps -a` 에 보인 것은 각각 이미지와 컨테이너 중 무엇이고, 어떻게 다른가요?
  - 쓸 내용: ① images 에 보인 것과 그 종류 ② ps -a 에 보인 것과 그 종류 ③ 둘의 차이
  - 답: 
  docker images는 PC에 저장된 Docker 이미지의 이름, ID, 디스크 사용량 등을 보여준다. 이미지는 컨테이너를 생성하기 위한 실행 환경과 파일을 담은 원본이다.
  docker ps -a는 실행 중이거나 종료된 컨테이너의 목록과 상태를 보여준다.
  차이: 이미지는 컨테이너를 만들기 위한 원본이고, 컨테이너는 해당 이미지를 기반으로 실제 생성되어 실행되는 인스턴스이다.
- (라) 🔍 `docker images` 출력을 붙여 넣고, `hello-world` 줄의 `IMAGE` · `ID` · `EXTRA` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `IMAGE` · `ID` · `EXTRA` 의 값과 뜻
  - 답:

```
  docker images
  IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
  hello-world:latest   11a3eb1597e8       25.9kB         9.49kB    U 

```
1. IMAGE : hello-world:latest, 이미지 이름이 hello-world이고 태그가 latest
2. ID :	11a3eb1597e8,	이미지를 식별하는 고유 ID
3. EXTRA :	U,	해당 이미지로 생성된 컨테이너가 존재함을 의미하며 종료된 컨테이너도 포함

- (마) 🔍 `docker ps -a` 출력을 붙여 넣고, `hello-world` 줄의 `STATUS` · `PORTS` · `NAMES` · `IMAGE` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `STATUS` · `PORTS` · `NAMES` · `IMAGE` 의 값과 뜻
  - 답:

```
  docker ps -a
  CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
  0681d1e9906c   hello-world   "/hello"   17 seconds ago   Exited (0) 16 seconds ago             awesome_cannon

```
1. STATUS :	Exited (0) 16 seconds ago,	컨테이너가 16초 전에 정상 종료되었음. 0은 정상 종료 코드
2. PORTS :	비어 있음,	호스트 PC와 연결된 포트가 표시되지 않음
3. NAMES :	awesome_cannon,	Docker가 자동으로 부여한 컨테이너 이름
4. IMAGE :	hello-world,	해당 컨테이너를 생성할 때 사용한 이미지

### 문제 5-2 · Docker Hub 에서 이미지 이름 읽고 없는 이미지 받아 보기

- (가) `nginx:1.28` 에서 `nginx` 와 `1.28` 이 각각 무엇을 정하는지 적어 주세요.
  - 쓸 내용: ① nginx 가 정하는 것 ② 1.28 이 정하는 것
  - 답: nginx: 사용할 이미지의 이름으로, Nginx 웹 서버 이미지를 의미한다.
        1.28: 이미지의 태그(Tag)로, Nginx 1.28 버전 계열을 지정한다.
- (나) 🔍 `docker pull nginxx` 를 쳤을 때 나온 오류 문구와 그 뜻을 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② 뜻 ③ 고치는 방법
  - 답:
  Using default tag: latest
  Error response from daemon: pull access denied for nginxx, repository does not exist or may require 'docker login'
  기본 태그 사용 중: latest
  데몬에서 오류 응답: nginxx에 대한 풀 접근이 거부되었거나, 저장소가 존재하지 않거나 'docker login'이 필요할 수 있음
  고치는 방법 : docker pull nginx:1.28
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(도커를 쓰면 무엇이 같아지는지)
  - 답: Docker를 사용하면 동일한 이미지를 기반으로 웹 서버의 실행 환경과 프로그램 버전을 일관되게 구성할 수 있습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: Docker 이미지는 이름과 태그로 구분되며, 이미지 이름을 잘못 입력하면 Docker Hub에서 이미지를 다운로드하지 못한다는 것을 알게 되었습니다.

## 6교시 · nginx 서버 켜고 접속 기록 읽기

### 문제 6-1 · 포트 없이 켜 보고, 포트를 연결해 접속하고, 기록 읽기

- (가) 포트 없이 켠 `web` 에 접속했을 때 어떻게 되었는지 적어 주세요.
  - 쓸 내용: 접속했을 때 나온 화면이나 오류와 `docker ps` 의 PORTS 열
  - 답: ERR_CONNECTION_REFUSED
  CONTAINER ID   IMAGE        COMMAND                   CREATED          STATUS          PORTS     NAMES
  3f4628c65e17   nginx:1.28   "/docker-entrypoint.…"   18 seconds ago   Up 17 seconds   80/tcp    web
- (나) 🔍 `-p 8080:80` 이 하는 일을 내 PC의 포트와 컨테이너의 포트로 나눠 설명해 주세요.
  - 쓸 내용: ① 내 PC 쪽 포트 ② 컨테이너 쪽 포트 ③ 연결이 하는 일
  - 답: ① 내 PC 쪽 포트: 8080 ② 컨테이너 쪽 포트: 80
        내 PC의 8080번 포트로 들어온 요청을 컨테이너의 80번 포트로 전달하여 브라우저에서 Nginx 웹 서버에 접속할 수 있도록 한다
- (다) 🔍 `docker logs web` 출력에서 `GET /` 줄 하나를 붙여 넣고, 접속자 주소 · 시각 · 요청 · 응답 번호를 찾아 적어 주세요.
  - 쓸 내용: ① `GET /` 줄 ② 접속자 주소 · 시각 · 요청 · 응답 번호 네 가지
  - 답: 172.17.0.1 - - [19/Oct/2026:06:14:31 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36 Edg/155.0.0.0" "-"
  접속자 주소 : 172.17.0.1, 시각: [19/Oct/2026:06:14:31 +0000], 요청: GET / HTTP/1.1 == 방법(GET) · 주소(/) · 프로토콜, 응답 번호: 304

### 문제 6-2 · 컨테이너 안을 들여다보고, 끄고, 지우기

- (가) 컨테이너 안에서 `ls /usr/share/nginx/html` 로 본 파일 이름을 모두 적고, 그중 브라우저의 첫 화면이 어느 파일인지 적어 주세요.
  - 쓸 내용: ① 파일 이름 모두 ② 첫 화면 파일
  - 답: 50x.html  index.html
        첫 화면 파일: index.html
- (나) 🔍 `docker stop web` 뒤에 `docker ps` 와 `docker ps -a` 에 각각 `web` 이 보이나요? 차이를 설명해 주세요.
  - 쓸 내용: ① stop 뒤 ps 에 보이는지 ② ps -a 에 보이는지 ③ 차이의 이유
  - 답: docker ps
        CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

        docker ps -a
        CONTAINER ID   IMAGE         COMMAND                   CREATED          STATUS                      PORTS     NAMES
        97b38ba3b041   nginx:1.28    "/docker-entrypoint.…"   12 minutes ago   Exited (0) 33 seconds ago             web
        docker ps는 켜져 있는 컨테이너만 확인할 수 있고, docker ps -a는 꺼져 있는 컨테이너 목록까지 모두 보인다.
- (다) 🔍 같은 이름으로 다시 `run` 했을 때 나온 오류 문구와, `docker rm` 이 필요한 이유를 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② rm 이 필요한 이유
  - 답: docker: Error response from daemon: Conflict. The container name "/web" is already in use by container "97b38ba3b0413934cf783f96c3c76d8d339b40c575dc9685c7a3e6e1a412da31". You have to remove (or rename) that container to be able to reusethat name.

  기존 컨테이너가 종료되었더라도 web이라는 이름을 계속 사용하고 있기 때문에 같은 이름으로 새로운 컨테이너를 생성할 수 없다. 따라서 docker rm web으로 기존 컨테이너를 삭제해야 같은 이름을 다시 사용할 수 있다.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(켜는 명령 · 기록 보는 명령 · 정리 방법)
  - 답: Docker 컨테이너는 `docker run`으로 실행하고, `docker logs`로 기록을 확인하며, 사용이 끝나면 `docker stop`으로 종료한 뒤 `docker rm`으로 삭제할 수 있습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: Docker 컨테이너는 종료해도 자동으로 삭제되지 않으며, 같은 이름으로 새로운 컨테이너를 생성하려면 기존 컨테이너를 삭제해야 한다는 것을 알게 되었습니다.

## 7교시 · 내 페이지 연결 · 두 서버 · 올리기

### 문제 7-1 · 컨테이너 안의 변경이 사라지는 것을 보고, 내 폴더를 연결하기

- (가) 컨테이너 안에서 바꾼 뒤 `docker rm -f web` 으로 지우고 다시 켰을 때 화면이 어떻게 되었는지 적어 주세요.
  - 쓸 내용: ① 바꾼 뒤 화면 ② 지우고 다시 켠 뒤 화면
  - 답: 컨테이너 안에서 고친 뒤	inside, 지우고 다시 켠 뒤	다시 Welcome to nginx! (고친 것이 사라짐)
- (나) 🔍 컨테이너 안에서 바꾼 내용이 사라진 이유와, `-v` 로 폴더를 연결하면 무엇이 달라지는지 적어 주세요.
  - 쓸 내용: ① 사라진 이유 ② -v 로 연결하면 달라지는 점
  - 답: 고친 파일은 이미지가 아니라 그 컨테이너에만 저장된다. 그래서 컨테이너를 지우면 함께 사라지고 다시 만든 컨테이너는 이미지의 원래 파일로 시작한다.
        -v는 내 PC폴더를 컨테이너 안 폴더에 연결하기 때문에 컨테이너를 지워도 함께 사라지지 않는다.
- (다) 🔍 `MSYS_NO_PATHCONV=1` 없이 `-v` 를 실행했을 때 화면에 무엇이 나왔고 왜 그랬는지 적어 주세요.
  - 쓸 내용: ① 화면에 나온 것 ② 그렇게 된 이유
  - 답: Welcome to nginx!
        Git Bash가 -v뒤에 컨테이너 쪽 경로를 'C:/Program Files/Git/usr/share/nginx/html'처럼 윈도 경로로 바꿔 버려서, 연결이 엉뚱한 곳에 됐기 때문이다.

### 문제 7-2 · 서버 두 대를 띄워 포트로 구분하고, 파일을 고쳐 바로 반영되는지 보기

- (가) 두 주소(`8080` · `8081`)에서 보이는 화면을 각각 적어 주세요.
  - 쓸 내용: 두 주소의 화면 문구
  - 답: site-one 첫 번째 서버입니다
        site-two 두 번째 서버입니다
- (나) 🔍 `docker ps` 의 PORTS 열에서 두 서버를 구분해 주는 것은 무엇인가요?
  - 쓸 내용: PORTS 열에서 서버를 구분하는 값
  - 답: 0.0.0.0:8081->80/tcp
        0.0.0.0:8080->80/tcp
        8081, 8080
- (다) 🔍 `:ro` 는 무슨 뜻이고, 왜 읽기 전용으로 연결하나요?
  - 쓸 내용: ① :ro 의 뜻 ② 읽기 전용으로 연결하는 이유
  - 답: `:ro`는 read-only의 약자로 읽기 전용을 의미한다. 컨테이너가 내 PC의 폴더에 있는 파일을 읽을 수는 있지만 수정하거나 삭제하지 못하도록 제한하여 원본 파일을 보호하기 위해 사용한다.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(두 서버를 어떻게 띄웠는지)
  - 답: 동일한 nginx 이미지를 사용해 web-one과 web-two 컨테이너를 각각 실행하고, 포트 8080과 8081로 구분했으며, 각 컨테이너에 서로 다른 PC 폴더를 읽기 전용으로 연결했습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: 같은 Docker 이미지로 여러 컨테이너를 실행할 수 있으며, 포트와 연결 폴더를 다르게 설정하면 서로 다른 웹페이지를 제공할 수 있다는 것을 알게 되었습니다.

### 문제 7-3 · 오늘 만든 것을 깃허브에 올리기

- (가) `git status` 를 쳤을 때 빨간 목록에 줄이 몇 개였는지, 그 가운데 `.env` · `.venv` 가 있었는지 적어 주세요.
  - 쓸 내용: ① 줄 수 ② .env · .venv 가 있었는지
  - 답: 8줄, 없다.
