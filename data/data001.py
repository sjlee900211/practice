import pandas as pd

df = pd.read_csv('sport_test.csv', index_col = '학생번호')
df

df['악력']
df.head(0)
df.shape