import numpy as np

A = np.array([0, 1, 2, 3]).reshape(2, 2)
A
B = np.array([3, 2, 0, 1]).reshape(2, 2)
B

A.dot()
np.dot(A, B)

np.transpose(A)
A.transpose()

# 역행렬
np.linalg.inv(A)

# 행렬식
np.linalg.det(A)