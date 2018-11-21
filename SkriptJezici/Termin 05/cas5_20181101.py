# -*- coding: utf-8 -*-

"""
Написати класу SortedDict која има следећа својства:
Наслеђује object (тј. не наслеђује ниједну колекцију)
У својој имплементацији не сме да користи dict, ни било коју сличну “мапу”
Подржава индексирање на следећи начин: може да се ради додела и читање са 
одређеног кључа; ако кључ не постоји у колекцији а покушано је читање, баца 
KeyError; ако је кључ у колекцији, придружује му нову вредност. Сви кључеви 
морају бити цели или реални бројеви - у случају да је покушано нешто друго, 
баца TypeError.
Подржава итерацију тако да се враћају парови (кључ, вредност) у сортираном 
поретку по кључу; за ову потребу направити интерну класу SortedDictIterator
Има методу keys(reverse=False), која враћа н-торку кључева у сортираном поретку,
а ако јој се проследи True као аргумент, враћа је сортирану у обрнутом поретку.
"""
#%%

class SortedDictIterator:
    def __init__(self, d):
        self._l = d._l
        self._i = -1
    
    def __next__(self):
        self._i += 1
        if self._i < len(self._l):
            s = sorted(self._l)
            return s[self._i]
        else:
            self._i = -1
            raise StopIteration

class SortedDict:
    def __init__(self):
        self._l = []
    
    def __setitem__(self, key, value):
        if not isinstance(key, (int, float)):
            raise TypeError('Nekompatibilan ključ %s' % repr(key))
        for i, t in enumerate(self._l):
            if t[0] == key:
                self._l[i] = (key, value)
                return
        self._l.append((key, value))
    
    def __getitem__(self, key):
        if not isinstance(key, (int, float)):
            raise TypeError('Nekompatibilan ključ %s' % repr(key))
        for k, v in self._l:
            if k == key:
                return v
        raise KeyError('Nepostojeći ključ %s' % repr(key))
    
    def __iter__(self):
        return SortedDictIterator(self)

    def keys(self, reverse=False):
        return tuple(sorted((k for k, v in self._l), reverse=reverse))
    
    def __str__(self):
        return 'SD%s' % str(self._l)
    
    __repr__ = __str__

#%%
"""
Направити декоратор log_exc за обраду изузетака. 
Декоратор треба да хвата изузетак из декорисане методе, додаје га у датотеку 
error_log.txt и затим баца исти изузетак у спољашњи контекст.    
"""
#%%

def log_exc(f):
    def wrap(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as e:
            fin = open('error_log.txt', 'a')
            fin.write('%s: %s\n' % (type(e).__name__, e))
            fin.close()
            raise e
    return wrap

@log_exc
def podeli(x, y):
    return x / y

#%%
"""
а) Направити генератор свих могућих корисничких лозинки од задате дужине 
    до задате дужине, састављених од прослеђене азбуке (азбука се задаје 
    као стринг). За лакше генерисање комбинација дозвољено је користити 
    itertools.product (проучити).
"""
def gen(poc, kraj, azbuka):
    import itertools
    for i in range(poc, kraj+1):
        for t in itertools.product(azbuka, repeat=i):
            yield ''.join(t)

#%%
"""
б) Направити rainbow таблицу која за сваки хеш памти листу могућих лозинки. 
Нека обухвата све лозинке над азбуком великих и малих слова енглеског алфабета 
и цифара које су дужине од 1 до 3 (укључујући оба броја). Користити hashlib.md5 
објекте (проучити).
"""
rainbow = {}

from string import digits, ascii_uppercase, ascii_lowercase
azbuka = digits + ascii_uppercase + ascii_lowercase

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

fin = open('passwords.txt')
fout = open('unlocked_passwords.txt', 'w')

ukupno = len(rainbow)
otklj = 0
neotklj = 0

for red in fin:
    un, pw = red.strip().split('\t')    
    if pw in rainbow:
        otklj += 1
        fout.write('%s\t%s\n' % (un, '\t'.join(rainbow[pw])))
    else:
        neotklj += 1

fin.close()
fout.close()

print('Veličina rainbow tablice: %d' % ukupno)
print('Otključanih: %d' % otklj)
print('Neotključanih: %d' % neotklj)


#%%

class MojBroj:
    def __init__(self, br):
        self._br = br
        self._i = 0
    
    def __add__(self, other):
        print('__add__', self._i)
        return self._br + other
    
    __radd__ = __add__
    
    def __matmul__(self, other):
        return self._br ** other._br
#    def __radd__(self, other):
#        self._i += 1
#        print('__radd__', self._i)

