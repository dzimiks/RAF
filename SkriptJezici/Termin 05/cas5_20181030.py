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
Има методу keys(reverse=False), која враћа н-торку кључева у сортираном
поретку, а ако јој се проследи True као аргумент, враћа је сортирану у
обрнутом поретку.
"""
#%%

class SortedDictIterator:
    def __init__(self, d):
        self._d = d
        self._i = -1
        
    def __next__(self):
        self._i += 1
        if self._i < len(self._d._k):
            k = sorted(zip(self._d._k, self._d._v), key=lambda x: x[0])
            return k[self._i]
        else:
            self._i = -1
            raise StopIteration

class SortedDict:

    def __init__(self):
        self._k = []
        self._v = []

    def __setitem__(self, key, value):
        if not isinstance(key, (int, float)):
            raise TypeError('Nepodržani tip ključa %s' % type(key))
        
        if key in self._k:
            index = self._k.index(key)
            self._v[index] = value
        else:
            self._k.append(key)
            self._v.append(value)
    
    def __getitem__(self, key):
        try:
            return self._v[self._k.index(key)]
        except:
            raise KeyError('Nepoznati ključ %s' % key)
    
    def __iter__(self):
        return SortedDictIterator(self)
    
    def keys(self, reverse=False):
        return tuple(sorted(self._k, reverse=reverse))

#%%
"""
Направити декоратор log_exc за обраду изузетака. Декоратор треба 
да хвата изузетак из декорисане методе, додаје га у датотеку 
error_log.txt и затим баца исти изузетак у спољашњи контекст.
"""

def log_exc(f):
    def wrap(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as e:
            with open('error_log.txt', 'a') as fi:
                fi.write(f'{type(e).__name__}: {e}\n')
            raise e

    return wrap

@log_exc
def deljenje(x, y):
    return x / y

#%%
"""
 1.   	Дата је датотека са корисничким именима и лозинкама, таква
 да је у сваком реду један запис. Корисничка имена и лозинке су
 раздвојене табом, корисничко име не садржи специјалне карактере.
 Лозинке су записане као md5 хешеви стрингова (лозинки) кодираних 
 у UTF-8 (подразумевано кодовање стрингова), записаних као hex
 digest. Датотека се зове passwords.txt.

а) Направити генератор свих могућих корисничких лозинки од задате 
    дужине до задате дужине, састављених од прослеђене азбуке 
    (азбука се задаје као стринг). За лакше генерисање комбинација 
    дозвољено је користити itertools.product (проучити).
б) Направити rainbow таблицу која за сваки хеш памти листу могућих 
    лозинки. Нека обухвата све лозинке над азбуком великих и малих 
    слова енглеског алфабета и цифара које су дужине од 1 до 3 
    (укључујући оба броја). Користити hashlib.md5 објекте (проучити).
в) Искористити rainbow таблицу и за свако корисничко име из датотеке
    покушати декрипцију лозинке. Ако је лозинка откључана, исписати 
    комбинацију корисничког имена и откључане лозинке у датотеци
    unlocked_passwords.txt, раздвојене табом, за свако корисничко
    име у посебном реду. Ако се хеш слаже са више лозинки, исписати
    сваку (раздвојене табовима у истом реду)
г) Пребројати колико је откључаних лозинки и исписати статус на 
    стандардни излаз:
- укупан број лозинки у rainbow таблици
- укупан број откључаних лозинки из датотеке
- укупан број неоткључаних лозинки из датотеке

Датотека passwords.txt је приложена уз материјале.
"""

def kombinacije(pocetak, kraj, azbuka):
    import itertools
    for i in range(pocetak, kraj+1):
        for t in itertools.product(azbuka, repeat=i):
            yield ''.join(t)

rainbow = {}

import hashlib
from string import ascii_uppercase, ascii_lowercase, digits

alfa = ascii_uppercase + ascii_lowercase + digits

for rec in kombinacije(1, 3, alfa):
    h = hashlib.md5(rec.encode()).hexdigest()
    rainbow.setdefault(h, []).append(rec)

otkljucano = 0
ukupno = 0

with open('passwords.txt') as fin, open('unlocked_passwords.txt', 'w') as fout:
    for line in fin:
        ukupno += 1
        user, password = line.strip().split('\t')
        if password in rainbow:
            fout.write('%s\t%s\n' % (user, '\t'.join(rainbow[password])))
            otkljucano += 1

print('Broj hasheva:', len(rainbow))
print('Broj otkljucanih:', otkljucano)
print('Preostalo:', ukupno - otkljucano)

