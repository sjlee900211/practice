import numpy as np
import pandas as pd

pd.set_option('precision', 3)
df = pd.read_csv('scores_em.csv', index_col='student number')
df.head()
# 데이터의 시각화
# 50명의 영어 점수 array
english_scores = np.array(df['english'])
# Series로 변환하여 describe를 표시
pd.Series(english_scores).describe()

# 도수분포표
freq, _ = np.histogram(english_scores, bins= 10, range=(0, 100))
freq
# 0~10, 10~20, ...이라는 문자열의 리스트를 작성
freq_class = [f'{i}~{i+10}' for i in range(0, 100, 10)]
# freq_class를 인덱스로 DataFrame을 작성
freq_dist_df = pd.DataFrame({'frequency':freq},
                            index=pd.Index(freq_class, name='class'))
freq_dist_df

class_value = [(i+(i+10))//2 for i in range(0,100,10)]
class_value

rel_freq = freq / freq.sum()
rel_freq

cum_rel_freq = np.cumsum(rel_freq)
cum_rel_freq

freq_dist_df['class value'] = class_value
freq_dist_df['relative frequency'] = rel_freq
freq_dist_df['cumulative relative frequency'] = cum_rel_freq
freq_dist_df = freq_dist_df[['class value', 'frequency', 'relative frequency', 'cumulative relative frequency']]

freq_dist_df

# 최빈값 재검토
freq_dist_df.loc[freq_dist_df['frequency'].idxmax(), 'class value']