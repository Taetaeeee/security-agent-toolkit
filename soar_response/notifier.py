import requests                                                # 인터넷으로 요청을 보내는 도구 (9/30)


def notify(message, url):                                      # 메시지를 알림 서버로 보내는 함수
    try:                                                       # 아래 줄을 해 본다
        requests.post(url, json={"text": message}, timeout=5)  # 메시지를 POST 한다 — 5초만 기다린다
        return True                                            # 보냈다
    except Exception as e:                                     # 에러가 나면 e 에 담아 여기로 온다
        print("[알림 실패]", type(e).__name__)                 # 에러 이름을 알린다 — 숨기지 않는다
        return False                                           # 못 보냈다 — 부른 쪽은 계속 간다
