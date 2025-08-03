import numpy as np 
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    y = np.zeros(N,dtype = complex)
    for k in range(N):
        s =0
        for n in range(N):
            phase = -2j*np.pi*k*n/N
            s += x[n]*np.exp(phase)
            y[k] = s
    return y 
       
x = np.array(eval(input('enter elements:')),dtype = complex)
shift = int(input('enter shift:'))
N = len(x)
x_shifted = np.roll(x,shift)
y = dft(x)
z = dft(x_shifted)
lhs = z
k = np.arange(N)
phase = -2j*np.pi*k*shift/N
rhs = y * np.exp(phase)
print('lhs: ',lhs)
print('rhs: ',rhs)
plt.subplot(2,2,1)
plt.title('magnitude of lhs')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('magnitude of rhs')
plt.stem(np.abs(rhs))
plt.subplot(2,2,3)
plt.title('phase of lhs')
plt.stem(np.angle(lhs))
plt.subplot(2,2,4)
plt.title('phase of rhs')
plt.stem(np.angle(rhs))
plt.tight_layout()
plt.show()