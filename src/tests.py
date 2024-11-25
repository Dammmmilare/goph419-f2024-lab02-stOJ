#This file contains unit tests to implement our function in our module file.


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
    


if __name__ == "__main__": #type: ignore