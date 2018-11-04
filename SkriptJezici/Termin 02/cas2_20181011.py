"""
f = open('test_izlaz.txt', 'w')
f.write('Prva linija\nDruga linija')
print('\nTreca linija', file=f)
f.close()
"""
"""
f = open('test_izlaz.txt', 'r')
s = f.readline()
print(s, end='')

for linija in f:
    print(linija, end='')

f.close()
"""
"""
#1.
s1 = input()
s2 = input()
set1 = set(s1)
set2 = set(s2)
print('Sva slova koja se pojavljuju bar jednom u oba:', set1.intersection(set2))
print('Svi karakteri koji se pojavljuju u prvom stringu, a ne pojavljuju u drugom:', set1.difference(set2))

slova = set1.intersection(set2)
d = {}
for slovo in slova:
    if s1.count(slovo) == s2.count(slovo):
        d[slovo] = s1.count(slovo)
print('Svi karakteri koji se jednak broj puta pojavljuju u oba stringa:', d)

slova = set1.union(set2)
d.clear()
for slovo in slova:
    if s1.count(slovo) != s2.count(slovo):
        d[slovo] = (s1.count(slovo), s2.count(slovo))
print('Svi karakteri koji se različit broj puta pojavljuju u oba stringa:', d)
"""

#2.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a[1::2])
