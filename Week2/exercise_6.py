'''
Sauer's book page 43.

Derive three different g(x) for finding roots to six correct decimal places of the following
f(x) = 0 by Fixed-Point Iteration. Run FPI for each g(x) and report results, convergence or
divergence. Each equation f (x) = 0 has three roots. Derive more g(x) if necessary until all
roots are found by FPI. For each convergent run, determine the value of S from the errors
e i+1 /e i , and compare with S determined from calculus as in (1.11). (a) f(x) = 2x**3 −
6x − 1 (b) f(x) = e**x−2 + x**3 − x (c) f(x) = 1 + 5x − 6x**3 − e**2x

A return 1 / ((2 * (x ** 2)) - 6) -0.1682544
return pow((0.5 + 3 * x), 1/3) 1.81003792

B return pow(x - e ** (x - 2), 1/3) 0.78894139
return -e ** (x - 2) / ((x ** 2) - 1) 0.16382224

C Complex solutions.
'''

from math import *

def psi(x, op):
    if op == 'A':
        return pow(x - e ** (x - 2), 1/3)
    if op == 'B':
        return -e ** (x - 2) / ((x ** 2) - 1)
    return x ** 3 + e ** (x - 2)

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
    print("A. f(x) = 2x**3 − 6x − 1")
    print("B. f(x) = e**x−2 + x**3 − x")
    print("C. f(x) = 1 + 5x − 6x**3 − e**2x)
    print("function: ")
    op = input()

    print("Type x0 value: ")
    x0 = float(input())
    root = str(fixed_point(x0, x0, 0, op))
    print("The root is: {:.10}".format(root))

if __name__ == "__main__":
    main()
