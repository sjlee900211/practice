import pandas as pd

df_WH = pd.DataFrame({'Weight':[62, 67, 55, 74],
                    'Height':[165,177,160,180]},
                    index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])
df_WH.index.name = 'User'
df_WH

bmi = df_WH['Weight'/(df_WH['Height']/100)**2]
bmi

df_WH['BMI']=bmi
df_WH

df_WH.to_csv('save_DataFrame.csv')