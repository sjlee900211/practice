from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

driver = webdriver.Chrome('C:/Myexam/chromedriver/chromedriver.exe')

driver.get("https://www.naver.com/")

driver.set_window_size(1024, 768)

driver.execute_script("alert('selenium test);")

try:
    alert = driver.switch_to.alert
    print(alert.text)
except:
    print('alert 없음')

alert.accept()

driver.find_element_by_css_selector(".btn_submit()").click()