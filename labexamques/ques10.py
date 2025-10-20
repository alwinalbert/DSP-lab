import numpy as np
import matplotlib.pyplot as plt
def lin_conv(x,h):
    N =len(x)
    M =len(h)
    len_y = N+M-1
    y = np.zeros(len_y)
    for n in range(len_y):
        s =0
        for k in range(N):
            if 0<=n-k<M:
                s+=x[k]*h[n-k]
        y[n]=s
    return y

x = np.array(eval(input("enter x[n]: ")))
h = np.array(eval(input("enter the h[n]: ")))
y_conv = lin_conv(x,h)
print("impulse response: ",y_conv)
plt.stem(y_conv)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Linear Convolution Output")
plt.show()