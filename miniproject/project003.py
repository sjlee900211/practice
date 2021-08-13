from project002 import DF_G
import matplotlib.pyplot as plt

figure, ax = plt.subplots(2, 2, figsize = (10, 10))

DF_G['운동을 할 충분한 시간이 없어서'].plot.pie(explode = [0, 0.02],
                                   ax = ax[0][0],
                                   autopct = '%1.1f%%')
ax[0][0].set_title('운동을 할 충분한 시간이 없어서')
ax[0][0].set_ylabel('')

DF_G['함께 운동을 할 사람이 없어서'].plot.pie(explode = [0, 0.02],
                                  ax = ax[0][1],
                                  autopct = '%1.1f%%')
ax[1][0].set_title('운동을 싫어해서')
ax[1][0].set_ylabel('')
DF_G['운동을 할 만한 장소가 없어서'].plot.pie(explode = [0, 0.02],
                                  ax = ax[1][1],
                                  autopct = '%1.1f%%')
ax[1][1].set_title('운동을 할 만한 장소가 없어서')
ax[1][1].set_ylabel('')

plt.show()

# 연령별 데이터 추출
DF_A = DF[DF['대분류'] == '연령별'].copy()
