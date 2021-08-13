import matplotlib.pyplot as plt
import pandas as pd

DF = pd.read_excel('notExercise.xls')
DF.head()
# 연령별 데이터 추출
DF_V = DF[DF['대분류'] == '학력별'].copy()
DF_V.drop(columns= '대분류', inplace=True)
DF_V.set_index('분류', inplace=True)
DF_V

figure, ax = plt.subplots(1, 2, figsize = (16, 8))

explode_set = [0.02, 0.02, 0.02, 0.02]

DF_V['운동을 할 충분한 시간이 없어서'].plot.pie(explode = explode_set,
                                   ax = ax[0],
                                   autopct = '%1.1f%%')
ax[0].set_title('운동을 할 충분한 시간이 없어서')
ax[0].set_ylabel('')

DF_V['운동을 싫어해서'].plot.pie(explode = explode_set,
                          ax = ax[1],
                          autopct = '%1.1f%%')
ax[1].set_title('운동을 싫어해서')
ax[1].set_ylabel('')

plt.show()