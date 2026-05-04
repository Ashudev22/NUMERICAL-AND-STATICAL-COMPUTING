equation = input("Enter function in x (example: x**3 - x - 2): ")

def f(x):
    return eval(equation)

a = float(input("Enter lower limit (a): "))
b = float(input("Enter upper limit (b): "))

if f(a) * f(b) >= 0:
    print("Invalid interval! f(a) and f(b) must have opposite signs.")
else:
    while abs(b - a) > 0.000001:
        c = (a + b) / 2
        
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Approximate Root =", c)