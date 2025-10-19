import numpy as np
import matplotlib.pyplot as plt
def auto_corelation(x):
    N = len(x)
    output_len = 2*N-1
    Rxx = np.zeros(output_len)
    lag = np.arange(-(N-1),N)
    for i in range(output_len):
        shift = lag[i]
        s =0
        for n in range(N):
            if 0<=n-shift<N:
                s+=x[n]*x[n-shift]
        Rxx[i]=s
    return Rxx,lag
x = np.ones(10)
plt.subplot(2,1,1)
plt.grid(True)
plt.stem(x)
plt.title("input Rectangular Pulse")
Rxx, lag = auto_corelation(x)
print("The auto-correlation is:", Rxx)
plt.subplot(2,1,2)
plt.stem(Rxx)
plt.grid(True)
plt.title("Auto-Correlated rectangular pulse")
plt.tight_layout()
plt.show()
