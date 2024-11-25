# This file contains the utility functions required for the workability of our 
# algorithm and system.

import numpy as np
#Function helps us solve large scale and sparse systems where the use of iteirative 
#methods can use sparsity to save computational stress.

def gauss_iter_solve(A, b, x0=None, tol=1e-8, alg='seidel'):
   
   """
        Parameters:
        ===========

        A:
        --
        Let 'A' be an array_like containing the coefficient matrix. 

        b:
        --
        Let 'b'in an array_like containing the right-hand-side vector(S). 

        x0:
        ---
        Let 'X0' ba an (optional) array_like containing the initial guess(es).

        tol:
        ----
        We may define 'tol' as an (optional) float that gives us the relative error tolerance 
        which is also the (stopping criterion) for our algorithm.

        alg:
        ----
        Defining 'alg' as an (optional) str flag for the alhorithm to be used .
       
        Note:
        =====
        We may aso assume that that our return value is a numpy.array with the same shape
        as 'b'.  Let it be an mxn array type.

        Returns:
        ========
        numpy.ndarray. an array type function

    """
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

#This function generates a spline interpolation function for our algorithm
#from scipy.interpolate import Univariatespline
import numpy as np

def cubic_spline(xd, yd):
    """
        Parameters:
        ===========
        xd:
        ---
        Let us define 'xd' as an array_like of float data strictlty increasing in value. 

        yd:
        ---
        Let us define 'yd' as an array_like of float data increasing in value 
        or with same shape as xd.

        Order:
        ------
        Let us define xd as an (optional) int  with possible values 
        1, 2, or 3 (default=3), and the return value is a function that takes one parameter (a 
        float or array_like of float) and returns the interpolated y value(s).

        Note:
        =====
        ""spline_function() should raise a ValueError in the following cases:""

        i. The flattened arrays of xd and yd do not have the same length (i.e. the 
        -- number of independent variable values is not equal to the number of 
           dependent variable values).

        ii.There are repeated values in xd (i.e. the number of unique independent 
        --- variable values is not equal to the number of independent variable values 
            given) [Hint: You may want to use numpy.unique().]

        iii. The xd values are not in increasing order (i.e. the sorted array of 
        ---- independent variable values is not equal to the flattened array of 
             independent variable values) [Hint: You may want to use numpy.sort().]

        iv. order is a value other than 1, 2, or 3.
        ---
 
        Returns:
        ========
        function

        Raises (ErrorType):
        ==================
        ValueError : if inputs are invalid or do not meet requirements as desired.
        """
 
    xd = np.asarray(xd)
    yd = np.asarray(yd)

    # Setting intervals (n) and interval lengths (h)
    n = len(xd) - 1
    h = np.diff(xd)

    #Step 1: setting the system up for second derivatives
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)

    #Neutral spline boundary conditions
    A[0, 0] = 1
    A[n, n] = 1

    #Internal continuity and smoothness conditons
    for i in range(1 + n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2 * (h[i -1 ] + h[i])
        A[i, i + 1] = h[i]
        b[i] = (3 / h[i]) * (yd[i + 1] - yd[i]) - (3 / h[i - 1]) * (yd[i] - yd[i - 1])
    
    #Solve for M second derivative
    M = np.linalg.solve(A, b)

    #Step 2: computing the coefficient for each segement
    splines = []
    for i in range(n):
        a = yd[i]
        b = (yd[i + 1] - yd[i]) / h[i] - h[i] * (2 * M[i] + M[1 + i]) / 3
        c = M[i]
        d = (M[1 + i] - M[i]) / (3 * h[i])
        splines.append((a, b, c, d))


#Step 3: Define spline function
    def spline_function():

        x = np.asarray(x)
        result = np.zeros_like(x, dtype=float)
    
        for i in range(n):
            mask = (xd[i] <= x) & (x <= xd[i + 1])
            dx = x[mask] - xd[i]
            a, b, c, d = splines[i]
            result[mask] = a + b * dx + c * dx**2 + d * dx**3
        return result 

    return spline_function