import numpy as np
import matplotlib.pyplot as plt

def convolution(x,h):

    len_x = len(x)
    len_h = len(h)
    len_y = len(x) + len(h) - 1

    y = np.zeros(len_y)

    for n in range(len_y):
        summation = 0
        for k in range(len_h):
            if 0 <= n-k < len_x:
                summation += h[k] * x[n-k]
        y[n] = summation

    return y

x = [1,2,3,4]
h = [1,0,1]
print('convolution result:',convolution(x,h))

            