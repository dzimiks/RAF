"""while True:
    try:
        vrednost = int(input('Uneti vrednost: '))
        print( 2 / vrednost)
        break
    except Exception as e:
        print(f'Izuzetak {e}')
    except KeyboardInterrupt:
        print('Probajte ponovo!')
        
"""
"""
def f(a):
    try:
        return a / 0
    finally:
        print('finally')
        return 0
"""

def dek(f):
    def wrap(*args, **kw):
        print('Dekorisano')
        return f(*args, **kw)
    return wrap
@dek
def test():
    return 10

