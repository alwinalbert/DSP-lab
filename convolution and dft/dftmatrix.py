import numpy as np

def dft_matrix(x):
    x = np.asarray(x, dtype=complex)      # Ensure input is a NumPy array (complex)
    N = len(x)                            # Length of the sequence
    n = np.arange(N)                      # Row indices
    k = n.reshape((N, 1))                 # Column indices as a column vector
    W = np.exp(-2j * np.pi * k * n / N)   # Construct the DFT matrix
    X = W @ x                             # Matrix multiply (DFT)
    return X

# Example usage:
x = [1, 2, 3, 4]
result = dft_matrix(x)
print("DFT (matrix form):", result)