#Test Script

import os
import numpy as np
import matplotlib.pyplot as plt
from src.linalg_interp import gauss_iter_solve, cubic_spline

def test_gauss_iter_solve():

    #System description:
    A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
    b = np.array([15, 10, 10])

    x_seidel = gauss_iter_solve(A, b, tol= 1e-8, alg='seidel')

    x_expected = np.linalg.solve(A, b)

    np.testing.assert_almost_equal(x_seidel, x_expected, decimals=6)
    print("Gauss-seidel test passed!")

#Test function to test the spline_function under the cubic spline function.
def test_spline_function():

    #Defining the test data
    xd = np.array([0, 1, 2, 3, 4])
    yd = np.array([0, 1, 2, 3, 4])

    spline = cubic_spline(xd, yd, order=2)

    x_test = np.array([0.5, 1.5, 2.5, 3.5])
    y_test = spline(x_test)

    y_expected = x_test**2

    np.testing.assert_almost_equal(y_test, y_expected, decimal=6)
    print("Cubic spline test passed!")

if __name__ == "__main__":

    test_gauss_iter_solve()
    test_spline_function()