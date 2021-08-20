from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Myexam/chromedriver/chromedriver.exe')
url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# songs = soup.select('table > tbody > tr')
# len(songs)

# song = songs[0]

# title = song.select('a.title')
# len(title)

# title = song.select('a.title')[0].text.strip()
# title

# singer = song.select('a.artist')[0].text.strip()
# singer

song_data = []
rank = 1
songs = soup.select('table > tbody > tr')
for song in songs:
    title = song.select('a.title')[0].text.strip()
    singer = song.select('a.artist')[0].text.strip()
    song_data.append(['Genie', rank, title, singer])
    rank = rank + 1
column = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=column)
pd_data.to_excel('C:/Users/Celine/practice/webcrawling/miniproject/files/genie.xlsx', index=False )