from bs4 import BeautifulSoup
import urllib.request as req

# HTML 가져오기
url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
res = req.urlopen(url)

# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
list = soup.select("#content div.keyword_rank.select_date .title")

if len(list) > 0:
    print("네이버 실시간 검색 순위")
    # 실시간 검색 시간을 가져온다.
    rank_time = soup.select_one("#content div.keyword_rank.select_date strong.rank_title")
    if len(rank_time) > 0:
        print(rank_time.get_text())

    for i,keyword in enumerate(list):
        print(str(i+1)+"위", keyword.string)