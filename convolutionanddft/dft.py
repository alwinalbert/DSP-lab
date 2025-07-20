import numpy as np

def dft(x):
    x = np.asarray(x, dtype=complex)            
    N = len(x)                              
    y = np.zeros(N, dtype=complex)              

    for k in range(N):                          
        s = 0
        for n in range(N):                      
            angle = -2j * np.pi * k * n / N     
            s += x[n] * np.exp(angle)        
        y[k] = s                                
    return y

x = eval(input('enter elements:'))
print("DFT result:",dft(x))