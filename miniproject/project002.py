import pandas as pd

DF = pd.read_excel('notExercise.xls')
DF.head()

# 기간 열 삭제
DF.drop(columns='기간', inplace=True)
DF.tail()

# 23~52번 지역분류 index 삭제
DF['대분류'][23:]
DF.drop(index= range(23, 53), inplace=True)
DF

# 성별 데이터 추출
DF_G = DF[DF['대분류'] == '성별'].copy()
DF_G

# 대분류 열 삭제
DF_G.drop(columns= '대분류', inplace=True)
DF_G

# 분류를 index로 지정
DF_G.set_index('분류', inplace = True)
DF_G

# 연령별 데이터 추출
DF_A = DF[DF['대분류'] == '연령별'].copy()
DF_A.drop(columns= '대분류', inplace=True)
DF_A.set_index('분류', inplace=True)
DF_A