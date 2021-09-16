import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
import numpy as np
import pandas as pd

mpl.rcParams['axes.unicode_minus'] = False
plt.rc('font', family='NanumBarunGothic')
warnings.filterwarnings('ignore')

df_covid = pd.read_csv('COVID-19.csv', encoding='utf-8')
df_subway = pd.read_csv('subway.csv', encoding='utf-8')
# df_subway = pd.read_csv('서울교통공사_1_8호선일별역별시간대별승하차인원.csv', encoding='utf-8')

df_subway = df_subway.drop(['a', 'b', 'c', 'd'],axis=1)
# df_subway = df_subway.set_index("date")
pre_sum = df_subway.sum(axis = 1)
df_subway['pre_sum'] = pre_sum

df_subway

subway_date_sum = pd.date_range('2021-01-01', periods=151) # 2021-01-01 ~ 05-31
df=pd.DataFrame(subway_date_sum, columns = ['date'])
df['sum'] = [0]*151
df = df.set_index('date')
df

for i, row in df_subway.iterrows():
    df.loc[row['date']]['sum'] += row['pre_sum']
    

df['confirmed case'] = [0]*151

df_covid

# df_covid_date = df_covid['date']
# df_covid_date
for i, row in df_covid.iterrows():
    if df.index.isin([row['date']]).any():
        df.loc[row['date']]['confirmed case'] += 1

#     row['date']
    
#     if (df['date'] == row['date']).all():
#         df.loc[row['date']]['confirmed case'] += 1

pd.set_option('display.max_row', 200)

df_corr = df.corr()
print('correlation matrix :')

import matplotlib.pyplot as plt

import seaborn as sns

# plt.rcParams['figure.figsize'] = [12, 8]

# # loading 'iris' dataset from seaborn

# df = sns.load_dataset('df')



df.shape


df.head()

plt.plot('confirmed case',

         'sum',

         data=df, 

         linestyle='none', 

         marker='o', 

         markersize=10,

         color='blue', 

         alpha=0.5)

plt.title("Scatter Plot of 'df' by matplotlib", fontsize=20)

plt.xlabel('confirmed case', fontsize=14)

plt.ylabel('sum', fontsize=14)

plt.show()