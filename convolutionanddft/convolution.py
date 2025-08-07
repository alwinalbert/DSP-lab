import numpy as np

def convolution(x,h):

    len_x = len(x)
    len_h = len(h)
    len_y = len(x) + len(h) - 1

    y = np.zeros(len_y)

    for n in range(len_y):
        summation = 0
        for k in range(len_x):
            if 0 <= n-k < len_h:
                summation += h[n-k] * x[k]
        y[n] = summation

    return y

x = eval(input('enter elements:'))
h = eval(input('enter elements:'))
print('convolution result:',convolution(x,h))

            
