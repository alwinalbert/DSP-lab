import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

def hanning(n,N):
    x =0.5-0.5*np.cos(2*np.pi*n/(N-1))
    return x

def hamming(n,N):
    x =0.54-0.46*np.cos((2*np.pi*n/(N-1)))
    return x

def mfreqz(b):
    w,h =sp.freqz(b,1)
    db =20*np.log10(abs(h))
    plt.subplot(2,1,1)
    plt.plot(w,db)
    plt.grid()
    plt.subplot(2,1,2)
    hpase = np.unwrap(np.arctan2(np.imag(h),np.real(h)))
    plt.plot(w,hpase)
    plt.grid()
    plt.show()

def hpf(N,wc,win):
    a= (N-1)/2
    h =[wc/np.pi if i == a else (np.sin((i - a)*np.pi) - np.sin((i - a)*wc))/(np.pi*(i-a)) for i in np.arange(0,N)]
    windows = [hanning,hamming]
    h = h*windows[win-1](np.arange(0,N),N)
    mfreqz(h)

N = int(input("enter the order or length of filter: "))
wc = float(input("enter the cutoff frequency in rad/s: "))
win = int(input("enter the type of window (1-Hanning, 2-Hamming): "))
hpf(N,wc,win)
