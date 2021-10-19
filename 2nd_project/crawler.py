import pymongo
import datetime
import requests
from bs4 import BeautifulSoup
import time
import re

# MongoDB 연결
client = pymongo.MongoClient(host='mongodb://52.197.26.81', port=27017, username = 'admin', password = '1234')
db = client['네이버']
col = db['네이버주식정보']

marketType = {
    "KOSPI": "0",
    "KOSDAQ": "1"
}


def crawling():
    # KOSPI, KOSDAQ
    for market, code in marketType.items():
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        print(f'Start {market}...', now)

        # 네이버 주식 시가총액 페이지 4page까지 추출
        for page in range(1, 5):
            html = requests.get(f"https://finance.naver.com/sise/sise_market_sum.naver?sosok={code}&page={page}").text
            soup = BeautifulSoup(html, 'lxml')
            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

            # 종목명, 현재가, 전일비, 등락률, 액면가, 시가총액, 상장주식수, 외국인비율, 거래량, PER, ROE 추출
            stockContents = soup.find_all('tr', {'onmouseover': 'mouseOver(this)'})
            
            for stockContent in stockContents:
                # 공백 제거 (strip() 사용시 종목명에 공백이 있을 경우 같이 분리되므로 아래와 같이 사용)
                content = re.split('\n|\t', stockContent.text)
                content = list(filter(None, content)) # None값 제거
                content = [market] + content  # content 항목에 시장(KOSPI, KOSDAQ) 추가
                        
                # 전일비 상승 하락 표시
                if stockContent.select("span.tah.p11.red02"):
                    content[4] = "+" + content[4]
                elif stockContent.select("span.tah.p11.nv01"):
                    content[4] = "-" + content[4]

                # 형 변환
                content[3] = int(content[3].replace(',', ''))
                content[6] = int(content[6].replace(',', ''))
                content[7] = int(content[7].replace(',', ''))
                content[8] = int(content[8].replace(',', ''))
                content[9] = float(content[9])
                content[10] = int(content[10].replace(',', ''))
                for i in range(11,13):
                    if content[i] == 'N/A':
                        pass
                    else:
                        content[i] = float(content[i].replace(',', ''))

                # Dictionary 데이터 생성
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
                
                # MongoDB에 저장
                col.insert_one(data)
        print(f"Complete {market}...", now)


if __name__ == "__main__":
    for i in range(50):
        crawling()
        time.sleep(30)