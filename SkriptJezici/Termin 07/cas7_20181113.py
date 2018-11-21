# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:21:55 2018

@author: mtomic
"""

#%%
# 1. Написати функцију f1 која као аргумент прима назив датотеке и чија је 
# повратна вредност мапа која чува све различите речи у датотеци, груписане 
# по броју слова и унутар сваке групе сортиране по азбучном реду. Кључеви 
# у мапи су дужине речи у групи, а вредности су листе сортираних речи. 
# При обради све речи претворити у велика слова, избацити све бројеве. 
# Знакове интерпункције елиминисати из речи (са почетка и краја). 
# Датотеку обавезно затворити по завршетку обраде! (Функцију тестирати на 
# приложеној датотеци.)

import codecs

def f1(dat1):
    ret = {}
    with codecs.open(dat1, 'r', 'utf-8') as f:
        for line in f:
            l = line.strip().split(' ')
            for rec in l:
                rec = rec.upper().strip(',.-;:„“–…()')
                try:
                    float(rec)
                except:
                    ret.setdefault(len(rec), []).append(rec)
    for key in ret:
        ret[key].sort()
    return ret

print(f1('kpripreme.txt'))

#%% 2. Написати генератор g2 који опонаша приоритетни ред. Генератору се 
# прослеђује као аргумент листа која представља ред и функција која представља
# кључ. При свакој итерацији, генератор избацује из реда и враћа елемент 
# највећег приоритета. Функција кључа се користи да се израчуна елемент 
# максималног приоритета (функција кључа као аргумент прима елемент из 
# листе и враћа вредност параметра по коме се елементи упоређују - по којој 
# се одређује приоритет). Већа вредност функције кључа представља већи 
# приоритет. Из прослеђене листе се избацује један по један елемент по 
# приоритету. Омогућити да се у листу у сваком тренутку између два генерисања 
# може додати нова вредност, при чему ће и та вредност бити узета у обзир при 
# следећем генерисању. Сложеност имплементације није битна (дозвољено је да 
# буде O(n**2)).

def g2(red, kljuc):
    while len(red) > 0:
#        maxind = 0
#        for i in range(1, len(red)):
#            if kljuc(red[i]) > kljuc(red[maxind]):
#                maxind = i
#        yield red.pop(maxind)
        yield red.pop(red.index(max(red, key=kljuc)))

red = [(5, 1), (3, 1), (2, 2), (4, 4), (7, 3)]
for e in g2(red, lambda x: x[1]):
    print(e)

#%% 3. Написати функцију f3 која као аргументе прима називе улазне и излазне 
# датотеке. У излазну датотеку треба да препише све редове који почињу 
# четвороцифреним бројем чија је последња цифра 1 или 4. Као повратну 
# вредност функција враћа збир почетних бројева из преписаних редова.

def f3(datin, datout):
    zbir = 0
    with codecs.open(datin, 'r', 'utf-8') as f:
        with codecs.open(datout, 'w', 'utf-8') as g:
            for line in f:
                l = line.strip().split(' ')
                rec = l[0].strip(',.-;:„“–…()')
                try:
                    broj = int(rec)
                    if broj >= 1000 and broj <= 9999 and broj % 10 in (1, 4):
                        g.write(line)
                        zbir += broj
                except:
                    pass
    return zbir

if __name__ == '__main__':
    print(f3('kpripreme.txt', 'kpripremeout.txt'))
    
#%% 4. Написати класу k4 која представља структуру података за Цезарову шифру. 
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
        for slovo in text:
            if not (slovo >= 'A' and slovo <= 'Z'):
                raise ValueError('Nepodržan simbol %s' % slovo)
        self._text = text
                
    def __str__(self):
        return self._text
    
    def __repr__(self):
        return 'k4(%s)' % repr(self._text)
    
    def __len__(self):
        return len(self._text)
    
    def __add__(self, other):
        if isinstance(other, int):
            s = ''
            for slovo in self._text:
                # pitaj Burgu sta je ovo
                broj = (ord(slovo)-ord('A')+other)%(ord('Z')-ord('A')+1)+ord('A')
                s += chr(broj)
            return k4(s)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            s = ''
            for slovo in self._text:
                # pitaj Burgu sta je ovo
                broj = (ord(slovo)-ord('A')-other)%(ord('Z')-ord('A')+1)+ord('A')
                s += chr(broj)
            return k4(s)
        elif isinstance(other, k4):
            if len(self) != len(other):
                raise ValueError('Nisu iste dužine')
            if len(self) == 0:
                return 0
            razlika = ord(self._text[0]) - ord(other._text[0])
            for i in range(1, len(self._text)):
                if ord(self._text[i]) - ord(other._text[i]) != razlika:
                    raise ValueError('Nisu kompatibilni tekstovi')
            return razlika
        return NotImplemented
    
    def __eq__(self, other):
        return isinstance(other, k4) and self._text == other._text
    