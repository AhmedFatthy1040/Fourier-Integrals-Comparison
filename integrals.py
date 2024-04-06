import numpy as np
from scipy.integrate import quad
from functions import integrand
from utils import complex_to_polar

def integrate_trapezoidal(integrand, a, b, n=10000):
    """
    Numerically integrate a given function using the trapezoidal rule.

    Parameters:
        integrand (callable): Function to integrate.
        a (float): Lower bound of integration.
        b (float): Upper bound of integration.
        n (int): Number of subdivisions.

    Returns:
        float: Approximate value of the integral.
    """
    h = (b - a) / n  # Calculate the step size
    sum_trap = 0
    for i in range(n + 1):  # Summation using the trapezoidal rule
        x = a + i * h
        if i == 0 or i == n:  # Endpoints
            coefficient = 1
        else:
            coefficient = 2
        sum_trap += coefficient * integrand(x)
    return h * sum_trap / 2

def integrate_complex(integrand, a, b, n=10000, w=1):
    """
    Numerically integrate a complex-valued function.

    Parameters:
        integrand (callable): Complex-valued function to integrate.
        a (float): Lower bound of integration.
        b (float): Upper bound of integration.
        n (int): Number of subdivisions.
        w (float): Frequency controller.

    Returns:
        complex: Approximate value of the integral.
    """
    h = (b - a) / n  # Calculate the step size
    sum_trap = 0
    for i in range(n + 1):  # Summation using the trapezoidal rule
        x = a + i * h
        if i == 0 or i == n:  # Endpoints
            coefficient = 1
        else:
            coefficient = 2
        sum_trap += coefficient * integrand(x, w)
    return h * sum_trap / 2

def get_integral_bounds():
    lower_bound = float(input("Enter your lower bound: "))
    upper_bound = float(input("Enter your upper bound: "))
    return lower_bound, upper_bound

def compute_integrals(lower_bound, upper_bound):
    trapezoidal_integral = integrate_trapezoidal(integrand, lower_bound, upper_bound, n=1000)
    builtin_result_real, _ = quad(lambda x: integrand(x, 1).real, lower_bound, upper_bound)
    builtin_result_image, _ = quad(lambda x: integrand(x, 1).imag, lower_bound, upper_bound)
    builtin_result = builtin_result_real + 1j * builtin_result_image
    return trapezoidal_integral, builtin_result

def print_integrals(trapezoidal_integral, builtin_result):
    trapezoidal_polar = complex_to_polar(trapezoidal_integral)
    builtin_polar = complex_to_polar(builtin_result)
    print("Integration using trapezoidal rule:")
    print("Complex:", trapezoidal_integral)
    print("Polar:", trapezoidal_polar)
    print("\nIntegration using built-in function (quad):")
    print("Complex:", builtin_result)
    print("Polar:", builtin_polar)