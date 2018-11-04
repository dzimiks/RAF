"""
f = open('izlaz.txt', 'w')
f.write('Prva linija\nDruga linija')
print('\nTreca linija', file=f)
f.close()

"""
"""
f = open('izlaz.txt')
for line in f:
    print(line, end='')
f.close()
"""
"""
f = 'nesto'
s = f'{s}'
print(s)
"""
"""
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

with open('test1.txt') as f:
    for linija in f:
        br = 0
        for c in linija.strip():
            if prime(int(c)):
                print(c)
"""
"""
#1.
#a)
s1 = input()
s2 = input()

set1 = set(s1)
set2 = set(s2)

print('Slova u oba stringa:', set1.intersection(set2))

#b)
print('Slova u prvom stringu a nisu u drugom:', set1.difference(set2))

#c)
d = {}
presek = set1.intersection(set2)
for slovo in presek:
    if s1.count(slovo) == s2.count(slovo):
        d[slovo] = s1.count(slovo)
print('Slova koja se pojavljuju jednak broj puta u oba:', d)

#d)
d.clear()
unija = set1.union(set2)
for slovo in unija:
    if s1.count(slovo) != s2.count(slovo):
        d[slovo] = (s1.count(slovo), s2.count(slovo))
print('Slova koja se pojavljuju razlicit broj puta u oba:', d)
"""
"""
#2.

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
print(a[1::2])
"""
d = {}
s = input().upper()
#d['A'] = s.count('A')
#d['E'] = s.count('E')
#d['I'] = s.count('I')
#d['O'] = s.count('O')
#d['U'] = s.count('U')

for slovo in s:
    for k in 'AEIOU':
        if slovo == k:
            d[k] = 1 if k not in d else d[k] + 1

print(d)


