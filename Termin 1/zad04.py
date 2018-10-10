def max_of_three(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


def max_of_three_list(a, b, c):
    list = [a, b, c]
    return max(list)


print(max_of_three(10, 233, 33))
print(max_of_three_list(1032, 233, 33))
