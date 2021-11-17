import requests
from urllib import parse

url = 'http://openapi.foodsafetykorea.go.kr/api/keyId/serviceId/dataType/startIdx/endIdx'
mykey = 'piyGwHd6LfjAN5DT8R9HBEetsXCWiypj4Gkpf8asve2XyywqyOtEknLJUlp8LzEK3pXz2iTFBpBQfp/SfmueBg=='
params ={'serviceKey' : mykey, 'Entrps' : '성풍양행(주)', 'Prduct' : '에스피 스피릿 - 크레아틴', 'Sttemnt_no' : '201400170875', 'pageNo' : '1', 'numOfRows' : '10', 'type' : 'xml' }

response = requests.get(url, params=params)
print(response.content)