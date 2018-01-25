from bs4 import BeautifulSoup

# 분석 대상 HTML
html = """
<html><body>
<div id="meigen">
    <h1>닌텐도 스위치 게임 목록</h1>
    <ul class="items">
        <li>슈퍼마리오 오디세이</li>
        <li>마리오카트 디럭스8</li>
        <li>젤다의 전설 브레스 오브 더 와일드</li> 
    </ul>
</div>
</body></html>
"""

# HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')

# 필요한 부분을 CSS 쿼리로 추출하기
# 타이틀 부분 추출하기
h1 = soup.select_one("div#meigen > h1").string
print("h1 =", h1)

# 목록 부분 추출하기
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
    print("li =", li.string)