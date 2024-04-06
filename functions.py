import numpy as np

def f(x):
    """
    Define the function to be integrated.

    Parameters:
        x (float): Input value.

    Returns:
        complex: Value of the function at x.
    """
    return np.sin(2 * x) + 6j + np.cos(x)

def integrand(x, w=1):
    """
    Define the integrand for the Fourier series.

    Parameters:
        x (float): Input value.
        w (float): Frequency controller.

    Returns:
        complex: Value of the integrand at x.
    """
    return f(x) * np.exp(1j * w * x)