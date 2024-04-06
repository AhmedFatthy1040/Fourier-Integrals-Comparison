import cmath

def complex_to_polar(z):
    """
    Convert a complex number to polar form.

    Parameters:
        z (complex): Input complex number.

    Returns:
        tuple: Polar coordinates (magnitude, angle).
    """
    r = abs(z)
    theta = cmath.phase(z)
    return r, theta