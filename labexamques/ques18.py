import numpy as np
import matplotlib.pyplot as plt
def crosscorelation(x,y):
    N =len(x)
    M =len(y)
    output_length = N+M-1
    Rxy = [0]*output_length
    lag = np.arange(-(M-1),N)
    for i in range(output_length):
        m = lag[i]
        for n  in range(N):
            if 0<=n-m<M:
                Rxy[i] += x[n]*y[n-m]
    return np.array(Rxy)

N =10
a = 0.5
n = np.arange(N)
x = a**n
y = np.roll(x,2)  
print("crosscolrelated o/p:  ",crosscorelation(x,y))
z = np.correlate(x,y,mode="full")    
print("Direct crosscorrelated o/p: ",z)
plt.subplot(2,1,1)
plt.stem(crosscorelation(x,y))
plt.title("Crosscorrelation output")
plt.subplot(2,1,2)
plt.stem(z)
plt.title("Direct crosscorrelation output")
plt.tight_layout()
plt.show()


