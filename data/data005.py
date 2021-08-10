import numpy as np
import pandas as pd

pd.set_option('precision', 3)

df = pd.read_csv('scores_em.csv',
                 index_col='student number')
en_scores = np.array(df['english'])[:10]
ma_scores = np.array(df['mathematics'])[:10]

scores_df = pd.DataFrame({'english':en_scores,
                          'mathematics':ma_scores},
                         index=pd.Index(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                                        name='student'))
scores_df

# 공분산
summary_df = scores_df.copy()
summary_df['english_deviation']=\
    summary_df['english'] - summary_df['english'].mean()
summary_df['mathematics_deviation'] = \
    summary_df['mathematics'] - summary_df['mathematics'].mean()
summary_df['product of deviations'] = \
    summary_df['english_deviation'] * summary_df['mathematics_deviation']
summary_df

summary_df['product of deviations'].mean()
cov_mat = np.cov(en_scores, ma_scores, ddof = 0)
cov_mat

cov_mat[0, 1], cov_mat[1, 0]
cov_mat[0, 0], cov_mat[1, 1]
np.var(en_scores, ddof=0), np.var(ma_scores, ddof=0)

np.cov(en_scores, ma_scores, ddof=0)[0, 1] /\
    (np.std(en_scores) * np.std(ma_scores))
np.corrcoef(en_scores, ma_scores)
scores_df.corr()