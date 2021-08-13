import numpy as np
import matplotlib.pyplot as plt
import CCTV005 as c5

DF = c5.DF
# 회귀계수 계산-소계~인구수
np.set_printoptions(suppress=True)

fp1 = np.polyfit(DF['인구수'], DF['소계'], 1)
fp1
f1 = np.poly1d(fp1)
print(f1, '\n')

fx = np.linspace(100000, 700000, 100)
print(fx)

# 회귀선 추가
plt.figure(figsize=(10,10))
plt.scatter(DF['인구수'], DF['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

# 오차 열 추가 후 시각화

fp1 = np.polyfit(DF['인구수'], DF['소계'], 1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)
DF['오차'] = np.abs(DF['소계']-f1(DF['인구수']))
df_sort = DF.sort_values(by='오차', ascending=False)
DF

# 최종시각화
plt.figure(figsize=(14,10))
plt.scatter(DF['인구수'], DF['소계'], c=DF['오차'], s=50)
plt.plot(fx, f1(fx), ls = 'dashed', lw=3, color='g')

for n in range(10):
    plt.text(df_sort['인구수'][n] * 1.02,
             df_sort['소계'][n] * 0.98,
             df_sort.index[n],
             fontsize=15)
plt.xlabel('인구수')
plt.ylabel('인구당비율')
plt.colorbar()
plt.grid()
plt.show()