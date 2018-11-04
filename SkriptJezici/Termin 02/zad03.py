string = input('Enter a string: ')
counts = {i: 0 for i in 'aeiouAEIOU'}

for char in string:
    if char in counts:
        counts[char] += 1

for k, v in counts.items():
    print('%c: %d' % (k, v))
