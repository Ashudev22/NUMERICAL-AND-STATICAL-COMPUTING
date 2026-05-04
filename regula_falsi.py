
equation = input("Enter function in x (example: x**3 - x - 2): ")

def f(x):
    return eval(equation)

a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))

tol = 0.000001

if f(a) * f(b) >= 0:
    print("Invalid interval! f(a) and f(b) must have opposite signs.")
else:

    for _ in range(100):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(c)) < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Approximate Root =", c)