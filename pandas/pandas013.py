import pandas as pd

pd.read_csv('sea_rain1_from_notepad.csv')

pd.read_csv('sea_rain1_from_notepad.csv', encoding="cp949")

pd.read_csv('sea_rain1_from_notepad.csv', encoding="cp949", sep=" ")

pd.read_csv('sea_rain1_from_notepad.csv', encoding="cp949", index_col="연도")