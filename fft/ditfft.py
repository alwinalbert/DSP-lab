import numpy as np
import matplotlib.pyplot as plt
def dit_fft(x):
    N =len(x)
    if N==1:
        return x
    if N%2 !=0:
        print("length must be the size of square of 2")
        return
    X_even = dit_fft(x[0::2])
    X_odd = dit_fft(x[1::2])
    twiddle = np.exp(-2j*np.pi*np.arange(N)/N)
    return np.concatenate([
        X_even + twiddle[:N//2]*X_odd,
        X_even - twiddle[:N//2]*X_odd
    ])

x = np.array(eval(input("enter x[n] should be lenght of power of 2:")))
x_fft = dit_fft(x)
x_straight = np.fft.fft(x)
print("FFT using numpy is: ", x_straight)
print("FFT of the given signal is: ", x_fft)
plt.subplot(2,1,1)
plt.stem(np.abs(x_straight))
plt.title("FFT Output using Numpy")
plt.subplot(2,1,2)
plt.stem(np.abs(x_fft))
plt.xlabel("k")
plt.ylabel("Magnitude")
plt.title("FFT Output using DIT-FFT Algorithm")
plt.tight_layout()
plt.show()