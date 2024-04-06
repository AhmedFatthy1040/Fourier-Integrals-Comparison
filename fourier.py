import numpy as np
from integrals import integrate_complex
from functions import integrand
from scipy.fft import fft, ifft

def fourier_series_approximation(x, periodic_time, no_of_terms=30, accuracy=10000, w=1):
    """
    Compute the Fourier series of a given function and compare integration methods.

    Parameters:
        x (array-like): Array of input values.
        periodic_time (float): Periodic time.
        no_of_terms (int): Number of Fourier series terms.
        accuracy (int): Accuracy of numerical integration.
        w (float): Frequency controller.

    Returns:
        tuple: Tuple containing Fourier series signal and integration comparison.
    """
    def a0(integrand, periodic_time, accuracy, w=w):
        return integrate_complex(integrand, 0, periodic_time, accuracy, w) / periodic_time

    def ak(integrand, k, periodic_time, accuracy, w=w):
        def integrand_fn(x, w=w):
            return integrand(x, w) * np.cos(2 * np.pi * k * x / periodic_time)
        return (2 / periodic_time) * integrate_complex(integrand_fn, 0, periodic_time, accuracy, w)

    def bk(integrand, k, periodic_time, accuracy, w=w):
        def integrand_fn(x, w=w):
            return integrand(x, w) * np.sin(2 * np.pi * k * x / periodic_time)
        return (2 / periodic_time) * integrate_complex(integrand_fn, 0, periodic_time, accuracy, w)

    a0_value = a0(integrand, periodic_time, accuracy, w)
    sum_terms = np.zeros_like(x, dtype=np.complex128)
    for i in range(1, no_of_terms + 1):
        sum_terms += ak(integrand, i, periodic_time, accuracy, w) * np.cos(2 * np.pi * i * x / periodic_time) + \
                     bk(integrand, i, periodic_time, accuracy, w) * np.sin(2 * np.pi * i * x / periodic_time)
    sum_terms += a0_value
    return sum_terms

def compute_fourier(x, integrand_values):
    fourier_coeffs = fft(integrand_values)
    reconstructed_signal = ifft(fourier_coeffs)
    return fourier_coeffs, reconstructed_signal