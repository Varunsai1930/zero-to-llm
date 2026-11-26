import numpy as np

one = np.ones((5,5))
zero = np.zeros((3,3))
zero[1,1] = 9
one[1:4,1:4] = zero
print(one)