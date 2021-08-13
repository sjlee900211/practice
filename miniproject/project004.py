import matplotlib.pyplot as plt
import pandas as pd

DF = pd.read_excel('notExercise.xls')
DF.head()
# 연령별 데이터 추출
DF_A = DF[DF['대분류'] == '연령별'].copy()
DF_A.drop(columns= '대분류', inplace=True)
DF_A.set_index('분류', inplace=True)
DF_A
figure, ax = plt.subplots(1, 3, figsize = (16, 8))
explode_set = [0.02, 0.02, 0.02, 0.02, 0.02, 0.02]
DF_A['운동을 할 충분한 시간이 없어서'].plot.pie(explode = explode_set,
                                   ax = ax[0],
                                   autopct = '%1.1f%%')
ax[0].set_title('운동을 할 충분한 시간이 없어서')
ax[0].set_ylabel('')

DF_A['함께 운동을 할 사람이 없어서'].plot.pie(explode = explode_set,
                                  ax = ax[1],
                                  autopct = '%1.1f%%')
ax[1].set_title('함께 운동을 할 사람이 없어서')
ax[1].set_ylabel('')

DF_A['운동을 할 만한 장소가 없어서'].plot.pie(explode = explode_set,
                                     ax = ax[2],
                                     autopct = '%1.1f%%')
ax[2].set_title('운동을 할 만한 장소가 없어서')
ax[2].set_ylabel('')

plt.show()