from urllib.parse import urljoin

base = "http://example.com/html/a.html"

# urljoin을 이용하여 상대경로를 절대경로로 반환한다.
print (urljoin(base, "b.html") )
print (urljoin(base, "sub/c.html") )
print (urljoin(base, "../index.html") )
print (urljoin(base, "../img/hoge.png") )
print (urljoin(base, "../assets/css/hoge.css") )