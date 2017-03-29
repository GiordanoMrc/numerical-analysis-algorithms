'''
Sauer's book page 43.

Calculate the cube roots of the following numbers to eight correct decimal places, by using
Fixed-Point Iteration with g(x) = (2x + A/x**2)/3, where A is (a) 2 (b) 3 (c) 5. State your
initial guess and the number of steps needed.
'''

from math import *

def psi(x, op):
    if op == 'A':
        return (2 * x + (2/x**2))/3.0
    if op == 'B':
        return (2 * x + (3/x**2))/3.0
    return (2 * x + (5/x**2))/3.0

def equal(xk1, xk):
    m = abs(xk1 - xk)
    e = 10**(-8) / 2.0

    if m < e:
        return True
    return False

def fixed_point(x, x0, k, op):
    b = x
    a = psi(x, op)
    if k and equal(a, b):
        return a
    else:
        fixed_point(a, b, k+1, op)

def main():
    print("Choose the function you want to test!")
    print("A. 2x + (2/x**2)/3.0")
    print("B. 2x + (3/x**2)/3.0")
    print("C. 2x + (5/x**2)/3.0")
    print("function: ")
    op = input()

    print("Type x0 value: ")
    x0 = float(input())
    root = str(fixed_point(x0, x0, 0, op))
    print("The root is: {:.10}".format(root))

if __name__ == "__main__":
    main()
