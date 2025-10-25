import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        s =0 
        for n in range(N):
            s += x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

def dtft_using_dft(x,N_fft):
    x_padded = np.pad(x,(0,N_fft - len(x)),'constant')
    X = dft(x_padded)
    w = 2*np.pi*np.arange(N_fft)/N_fft
    return X,w        

#x = np.array([2*(0.25)**n for n in range(6)])
x = np.array([1,2,3,4])
N_fft = 512 # Number of points for DFT to approximate DTFT
xw,w = dtft_using_dft(x,N_fft)
plt.subplot(2,1,1)
plt.stem(w,np.abs(xw))
plt.title("DTFT Magnitude using DFT")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Magnitude")
plt.subplot(2,1,2)
plt.stem(w,np.angle(xw))
plt.title("DTFT Phase using DFT")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Phase (radians)")
plt.tight_layout()
plt.show()