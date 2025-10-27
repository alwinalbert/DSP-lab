import numpy as np
import matplotlib.pyplot as plt
def autocorelation(x):
    N =len(x)
    output_length =2*N-1
    rxx = [0]*output_length
    lag = np.arange(-(N-1),N)
    for i in range(output_length):
        m = lag[i]
        for n in range(N):
            if 0<=n-m<N:
                rxx[i]+=x[n]*x[n-m]
    return rxx

x = np.array([(1/4)**n for n in range(0,5)])
Rxx = autocorelation(x)
plt.subplot(2,2,1)
plt.stem(x)
plt.title("Input Sequence x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.subplot(2,2,2)
plt.stem(Rxx)
plt.title("Autocorrelation Rxx[m]")
plt.xlabel("m")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()