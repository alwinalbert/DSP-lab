import numpy as np
import matplotlib.pyplot as plt

def dft(x):    
    N = len(x)
    y = np.zeros(N,dtype = complex)
    for k in range(N):
        s = 0
        for n in range(N):
            angle = -2j*np.pi*k*n/N
            s += x[n]*np.exp(angle)
            y[k] = s
    return y        

x = np.array(eval(input('enter elements:')),dtype = complex)
y = np.array(eval(input('enter elements:')),dtype = complex)
a = int(input('enter a: '))
b = int(input('enter b: '))
z = a*x+b*y
lhs = dft(z) 
rhs = a*dft(x) + b*dft(y)
print('lhs =',lhs)
print('rhs =',rhs)
plt.subplot(2,2,1)
plt.title('lhs magnitude')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('rhs magnitude')
plt.stem(np.abs(rhs))
plt.subplot(2,2,3)
plt.title('lhs phase')
plt.stem(np.angle(lhs))
plt.subplot(2,2,4)
plt.title('rhs phase')
plt.stem(np.angle(rhs))  
plt.tight_layout()
plt.show()