'''
Use the Method of False Position to find the solution of each equation in Exercise 1.
'''

from math import *

def f(x):
  if op == 'A':
    return (-1)*(x**3) + 2*x + 2
  if op == 'B':
    return pow(e, x) + x - 7
  return pow(e, x) + sin(x) - 4

def equal(xk1, xk):
  m = abs(xk1 - xk)
  e = 10**(-8) / 2.0

  if m < e:
      return True
  return False

def method_of_false_position(a, b):
  x = (b*f(a) - a*f(b))/(f(a) - f(b))

  if f(x) == 0.0 or equal(x, ant):
    print("The root is {:.8f}".format(x))
  elif f(a, op) * f(x, op) <= 0:
    method_of_false_position(a, x)
  else:
    method_of_false_position(x, b)


def main():
  print("Choose the function you want to test! You can choose between A, B and C.")
  op = input()
  print("Type the name of test file [empty for skip]: ")
  file_name = input()
  try:
    test_file = open(file_name, 'r')
    for line in test_file:
      a = float(line.strip().split()[0])
      b = float(line.strip().split()[1])

      if f(a) * f(b) < 0:
        print("False position method can be applied!")
        method_of_false_position(a, b)
      else:
        print("Sorry! False position method can not be used in this interval!")

    test_file.close()
  except IOError:
    print("How many intervals you want to try?")
    n = int(input())

    for i in range(n):
      print("Type the interval [a, b] to see if there is a way to apply bisection method.")
      print("Type a:")
      a = float(input())
      print("Type b:")
      b = float(input())

      if f(a) * f(b) < 0:
        print("False position method can be applied!")
        method_of_false_position(a, b)
      else:
        print("Sorry! False position method can not be used in this interval!")

if __name__ == "__main__":
    main()
