import requests
from urllib import parse

url = 'http://apis.data.go.kr/1471000/HtfsInfoService1/getHtfsList'
mykey = 'piyGwHd6LfjAN5DT8R9HBEetsXCWiypj4Gkpf8asve2XyywqyOtEknLJUlp8LzEK3pXz2iTFBpBQfp/SfmueBg=='
params ={'serviceKey' : mykey, 'Entrps' : '성풍양행(주)', 'Prduct' : '에스피 스피릿 - 크레아틴', 'Sttemnt_no' : '201400170875', 'pageNo' : '1', 'numOfRows' : '10', 'type' : 'xml' }

response = requests.get(url, params=params)
print(response.content)

from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET
import requests, bs4
import pandas as pd


#   parameter for request
#   pageNo를 다르게 주어도 다른데이터가 발생하지 않는 것을 확인
def open_api(YMD,CODE,pageNo = 1):
    
    # 1. URL 파라미터 분리하기.
    # Service URL
    xmlUrl = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
    My_API_Key = unquote('개인 서비스키')
    
    queryParams = '?' + urlencode(    # get 방식으로 쿼리를 분리하기 위해 '?'를 넣은 것이다. 메타코드 아님.
        {
            quote_plus('serviceKey') : My_API_Key,    # 필수 항목 1 : 서비스키 (본인의 서비스키)
            quote_plus('LAWD_CD') : CODE,          # 필수 항목 2 : 지역코드 (법정코드목록조회에서 확인)
            quote_plus('DEAL_YMD') : YMD,             # 픽수 항목 3 : 계약월
            quote_plus('pageNo') : pageNo
        }
    )
    response = requests.get(xmlUrl + queryParams)
    response.encoding = 'utf-8'
    return response.text