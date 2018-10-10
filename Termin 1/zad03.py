def fibonacci(n):
    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a


for i in range(0, 21):
    print("Fibonacci %2d: %4d" % (i, fibonacci(i)))
