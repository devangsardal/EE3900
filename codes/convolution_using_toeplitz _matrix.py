import numpy as np
from scipy import linalg

x=np.array([2,-1]).reshape(2,1) # x.reshape is to make it a 2 cross 1 matrix
h=np.array([-1,2,1])

# print(x.shape[])
# print(x.dtype)
padding = np.zeros(x.shape[0]-1, x.dtype)
# print(padding)
first_col = np.r_[h, padding]
# print(first_col)
first_row = np.r_[h[0], padding]
# print(first_row)

H=linalg.toeplitz(first_col,first_row)
# print(H)
print(H@x)
