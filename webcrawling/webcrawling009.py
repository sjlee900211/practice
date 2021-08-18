from bs4 import BeautifulSoup

html = """<html><body><div><span>\
    <a href=http://www.naver.com>naver</a>\
    <a href=https://www.google.com>google</a>\
    <a href=http://www.daum.net>daum</a>\
    </span></div></body></html>"""
    
soup = BeautifulSoup(html, 'lxml')
soup

print(soup.prettify())

soup.find('a')

soup.find('a').get_text()

soup.find_all('a')

site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())