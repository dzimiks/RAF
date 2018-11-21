# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:21:39 2018

@author: mtomic
"""

class File:
    def __init__(self, naziv, velicina, roditelj=None):
        if not isinstance(naziv, str):
            raise TypeError('Pogresan tip argumenta naziv:' + type(naziv).__name__)

        if not isinstance(velicina, int):
            raise TypeError('Pogresan tip argumenta velicina:' + type(velicina).__name__)

        if roditelj and not isinstance(roditelj, Folder):
            raise TypeError('Pogresan tip argumenta roditelj:' + type(roditelj).__name__)
        
        self.naziv = naziv
        self.velicina = velicina
        self.roditelj = roditelj
        if roditelj is not None:
            # dodati fajl u kolekciju roditelja
            roditelj.kolekcija.append(self)
    
    def __len__(self):
        return self.velicina
    
    def __str__(self):
        return self.naziv
    
    __repr__ = __str__
    
    def ls(self, *args):
        if not 'f' in args:
            yield self

class Folder(File):
    def __init__(self, naziv, roditelj=None):
        super().__init__(naziv, 4, roditelj)
        self.kolekcija = []
        
    def __len__(self):
        z = self.velicina
#        for f in self.kolekcija:
#            z += len(f)
        z += sum((len(f) for f in self.kolekcija))
        return z
    
    def __contains__(self, fajl):
        if fajl in self.kolekcija:
            return True
        else:
            return any((fajl in f for f in self.kolekcija if isinstance(f, Folder)))
#            for f in self.kolekcija:
#                if isinstance(f, Folder) and fajl in f:
#                    return True
#        return False
    
    def ls(self, *args):
        key = None
        for arg in args:
            if arg in ('n', 'v'):
                key = arg
        rev = 'r' in args
        rek = 'R' in args
        fo = 'f' in args
        
        kljucevi = {
            'n': lambda x: x.naziv,
            'v': lambda x: -len(x)
        }
        
        if key is not None:
            kol = sorted(self.kolekcija, key=kljucevi[key], reverse=rev)
        else:
            kol = self.kolekcija
        
        yield self
        for f in kol:
            if rek:
                for f2 in f.ls(*args):
                    yield f2
            elif (fo and isinstance(f, Folder)) or not fo:
                yield f
    
class Disk:
    def __init__(self, naziv, kapacitet, root):
        if not isinstance(naziv, str):
            raise TypeError('Pogresan tip argumenta naziv:' + type(naziv).__name__)

        if not isinstance(kapacitet, int):
            raise TypeError('Pogresan tip argumenta kapacitet:' + type(kapacitet).__name__)

        if not isinstance(root, Folder):
            raise TypeError('Pogresan tip argumenta root:' + type(root).__name__)

        if len(root) > kapacitet:
            raise ValueError('Velicina root foldera prevazilazi kapacitet diska')
        
        self.naziv = naziv
        self.kapacitet = kapacitet
        self.root = root
    
    def dodaj_fajl(self, folder, fajl):
        if not isinstance(folder, Folder):
            raise TypeError('Pogresan tip argumenta folder:' + type(folder).__name__)
        
        if not isinstance(fajl, File):
            raise TypeError('Pogresan tip argumenta fajl:' + type(fajl).__name__)
        
        # da li je folder na disku
        if folder != self.root and folder not in self.root:
            raise ValueError('Folder se ne nalazi na disku')
        # da li fajl nije na disku
        if fajl in self.root:
            raise ValueError('Fajl je vec na disku')
        # preostali prostor na disku ne sme biti prekoracen velicinom fajla
        if self.kapacitet - len(self.root) < len(fajl):
            raise ValueError('Velicina fajla prevazilazi preostali kapacitet diska')
        
        folder.kolekcija.append(fajl)
        fajl.roditelj = folder
    
    def ls(self, putanja, *args):
        print(f'{self.naziv} {self.kapacitet}')
        # nadji putanju
        delovi = putanja.split('/')
        f = self.root
        indeks = 1
        while indeks < len(delovi) and delovi[indeks] != '':
            for p in f.kolekcija:
                if p.naziv == delovi[indeks]:
                    f = p
                    indeks += 1
                    break
            else:
                raise IndexError('Nepostojeca putanja "%s"' % putanja)
        # ispisuj sa te putanje
        for fajl in f.ls(*args):
            print(f'{str(fajl)} ({len(fajl)}{"f" if isinstance(fajl, Folder) else ""})')
        
if __name__ == '__main__':
    root = Folder('/')
    fs = Disk('test', 8000, root)
    fo1 = Folder('folder1')
    fo2 = Folder('folder2')
    fs.dodaj_fajl(root, fo1)
    fs.dodaj_fajl(root, fo2)
    fs.dodaj_fajl(root, File('file4', 180))
    fs.dodaj_fajl(root, File('file6', 881))
    fs.dodaj_fajl(root, File('file7', 412))
    fs.dodaj_fajl(fo1, File('file1', 20))
    fs.dodaj_fajl(fo1, Folder('folder3'))
    fs.dodaj_fajl(fo1, File('file5', 4000))
    fs.dodaj_fajl(fo1, File('file2', 433))
    fs.dodaj_fajl(fo2, File('file3', 70))
    
    print('-'*10)
    fs.ls('/', 'R')
    print('-'*10)
    fs.ls('/folder1', 'n', 'R', 'r')
    print('-'*10)
    fs.ls('/', 'f', 'v')
    
    