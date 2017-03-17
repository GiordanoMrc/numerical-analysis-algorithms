from math import cos

def f(x):
  return x**3 - 9;
  #return 3*(x**3) + x**2 - x - 5
  #return cos(x)**2 - x + 6

def equal(xk1, xk, a, b, k):
  e = 10**(-6) / 2.0

  if m < e:
      return True
  return False

def bisection_method(a, b, ant, k):
  x = (a + b) / 2.0

  if f(x) == 0.0 or (k != 0 and equal(x, ant, a, b, k)):
    print("The root is ", x)
  elif f(a) * f(x) <= 0:
    bisection_method(a, x, x, k+1)
  else:
    bisection_method(x, b, x, k+1)

def main():
  
  print("Type the interval [a, b] to see if there is a way to apply bisection method.")
  print("Type a:")
  a = float(input())
  print("Type b:")
  b = float(input())

  if f(a) * f(b) < 0:
    print("Bisection method can be applied!")
    bisection_method(a, b, 0, 0)
  else:
    print("Sorry! Bisection method can not be used in this interval!")


if __name__ == "__main__":
    main()
