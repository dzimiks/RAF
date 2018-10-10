from math import floor, sqrt


def fibonacci(n):
    a, b = 0, 1

    for _ in range(0, n):
        a, b = b, a + b

    return a


# O(n)
def fib(n):
    return int(floor(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)) + 0.5))


for i in range(0, 21):
    print("Fibonacci %2d: %4d" % (i, fib(i)))
