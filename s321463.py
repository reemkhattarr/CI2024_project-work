# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html

def safe_divide(a, b):
    return np.divide(a, b, where=b != 0, out=np.full_like(a, np.nan))

def safe_sqrt(a):
    return np.sqrt(a, where=a >= 0, out=np.full_like(a, np.nan)) 

def safe_log(a):
    return np.log(a, where=a > 0, out=np.full_like(a, -np.inf)) 

"""
i have written the formulas using the safe functions, so that the functions can be evaluated without any errors
but i have in the comments the formulas without the safe functions as well
"""

# Notez bien: No need to include f0 -- it's just an example!
def f0(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
    return safe_divide(((x[0] - 0.7502398 + (-0.1204699)) * safe_sqrt(330.8889 - safe_divide(-0.8656612,x[0]) - (x[0] - safe_sqrt(x[1])) - (x[1] * x[2]))), 0.08655101)
    #return ((x[0] - 0.7502398 + (-0.1204699)) * np.square(330.8889 - (-0.8656612 / x[0]) - (x[0] - np.square(x[1])) - (x[1] * x[2]))) / 0.08655101


def f3(x: np.ndarray) -> np.ndarray: 
    return np.exp(np.sin((6.8302 - x[1])**2 + 3.9603)) + (11.053 - x[2]) + ((np.exp(0.000477 - x[1]) - np.exp(x[1])) + x[0]**2)


def f4(x: np.ndarray) -> np.ndarray:
    return safe_divide(safe_divide((np.cos(x[1] + -0.00180302) + np.cos(x[1])), 0.2017101), 1.4176001) + 1.074511 - (-2.203303)
    #return (((np.cos(x[1] + -0.00180302) + np.cos(x[1])) / 0.2017101) / 1.4176001) + 1.074511 - (-2.203303)


def f5(x: np.ndarray) -> np.ndarray:
    return np.sin(np.sin(np.exp(x[1] + x[0]) * -6.4885e-13))


def f6(x: np.ndarray) -> np.ndarray: 
    return (x[1] + x[1]) + (0.036213 - ((((x[0] - 0.11854001) - (x[1] - 9.445e-08)) * -0.30548) + x[0]))


def f7(x: np.ndarray) -> np.ndarray: 
    return (np.exp(((np.cos(x[1] * (x[1] - 0.1374602)) + np.cos(x[0] * x[0])) * -0.94102) + (((x[1] * 0.78139) * x[0]) - -0.65089)) + 4.088801)


def f8(x: np.ndarray) -> np.ndarray: 
    return ((safe_sqrt(safe_sqrt(x[5] * 1.4953)) * x[5]) - (safe_sqrt((x[4] * -2.00601) * x[4]) + ((x[1] * x[1]) + (x[3] * -45.16212))))
