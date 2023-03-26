import math
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(3000)


def func(x):
    return math.sin(x) - math.log(x * x, math.e) - 1


def save_tick(a, b, x1, x2, diff, methode=None):
    print(round(a, 4), round(b, 4), round(x1, 4), round(x2, 4), f"{round(diff, 4)}%", methode if methode else '')


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
    f_n, n = search_fib_by_natural((b - a) / eps)
    eps = ((b - a) / f_n) * 1.3
    if b - a <= eps:
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


def parabolic_method(a, b, eps):
    m = (a + b) / 2
    f_a, f_m, f_b = func(a), func(m), func(b)
    iteration = 0
    calls = 3
    length = a - b
    while b - a > eps:
        p = ((m - a) ** 2) * (f_m - f_b) - ((m - b) ** 2) * (f_m - f_a)
        q = 2 * ((m - a) * (f_m - f_b) - (m - b) * (f_m - f_a))
        u = m - p / q
        f_u = func(u)
        calls += 1
        if m > u:
            if f_m < f_u:
                a, f_a = u, f_u
            else:
                b, f_b = m, f_m
                m, f_m = u, f_u
        else:
            if f_m > f_u:
                a, f_a = m, f_m
                m, f_m = u, f_u
            else:
                b, f_b = u, f_u

        iteration += 1
        # save_tick(a, b, m, u, ((a - b) / length) * 100)

    """print(f"[Share's price]: {func((a + b) / 2)}\n\r[Time]: {(a + b) / 2}\n\r[Iterations]: {iteration}"
          f"\n\r[Func calculations]: {calls}")"""
    return (a + b) / 2, iteration, calls


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
plt.show()
eps = [5 * (10 ** i) for i in range(-5, 1)]
for val in eps:
    value, k, fun_k = methode_fibonacci(val)
    print(val, k, fun_k)"""


def brent_method(a, c, eps):
    gr = (math.sqrt(5) - 1) / 2
    x = w = v = a + gr * (c - a)
    fm = fw = fv = func(x)
    d = e = 0
    u = float('+inf')
    iteration = 0
    calls = 1
    length = a - c
    while c - a > eps:
        iteration += 1
        g, e = e, d
        if len({x, w, v}) == len({fm, fw, fv}) == 3:
            p = ((x - w) ** 2) * (fm - fv) - ((x - v) ** 2) * (fm - fw)
            q = 2 * ((x - w) * (fm - fv) - (x - v) * (fm - fw))
            u = x - p / q
        if a + eps <= u <= c - eps and 2 * abs(u - x) < g:
            algo_type = 'spi'
            d = abs(u - x)
        else:
            algo_type = 'gss'
            if x < (c + a) * .5:
                d = c - x
                u = x + gr * d
            else:
                d = x - a
                u = x - gr * d

        if abs(u - x) < eps:
            """print(f"[Share's price]: {func(x)}\n\r[Time]: {x}\n\r[Iterations]: {iteration}"
                  f"\n\r[Func calculations]: {calls}")"""
            return x, iteration, calls

        fu = func(u)
        calls += 1
        if fu <= fm:
            if u >= x:
                a = x
            else:
                c = x
            v, w, x = w, x, u
            fv, fw, fm = fw, fm, fu

        else:
            if u >= x:
                c = u
            else:
                a = u

            if fu <= fw or w == x:
                v, w = w, u
                fv, fw = fw, fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu
        # save_tick(a, c, x, u, ((a - c) / length) * 100, algo_type)
    """print(f"[Share's price]: {func(x)}\n\r[Time]: {x}\n\r[Iterations]: {iteration}"
          f"\n\r[Func calculations]: {calls}")"""
    return x, iteration, calls


"""value = brent_method(21, 24, 0.005)[0]

x = np.arange(21, 26.5, 0.01)
y = np.sin(x) - np.log(x*x) - 1
func_line = plt.plot(x, y, label='y = sin(x) - log(x * x, e) - 1', color='steelblue', linewidth = 3)
point = plt.scatter(value, func(value), color='orange', s=40, marker='o', label='global min')
plt.legend(shadow=True, fontsize=12)
plt.plot(x, y)
plt.grid(True)
plt.minorticks_on()
plt.xlim([20.5, 27])
plt.ylim([-9, 0])
plt.title("График функции (Метод Брента)")
plt.xlabel("Время, ч")
plt.ylabel("Цена, $")
plt.show()"""

eps = [5 * (10 ** i) for i in range(-5, 1)]
for val in eps:
    value, k, fun_k = brent_method(21, 24, val)
    print(val, k, fun_k)