from matplotlib import pyplot as plt
import numpy as np


def plot_original_vs_fourier(x, integrand_values, fs):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 5), sharey=True)
    ax1.plot(x, np.real(integrand_values), color='blue', label='Original (Real)')
    ax2.plot(x, np.imag(integrand_values), color='blue', label='Original (Imaginary)')
    ax1.plot(x, np.real(fs), 'x', color='red', label='Fourier Series (Real)', linewidth=0.2)
    ax2.plot(x, np.imag(fs), 'x', color='red', label='Fourier Series (Imaginary)', linewidth=0.2)
    ax1.set_xlabel('Time')
    ax2.set_xlabel('Time')
    ax1.set_ylabel('Signal')
    ax1.set_title('Real Part')
    ax2.set_title('Imaginary Part')
    ax1.legend()
    ax2.legend()
    plt.suptitle('Original vs Fourier')
    plt.tight_layout()
    plt.show()

def plot_built_in_vs_original(x, integrand_values, reconstructed_signal):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 5), sharey=True)
    ax1.plot(x, np.real(integrand_values), color='blue', label='Original (Real)')
    ax1.plot(x, np.real(reconstructed_signal), 'x', color='red', label='Fourier Series (Real)')
    ax1.legend()
    ax2.plot(x, np.imag(integrand_values), color='blue', label='Original (Imaginary)')
    ax2.plot(x, np.imag(reconstructed_signal), 'x', color='red', label='Fourier Series (Imaginary)')
    ax2.legend()
    plt.suptitle('Built-in vs Original')
    plt.tight_layout()
    plt.show()

def plot_built_in_vs_function(x, fs, reconstructed_signal):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 5), sharey=True)
    ax1.plot(x, np.real(fs), color='blue', label='Real & Original')
    ax1.plot(x, np.real(reconstructed_signal), 'x', color='red', label='Real & Fourier Series')
    ax1.legend()
    ax2.plot(x, np.imag(fs), color='blue', label='Imaginary & Original')
    ax2.plot(x, np.imag(reconstructed_signal), 'x', color='red', label='Imaginary & Fourier Series')
    ax2.legend()
    plt.suptitle('Built-in vs Our Function')
    plt.tight_layout()
    plt.show()