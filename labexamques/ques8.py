import numpy as np
import matplotlib.pyplot as plt
def dft_twiddle_factor_matrix(x):
    N=len(x)
    n =np.arange(N)
    k = n.reshape((N,1))
    w = np.exp(-2j*np.pi*k*n/N)
    print("twiddle factor matrix w: ")
    for i in range(N):
        for j in range (N):
            print(w[i,j],end='')
        print()
    X =np.dot(w,x)
    return X

x = np.array([1,2,3,4,5])
x1 = np.zeros(8)
x2 = np.zeros(16)
x1[:len(x)] = x
x2[:len(x)] = x
X_dft = dft_twiddle_factor_matrix(x1)
Y_dft = dft_twiddle_factor_matrix(x2)
plt.subplot(2,1,1)
plt.stem(np.abs(X_dft))
plt.xlabel('k')
plt.ylabel('Magnitude')
plt.title('DFT using Twiddle Factor Matrix for N=8')
plt.subplot(2,1,2)
plt.stem(np.abs(Y_dft))
plt.xlabel('k')
plt.ylabel('Magnitude')
plt.title('DFT using Twiddle Factor Matrix for N=16')
plt.tight_layout()
plt.show()

