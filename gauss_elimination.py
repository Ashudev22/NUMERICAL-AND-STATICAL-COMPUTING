n = int(input("Enter number of variables: "))

A = []
print("Enter coefficients row by row:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print("Enter constant terms:")
b = list(map(float, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        ratio = A[j][i] / A[i][i]

        for k in range(n):
            A[j][k] = A[j][k] - ratio * A[i][k]

        b[j] = b[j] - ratio * b[i]

x = [0] * n

for i in range(n - 1, -1, -1):
    s = 0
    for j in range(i + 1, n):
        s += A[i][j] * x[j]

    x[i] = (b[i] - s) / A[i][i]

print("Solution:")
for i in range(n):
    print("x", i + 1, "=", x[i])