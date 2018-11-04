"""
Написати генератор простих бројева из неког интервала.
Генератор треба да прима почетак и крај као опционе
аргументе и да има следеће понашање:
Ако није прослеђен ниједан аргумент, генератор генерише
све просте бројеве од 2 до бесконачности
Ако је прослеђен један аргумент, генератор генерише
све просте бројеве од 2 до тог броја
Ако су прослеђена два аргумента, генератор генерише
све просте бројеве од првог до другог. Ако прослеђени
аргументи нису цели или реални бројеви, бацити TypeError
изузетак са поруком о грешци. Ако су реални бројеви,
заокружити их на први ближи цео број и тако их користити.
"""

def tipovi(*targs, allow_null=False):
    def dec(f):
        def wrap(*args):
#            if len(args) != len(targs):
#                raise ValueError('Pogresan broj argumenata')
            for arg, t in zip(args, targs):
                if allow_null and arg is None:
                    continue
                if not isinstance(arg, t):
                    raise TypeError(f'Pogresan tip argumenta {arg!r}, ocekivano {t}')
            return f(*args)
        return wrap
    return dec

@tipovi((int, float), (int, float), allow_null=True)
def prosti(pocetak=None, kraj=None):
    if pocetak is None and kraj is None:
        pocetak = 2
    elif kraj is None:
        kraj = pocetak
        pocetak = 2
    elif pocetak is None:
        pocetak = 2
    """
    if not isinstance(pocetak, (float, int)):
        raise TypeError('Pogresan tip argumenta pocetak: %s' % repr(pocetak))
    if kraj is not None and not isinstance(kraj, (float, int)):
        raise TypeError('Pogresan tip argumenta kraj: %s' % repr(kraj))
    """
    pocetak = round(pocetak)
    if kraj:
        kraj = round(kraj)
    
    br = pocetak
    while kraj is None or br <= kraj:
        delilac = 2
        while delilac * delilac <= br:
            if br % delilac == 0:
                break
            delilac += 1
        else:
            yield br
        br += 1
        


    
