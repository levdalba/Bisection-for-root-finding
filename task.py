def f(x):
    return x**2 - 4


def bisection(f, a, b, epsilon):
    if f(a) * f(b) > 0:
        print("No root in this interval")
        return None
    else:
        iterations = 0
        while abs(b - a) > epsilon:
            iterations += 1
            c = (a + b) / 2
            if f(c) == 0:
                return c
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return c, iterations


print(bisection(f, 0, 5, 0.0001))
