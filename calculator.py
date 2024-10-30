import cmath
##########################################################################
##########################################################################
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y != 0.0:
    return x / y
  
  else:
    return "undefined"
##########################################################################
##########################################################################
def quadratic_formula(a, b, c):
  d = (b**2) - (4 * a * c)

  sol1 = (-b + cmath.sqrt(d)) / (2 * a)
  sol2 = (-b - cmath.sqrt(d)) / (2 * a)

  print("The answers are {0} and {1}".format(sol1, sol2))

def algebraic_equations(a, b, c, d):
  x = subtract(a, c) / subtract(d - b)
  print("x =", x)
##########################################################################
##########################################################################
while True:

  print("What type of problem are you needing?:")
  print("1. Standard (addition, subtraction, multiplication, or devision)")
  print("2. Quadratic (Quadratic Formula)")
  print("3. Algebreic (Ax + B = Cx + D)")

  problem_type = input("What type of problem is it? (1, 2, 3): ")

  if problem_type == '1':
    print("Which Operation?: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Which opperation? (1, 2, 3, or 4): ")

    if choice in ('1', '2', '3', '4'):
      try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
      except:
        ValueError("Invalid input.")

      if choice == '1':
        print(num1, '+', num2, '=', add(num1, num2))

      elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))

      elif choice == '3':
        print(num1, 'x', num2, '=', multiply(num1, num2))

      elif choice == '4':
        print(num1, '/', num2, '=', divide(num1, num2))

      else:
        print("Invalid input")

  elif problem_type == '2':
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    quadratic_formula(num1, num2, num3)

  elif problem_type == '3':
    print("If the number for a specific spot isn't there then put 0")
    a = float(input("Enter the value of A (exclude the x): "))
    b = float(input("Enter the value of B: "))
    c = float(input("Enter the value of C (exclude the x): "))
    d = float(input("Enter the value of D: "))

    algebraic_equations(a, b, c, d)
##########################################################################
##########################################################################
  another_equation = input("Do yoy want to do another problem? (yes/no): ")

  if another_equation == "no":
    break