def prime(num):
    if num == 2:
        return True

    if num == 1 or num % 2 == 0:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def fun(arr):
    file = open('res.txt', 'w')

    for i in arr:
        if prime(i):
            file.write(str(i) + '\n')

    file.close()


with open('11.txt') as f:
    arr = [int(x) for x in next(f).split()]

print(arr)
fun(arr)
