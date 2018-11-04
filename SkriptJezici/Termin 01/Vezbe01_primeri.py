"""
a = int(input('Unesite ceo broj: '))
b = input()
c = eval(input('Unesite izraz: '))
print('a =', a)
print('b =', b)
print('c =', c)
"""

"""
# ispis brojeva od 1 do x
x = int(input('Unesite broj: '))
for i in range(1, x+1):
    print(i)
"""

"""
# zbir cifara unetog broja
x = int(input('Unesite broj: '))
y = x
zbir = 0
while x > 0:
    zbir += x % 10
    x = x // 10
print('Zbir cifara %d je %d' % (y, zbir))

"""

"""
def zbir_u_range(start, end):
    " Zbir svih brojeva od start do end"
    s = 0
    for i in range(start, end):
        s += i
    return s

print(zbir_u_range(1, 101))
print(zbir_u_range(1, 11))
"""
"""
def fibonaci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    a = 1
    b = 1
    for i in range(3, n+1):
        c = a + b
#        a = b
#        b = c
        a, b = b, c
    return c

for i in range(1, 6):
    print(fibonaci(i))
"""
"""
zbir = 0
broj = 0

while zbir <= 100:
    x = float(input())
    zbir += x
    broj += 1
else:
    print('Zbir unetih %d brojeva je %.2f' % (broj, zbir))

"""

s = input()
n= len(s)
for i in range(1, n+1):
    print(s[:i])

