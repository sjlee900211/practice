import pandas as pd

table_data1={'a':[1,2,3,4,5],
             'b':[10,20,30,40,50],
             'c':[100,200,300,400,500]}
df1 = pd.DataFrame(table_data1)
df1

table_data2={'a':[1,2,3],
             'b':[10,20,30],
             'c':[100,200,300]}
df2= pd.DataFrame(table_data2)
df2
df1+df2

table_data3 = {'봄':[256.5,151.5,215.2,552.1,854.5],
               '여름':[256.5,151.5,215.2,552.1,854.5],
               '가을':[256.5,151.5,215.2,552.1,854.5],
               '겨울':[256.5,151.5,215.2,552.1,854.5]}
columns_list =['봄','여름','가을','겨울']
index_list = ['2012','2013','2014','2015','2016']
df3 = pd.DataFrame(table_data3, columns=columns_list, index=index_list)
df3
df3.mean()
df3.std()
df3.mean(axis=1)
df3.std(axis=1)
df3.describe()