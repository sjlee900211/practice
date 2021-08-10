import numpy as np
from numpy.lib.function_base import median
import pandas as pd

pd.set_option('precision', 3)
df = pd.read_csv('scores_em.csv', index_col='student number')
df.head()

scores = np.array(df['english'])[:10]
scores

scores_df = pd.DataFrame({'score':scores},
                         index=pd.Index(['A','B','C','D','E','F','G','H','I','J'],
                                        name='student'))
scores_df

# 평균값
sum(scores) / len(scores)
np.mean(scores)
scores_df.mean()

# 중앙값
sorted_scores = np.sort(scores)
sorted_scores

n = len(sorted_scores)
if n % 2 == 0:
    m0 = sorted_scores[n//2 - 1]
    m1 = sorted_scores[n//2]
    median = (m0 + m1) / 2
else:
    median = sorted_scores[(n+1)//2 - 1]
median

np.median(scores)
scores_df.median()

# 최빈값
pd.Series([1,1,1,2,2,3]).mode()
pd.Series([1,2,3,4,5]).mode()

# 편차
mean = np.mean(scores)
deviation = scores - mean
deviation
another_scores = [50, 60, 58, 54, 51, 56, 57, 53, 52, 59]
another_mean = np.mean(another_scores)
another_deviation = another_scores - another_mean
another_deviation

np.mean(deviation)
np.mean(another_deviation)

summary_df = scores_df.copy()
summary_df['deviation'] = deviation
summary_df

summary_df.mean()

# 분산
np.mean(deviation ** 2)
np.var(scores)
scores_df.var()

summary_df['square of deviation'] = np.square(deviation)
summary_df

# 표준편차
np.sqrt(np.var(scores, ddof=0))
np.std(scores, ddof=0)

# 범위
np.max(scores) - np.min(scores)

# 4분위수 범위
scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)
scores_IQR = scores_Q3 - scores_Q1
scores_IQR

# 데이터 지표 정리
pd.Series(scores).describe()

# 표준화
z=(scores - np.mean(scores)) / np.std(scores)
z

np.mean(z), np.std(z, ddof=0)

# 편차값
z = 50 + 10 * (scores - np.mean(scores)) / np.std(scores)
z

scores_df['deviation value'] = z
scores_df