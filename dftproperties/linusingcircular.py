import numpy as np

def dft(x):
    N =len(x)
    n = np.arange(N)
    k = n.reshape((N,1))
    w = np.exp(-2j * np.pi * k * n / N)
    return w @ x  

def idft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N,1))
    w = (1/N)*np.exp(2j * np.pi * k * n / N)
    return w @ x 

def linear_convolution_via_circular_convolution(x,h):
    N = len(x) + len(h) - 1
    x_padded = np.pad(x, (0, N - len(x)))
    h_padded = np.pad(h, (0, N - len(h)))
    
    X = dft(x_padded)
    H = dft(h_padded)
    
    Y = X * H
    y = idft(Y)
    
    return y

x = np.array(eval(input("Enter a list of numbers for x: ")), dtype=complex)
h = np.array(eval(input("Enter a list of numbers for h: ")), dtype=complex)
y = linear_convolution_via_circular_convolution(x, h)
print("Linear convolution result:", y)