
n = int(input("Enter number of variables: "))

A = []
print("Enter coefficients row by row:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print("Enter constant terms:")
b = list(map(float, input().split()))

x = [0] * n

tol = 0.000001

for _ in range(100):
    x_new = [0] * n

    for i in range(n):
        s = 0

        for j in range(n):
            if j != i:
                s += A[i][j] * x[j]

        x_new[i] = (b[i] - s) / A[i][i]

    error = max(abs(x_new[i] - x[i]) for i in range(n))

    if error < tol:
        x = x_new
        break

    x = x_new

print("Solution:")
for i in range(n):
    print("x", i + 1, "=", x[i])