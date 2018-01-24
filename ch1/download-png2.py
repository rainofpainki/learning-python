# 라이브러리 읽어 들이기
import urllib.request

# URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test2.png"

# 다운로드
mem = urllib.request.urlopen(url).read()

# 파일로 저장하기
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다.")