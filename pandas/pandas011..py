import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Class1':[95, 92, 98, 100],
                    'Class2':[91, 93, 97, 99]})
df1

df2 = pd.DataFrame({'Class1':[98, 100],
                    'Class2':[97, 99]})
df2

df1.append(df2, ignore_index=True)
df3 = pd.DataFrame({'Class1':[96, 83]})
df3

df2.append(df3, ignore_index=True)

df4 = pd.DataFrame({'Class3':[93,91,95,98]})
df4

df1.join(df4)

index_label = ['a','b','c','d']
df1a = pd.DataFrame({'Class1':[95,92,98,100],
                     'Class2':[91,93,97,99]}, index=index_label)

df4a = pd.DataFrame({'Class3':[93,91,95,98]}, index=index_label)

df1a.join(df4a)

df5 = pd.DataFrame({'Class4':[82,92]})
df5

df1.join(df5)