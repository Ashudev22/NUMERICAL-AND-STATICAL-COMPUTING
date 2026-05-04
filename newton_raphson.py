
equation = input("Enter function in x (example: x**3 - x - 2): ")

derivative = input("Enter derivative of function (example: 3*x**2 - 1): ")

def f(x):
    return eval(equation)

def df(x):
    return eval(derivative)

x = float(input("Enter initial guess: "))

tol = 0.000001

for _ in range(100):
    x_new = x - f(x) / df(x)

    if abs(x_new - x) < tol:
        break

    x = x_new

print("Approximate Root =", x_new)