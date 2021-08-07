import pandas as pd
import numpy as np

df_A_B = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품A': [100,50,15,45],
                       '제품B':[90,52,70,80]})
df_A_B

df_C_D = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품C': [180,50,15,45],
                       '제품D':[80,52,70,80]})
df_C_D

df_A_B.merge(df_C_D)

df_left = pd.DataFrame({'key':['A','B','C'], 'left':[1,2,3]})
df_left

df_right = pd.DataFrame({'key':['A','B','D'], 'right':[4,5,6]})
df_right

df_left.merge(df_right, how='left', on='key')
df_left.merge(df_right, how='right', on='key')
df_left.merge(df_right, how='outer', on='key')
df_left.merge(df_right, how='inner', on='key')