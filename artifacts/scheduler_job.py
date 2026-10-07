import argparse
import json
import os
import schedule
import time

# 문제 7-9 의 scheduler_job.py 셀을 이 셀에 복사해 온 뒤, job 안에 룰 ② 와 룰 ③ 을 더합니다
parser = argparse.ArgumentParser(description="정기 점검 작업")
parser.add_argument("--every", type=int, default=2, help="몇 초마다 돌릴지")
args = parser.parse_args()

THRESHOLD = 3
NIGHT_END = 6 # 추가

count = {} # 추가
table = {} # 추가



def load_done():
    if os.path.exists("processed_ids.json"):
        with open("processed_ids.json", encoding="utf-8") as f:
            return json.load(f)
    return []


def job():
    with open("normalized_logs.json", encoding="utf-8") as f:
        rows = json.load(f)

    count = {}                                # 룰 ① — 계정마다 실패 횟수를 센다 (9/29)
    table = {}

    for row in rows:
        user = row["user"]
        ip = row["ip"]

        if row["level"] == "WARN":
            if user in count:
                count[user] = count[user] + 1
            else:
                count[user] = 1

        ip = row["ip"]
        if ip in table:
            if user not in table[ip]:
                table[ip].append(user)
        else:
            table[ip] = [user]

    done = load_done()
    sent = 0

    for user in count:
        if count[user] >= THRESHOLD:
            event_id = f"brute_force:{user}"
            # 1. event_id 가 done 에 없으면 (not in)
            if event_id not in done:

                # 2. "[전송]" 과 event_id 를 출력하고, done 에 event_id 를 append 하고, sent 에 1 을 더하세요
                print(f"[전송] {event_id}")
                done.append(event_id)
                sent+=1

    # 룰 ② password_spraying
    for ip in table:
        if len(table[ip]) >= 2:
            event_id = f"password_spraying:{ip}"

            if event_id not in done:
                print(f"[전송] {event_id}")
                done.append(event_id)
                sent += 1

    for row in rows:
        if int(row["time"].split(":")[0]) < NIGHT_END and row["level"] == "INFO":
            event_id = f"night_login:{row['user']}:{row['time']}"

            if event_id not in done:
                print(f"[전송] {event_id}")
                done.append(event_id)
                sent+=1


    with open("processed_ids.json", "w", encoding="utf-8") as f:
        json.dump(done, f, ensure_ascii=False, indent=2)


    print(f"점검 완료 — 새 경보 {sent}건")


# 3. job 을 args.every 초마다 부르게 등록하세요
schedule.every(args.every).seconds.do(job)


for i in range(4):
    schedule.run_pending()
    time.sleep(1)
