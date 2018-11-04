"""
class svaki_drugi:
    def __init__(self, m, n):
        self._a = m - 1
        self._m = m
        self._n = n

    def __iter__(self):
        return svaki_drugi(self._m, self._n)

    def __next__(self):
        self._a += 2
        if self._a <= self._n:
            return self._a
        else:
            self._a = self._m - 1
            raise StopIteration

#s = svaki_drugi(1, 10)
#print(s)
"""
"""
if __name__== '__main__':
    d = {}
    rec = input()
    for slovo in set(rec):
        d[slovo] = rec.count(slovo)
    items = sorted(d.items(), key=lambda x: x[1])
    rez = ''.join((i[0] for i in items))
    print(rez)
"""
"""
def zbir(x, y):
    return x + y

l1 = [1, 3, 5, 7]
l2 = [2, 4, 6]
for rez in map(zbir, l1, l2):
    print(rez)

"""

"""
Написати генератор простих бројева из неког интервала.
Генератор треба да прима почетак и крај као опционе аргументе
и да има следеће понашање:
Ако није прослеђен ниједан аргумент, генератор генерише
све просте бројеве од 2 до бесконачности
Ако је прослеђен један аргумент, генератор генерише
све просте бројеве од 2 до тог броја
Ако су прослеђена два аргумента, генератор генерише
све просте бројеве од првог до другог.
Ако прослеђени аргументи нису цели или реални бројеви,
бацити TypeError изузетак са поруком о грешци.
Ако су реални бројеви, заокружити их на први ближи
цео број и тако их користити.
"""
def prosti(pocetak=None, kraj=None):
    if pocetak is None and kraj is None:
        pocetak = 2
    elif kraj is None:
        kraj = pocetak
        pocetak = 2
    elif pocetak is None:
        pocetak = 2

    if not isinstance(pocetak, (int, float)):
        raise TypeError('Pogresan tip argumenta pocetak: %s' % repr(pocetak))
    if not isinstance(pocetak, (int, float, type(None))):
        raise TypeError('Pogresan tip argumenta kraj: %s' % repr(kraj))

    pocetak = round(pocetak)
    if kraj:
        kraj = round(kraj)
    
    br = pocetak
    while kraj is None or br <= kraj:
        delilac = 2
        while delilac*delilac <= br:
            if br % delilac == 0:
                break
            delilac += 1
        else:
            yield br
        br += 1

def log_exc(f):
    def wrap(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as ex:
            ff = open('error_log.txt', 'a')
#            ff.write('%s: %s\n' % (type(ex).__name__, str(ex)))
            ff.write(f'{type(ex).__name__}: {ex}\n')
            ff.close()
            raise ex
    return wrap

@log_exc
def deljenje(a, b):
    return a / b
