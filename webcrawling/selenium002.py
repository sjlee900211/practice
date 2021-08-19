from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

driver = webdriver.Chrome('C:/Myexam/chromedriver/chromedriver.exe')

driver.get('https://www.ted.com/talks')

driver.find_element_by_css_selector('#banner-secondary').text

contents = driver.find_elements_by_css_selector('#browse-results > div > .col')
len(contents)

contents[0].find_element_by_css_selector('.media > .media__message .ga-link').text


titles = []
for content in contents:
    title = content.find_element_by_css_selector('.media > .media__message .ga-link').text
    titles.append(title)

languages = driver.find_element_by_css_selector('#languages').text
languages = languages.split("\n")[1:-1]
languages


driver.find_element_by_css_selector('#languages [lang="ko"]').click()


time.sleep(3)
contents = driver.find_elements_by_css_selector('#browse-results > div > .col')
titles = []
for content in contents:
    title = content.find_element_by_css_selector('.media > .media__message .ga-link').text
    titles.append(title)
titles[-5:]

time.sleep(3)
contents = driver.find_elements_by_css_selector('#browse-results > div > .col')
links = []
for content in contents:
    link = content.find_element_by_css_selector('.media > .media__message .ga-link').get_attribute('href')
    links.append(link)
links[-5:]

driver.quit()