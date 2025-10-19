import matplotlib.pyplot as plt
import numpy as np

def crosscorelation(x,y):
    M= len(y)
    N=len(x)
    output_len = N+M-1
    rxy = np.zeros(output_len)
    lag =np.arange(-(M-1),N)
    for i in range(output_len):
        shift = lag[i]
        s=0
        for n in range(N):
            if 0<= n+shift <M:
                s+= x[n]*y[n+shift]
        rxy[i]=s
    return rxy, lag
n = np.arange(0,10)
x = np.exp(0.7**n)
y= np.roll(x,2)
z = crosscorelation(x,y)
print("The cross-correlation is:", z)
plt.subplot(2,1,1)  
plt.stem(x)
plt.title("Input Exponential Decay Signal")
plt.subplot(2,1,2)
plt.stem(z[0])
plt.title("Cross-Correlation Output")
plt.tight_layout()  
plt.show()