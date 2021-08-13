import pandas as pd

SDF = pd.read_csv('seoulCCTV.csv', encoding='utf-8')

SDF.head()

# 기관명을 구별로 변경
SDF.columns
SDF.rename(columns={SDF.columns[0] : '구별'}, inplace=True)
SDF.head()

# 소계 오름차순 정렬 
SDF.sort_values(by = '소계', ascending=True).head(7)

# 소계 내림차순 정렬
SDF.sort_values(by = '소계', ascending=False).head(7)

# 최근 3년 CCTV 최근증가율 열 추가
SDF['최근증가율'] = ((SDF['2016년'] + SDF['2015년'] + SDF['2014년']) / SDF['2013년도 이전']) * 100

# 최근증가율 열로 내림차순 정렬
SDF.sort_values(by='최근증가율', ascending=False).head(7)