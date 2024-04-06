# main.py
from functions import integrand
from integrals import get_integral_bounds, compute_integrals, print_integrals
from fourier import compute_fourier, fourier_series_approximation
from plots import *

def main():
    lower_bound, upper_bound = get_integral_bounds()
    trapezoidal_integral, builtin_result = compute_integrals(lower_bound, upper_bound)
    print_integrals(trapezoidal_integral, builtin_result)

    x = np.linspace(0, 2 * 6 * np.pi, 600)
    T = 2 * np.pi
    fs = fourier_series_approximation(x, T)

    integrand_values = integrand(x)
    plot_original_vs_fourier(x, integrand_values, fs)

    fourier_coeffs, reconstructed_signal = compute_fourier(x, integrand_values)
    plot_built_in_vs_original(x, integrand_values, reconstructed_signal)

    plot_built_in_vs_function(x, fs, reconstructed_signal)

    value_at_T = int(input())
    print("Value of Fourier Series at T:", fs[value_at_T])
    print("Value of reconstructed signal at T:", reconstructed_signal[value_at_T])

if __name__ == "__main__":
    main()
