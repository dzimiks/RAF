def remove_spaces(text):
    str = ''

    for c in text:
        if c != ' ':
            str += c

    return str


def group_str(text, n):
    str = ''
    i = 0

    for c in text:
        str += c

        if i % n == n - 1:
            str += ' '

        i += 1

    return str


def fun(text, n):
    text = remove_spaces(text)
    text = text.upper()
    text = group_str(text, n)
    return text


print(fun('Ovo je test primer za zadatak', 4))
