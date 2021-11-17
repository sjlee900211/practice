import pymongo
import datetime
import requests
from bs4 import BeautifulSoup
import time
import re

# MongoDB 연결
client = pymongo.MongoClient("mongodb+srv://testdb:multi@cluster0.jxvfb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['food']
col = db['img']

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
print(f'Start 크롤링', now)

# 네이버 주식 시가총액 페이지 4page까지 추출
url = 'https://www.10000recipe.com/recipe/list.html?q='
# search = input('검색어를 입력하세요 : ')
for page in range(10):
    # html = requests.get(f"https://www.10000recipe.com/recipe/list.html?q={search}").text
    html = requests.get(f"https://www.10000recipe.com/recipe/list.html?order=reco&page={page}").text
    soup = BeautifulSoup(html, 'lxml')
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

    # 종목명, 현재가, 전일비, 등락률, 액면가, 시가총액, 상장주식수, 외국인비율, 거래량, PER, ROE 추출
    recipeContents = soup.select('div > a > img')
    
    for recipeContent in recipeContents:
        # 공백 제거 (strip() 사용시 종목명에 공백이 있을 경우 같이 분리되므로 아래와 같이 사용)
        content = re.split('\n|\t', recipeContents.text)
        content = list(filter(None, content)) # None값 제거

        # # 형 변환
        # content[3] = int(content[3].replace(',', ''))
        # content[6] = int(content[6].replace(',', ''))
        # content[7] = int(content[7].replace(',', ''))
        # content[8] = int(content[8].replace(',', ''))
        # content[9] = float(content[9])
        # content[10] = int(content[10].replace(',', ''))
        # for i in range(11,13):
        #     if content[i] == 'N/A':
        #         pass
        #     else:
        #         content[i] = float(content[i].replace(',', ''))

        # Dictionary 데이터 생성
        data = {
            '시간':now,
            'recipe':content[0],
            'title':content[1],

        }
        
        # MongoDB에 저장
        col.insert_one(data)
print(f"Complete 크롤링...", now)




if __name__ == "__main__":
        time.sleep(30)