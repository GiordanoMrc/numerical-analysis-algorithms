'''
Use the Secant Method to find the (single) solution of each equation in Exercise 1.
'''

from math import *

op

def f(x):
  print(op)
  if op == 'A':
    return (-1)*x**3 + 2*x + 2
  if op == 'B':
    return pow(e, x) + x - 7
  return pow(e, x) + sin(x) - 4

def equal(xk1, xk):
  m = abs(xk1 - xk)
  e = 10**(-6) / 2.0

  if m < e:
      return True
  return False

def secant_method(xk, xk_1):
    if(f(xk) == 0 or equal(xk, xk_1)):
        return xk;

    xk1 = xk - f(xk)*((xk - xk_1)/(f(xk) - f(xk_1)))
    return secant_method(xk1, xk)


def main():
  print("Choose the function you want to test! You can choose between A, B and C.")
  op = input()
  print("Utilizando o método da secante encontramos a raiz ", secant_method(2, 1), " na função ", op);

if __name__ == "__main__":
    main()
