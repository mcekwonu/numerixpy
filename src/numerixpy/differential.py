#!/usr/bin/env/python3

"""Numerical Differentiation class for forward, backward and central method
of 1-order, 2-order, 4-order and 6-order
"""

import sys
import numpy as np


class Diff:
    """
    Numerical approximation of First-order derivative.
    
         
        f'(x)  = h^{-1} * \sum_{i=-r}^{r} w_{i} * f(x{_i})
        
        
    Attributes:
        f (callable): 
            function to differentiate
        h (float): 
            step size, default 1e-5
        method (str): 
            Finite difference approximation method
        order (int): 
            Order of approximation
    """
    
    table = {
        ("forward", 1): [0, 0, 0, 0, -1, 1, 0, 0, 0],
        ("forward", 2): [0, 0, 0, 0, -3/2, 2, -1/2, 0, 0],
        ("backward", 1): [0, 0, 0, -1, 1, 0, 0, 0, 0],
        ("backward", 2): [0, 0, 1/2, -2, 3/2, 0, 0, 0, 0],
        ("forward", 3): [0, 0, 0, -2/6, -1/2, 1, -1/6, 0, 0],
        ("central", 2): [0, 0, 0, -1/2, 0, 1/2, 0, 0, 0],
        ("central", 4): [0, 0, 1/12, -2/3, 0, 2/3, -1/12, 0, 0],
        ("central", 6): [0, -1/60, 3/20, -3/4, 0, 3/4, -3/20, 1/60, 0],
        ("central", 8): [1/280, -4/105, 12/60, -4/5, 0, 4/5, -12/60, 4/105, -1/280]
        }
    
    def __init__(self, f, h=1e-5, method="central", order=2):
        self.f = f
        self.h = h
        self.method = method
        self.order = order
        self.weights = np.array(self.table.get((method, order)))
        
        if not self.weights.any():
            print(f"{method.title()} method with order of {order} is not implemented!")
            sys.exit()
        
    def __call__(self, x):
        f_values = np.array([self.f(x + i*self.h) for i in range(-4, 5)])
        
        return (self.weights @ f_values) / self.h
        

class Diff2:
    """
    Numerical approximation of Second-order derivative.
    
         
        f''(x)  = 1/h^2 * \sum_{i=-r}^{r} w_{i} * f(x{_i})
        
        
    Attributes:
        f (callable): 
            function to differentiate
        h (float): 
            step size, default 1e-5
        method (str): 
            Finite difference approximation method
        order (int): 
            Order of approximation
    """
    
    table = {
        ("forward", 1): [0, 0, 0, 0, 1, -2, 1, 0, 0],
        ("forward", 2): [0, 0, 0, 0, 2, -5, 4, -1, 0],
        ("backward", 1): [0, 0, 1, -2, 1, 0, 0, 0, 0],
        ("backward", 2): [0, -1, 4, -5, 2, 0, 0, 0, 0],
        ("central", 2): [0, 0, 0, 1, -2, 1, 0, 0, 0],
        ("central", 4): [0, 0, -1/12, 4/3, -5/2, 4/3, -1/12, 0, 0],
        }
    
    def __init__(self, f, h=1e-5, method="central", order=2):
        self.f = f
        self.h = h
        self.method = method
        self.order = order
        self.weights = np.array(self.table.get((method, order)))
        
        if not self.weights.any():
            print(f"{method.title()} method with order of {order} is not implemented!\nProgram exited!")
            sys.exit()

    def __call__(self, x):
        f_values = np.array([self.f(x + i*self.h) for i in range(-4, 5)])
        
        return (self.weights @ f_values) / self.h**2
    

def test_diff():
    x = 2
    for (method, order) in zip(["forward", "forward", "backward", "backward", "central", "central"], [1, 2, 1, 2, 2, 4]):
        dfdx = Diff(lambda x: x ** 3, method=method, order=order)(x=x)
        output = f"{Diff.__qualname__} of x^3 at x={x}, using {method} of order {order} = {dfdx:.5f}"
        print(output)


def test_diff2():
    x = 2
    for (method, order) in zip(["forward", "forward", "backward", "backward", "central", "central"], [1, 2, 1, 2, 2, 4]):
        d2fdx = Diff2(lambda x: x ** 3, method=method, order=order)(x=x)
        output = f"{Diff2.__qualname__} of x^3 at x={x}, using {method} of order {order} = {d2fdx:.5f}"
        print(output)
        
        
    
if __name__ == "__main__":
    test_diff()
    print()
    test_diff2()
