""" import numpy as np
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

x = np.array(eval(input("enter the elements: ")),dtype=complex)
shift = int(input("enter the shift: "))
N =len(x)
k = np.arange(N)
x_shifted = np.roll(x,shift)
z = dft(x_shifted)
lhs = z
w = dft(x)
phase=np.exp(-2j*np.pi*k*shift/N)
rhs = w *phase
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,2,1)
plt.title('magnitude of lhs')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('magnitude of rhs')
plt.stem(np.abs(rhs))
plt.tight_layout()
plt.show()
"""
""" import numpy as np
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
x = np.array([1, 2, 3, 4], dtype=complex)  # Example: replace with your values
shift = 2  # Example shift value
# x = np.array(eval(input("enter the elements: ")),dtype=complex)  # Original line
# shift = int(input("enter the shift: "))  # Original line
N =len(x)
n = np.arange(N)
x_modulated = x*np.exp(2j*np.pi*shift*n/N)
z = dft(x_modulated)
lhs = z
w = dft(x)
rhs = np.roll(w,-shift)
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,2,1)
plt.title('magnitude of lhs')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('magnitude of rhs')
plt.stem(np.abs(rhs))
plt.tight_layout()
plt.show() """

""" import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N =len(x)
    X = []
    for k in range(N):
        s =0 
        for n in range(N):
            s += x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

def parsevals(x):
    N = len(x)
    X = dft(x)
    lhs = np.sum(np.abs(x)**2)
    rhs = (1/N)*np.sum(np.abs(X)**2)  
    return lhs, rhs

x = np.array(eval(input("enter the elements: ")),dtype=complex)
lhs,rhs = parsevals(x)
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,1,1)
plt.title('lhs value')      
plt.bar([0],lhs)
plt.subplot(2,1,2)
plt.title('rhs value')
plt.bar([0],rhs)
plt.tight_layout()
plt.show() """

""" import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        s = 0 
        for n in range(N):
            s += x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)
def circular_convolution(x,h):
    N = len(x)
    z = np.zeros(N)
    for n in range(N):
        for m in range(N):
            z[n]+=x[m]*h[(n-m) % N]
    return z

x = np.array(eval(input("enter the elements x: ")),dtype=complex)
h = np.array(eval(input("enter the elements h: ")),dtype=complex)
N = len(x)
lhs = dft(x*h)
rhs = (1/N)*circular_convolution(dft(x),dft(h))
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,2,1)
plt.title('magnitude of lhs')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('magnitude of rhs')
plt.stem(np.abs(rhs))
plt.tight_layout()
plt.show() """

"""import numpy as np
import matplotlib.pyplot as plt

x = np.array([3,-1,0,1,3,2,0,1,2,1])
h = np.array([1,1,1])
L =3
M = len(h)
N =L+M-1
x_padded = np.pad(x,(M-1,0))
h_padded = np.pad(h,(0,N-M))
blocks = [x_padded[i:i+N]for i in range(0,x_padded.size-N+1,L)]
if x_padded.size % L != (M-1)%L:
    last_block_start = len(blocks)*L
if last_block_start<x_padded.size:
    last_block = x_padded[last_block_start:]
    last_block = np.pad(last_block,(0,N - len(last_block)))
    blocks.append(last_block)

y = np.zeros(len(x)+M-1)
cursor = 0
for b, block in enumerate(blocks):
    y_blk = np.fft.ifft(np.fft.fft(block)*np.fft.fft(h_padded)).real
    y_valid = y_blk[M-1:]
    end_idx = min(cursor+len(y_valid),len(y))
    y[cursor:end_idx] = y_valid[:end_idx-cursor]
    cursor += L

print('The output signal is: ', y)
plt.stem(y) 
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()"""

import numpy as np
import matplotlib.pyplot as plt
x =np.array([-3,-1,0,1,3,2,0,1,2,1])
h =np.array([1,1,1])
L=4
M = len(h)
N=L+M-1
h_padded =np.pad(h,(0,N-M)) 
blocks =[x[i:i+L]for i in range(0,len(x),L)]
y =np.zeros(len(x)+M-1)
for b,block in enumerate(blocks):
    block_padded = np.pad(block,(0,N-len(block)))
    y_blk = np.fft.ifft(np.fft.fft(block_padded)*np.fft.fft(h_padded)).real
    start_pos = b * L
    end_pos = min(start_pos + N, len(y))
    y[start_pos:end_pos] += y_blk[:end_pos - start_pos]

print('The output signal is: ', y)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()


