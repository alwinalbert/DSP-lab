import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    """Compute DFT of sequence x"""
    X = []
    N = len(x)
    for k in range(N):
        s = 0
        for n in range(N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(s)
    return np.array(X)

def idft(X):
    """Compute IDFT of sequence X"""
    N = len(X)
    x_t = []
    for n in range(N):
        s = 0
        for k in range(N):
            s += (1/N) * X[k] * np.exp(2j * np.pi * k * n / N)
        x_t.append(s)
    return np.array(x_t)

def circular_convolution(x1, x2):
    """Compute circular convolution of x1 and x2"""
    N = len(x1)
    y = np.zeros(N, dtype=complex)
    for n in range(N):
        for m in range(N):
            y[n] += x1[m] * x2[(n - m) % N]
    return y

def demonstrate_theorem():
    """Demonstrate the DFT-Circular Convolution Theorem"""
    
    print("=" * 60)
    print("DFT-CIRCULAR CONVOLUTION THEOREM DEMONSTRATION")
    print("=" * 60)
    
    # Original sequences
    x1_orig = np.array([1, 2, 3])
    x2_orig = np.array([2, 3])
    
    print(f"Original sequences:")
    print(f"x1 = {x1_orig}")
    print(f"x2 = {x2_orig}")
    
    # Zero-pad to same length (N=5)
    N = 5
    x1 = np.zeros(N)
    x2 = np.zeros(N)
    x1[:len(x1_orig)] = x1_orig
    x2[:len(x2_orig)] = x2_orig
    
    print(f"\nZero-padded sequences (N={N}):")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    
    # Method 1: Time domain circular convolution
    print("\n" + "-" * 40)
    print("METHOD 1: TIME DOMAIN CIRCULAR CONVOLUTION")
    print("-" * 40)
    
    y_time = circular_convolution(x1, x2)
    print(f"Circular convolution result: {np.real(y_time)}")
    
    # Method 2: Frequency domain multiplication
    print("\n" + "-" * 40)
    print("METHOD 2: FREQUENCY DOMAIN MULTIPLICATION")
    print("-" * 40)
    
    # Compute DFTs
    X1 = dft(x1)
    X2 = dft(x2)
    
    print(f"DFT(x1) = {X1}")
    print(f"DFT(x2) = {X2}")
    
    # Multiply DFTs
    Y_freq = X1 * X2
    print(f"DFT(x1) * DFT(x2) = {Y_freq}")
    
    # Take IDFT
    y_freq = idft(Y_freq)
    print(f"IDFT(DFT(x1) * DFT(x2)) = {np.real(y_freq)}")
    
    # Verification
    print("\n" + "=" * 60)
    print("THEOREM VERIFICATION")
    print("=" * 60)
    
    difference = np.abs(y_time - y_freq)
    max_error = np.max(difference)
    
    print(f"Time domain result:      {np.real(y_time)}")
    print(f"Frequency domain result: {np.real(y_freq)}")
    print(f"Absolute difference:     {difference}")
    print(f"Maximum error:           {max_error:.2e}")
    
    if max_error < 1e-10:
        print("\n✓ THEOREM VERIFIED: Both methods give identical results!")
        print("  This proves: IDFT(DFT(x1) * DFT(x2)) = x1 ⊛ x2")
    else:
        print("\n✗ Error detected - check implementation")
    
    # Create plots
    fig, axes = plt.subplots(3, 2, figsize=(12, 10))
    
    # Original sequences
    axes[0,0].stem(range(len(x1)), np.real(x1))
    axes[0,0].set_title('x1[n] (zero-padded)')
    axes[0,0].set_xlabel('n')
    axes[0,0].grid(True, alpha=0.3)
    
    axes[0,1].stem(range(len(x2)), np.real(x2))
    axes[0,1].set_title('x2[n] (zero-padded)')
    axes[0,1].set_xlabel('n')
    axes[0,1].grid(True, alpha=0.3)
    
    # DFT magnitudes
    axes[1,0].stem(range(N), np.abs(X1))
    axes[1,0].set_title('|DFT(x1)|')
    axes[1,0].set_xlabel('k')
    axes[1,0].grid(True, alpha=0.3)
    
    axes[1,1].stem(range(N), np.abs(X2))
    axes[1,1].set_title('|DFT(x2)|')
    axes[1,1].set_xlabel('k')
    axes[1,1].grid(True, alpha=0.3)
    
    # Results comparison
    axes[2,0].stem(range(N), np.real(y_time), linefmt='b-', markerfmt='bo', label='Circular Conv')
    axes[2,0].stem(range(N), np.real(y_freq), linefmt='r--', markerfmt='ro', label='IDFT(X1*X2)')
    axes[2,0].set_title('Comparison of Both Methods')
    axes[2,0].set_xlabel('n')
    axes[2,0].legend()
    axes[2,0].grid(True, alpha=0.3)
    
    # Error plot
    axes[2,1].stem(range(N), difference)
    axes[2,1].set_title('Absolute Difference')
    axes[2,1].set_xlabel('n')
    axes[2,1].set_yscale('log')
    axes[2,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.suptitle('DFT-Circular Convolution Theorem Demonstration', y=0.98)
    plt.show()

if __name__ == "__main__":
    demonstrate_theorem()