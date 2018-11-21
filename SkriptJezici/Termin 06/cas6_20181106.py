# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:23:00 2018

@author: mtomic
"""

class Pekara:
    
    def __init__(self, naziv, lokacija):
        self.naziv = naziv
        self.lokacija = lokacija
        self._kasa = []
        self._proizvodi = {}

    def dodaj_proizvod(self, proizvod, kolicina):
        if isinstance(proizvod, Akcija):
            if len(proizvod._kombinacija) < 2:
                return False
        if proizvod in self:
            self._proizvodi[proizvod] += kolicina
        else:
            self._proizvodi[proizvod] = kolicina
        return True
            
    def __contains__(self, item):
        return item in self._proizvodi
    
    def proizvodi(self):
        f = filter(lambda x: not isinstance(x, Akcija), self._proizvodi)
        # [x for x in self._proizvodi if not isinstance(x, Akcija)]
        return tuple(sorted(f, key=lambda x : x.naziv))
        
    def akcije(self):
        f = filter(lambda x: isinstance(x, Akcija), self._proizvodi)
        return tuple(sorted(f, key=lambda x : x.naziv))
    
    def kupi(self, proizvod, kolicina):
        k = self._proizvodi.get(proizvod, 0)
        if k >= kolicina:
            self._proizvodi[proizvod] -= kolicina
            self._kasa.append((proizvod, kolicina))
            return True
        return False
    
    def izvestaj(self, kljuc=None):
        izv = {}
        for k, v in self._kasa:
            if k not in izv:
                izv[k] = v
            else:
                izv[k] += v
        t = ((p, k, p.cena*k) for p, k in izv.items())
        if kljuc is None:
            for z in sorted(t, key=lambda x: x[0].naziv):
                yield z
        elif kljuc == 'kolicina':
            for z in sorted(t, key=lambda x: -x[1]):
                yield z
        elif kljuc == 'zarada':
            for z in sorted(t, key=lambda x: -x[2]):
                yield z
    
    def ispis(self):
        with open('pekara.txt', 'w') as f:
            for p, k in self._kasa:
                f.write('%s, %d, %.2f\n' % (p, k, p.cena*k))
                
    def __len__(self):
        return len(self._kasa)

class Proizvod:
    
    def __init__(self, naziv, jm, cena):
        self.naziv = naziv
        self.jm = jm
        self.cena = cena
        
    def __eq__(self, other):
        if isinstance(other, Proizvod):
            return self.naziv == other.naziv
        return False
    
    def __hash__(self):
        return hash(self.naziv)

    def __str__(self):
        return f'{self.naziv} - {self.cena:.2f}'
    
    __repr__ = __str__


class Akcija(Proizvod):
    
    def __init__(self, naziv, cena):
        super().__init__(naziv, 'komad', cena)
        self._kombinacija = []
    
    def ubaci_proizvod(self, proizvod, kolicina):
        if not isinstance(proizvod, Akcija) and isinstance(proizvod, Proizvod):
            self._kombinacija.append((proizvod, kolicina))
            return True
        return False

    def __str__(self):
        p = ', '.join(['%d %s' % (x[1], x[0].naziv) for x in self._kombinacija])
        return f'{self.naziv} ({p}) - {self.cena:.2f}'

    __repr__ = __str__

 
if __name__ == '__main__':
    pekara = Pekara('Toma', 'Kolarceva X')
    proizvodi = [
            Proizvod('Pizza Rosa', 'parce', 120),
            Proizvod('Pizza Vulkan', 'parce', 180),
            Proizvod('Sendvic', 'komad', 160),
            Proizvod('Coca Cola', '0.5l', 80),
            Proizvod('Cokoladno mleko', '0.2l', 30),
    ]
    akcije = [
            Akcija('Rosa + Coca Cola', 170),
            Akcija('Vulkan + Coca Cola', 190)
    ]
    import random
    for p in proizvodi:
        pekara.dodaj_proizvod(p, random.randint(5, 20))
        
    akcije[0].ubaci_proizvod(proizvodi[0], 1)
    akcije[0].ubaci_proizvod(proizvodi[3], 1)

    akcije[1].ubaci_proizvod(proizvodi[1], 1)
    akcije[1].ubaci_proizvod(proizvodi[3], 1)

    for p in akcije:
        pekara.dodaj_proizvod(p, random.randint(5, 20))
    
    for i in range(10):
        p = random.choice(pekara.proizvodi() + pekara.akcije())
        r = random.randint(1, 3)
        if pekara.kupi(p, r):
            print('Kupljeno', p, ': ', r)
        else:
            print('Nije uspela kupovina', p, ': ', r)
    
    for i in pekara.izvestaj():
        print(i)
        
    pekara.ispis()