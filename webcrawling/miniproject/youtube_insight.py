from numpy import pi
from pandas.core.reshape.pivot import pivot
import youtube as you
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family = font_name) 
elif platform.system() == 'Darwin':
    rc('font', family = 'Gothic')
else:
    print('Check your OS system')
    
# 엑셀 불러오기
df = pd.read_excel('C:/Users/Celine/practice/webcrawling/miniproject/files/youtube.xlsx')
df.head()
df.tail()
df['subscriber']
df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df.head()
df.info()
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
df.info()

pivot_df = df.pivot_table(index='category', values='replaced_subscriber', aggfunc=['sum','count'])
pivot_df.head()

pivot_df.columns=['subscriber_sum', 'category_count']
pivot_df.head()

# 데이터프레임 인덱스 초기화
pivot_df = pivot_df.reset_index()
pivot_df.head()

# 데이터프레임 내림차순정렬
pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)
pivot_df.head()

# 카테고리별 구독자 시각화하기
plt.figure(figsize=(30,10))
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='.%1.1f%%')
plt.show()

# 카테고리별 채널 수 시각화하기
pivot_df = pivot_df.sort_values(by='category_count', ascending=False)
pivot_df.head()
plt.figure(figsize=(30, 10))
plt.pie(pivot_df['category_count'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()