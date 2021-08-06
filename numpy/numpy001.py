import numpy as np

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
a1

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
a2

a1.dtype
a2.dtype

np.array([0.5, 2, 0.01, 8])
np.array([[1,2,3], [4,5,6], [7,8,9]])

np.arange(0, 10, 2)
np.arange(1, 10)
np.arange(5)

np.arange(12).reshape(4,3)

b1 = np.arange(12).reshape(4, 3)
b1.shape

b2 = np.arange(5)
b2.shape