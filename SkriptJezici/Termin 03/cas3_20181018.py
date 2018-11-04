"""
class Test:
    def __init__(self, poruka):
        self._poruka = poruka

    def test(self):
        print('Test:', self._poruka)

class B(Test):
    pass
#    def test(self):
#        print('B:', self._poruka)
#        super().test()

class MojTest(Test):
    def test(self):
        print('MojTest:', self._poruka)
        super().test()

class UltimateTest(MojTest, B):
    def test(self):
        print('UltimateTest:', self._poruka)
        super().test()

b = B('b')
m = MojTest('m')
u = UltimateTest('u')

b.test()
#m.test()
u.test()
"""

while True:
    try:
        vrednost = int(input('Vrednost: '))
        print(2 / vrednost)
        break
    except (ValueError, ArithmeticError) as e:
        print('Izuzetak:', e)
    except KeyboardInterrupt:
        print('Dobar pokusaj :P')
        
        
