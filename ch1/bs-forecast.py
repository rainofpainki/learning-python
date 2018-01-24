#!/usr/bin/env python3
#  Load Libraries
import datetime
import sys
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as parse

# 명령줄 매개변수 추출
if len(sys.argv) <= 1:
    print("사용법 : download-forecast-argv <지역 번호>")
    print("전국: 108")
    print("서울 / 경기도: 109")
    print("강원도: 105")
    print("충청북도: 131")
    print("충청남도: 133")
    print("전라북도: 146")
    print("전라남도: 156")
    print("경상북도: 143")
    print("경상남도: 159")
    print("제주특별자치도: 184")
    sys.exit()
regionNumber = sys.argv[1]

# 기상청 육상 중기예보 rss
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId': regionNumber
}

# 매개변수를 url 인코딩
params = parse.urlencode(values)
url = API + "?" + params
print("요청 URL : " + url)

res = req.urlopen(url)

# print(res.read().decode("utf-8"))

# BeautifulSoup 으로 분석하기
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출하기
title_list = soup.find_all("title")
title_idx = len(title_list)-1
title = title_list[title_idx].string
wf = soup.find("wf").string
tm = soup.find("tm").string
date = datetime.datetime.strptime(tm, '%Y%m%d%H%M')
print(title + " / " + date.strftime('%Y년 %m월 %d일 %H시 %M분'))
print("예보 : " + wf)