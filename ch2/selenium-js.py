from selenium import webdriver

# PhantomJS 드라이버 추출
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# 웹 페이지 열기
browser.get("https://www.naver.com")

# 자바스크립트 실행하기
r = browser.execute_script("return 123 + 123")
print(r)

# 브라우저 종료하기
browser.quit()