from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

browser = webdriver.Chrome('C:/Myexam/chromedriver/chromedriver.exe')
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

channel_list = soup.select('form > table> tbody > tr')
print(len(channel_list))
print(channel_list[0])

channel = channel_list[0]

# 카테고리 정보 추출
category = channel.select('p.category')[0].text.strip()
print(category)

# 채널명
title = channel.select('h1 > a')[0].text.strip()
title

# 구독자 수, view 수, 동영상 수 추출
subscriber = channel.select('.subscriber_cnt')[0].text
view = channel.select('.view_cnt')[0].text
video = channel.select('.video_cnt')[0].text

# 반복문으로 채널 정보 추출
channel_list = soup.select('tbody > tr')
for channel in channel_list:
    title = channel.select('h1 > a')[0].text.strip()
    subscriber = channel.select('.subscriber_cnt')[0].text
    view = channel.select('.view_cnt')[0].text
    video = channel.select('.video_cnt')[0].text
    print(title, category, subscriber, view, video)

# 페이지별 URL 만들기
page = 1
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={}'.format(page)

# 반복문으로 유튜브 랭킹 여러 페이지 크롤링
results = []
for page in range(1, 11):
    url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}"
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    channel_list = soup.select('form > table> tbody > tr')
    for channel in channel_list:
        title = channel.select('h1 > a')[0].text.strip()
        category = channel.select('p.category')[0].text.strip()
        subscriber = channel.select('.subscriber_cnt')[0].text
        view = channel.select('.view_cnt')[0].text
        video = channel.select('.video_cnt')[0].text
        data = [title, category, subscriber, view, video]
        results.append(data)
df = pd.DataFrame(results)
df.columns = ['title', 'category', 'subscriber', 'view', 'video']
df.to_excel('C:/Users/Celine/practice/webcrawling/miniproject/files/youtube.xlsx', index=False)