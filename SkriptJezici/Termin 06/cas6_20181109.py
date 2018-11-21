# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:17:33 2018

@author: mtomic
"""

class File:
    def __init__(self, naziv, velicina, roditelj=None):
        if not isinstance(naziv, str):
            raise TypeError('Naziv treba da bude string')
        if not isinstance(velicina, int):
            raise TypeError('Velicina treba da bude ceo broj')
        if roditelj and not isinstance(roditelj, Folder):
            raise TypeError('Roditelj treba da bude folder')
        
        self.naziv = naziv
        self.velicina = velicina
        self.roditelj = roditelj
        if roditelj is not None:
            roditelj.kolekcija.append(self)
            
    def __len__(self):
        return self.velicina
    
    def __repr__(self):
        return self.naziv
    
    __str__ = __repr__

    def ls(self, *args):
        if 'f' not in args:
            yield self


class Folder(File):
    def __init__(self, naziv, roditelj=None):
        super().__init__(naziv, 4, roditelj)
        self.kolekcija = []
    
    def __len__(self):
        s = self.velicina
        for f in self.kolekcija:
            s += len(f)
        return s
    
    def ls(self, *args):
        rek = 'R' in args
        fol = 'f' in args
        rev = 'r' in args
        kljuc = None
        for arg in args[::-1]:
            if arg in ('n', 'v'):
                kljuc = arg
                break
        kolekcija = self.kolekcija
        if kljuc == 'n':
            kolekcija = sorted(kolekcija, key=lambda x: x.naziv, reverse=rev)
        if kljuc == 'v':
            kolekcija = sorted(kolekcija, key=lambda x: len(x), reverse=not rev)
        
        yield self
        for f in kolekcija:
            if rek:
                for ff in f.ls(*args):
                    yield ff
            else:
                if not fol or isinstance(f, Folder):
                    yield f

    
class Disk:
    def __init__(self, naziv, kapacitet, root):
        if not isinstance(naziv, str):
            raise TypeError('Naziv treba da bude string')
        if not isinstance(kapacitet, int):
            raise TypeError('Kapacitet treba da bude ceo broj')
        if not isinstance(root, Folder):
            raise TypeError('Root treba da bude folder')
        if len(root) > kapacitet:
            raise ValueError('Root folder je veci od kapaciteta diska')
        
        self.naziv = naziv
        self.kapacitet = kapacitet
        self.root = root
    
    def dodaj_fajl(self, folder, fajl):
        if not isinstance(folder, Folder):
            raise TypeError('Folder mora da bude folder')
        if not isinstance(fajl, File):
            raise TypeError('Fajl mora da bude file')
        if not folder in tuple(self.root.ls('R')):
            raise ValueError('Folder mora biti na disku')
        if fajl in tuple(self.root.ls('R')):
            raise ValueError('Fajl ne sme biti na disku')
        if self.kapacitet - len(self.root) < len(fajl):
            raise ValueError('Nema dovoljno prostora na disku')
        folder.kolekcija.append(fajl)
        fajl.roditelj = folder
    
    def ls(self, putanja, *args):
        print(self.naziv, self.kapacitet)
        delovi = putanja.split('/')
        folder = self.root
        for i in range(1, len(delovi)):
            if delovi[i] != '' and isinstance(folder, Folder):
                for f in folder.kolekcija:
                    if f.naziv == delovi[i]:
                        folder = f
                        break
                else:
                    raise ValueError('Nepostojeca putanja: %s' % putanja)
            elif delovi[i] != '':
                raise ValueError('Nepostojeca putanja: %s' % putanja)
        for f in folder.ls(*args):
            print('%s (%d%s)' % (f, len(f), 'f' if isinstance(f, Folder) else ''))             
        
if __name__ == '__main__':
    root = Folder('/')
    d = Disk('test', 8000, root)
    fo1 = Folder('folder1')
    fo2 = Folder('folder2')
    fo3 = Folder('folder3')
    f1 = File('file1', 20)
    f2 = File('file2', 433)
    f3 = File('file3', 70)
    f4 = File('file4', 180)
    f5 = File('file5', 4000)
    f6 = File('file6', 881)
    f7 = File('file7', 412)
    d.dodaj_fajl(root, fo1)
    d.dodaj_fajl(root, fo2)
    d.dodaj_fajl(root, f4)
    d.dodaj_fajl(root, f6)
    d.dodaj_fajl(root, f7)
    d.dodaj_fajl(fo1, f1)
    d.dodaj_fajl(fo1, fo3)
    d.dodaj_fajl(fo1, f5)
    d.dodaj_fajl(fo1, f2)
#    d.dodaj_fajl(fo1, f2)  # izuzetak?
    d.dodaj_fajl(fo2, f3)
    
    print('-'*10)
    d.ls('/', 'R')
    print('-'*10)
    d.ls('/folder1', 'n', 'R', 'r')
    print('-'*10)
    d.ls('/', 'f', 'v')
    