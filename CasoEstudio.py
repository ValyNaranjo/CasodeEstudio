import numpy as np

def tridiag(n, d, a, c, b):
    x = np.zeros(n)
    for i in range(1, n):
        mult = a[i - 1] / d[i - 1]
        d[i] = d[i] - mult * c[i - 1]
        b[i] = b[i] - mult * b[i - 1]
    x[n - 1] = b[n - 1] / d[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = x[i] = (b[i] - c[i] * x[i + 1]) / d[i]
        print(i)
    return x


# Datos del ejercicio
n = 100
d = np.repeat(1.0, n)
c = np.repeat(0.5, n - 1)
a = np.repeat(0.5, n - 1)
b1 = 1.5
b_2_99 = 2.0
b100 = 1.5
b = np.hstack((b1, np.repeat(b_2_99, 98), b100))  #NOTA: b es un vector

# Uso de función
x = tridiag(n=n, d=d, a=a, c=c, b=b)
print(x)

# Solución exacta:

d = 1
c = 0.5
a = 0.5
b1 = 1.5
b_2_99 = 2
b100 = 1.5

A = np.zeros((100, 100))
b = np.zeros((100))
for i in range(100):
    A[i, i] = d
    if i < 1:
        A[i, i + 1] = c
        b[i] = b1
    elif i >= 1 and i < 99:
        A[i, i - 1] = a
        A[i, i + 1] = c
        b[i] = b_2_99
    elif i >= 99:
        A[i, i - 1] = a
        b[i] = b100

x = np.linalg.solve(A, b)