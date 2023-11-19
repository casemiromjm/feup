P = int(input())
r = float(input())
n = int(input())

t = 2

A = P*((1 + r/n)**(n*t))
A = round(A,3)

print(A)