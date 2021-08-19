from os import replace
from bs4 import BeautifulSoup
import webcrawling012 as w12

soup = BeautifulSoup(w12.html_source, "lxml")

title = soup.find('p', {"id":"title"})
contents = soup.find_all('p', {"id":"content"})

print(title.get_text(), '\n')

for content in contents:
    w12.content1 = w12.replace_newline(content)
    print(w12.content1.get_text(), '\n')