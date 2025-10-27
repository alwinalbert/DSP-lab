import numpy as np
import matplotlib.pyplot as plt

x = np.array(eval(input("Enter x: ")))
h = np.array(eval(input("Enter h: ")))

def circ_convolve(a, b):
  N = a.size
  result = np.zeros(N)
  for k in range(N):
    for n in range(N):
      result[k] += a[n] * b[(k - n) % N]

  return result

def overlap_add(x, h, N):
    M = len(h)
    L = N - M + 1

    x_pad = 0

    if x.size % L != 0:
       x_pad = x.size % L
       x = np.pad(x, (0, x_pad))

    h = np.pad(h, (0, N - M))
    y = np.zeros(len(x) + M - 1)

    for i in range(0, len(x), L):
      x_block = np.pad(x[i:i+L], (0, N-len(x[i:i+L])))
      y_block = circ_convolve(x_block, h)
      y[i:i+N] += y_block[:len(y[i:i+N])]

    return y[:len(y) - x_pad]

N = int(input("Enter block size: "))  
y_regular = np.convolve(x, h)
y_block = overlap_add(x, h, N)
fig, a = plt.subplots(2,1)

a[0].stem(y_block)
a[0].set_title("Block Convolution")
a[0].set_xlabel("n")
a[0].set_ylabel("Amplitude")
a[0].grid(True)

a[1].stem(y_regular)
a[1].set_title("Regular Convolution")
a[1].set_xlabel("n")
a[1].set_ylabel("Amplitude")
a[1].grid(True)

fig.tight_layout()
plt.show()