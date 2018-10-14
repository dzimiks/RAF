def fun(filename, word):
    with open(filename) as file:
        for line in file:
            for w in line:
                if w == word:
                    return True
    return False


print(fun('12.txt', 'word'))
