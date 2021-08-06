import numpy as np

b1 = np.array([0, 10, 20, 30, 40, 50])
b1[1:4]

b1[:3]
b1[2:]

b1[2:5] = np.array([25, 35, 45])
b1

b1[3:6] = 60
b1

b2 = np.arange(10, 100, 10).reshape(3,3)
b2
b2[1:3, 1:3]

b2[:3, 1:]
b2[1][0:2]

b2[0:2, 1:3] = np.array([[25, 35], [55, 65]])
b2