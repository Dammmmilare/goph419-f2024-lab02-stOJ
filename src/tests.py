#Test Script

import os
import numpy as np
import matplotlib.pyplot as plt
from src.linalg_interp import gauss_iter_solve, cubic_spline

def test_gauss_iter_solve():
    A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
    b = np.array([15, 10, 10])
    x_expected = np.linalg.solve(A, b)
    x_test = gauss_iter_solve(A, b, alg='seidel')
    assert np.allclose(x_test, x_expected), "Gauss-Seidel failed."
    x_test_jacobi = gauss_iter_solve(A, b, alg='jacobi')
    assert np.allclose(x_test_jacobi, x_expected), "jacobi failed."

#Test function to test the spline_function under the cubic spline function.
def test_spline_function():
    xd = np.array([0, 1, 2, 3, 4])
    yd = np.array([0, 1, 2, 3, 4])
    spline = cubic_spline(xd, yd, order=2)
    assert np.isclose(spline(2.5), 6.25), "Quadratic spline failed"
    scipy_spline = Univariatespline(xd, yd, k=2, s=0, ext= 'raise')
    assert np.isclose(spline(2.5), scipy_spline(2.5)), "Scipy comparisonfailed"



if __name__ == "__main__": #type: ignore