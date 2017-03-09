def f(x):
  return 3 * x**5 + 14 * x**4 + 15 * x**3 + 92 * x**2 + 65 * x + 35 * 1

def equal(xk1, xk):
  e = 0.000001 # verify which error value to use

  if abs(xk1 - xk) < e:
    return True
  return False

def bisection_method(a, b, xk):
  xk1 = (a + b) / 2.0
  
  if equal(xk1, xk):
    return xk1;
  elif: f(a) * f(xk1) < 0:
    bisection_method(a, xk1, xk)
  else:
    bisection_method(xk1, b, xk)

def main():
  print("Type the interval [a, b] to see if there is a way to apply bisection method.")
  print("Type a:")
  a = float(input())
  print("Type b:")
  b = float(input())
  
  if f(a) * f(b) < 0:
    print("Bisection method can be applied!")
    print("The root is {}".format(bisection_method(a, b, b*2)))
  else:
    print("Sorry! Bisection method can not be used in this terminal!")
    

if __name__ == "__main__":
  main()
