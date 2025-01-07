#fabonacci series to find minimam of a function

import numpy as np
import matplotlib.pyplot as plt

# Initial interval
a = 1
b = 3
# Tolerance
tol = 0.5

def f(x):
    return 2*x+(1/((2*x**2)-1))

#iterations
i=0

# Initial points

#fibonacci series
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=0
while fibonacci(n)<((b-a)/tol):
    n+=1
x1 = a + (fibonacci(n-2)/fibonacci(n))*(b - a)
x2 = a + (fibonacci(n-1)/fibonacci(n))*(b - a)
f1 = f(x1)
f2 = f(x2)
i=0
# Loop until the interval is small enough
while (b - a) > tol:
    if f1 < f2:
        b = x2
        x2 = x1
        f2 = f1
        x1 = a + (fibonacci(n-2)/fibonacci(n))*(b - a)
        f1 = f(x1)
    else:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + (fibonacci(n-1)/fibonacci(n))*(b - a)
        f2 = f(x2)
    i+=1
xmin=(a + b) / 2

print(f"Minimum point: {xmin} and value: {f(xmin)} iterations: {i}")
# Plot
x = np.linspace(-2, 2, 100)
y = f(x)
plt.plot(x, y)
plt.plot(xmin, f(xmin), 'ro')

plt.show()
