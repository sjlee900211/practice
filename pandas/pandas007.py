import pandas as pd

table_data = {'연도':[2015,2016,2016,2017,2017],
              '지사':['한국','한국','미국','한국','미국'],
              '고객수':[200,250,450,300,500]}
table_data
pd.DataFrame(table_data)

df =pd.DataFrame(table_data, columns=['연도','지사', '고객수'])
df
df.index
df.columns
df.values