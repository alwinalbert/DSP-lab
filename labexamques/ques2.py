import numpy as np
import matplotlib.pyplot as plt
def cir_conv_using_matrix(x,h):
    N=len(x)
    H = np.zeros((N,N))
    x_padded=np.zeros(N)
    h_padded = np.zeros(N)
    x_padded[:min(len(x),N)] = x[:min(len(x),N)]
    h_padded[:min(len(h),N)] = h[:min(len(h),N)]

    for n in range(N):
        for k in range(N):
            H[n,k] = h_padded[(n-k)%N]

    y_circ = np.dot(H,x_padded)
    return y_circ


def lin_conv_using_matrix(x,h):
    len_y = len(x)+len(h)-1
    H = np.zeros((len_y,len(x)))
    for n in range(len_y):
        for k in range(len(x)):
            if 0<= n-k < len(h):
                H[n,k] = h[n-k]
    y = np.dot(H,x)
    return y         

x = np.array(eval(input("enter the elements X:")))
h = np.array(eval(input("enter the elements h: ")))
y_linear = lin_conv_using_matrix(x,h)
y_linear= np.trim_zeros(y_linear,"b")
print("The output signal is: ",y_linear)
print("The circular convolution is:", cir_conv_using_matrix(x,h))
plt.subplot(2,1,1)
plt.stem(y_linear)
plt.title("Linear Convolution Output")
plt.subplot(2,1,2)
plt.stem(cir_conv_using_matrix(x,h))
plt.title("Circular Convolution Output")
plt.tight_layout()
plt.show()
