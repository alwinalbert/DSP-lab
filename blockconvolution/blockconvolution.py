import numpy as np

signal = input('enter the signal: ')
x = np.array([float(num) for num in signal.strip().split()])
filter = input('enter the filter: ')
h = np.array([float(num) for num in filter.strip().split()])

L = int(input('enter the block length it should be >= filter length: '))
M = len(h)
N = L+M-1

x_pad = np.concatenate((np.zeros(M-1),x))
blocks = int(np.ceil(len(x)/L))
output=[]

for b in range(blocks):
    block_start = b*L
    x_block = x_pad[block_start:block_start+N]
    if len(x_block) < N:
        x_block = np.concatenate((x_block,np.zeros(N-len(x_block))))
    h_pad = np.concatenate((h,np.zeros(N-M)))

    X = np.fft.fft(x_block)
    H = np.fft.fft(h_pad)
    Y = X*H
    y_block = np.fft.ifft(Y).real

    output.append(y_block[M-1:M-1+L])

y = np.concatenate(output)
y = y[:len(x) + M - 1]
print('The output signal is: ', y)

