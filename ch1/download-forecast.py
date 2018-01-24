import urllib.request
import urllib.parse
# 기상청 육상 중기예보 rss
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

"""
매개변수 : stnId / 기상 정보를 알고 싶은 지역을 지정한다.

전국 : 108
서울/경기도 : 109
강원도 : 105
충청북도 : 131
충청남도 : 133
전라북도 : 146
전라남도 : 156
경상북도 : 143
경상남도 : 159
제주특별자치도 : 184
"""

# 지역번호는 경상북도로 설정
values = {
    'stnId': '143'
}

# 매개 변수 dictionary 를 url encoding 하여 parsing 한다.
params = urllib.parse.urlencode(values)

# 요청 전용 URL을 생성한다.
url = API + "?" + params
print("요청 URL : " + url)

# 다운로드 한다.
data = urllib.request.urlopen(url).read()

# decoding 하여 결과를 출력한다.
text = data.decode("utf-8")
print(text)