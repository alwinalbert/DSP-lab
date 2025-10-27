import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
def hamming(n,N):
    x = 0.54-0.46*np.cos(2*np.pi*n/(N-1))
    return x

def mfreqz(b):
    w,h =sp.freqz(b,1)
    db = 20*np.log2(np.abs(h))
    plt.subplot(2,1,1)
    plt.plot(w,db)
    plt.grid()
    plt.subplot(2,1,2)
    hphase = np.unwrap(np.arctan2(np.imag(h),np.real(h)))
    plt.plot(w,hphase)
    plt.grid()
    plt.show()

def lpf(N,wc,win):
    a =(N-1)/2
    h = [(wc/np.pi) if i == a else np.sin(wc*(i-a))/(np.pi*(i-a)) for i in range(0,N)]
    h = h*win
    mfreqz(h)

N = int(input("Enter the order of filter (N): "))
wc = float(input("Enter the cut-off frequency in rad/s (wc): "))
win = hamming(np.arange(0,N),N)
lpf(N,wc,win)
