import pandas as pd
import numpy as np

s3 = pd.Series([np.nan, 10, 30])
s3

index_date = ['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10']
s4 = pd.Series([200, 195, np.nan, 205], index = index_date)
s4

s5 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
s5