import urllib.request as req
import os.path
import json

# 다운받을 사용자 id
USER = "<ID>"

# JSON 데이터 내려받기
url = "https://api.github.com/users/{user}/repos".format(user=USER)
savename = "{user}-repo.json".format(user=USER)
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# JSON 파일 분석하기
items = json.load(open(savename, "r", encoding="utf-8"))
# 또는
# s = open(savename, "r", encoding="utf-8").read()
# items = json.loads(s)

# 출력하기
for item in items:
    print(item["name"] + " - " + item["owner"]["login"])

    # 설명이 있으면 출력한다
    if item["description"] is not None:
        print("└", item["description"])