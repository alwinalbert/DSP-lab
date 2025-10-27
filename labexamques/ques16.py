import numpy as np
import matplotlib.pyplot as plt

def circular_conv(x,h):
    N =len(x)
    z = [0]*N
    for n in range(N):
        for k in range(N):
            z[n] += x[k]*h[(n-k)%N]
    return np.array(z)

def overlap_save(x,h,L):
    M =len(h)
    N = len(x)
    output_length = N +M-1
    y = np.zeros(output_length)
    x_padded = np.concatenate([np.zeros(M-1),x])
    blocks = []
    i =0
    while i<len(x_padded):
        if i+L <= len(x_padded):
            block = x_padded[i:i+L]
        else:
            block= x_padded[i:]
            if len(block) < L:
                block = np.concatenate([block,np.zeros(L-len(block))])
        blocks.append(block)
        i += L-(M-1)

    h_padded = np.concatenate([h,np.zeros(L-M)])
    result_segments =[]
    for block in blocks:
        conv_result = circular_conv(block,h_padded)
        valid_samples = conv_result[M-1:]
        result_segments.append(valid_samples)
    y = np.concatenate(result_segments)
    return y[:output_length]
x = np.array(eval(input("Enter the elements x: ")))
h = np.array(eval(input("Enter the elements h: ")))
L = int(input("Enter the block length L: "))
z = np.convolve(x,h)
result = overlap_save(x,h,L)
print("Overlap-save result: ",result)
print("Direct convolution result: ",z)
