"""
f = open('izlaz_test.txt','w')

f.write('Prva linija\nDruga linija')
print('\nTreca linija', file=f)

f.close()
"""
"""
f = open('izlaz_test.txt','r')
linija = f.readline()
print(linija.strip())

for linija in f:
    print(linija, end='')

f.close()
"""
"""
a = 20
b = 30.3

s1 = '{0}, {1}'
s2 = f'{a}, {b}'

print(s1.format(a, b))
print(s2)

a = 40

print(s1.format(a, b))
print(s2)
"""
"""
def f(y, *args, z=30, **kw):
    print('y=',y)
    print(args)
    print('z=',z)
    print(kw)

f(15, 50, 20, 40, z=14, a=10)
"""
#4.
'''
4. Napisati program koji čita string sa standardnog ulaza i prebrojava i
ispisuje sve karaktere sortirano u rastućem poretku:
a. Sa dozvoljenim ponavljanjima
b. Bez ponavljanja (svaki karakter po jednom, koliko god puta da se pojavljuju)
'''
s = input()
#a
slova = set(s)
d = {}
for slovo in slova:
    d[slovo] = s.count(slovo)

def kljuc(slovo):
    return d[slovo]

def kljuc2(par):
    return par[1]

#lista = list(slova)
lista = list(d.items())
#lista.sort(key=kljuc)
lista.sort(key=kljuc2)
print(lista)
