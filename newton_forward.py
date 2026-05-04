
n = int(input("Enter number of data points: "))


print("Enter x values:")
x = list(map(float, input().split()))

print("Enter y values:")
y = list(map(float, input().split()))

xp = float(input("Enter value of x to find y: "))

diff = [y]

for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i-1][j+1] - diff[i-1][j])
    diff.append(temp)


h = x[1] - x[0]

u = (xp - x[0]) / h

result = y[0]
u_term = 1
fact = 1

for i in range(1, n):
    u_term = u_term * (u - i + 1)
    fact = fact * i
    result = result + (u_term * diff[i][0]) / fact

print("Interpolated value at", xp, "=", result)