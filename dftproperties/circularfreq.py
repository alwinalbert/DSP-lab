import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    y = np.zeros(N, dtype=complex)
    for k in range(N):
        s = 0
        for n in range(N):
            phase = -2j * np.pi * k * n / N
            s += x[n] * np.exp(phase)
        y[k] = s
    return y

def circular_freq_shift(x, shift):
    N = len(x)
    y = dft(x)
    y_shifted = np.roll(y, shift)
    n = np.arange(N)
    phase = 2j*shift*np.pi*n/N
    lhs = y * np.exp(phase)
    rhs = np.fft.ifft(y_shifted)
    return lhs, rhs
# check this code later to  be changed
x = np.array(eval(input("Enter a list of numbers: ")), dtype=complex)
shift = int(input("Enter the shift value: "))
lhs, rhs = circular_freq_shift(x, shift)
print("Left-hand side (DFT with shift):", lhs)
print("Right-hand side (DFT of shifted signal):", rhs)
plt.subplot(2,2,1)
plt.stem(np.abs(lhs))
plt.title("Magnitude of LHS (DFT with shift)")
plt.subplot(2,2,2)
plt.stem(np.abs(rhs))
plt.title("Magnitude of RHS (DFT of shifted signal)")
plt.subplot(2,2,3)
plt.stem(np.angle(lhs))
plt.title("Phase of LHS (DFT with shift)")
plt.subplot(2,2,4)
plt.stem(np.angle(rhs))
plt.title("Phase of RHS (DFT of shifted signal)")
plt.tight_layout()
plt.show()
