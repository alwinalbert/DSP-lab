import numpy as np
import matplotlib.pyplot as plt

def circular_convolution(x,h):
    N =len(x)
    z =np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k]*h[(n-k)%N]
    return z

def overlap_save(x, h, L):
    M = len(h)
    N = len(x)
    
    # Step 1: Pad input sequence with M-1 zeros at the beginning
    x_padded = np.concatenate([np.zeros(M-1), x])
    blocks = []
    
    # Step 2: Divide the padded sequence into overlapping blocks of length L
    i = 0
    while i < len(x_padded):
        if i + L <= len(x_padded):
            block = x_padded[i:i+L]
        else:
            block = x_padded[i:]
            if len(block) < L:
                block = np.concatenate([block, np.zeros(L-len(block))])
        blocks.append(block)
        i += L - (M - 1)  # Overlap by M-1 samples
    
    # Step 3: Pad filter h to length L
    h_padded = np.concatenate([h, np.zeros(L-M)])
    
    # Step 4: Perform circular convolution for each block and extract valid samples
    result_segments = []
    for block in blocks:
        conv_result = circular_convolution(block, h_padded)
        valid_samples = conv_result[M-1:]  # Discard first M-1 samples
        result_segments.append(valid_samples)
    
    # Step 5: Concatenate all valid segments
    y = np.concatenate(result_segments)
    return y

#x = np.array(eval(input("Enter the elements x: ")))
x = np.ones(100)
h = np.array(eval(input("Enter the elements h: ")))
L = int(input("Enter the block length L: "))
z = np.convolve(x,h)

result = overlap_save(x, h, L)
print(f"Overlap-save result: {result}")
print(f"Direct convolution result: {z}")

