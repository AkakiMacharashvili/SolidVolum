import math
import numpy

def fun(x, y):
    return x + y

def vandermonde(x, y):
    ans = []
    n = len(x)
    for i in range(n):
        cur_x = x[i]
        for j in range(n):
            cur_y = y[j]
            lst = []
            for p in range(n):
                for q in range(n):
                   lst.append(math.pow(cur_x, p) * math.pow(cur_y, q))
            ans.append(lst)
    return ans

def define_solution(fun, x, y):
    b = []
    n = len(x)
    for i in range(n):
        for j in range(n):
            b.append(fun(x[i], y[j]))
    A = vandermonde(x, y)
    inverse_A = numpy.linalg.inv(A)
    transpone_b = numpy.transpose(b)
    ans = numpy.matmul(inverse_A, transpone_b)
    return numpy.array(ans)

def compute_integral(fun, a, b):
    n = 5
    x, y = generate_X_Y(n)
    sol = define_solution(fun, x, y)
    ans = 0
    n = math.sqrt(len(sol))
    for i in range(len(sol)):
        pow1 = (i - i % n) / n
        pow2 = n - pow1
        mul1 = numpy.pi ** (pow2 + 1) / (pow2 + 1) - (-numpy.pi) ** (pow2 + 1) / (pow2 + 1)
        mul2 = b ** (pow1 + 1) / (pow1 + 1) - a ** (pow1 + 1) / (pow1 + 1)
        ans += sol[i] * mul1 * mul2

    return ans

def generate_X_Y(n):
    x = []
    for i in range(n):
        x.append(i * 5)
    y = []
    for i in range(n):
        y.append(i * 10 + i ** 2)
    return [x, y]

def find_part(fun, a, b):
    total_volume = compute_integral(fun, a, b)
    ans = [0, 0, 0]
    i = a
    while i <= b:
        cur_volume = compute_integral(fun, a, i)
        fraction = cur_volume / total_volume
        if fraction - 1/3 <= 0.01:
            ans[0] = i
        elif fraction - 1/2 <= 0.01:
            ans[1] = i
        elif fraction - 3/5 <= 0.01:
            ans[2] = i

        i += 0.01

    return ans

