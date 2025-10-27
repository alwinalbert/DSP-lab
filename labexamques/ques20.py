import numpy as np
import matplotlib.pyplot as plt
def toeplitz(x,h):
    N = len(x)
    M = len(h)
    L = N+M-1
    H = np.zeros((L,N))
    for n in range (L):
        for k in range(N):
            if 0<=n-k<M:
                H[n,k] = h[n-k]
    y = np.dot(H,x)
    return y

x = np.array(eval(input("enter the elements x: ")))
h = np.array(eval(input("enter the elements h: ")))
print("convolution result by toeplitz method:",toeplitz(x,h))
z = np.convolve(x,h)
print("convolution result by numpy method:",z)
