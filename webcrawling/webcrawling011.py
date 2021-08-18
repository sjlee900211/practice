from bs4 import BeautifulSoup

f = open('C:\Users\Celine\practice\webcrawling\HTML_example_my_site.html', encoding='utf-8')

html3 = f.read()
f.close()

soup3 = BeautifulSoup(html3, 'lxml')
soup3.select('a')

soup3.select('a.portal')
soup3.select('a#naver')