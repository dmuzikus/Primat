import math
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(3000)


def func(x):
    return math.sin(x) - math.log(x * x, math.e) - 1


def save_tick(a, b, x1, x2, diff):
    print(round(a, 4), round(b, 4), round(x1, 4), round(x2, 4), f"{round(diff, 4)}%")


def methode_dichotomy(eps=0.005):
    delta = eps / 3
    a = 21
    b = 24
    c = (a + b) / 2
    length = b - a
    k = 1
    func_k = 0
    while b - a > eps:
        k += 1
        c = (a + b) / 2
        x1 = c - delta
        x2 = c + delta
        func_k += 2
        if func(x1) > func(x2):
            a = x1
        else:
            b = x2
        save_tick(a, b, x1, x2, ((b - a) / length) * 100)
    print(f"[Share's price]: {func(c)}\n\r[Time]: {c}.\n\r[Iterations]: {k}\n\r[Func "
          f"calculations]: {func_k}")
    return c, k, func_k


def methode_gold(eps=0.005):
    a = 21
    b = 24
    func_k = 2
    length = b - a
    phi = (3 - math.sqrt(5)) / 2
    x1 = a + phi * (b - a)
    value1 = func(x1)
    x2 = b - phi * (b - a)
    value2 = func(x2)
    k = 1
    while b - a > eps:
        k += 1
        if value1 < value2:
            b = x2
            x2 = x1
            value2 = value1
            x1 = a + phi * (b - a)
            value1 = func(x1)
            func_k += 1
        else:
            a = x1
            x1 = x2
            value1 = value2
            x2 = b - phi * (b - a)
            value2 = func(x2)
            func_k += 1
        save_tick(a, b, x1, x2, ((b - a) / length) * 100)
    print(f"[Share's price]: {func((a + b) / 2)}\n\r[Time]: {(a + b) / 2}.\n\r[Iterations]: {k}\n\r[Func "
          f"calculations]: {func_k}")
    return (a + b) / 2, k, func_k


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def search_fib_by_natural(n):
    k = 2
    a = 0
    b = 1
    while b < n:
        b += a
        a = b - a
        k += 1
    return b, k


def methode_fibonacci(eps):
    data = []
    a = 21
    b = 24
    k = 1
    func_k = 2
    f_n, n = search_fib_by_natural((b-a)/eps)
    eps = ((b-a)/f_n)*1.3
    if b-a <= eps:
        return (a + b) / 2, k, func_k
    length = b - a
    x1 = a + (fibonacci(n - k - 1) / fibonacci(n - k + 1)) * (b - a)
    value1 = func(x1)
    x2 = a + (fibonacci(n - k) / fibonacci(n - k + 1)) * (b - a)
    value2 = func(x2)
    data.append([a, b, x1, x2])
    while b - a > eps:
        if value1 > value2:
            a = x1
            x1 = x2
            value1 = value2
            x2 = a + (fibonacci(n - k - 1) / fibonacci(n - k)) * (b - a)
            value2 = func(x2)
            func_k += 1
        else:
            b = x2
            x2 = x1
            value2 = value1
            x1 = a + (fibonacci(n - k - 2) / fibonacci(n - k)) * (b - a)
            value1 = func(x1)
            func_k += 1
        data.append([a, b, x1, x2])
        if k != n - 2:
            k += 1
        else:
            break
        save_tick(a, b, x1, x2, ((b - a) / length) * 100)
    print(f"[Share's price]: {func((x1 + x2) / 2)}\n\r[Time]: {(x1 + x2) / 2}\n\r[Iterations]: {k}\n\r[Func "
          f"calculations]: {func_k}")
    return (x1 + x2) / 2, k, func_k


"""eps = [5*(10**i) for i in range(-5, 1)]
for val in eps:
    value, k, fun_k = methode_gold(val)
    print(val, k, fun_k)"""


"""x = np.arange(21, 26.5, 0.01)
y = np.sin(x) - np.log(x*x) - 1
func_line = plt.plot(x, y, label='y = sin(x) - log(x * x, e) - 1', color='steelblue', linewidth = 3)
point = plt.scatter(value, func(value), color='orange', s=40, marker='o', label='global min')
plt.legend(shadow=True, fontsize=12)
plt.plot(x, y)
plt.grid(True)
plt.minorticks_on()
plt.xlim([20.5, 27])
plt.ylim([-9, 0])
plt.title("График функции (Метод Фибоначчи)")
plt.xlabel("Время, ч")
plt.ylabel("Цена, $")
plt.show()"""
eps = [5*(10**i) for i in range(-5, 1)]
for val in eps:
    value, k, fun_k = methode_fibonacci(val)
    print(val, k, fun_k)
