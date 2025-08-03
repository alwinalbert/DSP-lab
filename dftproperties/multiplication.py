import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    y = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            y[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return y

def mul(x,h):
    N = len(x)
    lhs = dft(x*h)
    a = dft(x)
    b = dft(h)
    rhs = 1/N * np.fft.ifft(np.fft.fft(a)*np.fft.fft(b))
    return lhs, rhs

x =np.array(eval(input("Enter the signal as a list of numbers: ")),dtype = 'complex')
h = np.array(eval(input("Enter the filter as a list of numbers: ")),dtype = 'complex')
lhs, rhs = mul(x, h)
print('lhs: ',lhs)
print('rhs:',rhs)
plt.subplot(2, 2, 1)
plt.title('lhs magnitude')
plt.stem(np.abs(lhs))
plt.subplot(2, 2, 2)
plt.title('rhs magnitude')
plt.stem(np.abs(rhs))
plt.subplot(2, 2, 3)
plt.title('lhs phase')
plt.stem(np.angle(lhs))
plt.subplot(2, 2, 4)
plt.title('rhs phase')
plt.stem(np.angle(rhs))
plt.tight_layout()
plt.show()