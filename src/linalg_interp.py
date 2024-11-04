"""
Note:
Create a linalg_interp.py file that will contain your utility functions. This file 
should NOT contain an
 if __name__ == "__main__":
 guard and should not have any code that runs outside of function definitions 
(other than import statements)."""

import numpy as np

def gauss_iter_solve():

    """
        Parameters:
        !!!!! A :
        Let 'A' be an array_like containing the coefficient matrix. 
        !!!!!! b :
        Let 'b'in an array_like containing the right-hand-side vector(S). 
        !!!!!! Xo
        Let 'Xo' ba an (optional) array_like containing the initial guess(es).
        !!!!!! tol :
        We may define tol as an (optional) float that gives us the relative error tolerance 
        which is also the (stopping criterion) for our algorithm.
        !!!!!! alg :
        Defining alg as an (optional) str flag for the alhorithm to be used .

        Note:
        We may aso assume that that our return value is a numpy.array with the same shape
        as 'b'.

        Returns:
        numpy.ndarray
    """




def spline_function():

    """
        Parameters:
        !!!!! xd:
        Let us define xd as an array_like of float data increasing in value. 
        !!!!! yd:
        Let us define yd as an array_like of float data increasing in value 
        or with same shape as xd.
        !!!!! order:
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
    