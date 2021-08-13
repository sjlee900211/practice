import numpy as np
import CCTV003 as c3

# 상관계수
DF = c3.DF

# 고령자비율 VS. 소계
print(np.corrcoef(DF['고령자비율'], DF['소계']))

# 외국인비율 VS. 소계
print(np.corrcoef(DF['외국인비율'], DF['소계']))

# 인구수 VS. 소계
print(np.corrcoef(DF['인구수'], DF['소계']))

# CCTV개수(소계)와 인구수의 관계
DF.sort_values(by='소계', ascending=False).head()

DF.sort_values(by='인구수', ascending=False).head()