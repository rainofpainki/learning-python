from selenium import webdriver
USER = "<ID>"
PASS = "<PASSWORD>"

# PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# 로그인 페이지에 접근하기
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

# 텍스트 박스에 아이디와 비밀번호 입력하기
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인하기
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

try:
    print("새로운 기기 등록을 클릭합니다.")
    # 새로운 기기 등록 클릭하기
    dev = browser.find_element_by_css_selector(".btn_upload a")
    dev.click()

    dev = browser.find_element_by_css_selector(".btn_maintain a")
    dev.click()

except Exception as err:
    print("이미 기기 등록이 되어 있습니다.")

# 쇼핑 페이지의 데이터 가져오기
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# 쇼핑 목록 출력하기
products = browser.find_elements_by_css_selector(".p_info span:not(.state)")
for product in products:
    print("-", product.text)

browser.quit()