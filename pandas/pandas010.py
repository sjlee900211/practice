import pandas as pd
import numpy as np

KTX_data = {'경부선 KTX':[39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX':[7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX':[3627, 4168, 4424, 4606, 4984, 5570, 4581],
            '전라선 KTX':[309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동혜선 KTX':[np.nan, np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX', '호남선 KTX', '경전선 KTX', '전라선 KTX', '동해선 KTX']
index_list = ['2011', '2012','2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns=col_list, index=index_list)
df_KTX
df_KTX.index
df_KTX.columns
df_KTX.values

df_KTX.head()#인자 지정하지 않으면 5개 반환
df_KTX.tail()

df_KTX.head(3)
df_KTX.tail(2)

df_KTX[1:2]
df_KTX[2:5]
df_KTX.loc['2011']
df_KTX.loc['2013':'2016']
df_KTX['경부선 KTX']
df_KTX['경부선 KTX']['2012':'2014']
df_KTX['경부선 KTX'][2:5]

df_KTX.loc['2016']['호남선 KTX']
df_KTX.loc['2016', '호남선 KTX']
df_KTX['호남선 KTX']['2016']
df_KTX['호남선 KTX'][5]
df_KTX['호남선 KTX'].loc['2016']

df_KTX.T # 전치를 구하기(데이터의 행렬 바꾸기Transpose)
df_KTX

df_KTX[['동해선 KTX', '전라선 KTX', '경전선 KTX', '호남선 KTX', '경부선 KTX']]