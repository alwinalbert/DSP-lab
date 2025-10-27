import numpy as np
import matplotlib.pyplot as plt

def autocorrelation(x):
    N = len(x)
    output_length = 2*N-1
    Rxx = [0]*output_length 
    lag = np.arange(-(N-1),N)
    for i in range(output_length):
        m = lag[i]
        for n in range(N):
            if 0<= n-m <N:
                Rxx[i] += x[n] *x[n-m]
    return np.array(Rxx)

def crosscorrelation(x,y):
    N = len(x)
    M = len(y)
    output_len = N+M-1
    Rxy = [0]*output_len
    lag = np.arange(-(M-1),N)  
    for i in range(output_len):
        m = lag[i]
        for n in range(N):
            if 0<=n-m<M:  
                Rxy[i] += x[n]*y[n-m]
    return np.array(Rxy)

x = np.array(eval(input("enter the elements: ")))
y = np.array(eval(input("enter the y elements: ")))
print("crosscolrelated o/p:  ",crosscorrelation(x,y))
z = np.correlate(x,y,mode="full")
print(z)
print("autocorrelated o/p : ",autocorrelation(x))
y = np.correlate(x,x,mode='full')
print(y)