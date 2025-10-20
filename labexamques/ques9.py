import numpy as np
import matplotlib.pyplot as plt
def linear_conv_using_matrix(x,h):
    N = len(x)
    M =len(h)
    len_y = N+M-1
    H =np.zeros((len_y,N))
    for n in range(len_y):
        for k in range(N):
            if 0<=n-k<M:
                H[n,k] = h[n-k]
    y=np.dot(H,x)
    return y

x = np.array(eval(input("enter x[n]: ")))
h = np.array(eval(input("enter the h[n]: ")))
conv_result = linear_conv_using_matrix(x,h)
print("The linear convolution result is: ", conv_result)
plt.stem(conv_result)
plt.title("Linear Convolution Output")  
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.show()    