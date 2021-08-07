from os import sep
import pandas as pd

df_pr = pd.DataFrame({'판매가격':[2000,3000,5000,10000],
                      '판매량':[32,53,40,25]},
                     index=['P1001', 'P1002', 'P1003', 'P1004'])
df_pr.index.name='제품번호'
df_pr

file_name = 'save_DataFrame_cp949.txt'
df_pr.to_csv(file_name, sep= " ", encoding="cp949")