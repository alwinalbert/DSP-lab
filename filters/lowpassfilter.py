import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

def hanning(n,N):
    x =0.5-0.5*np.cos(2*np.pi*n/(N-1))
    return x

def hamming(n,N):
    x = 0.54 - 0.46*np.cos(2*np.pi*n/(N-1))
    return x

def mfreqz(b):
    w, h = sp.freqz(b, 1) 
    db = 20 * np.log10(abs(h)) 
    plt.subplot(2, 1, 1) 
    plt.plot(w, db) 
    plt.grid() 
    plt.subplot(2, 1, 2) 
    hphase = np.unwrap(np.arctan2(np.imag(h), np.real(h))) 
    plt.plot(w, hphase) 
    plt.grid() 
    plt.show()   

def lpf(N,wc,win):
    a = (N-1)/2
    h = [wc/np.pi if i == a else np.sin(wc*(i-a))/((i-a)*np.pi) for i in range(0,N)]
    windows = [hanning,hamming]
    h = np.array(h) * windows[win-1](np.arange(0,N),N)
    mfreqz(h)

N = int(input("Enter the order of filter (N): "))
wc = float(input("Enter the cut-off frequency in rad/s (wc): "))
win = int(input("Enter the type of window (1-Hanning, 2-Hamming): "))
lpf(N,wc,win)