# -*- coding: utf-8 -*-

#%%
"""
а) Направити генератор свих могућих корисничких лозинки од задате дужине до 
задате дужине, састављених од прослеђене азбуке (азбука се задаје као стринг). 
За лакше генерисање комбинација дозвољено је користити itertools.product 
(проучити).
"""
#%%
def gen(poc, kraj, azbuka):
    from itertools import product
    for duzina in range(poc, kraj+1):
        for t in product(azbuka, repeat=duzina):
            yield ''.join(t)

#for rec in gen(2, 3, 'abc'):
#    print(rec)

#%%
"""
б) Направити rainbow таблицу која за сваки хеш памти листу 
могућих лозинки. Нека обухвата све лозинке над азбуком 
великих и малих слова енглеског алфабета и цифара које 
су дужине од 1 до 3 (укључујући оба броја). Користити
hashlib.md5 објекте (проучити).
"""
#%%
rainbow = {}

from string import ascii_uppercase, ascii_lowercase, digits
azbuka = ''.join((ascii_uppercase, ascii_lowercase, digits))

import hashlib

for rec in gen(1, 3, azbuka):
    h = hashlib.md5(rec.encode()).hexdigest()
#    if h in rainbow:
#        rainbow[h].append(rec)
#    else:
#        rainbow[h] = [rec]
    rainbow.setdefault(h, []).append(rec)

#%%
"""
в) Искористити rainbow таблицу и за свако корисничко име из датотеке покушати 
декрипцију лозинке. Ако је лозинка откључана, исписати комбинацију корисничког 
имена и откључане лозинке у датотеци unlocked_passwords.txt, раздвојене табом,
за свако корисничко име у посебном реду. Ако се хеш слаже са више лозинки,
исписати сваку (раздвојене табовима у истом реду)
г) Пребројати колико је откључаних лозинки и исписати статус на стандардни излаз:
- укупан број лозинки у rainbow таблици
- укупан број откључаних лозинки из датотеке
- укупан број неоткључаних лозинки из датотеке
"""
#%%
fin = open('passwords.txt', 'r')
fout = open('unlocked_passwords.txt', 'w')

neotkljucane = 0
otkljucane = 0

for line in fin:
    sl = line.strip().split('\t')
    h = sl[1]
    if h in rainbow:
        otkljucane += 1
        lozinke = rainbow[h]
        fout.write('%s\t%s\n' % (sl[0], '\t'.join(lozinke)))
    else:
        neotkljucane += 1

fout.close()
fin.close()
print('Ukupan broj lozinki u rainbow:', len(rainbow))
print('Ukupan broj otkljucanih lozinki:', otkljucane)
print('Ukupan broj neotkljucanih lozinki:', neotkljucane)
#%%
"""
2.   	Направити структуру података (класу) вектор. 
Као аргументе у конструктору може да прими итерабилни 
објекат и тип података. Сви елементи у прослеђеном објекту
морају бити конвертибилни у прослеђени тип. Подржани типови 
су int и float. Ако се деси било каква грешка при валидацији,
баца се одговарајући изузетак.

а) сабирање (лево и десно асоцијативно - __radd__!) – сабирање 
може да се изврши или са вектором који је исте величине 
(када се елементи на одговарајућим индексима сабирају) или са
скаларом (када се исти број додаје сваком елементу)

б) множење (лево и десно асоцијативно) – такође може да се 
изврши или са вектором исте величине (када се елементи на 
одговарајућим индексима множе) или са скаларом (када се цео 
вектор множи тим бројем)

в) „матрично” множење (__matmul__) – могуће га је извести
само са вектором исте величине, а резултат је скалар који
се добије као скаларни производ вектора (тј. збир производа по
компонентама)
"""
#%%

class Vektor:
    def __init__(self, it, tp):
        if not tp in [int, float]:
            raise ValueError('Подржани типови су само int и float')
        self._z = tuple(tp(x) for x in it)
        self._t = tp
        
    def __add__(self, other):
        if not isinstance(other, (int, float, Vektor)):
            return NotImplemented
        if isinstance(other, Vektor) and len(other._z) != len(self._z):
            raise TypeError('Вектори морају бити исте дужине')
        if isinstance(other, Vektor):
            lst = [z1 + z2 for z1, z2 in zip(self._z, other._z)]
        else:
            lst = list(map(lambda x: x + other, self._z))
        tp = int
        if any(filter(lambda x: type(x) is float, lst)):
            tp = float
        return Vektor(lst, tp)
    
    __radd__ = __add__

    def __mul__(self, other):
        if not isinstance(other, (int, float, Vektor)):
            return NotImplemented
        if isinstance(other, Vektor) and len(other._z) != len(self._z):
            raise TypeError('Вектори морају бити исте дужине')
        if isinstance(other, Vektor):
            lst = [z1 * z2 for z1, z2 in zip(self._z, other._z)]
        else:
            lst = list(map(lambda x: x * other, self._z))
        tp = int
        if any(filter(lambda x: type(x) is float, lst)):
            tp = float
        return Vektor(lst, tp)
        
    __rmul__ = __mul__
    
    def __matmul__(self, other):
        if not isinstance(other, Vektor):
            return NotImplemented
        if len(other._z) != len(self._z):
            raise TypeError('Вектори морају бити исте дужине')
        lst = [z1 * z2 for z1, z2 in zip(self._z, other._z)]
        return sum(lst)

    def __str__(self):
        return f'v{self._z}'
    
    __repr__ = __str__

    def __len__(self):
        return len(self._z)

