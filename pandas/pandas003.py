import pandas as pd

pd.date_range(start = '2019-01-01', end = '2019-01-07')

pd.date_range(start='2019/01/01', end='2019.01.07')

pd.date_range(start='01-01-2019', end='01/07/2019')

pd.date_range(start='2019-01-01', end='01.07.2019')

pd.date_range(start='2019-01-01', periods=4, freq='2D')

pd.date_range(start='2019-01-01', periods=4, freq='W')

pd.date_range(start='2019-01-01', periods=12, freq='2BM')

pd.date_range(start='2019-01-01', periods=4, freq='QS')

pd.date_range(start='2019-01-01', periods=3, freq='AS')

pd.date_range(start='2019-01-01 08:00', periods=10, freq='H')

pd.date_range(start='2019-01-01 10:00', periods=4, freq='30min')

pd.date_range(start='2019-01-01 10:00', periods=4, freq='30T')

pd.date_range(start='2019-01-01 10:00:00', periods=4, freq='10S')

index_date = pd.date_range(start='2019-03-01', periods=5, freq='D')
pd.Series([51, 62, 55, 49, 58], index=index_date)