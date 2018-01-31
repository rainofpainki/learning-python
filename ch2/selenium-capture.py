from selenium import webdriver

url = "https://m.naver.com"

# PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS()

# 3초 대기하기 / 드라이버가 초기화될 때까지 대기한다
browser.implicitly_wait(3)

# URL 읽어 들이기
browser.get(url)

# 화면을 캡처해서 저장하기
browser.save_screenshot("Website.png")

# 브라우저 종료하기 (반드시 종료해야 한다)
browser.quit()