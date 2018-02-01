from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# XML 다운로드
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss.jsp?stnId=108"
savename = "forecast.xml"
if not os.path.exists(savename): # 파일이 없으면 파일을 다운로드 한다. 두번째 실행시부터는 파일을 읽어서 사용한다.
    req.urlretrieve(url, savename)

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

# 각 지역 확인하기
info = {}
for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

# 각 지역의 날씨를 구분해서 출력하기
for weather in info.keys():
    print("┌", weather)
    for name in info[weather]:
        print("┣─ ", name)