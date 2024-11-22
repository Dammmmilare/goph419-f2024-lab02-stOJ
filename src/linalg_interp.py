# This file contains the utility functions required for the workability of our 
# algorithm and system.

import numpy as np

"""
        Parameters:

        Let 'A' be an array_like containing the coefficient matrix. 
        Let 'b'in an array_like containing the right-hand-side vector(S). 
        Let 'Xo' ba an (optional) array_like containing the initial guess(es).
        We may define 'tol' as an (optional) float that gives us the relative error tolerance 
        which is also the (stopping criterion) for our algorithm.
        Defining 'alg' as an (optional) str flag for the alhorithm to be used .
        Let it be an mxn array type.

        Note:
        We may aso assume that that our return value is a numpy.array with the same shape
        as 'b'.

        Returns:
        numpy.ndarray.
    """

# Function helps us solve large scale and sparse systems where the use of iteirative 
# methods can use sparsity to save computational stress.

def gauss_iter_solve(A, b, x0=None, tol=1e-8, alg='seidel'):
    # Converting the values of A and B into arrays
   A = np.asarray(A, dtype=float)
   b = np.asarray(b, dtype=float)

   # Validates dimensions
   n, m = A.shape
   if n != m or b.shape[0] != n:
        raise ValueError("Matrix dimensions shuld match the form Ax=b ")

    # Initialising our variable x
   if x0 is None:
      x = np.zeros_like(b, dtype=float)
   else:
    x0 = np.asarray(x0, dtype=float)
    if x0.shape == b.shape:
        x = x0 
    elif x0.ndim == 1 and x0.shape[0] == n:
        x = np.title(x0[:, None], (1, b.shape[1]))
    else:
        raise ValueError("x0 must match the shape of b or be a valid initial guess")

    # Initializing algorithm choice
    alg = str(alg).strip().lower() 
    if alg not in {'seidel', 'jacobi'}:
        raise ValueError("Our expected algorithm must be of 'seidel' or 'jacobi' form.")

    #Our iterative solver
    max_iter = 10000
    for _  in range (max_iter):
        x_new = x.copy()
    for i in range(n):
        # Sum computations
        if alg == 'seidel':
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
        elif alg == 'jacobi':
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
        x_new[i] = (b[i] - sum1 - sum2 )/ A[i, i]

    # Checking for Convergence
    if np.linalg.norm(x_new - x) / np.linalg.norm(x_new) < tol:
        return x_new

    x = x_new
# Warning to be raised if our maximum iterations are reached
raise RuntimeWarning("Solution did not converge within maximum iterations.")






def spline_function():

    """
        Parameters:
        Let us define 'xd' as an array_like of float data increasing in value. 
        Let us define 'yd' as an array_like of float data increasing in value 
        or with same shape as xd.
        Let us define xd as an (optional) int  with possible values 
        1, 2, or 3 (default=3), and the return value is a function that takes one parameter (a 
        float or array_like of float) and returns the interpolated y value(s).

        Note:
        spline_function() should raise a ValueError in the following cases:
        i. The flattened arrays of xd and yd do not have the same length (i.e. the 
        number of independent variable values is not equal to the number of 
        dependent variable values)
        ii.There are repeated values in xd (i.e. the number of unique independent 
        variable values is not equal to the number of independent variable values 
        given) [Hint: You may want to use numpy.unique().]
        iii. The xd values are not in increasing order (i.e. the sorted array of 
        independent variable values is not equal to the flattened array of 
        independent variable values) [Hint: You may want to use numpy.sort().]
        iv. order is a value other than 1, 2, or 3.
 
        Returns:
        function
    """
    