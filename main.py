"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def quadratic_multiply(x, y):
    ### TODO
    xvec = x.binary_vec
    yvec = y.binary_vec
 
    # base case: both are single bits
    n = max(len(xvec), len(yvec))
    if n == 1:
        return x.decimal_val * y.decimal_val
 
    # pad with zeros so both have the same even length
    if n % 2 == 1:
        n = n + 1
    xvec = ['0'] * (n - len(xvec)) + xvec
    yvec = ['0'] * (n - len(yvec)) + yvec
 
    # split into left and right halves
    half = n // 2
    x_left = BinaryNumber(int(''.join(xvec[:half]), 2))
    x_right = BinaryNumber(int(''.join(xvec[half:]), 2))
    y_left = BinaryNumber(int(''.join(yvec[:half]), 2))
    y_right = BinaryNumber(int(''.join(yvec[half:]), 2))
 
    # four recursive multiplications
    left = quadratic_multiply(x_left, y_left)
    middle = quadratic_multiply(x_left, y_right) + quadratic_multiply(x_right, y_left)
    right = quadratic_multiply(x_right, y_right)
 
    return 2**n * left + 2**half * middle + right
    ###

def subquadratic_multiply(x, y):
    ### TODO
    xvec = x.binary_vec
    yvec = y.binary_vec
 
    # base case: both are single bits
    n = max(len(xvec), len(yvec))
    if n == 1:
        return x.decimal_val * y.decimal_val
 
    # pad with zeros so both have the same even length
    if n % 2 == 1:
        n = n + 1
    xvec = ['0'] * (n - len(xvec)) + xvec
    yvec = ['0'] * (n - len(yvec)) + yvec
 
    # split into left and right halves
    half = n // 2
    x_left = BinaryNumber(int(''.join(xvec[:half]), 2))
    x_right = BinaryNumber(int(''.join(xvec[half:]), 2))
    y_left = BinaryNumber(int(''.join(yvec[:half]), 2))
    y_right = BinaryNumber(int(''.join(yvec[half:]), 2))
 
    # only three recursive multiplications
    left = subquadratic_multiply(x_left, y_left)
    right = subquadratic_multiply(x_right, y_right)
    both = subquadratic_multiply(BinaryNumber(x_left.decimal_val + x_right.decimal_val),
                                 BinaryNumber(y_left.decimal_val + y_right.decimal_val))
    middle = both - left - right
 
    return 2**n * left + 2**half * middle + right
    ###

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000
    
def compare_multiply():
    pass
    # compare the empirical runtimes of multiplication functions
    ### TODO - add test cases and measure runtime
    for n in [8, 16, 32, 64, 128, 256, 512]:
        x = BinaryNumber(2**n - 1)
        y = BinaryNumber(2**n - 1)
        print(n, time_multiply(x, y, quadratic_multiply), time_multiply(x, y, subquadratic_multiply))
 
compare_multiply()
    
    

