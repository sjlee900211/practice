from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Myexam/chromedriver/chromedriver.exe')
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 반복문으로 곡과 가수명 song_data에 저장
song_data = []
rank = 1

songs = soup.select('table > tbody > tr')
for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > span > a')[0].text
    song_data.append(['Melon', rank, title, singer])
    rank = rank + 1

# song_data 리스트를 이용해 데이터프레임 만들기
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns=columns)
pd_data.head()

# 크롤링 결과 엑셀파일로 저장
pd_data.to_excel('C:/Users/Celine/practice/webcrawling/miniproject/files/melon.xlsx', index=False)