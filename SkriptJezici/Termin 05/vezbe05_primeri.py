""" # passwords.txt generator
import hashlib
from string import ascii_uppercase, ascii_lowercase, digits
import random

alfa = ascii_uppercase + ascii_lowercase + digits
with open('passwords.txt', 'w') as f:
    for i in range(300):
        username = ''.join((random.choice(alfa) for _ in range(random.randint(5,10))))
        password = ''.join((random.choice(alfa) for _ in range(random.randint(2, 6))))
        h = hashlib.md5(password.encode()).hexdigest()
        f.write(f'{username}\t{h}\n')
"""



"""
Направити декоратор log_exc за обраду изузетака. Декоратор треба да хвата
изузетак из декорисане методе, додаје га у датотеку error_log.txt и затим
баца исти изузетак у спољашњи контекст.
"""
def log_exc(f):
    def dekorisi(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as e:
            log = open('error_log.txt', 'a')
            log.write(f'{type(e)}: {e}\n')
            log.close()
            raise e

    return dekorisi

@log_exc
def podeli(x, y):
    return x / y

#podeli(1, 0)

"""
 1.   	Дата је датотека са корисничким именима и лозинкама, таква да је у
 сваком реду један запис. Корисничка имена и лозинке су раздвојене табом,
 корисничко име не садржи специјалне карактере. Лозинке су записане као md5
 хешеви стрингова (лозинки) кодираних у UTF-8 (подразумевано кодовање стрингова),
 записаних као hex digest. Датотека се зове passwords.txt.

а) Направити генератор свих могућих корисничких лозинки од задате дужине до
задате дужине, састављених од прослеђене азбуке (азбука се задаје као стринг).
За лакше генерисање комбинација дозвољено је користити itertools.product
(проучити).
б) Направити rainbow таблицу која за сваки хеш памти листу могућих лозинки.
Нека обухвата све лозинке над азбуком великих и малих слова енглеског алфабета
и цифара које су дужине од 1 до 3 (укључујући оба броја).
Користити hashlib.md5 објекте (проучити).
в) Искористити rainbow таблицу и за свако корисничко име из датотеке покушати
декрипцију лозинке. Ако је лозинка откључана, исписати комбинацију корисничког
имена и откључане лозинке у датотеци unlocked_passwords.txt, раздвојене табом,
за свако корисничко име у посебном реду. Ако се хеш слаже са више лозинки,
исписати сваку (раздвојене табовима у истом реду)
г) Пребројати колико је откључаних лозинки и исписати статус на стандардни
излаз:
- укупан број лозинки у rainbow таблици
- укупан број откључаних лозинки из датотеке
- укупан број неоткључаних лозинки из датотеке

Датотека passwords.txt је приложена уз материјале.
"""
"""
import hashlib
from string import ascii_uppercase, ascii_lowercase, digits
alfabet = ascii_uppercase + ascii_lowercase + digits

def kombinacije(poc, kraj, azbuka):
    import itertools
    for duzina in range(poc, kraj + 1):
        for t in itertools.product(azbuka, repeat=duzina):
            yield ''.join(t)

rainbow = {}
for z in kombinacije(1, 3, alfabet):
    h = hashlib.md5(z.encode()).hexdigest()
    if h in rainbow:
        rainbow[h].append(z)
    else:
        rainbow[h] = [z]

    # rainbow.setdefault(h, []).append(z)

fin = open('passwords.txt')
fout = open('unlocked_passwords.txt', 'w')

ukupno = 0
nadjeno = 0

for line in fin:
    ukupno += 1
    username, password = line.strip().split('\t')
    if password in rainbow:
        nadjeno += 1
        f = "\t".join(rainbow[password])
        fout.write(f'{username}\t{f}\n')

fin.close()
fout.close()

print(f'Velicina tablice: {len(rainbow)}')
print(f'Otkljucano: {nadjeno}')
print(f'Preostalo: {ukupno-nadjeno}')
"""

"""
2.   	Направити структуру података (класу) вектор. Као аргументе у конструктору
може да прими итерабилни објекат и тип података. Сви елементи у прослеђеном објекту
морају бити конвертибилни у прослеђени тип. Подржани типови су int и float. Ако
се деси било каква грешка при валидацији, баца се одговарајући изузетак.

Класа треба да имплементира следећа понашања:
а) сабирање (лево и десно асоцијативно - __radd__!) – сабирање може да се
изврши или са вектором који је исте величине (када се елементи на одговарајућим
индексима сабирају) или са скаларом (када се исти број додаје сваком елементу)
б) множење (лево и десно асоцијативно) – такође може да се изврши или са вектором
исте величине (када се елементи на одговарајућим индексима множе) или са скаларом
(када се цео вектор множи тим бројем)
в) „матрично” множење (__mmul__) – могуће га је извести само са вектором исте
величине, а резултат је скалар који се добије скаларни производ вектора (тј.
збир производа по компонентама)

Направити две инстанце вектора (нпр. [1, 3, 5], [2, 4, 6]) и демонстрирати
свих 5 операција у главном програму, користећи операторе +, * и @.
"""

class vektor:
    def __init__(self, it, tip):
        self._kol = tuple(map(tip, it))
        self._tip = tip

    def __len__(self):
        return len(self._kol)

    def __add__(self, other):
        if isinstance(other, vektor):
            if len(self) != len(other):
                raise ValueError('Nisu iste duzine')
            return vektor(map(lambda x, y: x + y, self._kol, other._kol), self._tip)
        else:
            if isinstance(other, (int, float)):
                other = self._tip(other)
                return vektor(map(lambda x: x + other, self._kol), self._tip)
        return NotImplemented

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, vektor):
            if len(self) != len(other):
                raise ValueError('Nisu iste duzine')
            return vektor(map(lambda x, y: x * y, self._kol, other._kol), self._tip)
        else:
            if isinstance(other, (int, float)):
                other = self._tip(other)
                return vektor(map(lambda x: x * other, self._kol), self._tip)
        return NotImplemented

    __rmul__ = __mul__

    def __matmul__(self, other):
        if isinstance(other, vektor):
            if len(self) != len(other):
                raise ValueError('Nisu iste duzine')
            return sum(map(lambda x, y: x * y, self._kol, other._kol))
        return NotImplemented

    def __str__(self):
        return '[%s]' % ' '.join(map(str, self._kol))

    __repr__ = __str__

def intvektor(kol):
    return vektor(kol, int)

def floatvektor(kol):
    return vektor(kol, float)

