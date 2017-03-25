'''
Sauer's book page 43.

Apply Fixed-Point Iteration to find the solution of each equation to eight correct decimal
places. (a) x**5 + x = 1 (b) sin x = 6x + 5 (c) ln x + x**2 = 3
'''

from math import *

def psi(x, op):
    if op == 'A':
        return 1 / ((x ** 4) + 1)
    if op == 'B':
        return (sin(x) - 5) / 6.0
    return sqrt(3 - log(x))

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
        return fixed_point(a, b, k+1, op)

def main():
    print("Choose the function you want to test!")
    print("A. x**5 + x = 1")
    print("B. sin x = 6x + 5")
    print("C. ln x + x**2 = 3")
    print("function: ")
    op = input()

    print("Type x0 value: ")
    x0 = float(input())
    root = str(fixed_point(x0, x0, 0, op))
    print("The root is: {:.10}".format(root))

if __name__ == "__main__":
    main()
