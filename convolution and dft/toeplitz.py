import numpy as np
import matplotlib.pyplot as plt

def convolution(x,h):

    len_x = len(x)
    len_h = len(h)
    len_y = len(x) + len(h) - 1

    toeplitz_matrix = np.zeros((len_y,len_x))

    for n in range(len_y):
        for k in range(len_x):
            if 0 <= n-k < len_h:
                toeplitz_matrix[n,k] = h[n-k]

    y = toeplitz_matrix @ x            
    return y

x = [1,2,3,4]
h = [1,0,1]
print('convolution result:',convolution(x,h))

            