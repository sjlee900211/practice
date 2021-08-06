import numpy as np

np.array(['1.5', '0.62', '2', '3.14', '3.141592'])

str_a1 = np.array(['1.567', '0.123', '5.123', '9', '8'])
num_a1 = str_a1.astype(float)
num_a1

str_a1.dtype
num_a1.dtype

str_a2 = np.array(['1', '3', '5', '7', '9'])
num_a2 = str_a2.astype(int)
num_a2

str_a2.dtype
num_a2.dtype

num_f1 = np.array([10, 21, 0.549, 4.75, 5.98])
num_i1 = num_f1.astype(int)
num_i1

num_f1.dtype
num_i1.dtype