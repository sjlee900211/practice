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