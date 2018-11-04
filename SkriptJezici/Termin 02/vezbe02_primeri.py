"""
f = open('test_out.txt', 'w')
f.write('Prva linija\nDruga linija')
print('\nTreca linija', file=f)
f.close()
"""

"""
f = open('test_out.txt', 'r')
for line in f:
    print(line, end='')
f.close()
"""
"""
a = 20
b = 13.4278135
c = 'FIN'
s = '{0}, {1:<7.3f}, {2}'.format(a, b, c)
print(s)

s2 = f'{a}, {a+b:<7.3f}, {c}'
print(s2)

"""
"""
def zbir(x, y):
    return x + y

l = [(1, 2), (3, 4), (5, 6)]
for par in l:
    rezultat = zbir(*par)
    print(f'{par[0]} + {par[1]} = {rezultat}')

d = {'x': 12 , 'y': 13}
print(f'{d["x"]} + {d["y"]} = {zbir(**d)}')
"""
"""
from string import ascii_uppercase
from random import choice as izbor

for i in range(5):
    print(izbor(ascii_uppercase), end=', ')

print(__name__)

if __name__ == '__main__':
    print('Glavni program')

"""
"""
#1. 
s1 = input()
s2 = input()

print('Svi karakteri koji se pojavljuju u oba: ')
set1 = set(s1)
set2 = set(s2)
print(set1.intersection(set2))

print('Svi karakteri koji se pojavljuju u prvom stringu, a ne pojavljuju u drugom')
print(set1.difference(set2))

print('Svi karakteri koji se jednak broj puta pojavljuju u oba stringa – i koliko puta')
kljucevi = set1.intersection(set2)
brojevi = {}
for kljuc in kljucevi:
    if s1.count(kljuc) == s2.count(kljuc):
        brojevi[kljuc] = s1.count(kljuc)
print(brojevi)

print('Svi karakteri koji se različit broj puta pojavljuju u oba stringa – i koliko puta')
kljucevi = set1.union(set2)
brojevi.clear()
for kljuc in kljucevi:
    if s1.count(kljuc) != s2.count(kljuc):
        brojevi[kljuc] = (s1.count(kljuc), s2.count(kljuc))
print(brojevi)
"""
#2.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a[1::2])
