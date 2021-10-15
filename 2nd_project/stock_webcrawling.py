import pymongo
import datetime
import requests
from bs4 import BeautifulSoup
import re
import time

# ID_생성하기-> 순위별로 추가해야 함
client = pymongo.MongoClient("mongodb+srv://testdb:multi@cluster0.jxvfb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# client = pymongo.MongoClient(host='mongodb://52.197.26.81', port=27017, username = 'admin', password = '1234')
mydb = client['네이버']
mycol = mydb["네이버주식정보"]


marketType = {
    "KOSPI": "0",
    "KOSDAQ": "1"
}


for market, code in marketType.items():
    for page in range(1, 5):
        html = requests.get(f"https://finance.naver.com/sise/sise_market_sum.naver?sosok={code}&page={page}").text
        soup = BeautifulSoup(html, 'lxml')
        now = datetime.datetime.now().strftime("%Y%m%d%H%M")

        stockContents = soup.select("table.type_2 > tbody > tr")

        for stockContent in stockContents[1:]:
            try:
                content = re.split('\n|\t', stockContent.text)
                content = list(filter(None, content))
                content = [market] + content
                
                # 전일비 상승 하락 표시
                if stockContent.select("td:nth-of-type(4) > span.tah p11 red02"):
                    content[4] = "+" + content[4]
                elif stockContent.select("td:nth-of-type(4) > span.tah p11 nv01"):
                    content[4] = "-" + content[4]

                # collection 이름 시작과 끝 '.'로 시작 X
                if content[2].endswith('.') | content[2].startswith('.'):
                    content[2] = content[2].strip('.')
                
                
                
                data = {
                    '시간':now,
                    '시장':content[0],
                    '순위':content[1],
                    '종목명':content[2],
                    '현재가':content[3],
                    '전일비':content[4],
                    '등락률':content[5],
                    '액면가':content[6],
                    '시가총액':content[7],
                    '상장주식수':content[8],
                    '외국인비율':content[9],
                    '거래량':content[10],
                    'PER':content[11],
                    'ROE':content[12],
                }
                        
                mycol.insert_one(data)

            except IndexError:
                continue
            
time.sleep(10)