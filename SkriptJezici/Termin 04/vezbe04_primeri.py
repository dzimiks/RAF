# -*- coding: utf-8 -*-
"""
Написати генератор простих бројева из неког интервала. Генератор треба да прима почетак и крај
као опционе аргументе и да има следеће понашање:
Ако није прослеђен ниједан аргумент, генератор генерише све просте бројеве од 2 до бесконачности
Ако је прослеђен један аргумент, генератор генерише све просте бројеве од 2 до тог броја
Ако су прослеђена два аргумента, генератор генерише све просте бројеве од првог до другог.
Ако прослеђени аргументи нису цели или реални бројеви, бацити TypeError изузетак са поруком о грешци.
Ако су реални бројеви, заокружити их на први ближи цео број и тако их користити.
"""
def prosti2(pocetak=None, kraj=None):
    if pocetak is None and kraj is None:
        pocetak = 2
    elif kraj is None:
        kraj = pocetak
        pocetak = 2
    elif pocetak is None and kraj is not None:
        pocetak = 2

    if not isinstance(pocetak, (int, float)) \
        or (kraj is not None and not isinstance(kraj, (int, float))): 
        raise TypeError('Pogresni argumenti %s i %s' % (repr(pocetak), repr(kraj)))

    if type(pocetak) is float:
        pocetak = round(pocetak)
    if type(kraj) is float:
        kraj = round(kraj)

    broj = pocetak
    while kraj is None or broj <= kraj:
        # da li je broj prost
        prost = True
        delilac = 2
        while delilac * delilac <= broj:
            if broj % delilac == 0:
                prost = False
                break
            delilac += 1
        # ako jeste vrati ga
        if prost:
            yield broj
        # predji na sledeci broj
        broj += 1

# obican generator prostih brojeva

def prosti(n=None):
    broj = 2
    while n is None or broj <= n:
        # da li je broj prost
        prost = True
        delilac = 2
        while delilac * delilac <= broj:
            if broj % delilac == 0:
                prost = False
                break
            delilac += 1
        # ako jeste vrati ga
        if prost:
            yield broj
        # predji na sledeci broj
        broj += 1

"""
Написати класу SortedDict која има следећа својства:
- Наслеђује object (тј. не наслеђује ниједну колекцију)
- У својој имплементацији не сме да користи dict, ни било коју сличну “мапу”
- Подржава индексирање на следећи начин: може да се ради додела и читање са одређеног кључа;
ако кључ не постоји у колекцији а покушано је читање, баца KeyError;
ако је кључ у колекцији, придружује му нову вредност.
Сви кључеви морају бити цели или реални бројеви - у случају да је покушано нешто друго, баца TypeError.
- Подржава итерацију тако да се враћају парови (кључ, вредност) у сортираном поретку по кључу;
за ову потребу направити интерну класу SortedDictIterator
- Има методу keys(reverse=False), која враћа н-торку кључева у сортираном поретку, а ако јој се
проследи True као аргумент, враћа је сортирану у обрнутом поретку.
"""
def find(self, obj):
    if obj in self:
        return self.index(obj)
    else:
        return -1

class SortedDictIterator:
    def __init__(self, d):
        self._parovi = zip(d._kljucevi, d._vrednosti)
        self._parovi = sorted(self._parovi, key=lambda x: x[0])
        self._index = -1
        
    def __next__(self):
        self._index += 1
        if self._index < len(self._parovi):
            return self._parovi[self._index]
        else:
            self._index = -1
            raise StopIteration

class SortedDict:
    def __init__(self):
        self._kljucevi = []
        self._vrednosti = []

    def __setitem__(self, key, value):
        if not isinstance(key, (float, int)):
            raise TypeError('Nepodrzan kljuc %s' % repr(key))
        index = find(self._kljucevi, key)
        if index == -1:
            self._kljucevi.append(key)
            self._vrednosti.append(value)
        else:
            self._vrednosti[index] = value

    def __getitem__(self, key):
        if not isinstance(key, (float, int)):
            raise TypeError('Nepodrzan kljuc %s' % repr(key))
        index = find(self._kljucevi, key)
        if index == -1:
            raise KeyError('Nepostojeci kljuc %s' % key)
        else:
            return self._vrednosti[index]

    def __iter__(self):
        return SortedDictIterator(self)

    def keys(self, reverse=False):
        return tuple(sorted(self._kljucevi, reverse=reverse))

