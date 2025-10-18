import numpy as np
import matplotlib.pyplot as plt

signal = input('enter the signal: ')
x = np.array([float(num) for num in signal.strip().split()])
filter = input('enter the filter: ')
h = np.array([float(num) for num in filter.strip().split()])
L = int(input('enter the block length it should be >=1: '))
M = len(h)
N = L + M - 1

# Pad the signal so total length is a multiple of L
needed = L * int(np.ceil(len(x)/L)) - len(x)
x_pad = np.concatenate((x, np.zeros(needed)))
blocks = int(len(x_pad) / L)
output = np.zeros(len(x) + M - 1)

# FFT of zero-padded h
h_pad = np.concatenate((h, np.zeros(N - M)))
H = np.fft.fft(h_pad)

for b in range(blocks):
    block_start = b * L
    x_block = x_pad[block_start:block_start+L]
    x_block_pad = np.concatenate((x_block, np.zeros(N - L)))
    X = np.fft.fft(x_block_pad)
    Y = X * H
    y_block = np.fft.ifft(Y).real
    out_start = b * L
out_end = min(out_start + N, len(output))
output[out_start:out_end] += y_block[:out_end - out_start]

y = output[:len(x) + M - 1]
print('The output signal is: ', y)
plt.stem(y)
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()