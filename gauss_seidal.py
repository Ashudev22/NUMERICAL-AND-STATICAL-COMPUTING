# Simple Dynamic Gauss-Seidel Method

n = int(input("Enter number of variables: "))

# Input coefficient matrix A
A = []
print("Enter coefficients row by row:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

# Input constants b
print("Enter constant terms:")
b = list(map(float, input().split()))

# Initial guess
x = [0] * n

# Tolerance
tol = 0.000001

# Gauss-Seidel Iteration
for _ in range(100):
    x_old = x.copy()

    for i in range(n):
        s = 0

        for j in range(n):
            if j != i:
                s += A[i][j] * x[j]

        x[i] = (b[i] - s) / A[i][i]

    # Check convergence
    error = max(abs(x[i] - x_old[i]) for i in range(n))

    if error < tol:
        break

# Output
print("Solution:")
for i in range(n):
    print("x", i + 1, "=", x[i])