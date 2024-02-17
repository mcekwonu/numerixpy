#!/usr/bin/env python3
"""Numerical Integration Method implementing Trapeziodal method, Simpson's rule,
midpoint method and Two-point Gauss-Legendre method
"""

import numpy as np


class Integral:
    """
    Numerical integration class.
    
    
    Attributes:
        f (callable): function to integrate
        a (int): lower interval of integration
        b (int): upper interval of integration
        n (int): Number of subinterval in [a, b]
    
    \int f(x) = \sum w_i * f(x_i)        
    """
    
    def __init__(self, f, a, b, n, method="trapz"):
        """Returns:
            Approximate integral of f(x)
        """
        
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.method = method
        
        if method == "midpoint":
            self.h = (self.b - self.a)/self.n
        else:
            self.h = (self.b - self.a)/(self.n - 1)
        
        if method == "trapezoidal":
            weights = []
            weights.append(self.h/2)
            
            for i in range(1, n-1):
                weights.append(self.h)            
            weights.append(self.h/2)
            
        elif method == "midpoint":
            weights = []
            
            for i in range(n):
                weights.append(self.h)
                
        elif method == "simpson":
            weights = []
            weights.append(self.h/3)
            
            for i in range(1, n-1):
                if i % 2 == 1:
                    weights.append((4*self.h)/3)
                else:
                    weights.append((2*self.h)/3)                
            weights.append(self.h/3)
            
        else:
            raise NotImplementedError(f"{method.title()} method is not implemented yet!")
        
        self.weights = np.array(weights)
            
    def __call__(self):
                
        f_values = np.array([self.f(self.a + i*self.h) for i in range(self.n)])
     
        return (self.weights @ f_values).sum()
        

def test():
    f = lambda x: 1/ (2 + x)
        
    for method in ["trapezoidal", "midpoint", "simpson"]:
        fx = Integral(f, a=-1, b=1, n=100, method=method)
        print(f"{Integral.__name__} of 1/(2+x), using {method.title()} = {fx():.5f}")
    
        
def test2():
    f = lambda x: np.sin(x)
        
    for method in ["trapezoidal", "midpoint", "simpson"]:
        fx = Integral(f, a=0, b=1, n=100, method=method)
        print(f"{Integral.__name__} of sin(x), using {method.title()} = {fx():.5f}")
    
             
    
if __name__ == "__main__":
    test() 
    print()
    test2()
