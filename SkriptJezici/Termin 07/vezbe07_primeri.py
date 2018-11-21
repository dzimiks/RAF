# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:21:26 2018

@author: mtomic
"""

# 1. Написати функцију f1 која као аргумент прима назив датотеке и чија је 
# повратна вредност мапа која чува све различите речи у датотеци, груписане 
# по броју слова и унутар сваке групе сортиране по азбучном реду. Кључеви 
# у мапи су дужине речи у групи, а вредности су листе сортираних речи. 
# При обради све речи претворити у велика слова, избацити све бројеве. 
# Знакове интерпункције елиминисати из речи (са почетка и краја). 
# Датотеку обавезно затворити по завршетку обраде! (Функцију тестирати на 
# приложеној датотеци.)

import codecs


def f1(dat):
    f = codecs.open(dat, 'r', 'utf-8')
    d = {}
    
    for line in f:
        l = line.strip().split(' ')
        for rec in l:
            rec = rec.strip('“„,.…').upper()
            if rec[0] in '0123456789':
                continue
            d.setdefault(len(rec), []).append(rec)
    f.close()
    for key in d:
        d[key].sort()
    return d

# Написати генератор g2 који опонаша приоритетни ред. Генератору се прослеђује
# као аргумент листа која представља ред и функција која представља кључ. При 
# свакој итерацији, генератор избацује из реда и враћа елемент највећег 
# приоритета. Функција кључа се користи да се израчуна елемент максималног 
# приоритета (функција кључа као аргумент прима елемент из листе и враћа 
# вредност параметра по коме се елементи упоређују - по којој се одређује 
# приоритет). Већа вредност функције кључа представља већи приоритет. Из 
# прослеђене листе се избацује један по један елемент по приоритету. Омогућити 
# да се у листу у сваком тренутку између два генерисања може додати нова 
# вредност, при чему ће и та вредност бити узета у обзир при следећем 
# генерисању. Сложеност имплементације није битна (дозвољено је да буде O(n**2)).

def g2(red, kljuc):
    while len(red) > 0:
#        maxind = 0
#        for i in range(1, len(red)):
#            if kljuc(red[i]) > kljuc(red[maxind]):
#                maxind = i
#        e = red.pop(maxind)
#        yield e
#        e = red[maxind]
#        red.remove(e)
        e = max(red, key=kljuc)
        red.remove(e)
        yield e

# Написати функцију f3 која као аргументе прима називе улазне и излазне 
# датотеке. У излазну датотеку треба да препише све редове који почињу 
# четвороцифреним бројем чија је последња цифра 1 или 4. Као повратну 
# вредност функција враћа збир почетних бројева из преписаних редова.

def f3(datin, datout):
    f = codecs.open(datin, 'r', 'utf-8')
    g = codecs.open(datout, 'w', 'utf-8')
    zbir = 0
    
    for line in f:
        l = line.strip().split(' ')
        rec = l[0].strip('“„,.…')
        try:
            broj = int(rec)
            if len(rec) == 4 and (rec[3] == '1' or rec[3] == '4'):
                g.write(line)
                zbir += broj
        except:
            pass
    f.close()
    g.close()
    return zbir

# Написати класу k4 која представља структуру података за Цезарову шифру. 
# Иницијализатор структуре прима стринг састављен од великих слова абецеде, 
# која представљају текст који се шифрује. Ако стринг садржи било шта осим 
# великих слова абецеде, треба бацити ValueError изузетак. Подржати операције 
# __str__ - враћа стринг из кога је иницијализована, __len__ - враћа дужину 
# стринга, __add__ - ако се сабира са целим бројем, враћа нову инстанцу исте 
# класе која је шифрована Цезаровом шифром - померањем слова за задати број, 
# __sub__ - ако се одузима са целим бројем, ради инверзно од __add__, а ако 
# се одузима са другом инстанцом исте класе, враћа цео број који представља 
# кључ за претварање друге инстанце у прву (помоћу сабирања) или баца 
# ValueError ако стрингови нису компатибилни (тј. ако се један не може 
# добити Цезаровом шифром из другог). Абецеда је кружна (после 'Z' иде 'A').

class k4:
    def __init__(self, text):
        self._text = text
        for s in self._text:
            if not (s >= 'A' and s <= 'Z'):
                raise ValueError('Nepodrzano slovo %s' % s)
    
    def __str__(self):
        return self._text
    
    def __len__(self):
        return len(self._text)
    
    def __add__(self, drugi):
        if type(drugi) is int:
        # if isinstance(drugi, int):
            z = ''
            for s in self._text:
                broj = ord(s)
                broj -= 65
                broj = (broj + drugi) % 26
                broj += 65
                z += chr(broj)
            return k4(z)
        return NotImplemented
    
    def __sub__(self, drugi):
        if type(drugi) is int:
            z = ''
            for s in self._text:
                broj = ord(s)
                broj -= 65
                broj = (broj - drugi) % 26
                broj += 65
                z += chr(broj)
            return k4(z)
        elif isinstance(drugi, k4):
            z = str(drugi)
            if len(self._text) != len(z):
                raise ValueError('Tekstovi su razlicite duzine')
            if len(self._text):
                razlika = ord(self._text[0]) - ord(z[0]) 
                for s1, s2 in zip(self._text, z):
                    if ord(s1) - ord(s2) != razlika:
                        raise ValueError('Tekstovi nisu kompatibilni')
                return razlika
            else:
                return 0
        return NotImplemented

import random

def main():
#    d = f1('kpripreme.txt')
#    for k in sorted(d.keys()):
#        print(k, d[k])
    
#    red = [(0, 5), (1, 4)]
#    i = 3
#    for e in g2(red, lambda x: x[1]):
#        print(e)
#        if random.randint(0, 4) > 2:
#            red.append((i, random.randint(0, 20)))
#            i += 1
#        print(red)

#    print(f3('kpripreme.txt', 'kpripreme_out.txt'))
    pass

if __name__ == '__main__':
    main()