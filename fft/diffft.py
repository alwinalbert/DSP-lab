import numpy as np
import matplotlib.pyplot as plt

def bit_reversal(N):
    N = len(x)
    bits = int(np.log2(N))
    reversal = np.zeros(N,dtype= int)

    for i in range(N):
        b = bin(i)[2:].zfill(bits)
        reversal[i]= int(b[::-1],2)
    return reversal

def dif_fft(x):
    N = len(x)
    if N ==1:
        return x
    if N%2!=0:
        print("length must be the size of square of 2")
        return
    twiddle = np.exp(-2j*np.pi*np.arange(N//2)/N)
    even = x[:N//2] + x[N//2:]
    odd = (x[:N//2]-x[N//2:]) * twiddle
    X_even = dif_fft(even)
    X_odd = dif_fft(odd)    
    return np.concatenate([X_even,X_odd])


x = np.array(eval(input("enter x[n] should be lenght of power of 2:")))
x_fft = dif_fft(x)
x_straight = np.fft.fft(x)

bit_rev = bit_reversal(len(x))
X_ordered = np.zeros(len(x), dtype=complex)
for i in range(len(x)):
    X_ordered[bit_rev[i]] = x_fft[i]

print("FFT using numpy is: ", x_straight)
print("FFT of the given signal is: ", X_ordered)    
plt.subplot(2,1,1)
plt.stem(np.abs(X_ordered))
plt.title("FFT Output using DIF-FFT Algorithm")
plt.subplot(2,1,2)  
plt.stem(np.abs(x_straight))
plt.xlabel("k")
plt.ylabel("Magnitude") 
plt.title("FFT Output using Numpy")
plt.tight_layout()
plt.show()
