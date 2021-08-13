import pandas as pd
import CCTV001 as c1
import CCTV002 as c2

# 두 데이터프레임에 공통으로 있는 구별로 merge
DF = pd.merge(c1.SDF, c2.SDFP, on = '구별')
DF.head()

# 불필요한 열 삭제
del DF['2013년도 이전']
del DF['2014년']
del DF['2015년']
del DF['2016년']
DF.head()

# 구별을 index로 지정
DF.set_index('구별', inplace=True)
DF.head()