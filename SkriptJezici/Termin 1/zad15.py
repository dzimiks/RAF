string = 'dzimiks'
st = ''

for s in string:
    st += str(ord(s)) + ', '
    # print(ord(s), ', ', end='')

print(st[:len(st) - 2], end='')
