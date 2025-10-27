import numpy as np
import matplotlib.pyplot as plt

def dit_fft(x):
    N =len(x)
    if N ==1:
        return x
    if np.log2(N)%1 != 0:
        print("length elements should be in the range of power of 2")
        return
    X_even = dit_fft(x[0::2])
    X_odd = dit_fft(x[1::2])
    twiddle = np.exp(-2j*np.pi*np.arange(N)/N)
    return np.concatenate(
        [
            X_even + twiddle[:N//2]*X_odd,
            X_even - twiddle[:N//2]*X_odd
        ]
    )
x = np.array(eval(input("enter x[n] should be length of power of 2:")))
x_dft = dit_fft(x)
print("DFT using FFT method: ",x_dft)
plt.stem(np.abs(x_dft))
plt.title("Magnitude of DFT using FFT")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Magnitude")
plt.show()

