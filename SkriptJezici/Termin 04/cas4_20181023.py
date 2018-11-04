# obican generator
def svaki_drugi(m, n):
    a = m + 1
    while a <= n:
        yield a
        a += 2


def zbir(a, b):
    return a + b

l1 = [1, 5, 2, 7, 8]
l2 = [2, 4, 6]

rez = tuple(map(zbir, l1, l2))
print(rez)


def prosti(pocetak=None, kraj=None):
    if pocetak is None and kraj is None:
        pocetak = 2
    elif pocetak is None:
        pocetak = 2
    elif kraj is None:
        kraj = pocetak
        pocetak = 2

    if not isinstance(pocetak, (int, float)):
        raise TypeError('Pogresan tip argumenta pocetak: %s'% repr(pocetak))
    if kraj is not None and not isinstance(kraj, (int, float)):
        raise TypeError('Pogresan tip argumenta kraj: %s'% repr(kraj))

    if type(pocetak) is float:
        pocetak = round(pocetak)
    if kraj is not None:
        kraj = round(kraj)

    broj = pocetak
    while kraj is None or broj <= kraj:
        delilac = 2
        while delilac*delilac <= broj:
            if broj % delilac == 0:
                break
            delilac += 1
        else:
            # broj je prost jer smo prosli sve delioce
            yield broj
        broj += 1

