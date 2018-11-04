"""
class MojBroj:
    broj = 42

    def __init__(self, *args):
        if len(args) > 0:
            self.broj = args[0]
        print(getattr(self, 'broj', None) == MojBroj.broj)

class MB2(MojBroj):
    pass

print(MojBroj.broj)

broj_klasni = MojBroj()
print(broj_klasni.broj)

broj_obj_1 = MB2(5)
print(broj_obj_1.broj)

broj_obj_2 = MojBroj()
print(broj_obj_2.broj)
broj_obj_2.broj = 16
print(broj_obj_2.broj)

print(MojBroj.broj)
MojBroj.broj = 50

print(broj_klasni.broj)
print(broj_obj_1.broj)
print(broj_obj_2.broj)

print(type(broj_obj_1) == MojBroj)
print(isinstance(broj_obj_1, (MojBroj, list, int)))
"""
"""
class Test:
    def test(self):
        print('Test ok')

    def __setattr__(self, name, value):
        a = getattr(self, name, None)
        if a and callable(a):
            print('Nije uspelo')
        else:
            super().__setattr__(name, value)
            print('Setovano %s = %s' % (name, repr(value)))

t = Test()
t.test()
t.test = 'sta god'
t.test()
t.atr = 'vrednost'
"""
"""
import json


def jsonify(f):
    def wrap(*args, **kw):
        x = f(*args, **kw)
        return json.dumps(x)

    return wrap

@jsonify
def obj(**kw):
    return kw

obj = jsonify(obj)

print(repr(obj(a=2, b=3, c=4)))
"""

def param_dec(param1, param2):
    def dec(f):
        def wrap(*args, **kw):
            print('Parametri: ', param1, param2)
            return f(*args, **kw)
        return wrap
    return dec

@param_dec(10, 20)
def a(x):
    return x**3

print(a(12))
