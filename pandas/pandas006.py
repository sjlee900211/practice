import numpy as np
import pandas as pd

data = np.array([[1,2,3], [4,5,6],[7,8,9], [10,11,12]])
index_date = pd.date_range('2019-09-01', periods=4)
columns_list = ['A', 'B', 'C']
pd.DataFrame(data, index=index_date, columns=columns_list)