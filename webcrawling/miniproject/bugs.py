from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Myexam/chromedriver/chromedriver.exe')
url = 'https://music.bugs.co.kr/chart'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# tr 태그로 곡정보 찾기1
# songs = soup.select('tr')
# print(len(songs))

# tr 태그로 곡정보 찾기2
# songs = soup.select('table > tbody > tr')
# print(len(songs))

# tr 태그로 곡정보 찾기3
songs = soup.select('table.byChart > tbody > tr')
print(len(songs))

print(songs[0])

song = songs[0]

# title = song.select('p.title > a')
# len(title)

# title = song.select('p.title > a')[0].text
# title

# singer = song.select('p.artist > a')[0].text.strip()
# singer

# songs = soup.select('table.byChart > tbody > tr')
# for song in songs:
#     title = song.select('p.title > a')[0].text
#     singer = song.select('p.artist > a')[0].text
#     print(title, singer, sep = '|')

song_data = []
rank = 1
songs = soup.select('table.byChart > tbody > tr')
for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    song_data.append(['Bugs', rank, title, singer])
    rank = rank + 1
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
# pd_data.info()
pd_data.to_excel('C:/Users/Celine/practice/webcrawling/miniproject/files/bugs.xlsx', index=False )