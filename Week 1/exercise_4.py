def f(x, op):
  if op == 'A':
    return x**2 - 2
  if op == 'B':
    return x**2 - 3
  return x**2 - 5

def equal(xk1, xk):
  m = abs(xk1 - xk)
  e = 10**(-8) / 2.0

  if m < e:
      return True
  return False

def bisection_method(a, b, ant, op, k):
  x = (a + b) / 2.0

  if f(x, op) == 0.0 or (k != 0 and equal(x, ant)):
    print("We needed just {} iterations".format(k))
    print("The root is {:.8f}".format(x))
  elif f(a, op) * f(x, op) <= 0:
    bisection_method(a, x, x, op, k+1)
  else:
    bisection_method(x, b, x, op, k+1)

def main():
  print("Choose the function you want to test! You can choose between A, B and C.")
  op = input()

  print("How many intervals you want to try?")
  n = int(input())

  for i in range(n):
    print("Type the interval [a, b] to see if there is a way to apply bisection method.")
    print("Type a:")
    a = float(input())
    print("Type b:")
    b = float(input())

    if f(a, op) * f(b, op) < 0:
      print("Bisection method can be applied!")
      bisection_method(a, b, 0, op, 0)
    else:
      print("Sorry! Bisection method can not be used in this interval!")

if __name__ == "__main__":
    main()
