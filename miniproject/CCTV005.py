import matplotlib.pyplot as plt
import CCTV004 as c4

DF = c4.DF

# 막대그래프-pandas
# 소계
DF['소계'].plot(kind='barh', grid = True, figsize = (10, 10))
plt.show()

DF['소계'].sort_values().plot(kind='barh', grid = True, figsize = (10, 10))
plt.show()

# 인구수대비 CCTV비율 계산 후 정렬하여 시각화
DF['CCTV비율'] = DF['소계'] / DF['인구수'] * 100
DF['CCTV비율'].sort_values().plot(kind = 'barh', grid = True, figsize =(10,10))
plt.show()

# 산점도-소계~인구수
plt.figure(figsize=(6,6))
plt.scatter(DF['인구수'], DF['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()