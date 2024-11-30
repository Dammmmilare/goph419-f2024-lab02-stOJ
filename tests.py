# Test Script

import os
import numpy as np
import matplotlib.pyplot as plt
from src.linalg_interp import gauss_iter_solve, cubic_spline

def test_gauss_iter_solve():

    # System description.
    A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
    b = np.array([15, 10, 10])

    x_seidel = gauss_iter_solve(A, b, tol= 1e-8, alg='seidel')

    if x_seidel is None:
        print("Gauss-Seidel didnt converge")
        return 
    
    x_expected = np.linalg.solve(A, b)

    np.testing.assert_almost_equal(x_seidel, x_expected, decimal=6)
    print("Gauss-seidel test passed!")

# Test function to test the spline_function under the cubic spline function.
def test_spline_function():

    # Defining the test data.
    xd = np.array([0, 1, 2, 3, 4])
    yd = xd**2

    # Invoking our cubic spline.
    spline = cubic_spline(xd, yd, order=3)

    # Trying for interpolation.
    x_test = np.array([0.5, 1.5, 2.5, 3.5])
    y_test = spline(x_test)

    # Expected results.
    y_expected = x_test**2

    # Results verification to check for equality.
    np.testing.assert_almost_equal(y_test, y_expected, decimal=6)
    print("Cubic spline interpolating test passed!")


    try:
        spline(-1)
    except ValueError as e:
        print("Correctl raised error for x < xd[0]:", e)

    try:
        spline(5)
    except ValueError as e:
        print("Correct raised error for x > xd[-1]:", e)


if __name__ == "__main__":

    test_gauss_iter_solve()
    test_spline_function()