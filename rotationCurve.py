import numpy
import numpy as np
import matplotlib.pyplot as plt
import math

def fun1(x):
    return numpy.sin(x)

def fun2(x):
    return x**5 + x**3 + 7

def g(x):
    return fun2(x)**2

def generate_x_y(fun, n):
    x = []
    y = []
    for i in range(n):
        x.append(i)
        y.append(fun(i))
    return [x, y]

def vandermonde(x):
    ans = []
    n = len(x)
    for i in range(n):
        cur = []
        for j in range(n):
            cur.append(math.pow(x[i], j))
        ans.append(cur)
    return ans

def approximation(x, y):
    matrix = vandermonde(x)
    transpose = numpy.transpose(y)
    inverse = numpy.linalg.inv(matrix)
    sol = numpy.matmul(inverse, transpose)
    return sol

def integral(fun, point, epsilon):
    n = 5
    x, y = generate_x_y(fun, n)
    polynomial = approximation(x, y)
    prev_ans = 0
    for i in range(len(polynomial)):
        prev_ans += point**(i + 1) / (i + 1) * polynomial[i]

    cont = True
    while cont:
        if n > 30:
            print('please increase the epsilon and try again...')
            return None
        n += 1
        x, y = generate_x_y(fun, n)
        polynomial = approximation(x, y)
        ans = 0
        for i in range(len(polynomial)):
            ans += point ** (i + 1) / (i + 1) * polynomial[i]
        if abs(ans - prev_ans) <= epsilon:
            return ans

        prev_ans = ans

    return prev_ans

def compute_integral_a_b(fun, min, max, epsilon):
    a = integral(fun, max, epsilon)
    b = integral(fun, min, epsilon)
    return a - b

# visual part
def find_part(fun, a, b, epsilon):
    total_volume = math.pi * compute_integral_a_b(fun, a, b, epsilon)
    ans = [0, 0, 0]
    i = a
    while i <= b:
        cur_volume = math.pi * compute_integral_a_b(fun, a, i, epsilon)
        fraction = cur_volume / total_volume
        if fraction - 1/3 <= 0.01:
            ans[0] = i
        elif fraction - 1/2 <= 0.01:
            ans[1] = i
        elif fraction - 3/5 <= 0.01:
            ans[2] = i

        i += 0.01

    return ans

def test(g, a, b, epsilon):
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = g(x)

    lst = find_part(g, 0, 1, epsilon)

    plt.plot(x, y, label='g(x)')
    for val in lst:
        plt.axvline(x=val, color='red', linestyle='--', alpha=0.7)
    plt.axvline(x=a, color='blue', linestyle='--', alpha=0.7)
    plt.axvline(x=b, color='blue', linestyle='--', alpha=0.7)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of g(x) with vertical lines at x values from lst')
    plt.grid(True)
    plt.legend()
    plt.show()

