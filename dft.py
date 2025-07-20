import numpy as np

def dft(x):
    x = np.asarray(x, dtype=complex)            
    N = len(x)                              
    X = np.zeros(N, dtype=complex)              

    for k in range(N):                          
        s = 0
        for n in range(N):                      
            angle = -2j * np.pi * k * n / N     
            s += x[n] * np.exp(angle)        
        X[k] = s                                
    return X

x = [1, 2, 3, 4]
result = dft(x)
print("DFT result:", result)