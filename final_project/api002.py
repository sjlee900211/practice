import requests
from urllib.parse import urlencode, quote_plus, unquote, urlparse
import json
import pymysql

conn = pymysql.connect(db='project', user='admin', passwd='1234',
                       charset='utf8', port=3306, host='13.114.158.172')

c = conn.cursor()



apiKey = unquote('4DJ1VQS4ddl8Atjq1OljTLSkAEhOCTNcyxydHBiR%2FTsJmBUI2SRnDbfoQkxx8Y4GudA67W0poAc%2BuqULvv2Jgw%3D%3D')
url = 'http://apis.data.go.kr/1471000/FoodNtrIrdntInfoService1/getFoodNtrItdntList1'

# pageNo의 max값 :227
n = 1
for n in range(227):
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : apiKey,
                                   quote_plus('pageNo') : n,
                                   quote_plus('numOfRows') : '100',
                                   quote_plus('type') : 'json'})
    

    result = requests.get(urlparse(url + queryParams).geturl(), headers = {'User-Agent': 'Mozilla/5.0'})
    json_obj = result.json()
    temp_data = json.dumps(json_obj.get('body',{}).get('items'))
    json_data = json.loads(temp_data)
    
    
    i = 1
    for i in range(100):
                
        # food_code 만들기-> max로 바꿔야 함
        c.execute('SELECT CAST(RIGHT(FOOD_CODE,5)AS SIGNED) AS MAX0, CAST(RIGHT(FOOD_CODE,5)AS SIGNED)+1 AS MAX1 FROM FOOD_BIO ORDER BY 1 DESC') 
        result = c.fetchone()
        if result is not None and result[0] is not None and result[1] is not None:
            one = result[0]
            two = result[1]
            while result:
                result = c.fetchone()            
                if one == 0:
                    max = 1
                else :                 
                    max = two
        if len(str(max)) == 1:
            food_code = "B0000"+str(max)
        elif len(str(max)) == 2:
            food_code = "B000"+str(max)
        elif len(str(max)) == 3:
            food_code = "B00"+str(max)
        elif len(str(max)) == 4:
            food_code = "B0"+str(max)
        else :
            food_code = "B"+str(max)
        

        if json_data is not None and json_data[i].get('DESC_KOR') is not None:
            default = round(float(0.0),1)
            food_nm = json_data[i].get('DESC_KOR')
            cal = round(float(json_data[i]['NUTR_CONT1']),1)
            if isinstance(json_data[i]['NUTR_CONT2'],str):
                carb = default
            else:
                carb = round(float(json_data[i]['NUTR_CONT2']),1)            
            if isinstance(json_data[i]['NUTR_CONT3'],str):
                prot = default
            else:
                prot = round(float(json_data[i]['NUTR_CONT3']),1)
                
            if isinstance(json_data[i]['NUTR_CONT4'],int):
                fat = round(float(json_data[i]['NUTR_CONT4']),1)                
            else:
                fat = default         
                
            if isinstance(json_data[i]['NUTR_CONT6'],str):
                sodium = default
            else:
                sodium = round(float(json_data[i]['NUTR_CONT6']),1)
                
            if isinstance(json_data[n]['SERVING_WT'],int) or isinstance(json_data[n]['SERVING_WT'],float):
                amt_serve = round(float(json_data[i]['SERVING_WT']),1) 
            else:
                amt_serve = default              
            
            sql = 'INSERT INTO FOOD_BIO(FOOD_CODE, FOOD_NM, CAL, CARB, PROT, FAT, SODIUM, AMT_SERVE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            c.execute(sql, (food_code, food_nm, cal, carb, prot, fat, sodium, amt_serve))
            # conn.commit()
        i += 1
    
    n += 1



conn.commit()
c.execute('SELECT * FROM FOOD_BIO')



for row in c.fetchall():
    print(row)
conn.close()

