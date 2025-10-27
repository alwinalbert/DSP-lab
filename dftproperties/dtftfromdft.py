import numpy as np
import matplotlib.pyplot as plt

x = eval(input("Enter the input"))
N = int(input("enter dft size"))

def dft_matrix(x):
    x = np.array(x, dtype="complex")
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    X = W @ x
    return X

X_dft = dft_matrix(x)
X_padded = np.pad(x, (0, N - len(x)))
X_dftt = dft_matrix(X_padded)

plt.plot(X_dftt)
plt.show()