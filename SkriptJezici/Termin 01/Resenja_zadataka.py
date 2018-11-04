#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:58:20 2018

@author: milan
"""
"""
#1.
# ispis brojeva od 1 do a
a = int(input("Unesite broj: "))
for i in range(1,a+1):
    print("broj: ",i)
"""

"""
#2.
#zbir cifara unetog broja
a = int(input("Unesite broj: "))
b=a
zbir = 0
while (a>0):
    zbir += a % 10
    a = a // 10
print("Zbir cifara %d je %d. " % (b,zbir))
"""

"""
#3.
#n-ti broj fibonacijevog niza
def fibonaci(n):
    if(n==1):
        return 1
    if(n==2):
        return 1
    a=1
    b=1
    for i in range(3,n+1):
        c = a + b
        a,b = b,c
    return c

n = int(input("Unesi broj: "))
print("n-ti broj fibonacijevog niza je ",fibonaci(n))
"""

"""
#4.
#najveci od 3 uneta broja
max=0
for i in range(1,4):
    n=int(input("Unesi broj: "))
    if(max<n):
        max = n
print("Maksimum je: ",max)
"""

"""
#5
#ucitava brojeve dok zbir ne predje 100
a=0
zbir=0
while(zbir<=100):
    x = int(input())
    zbir += x
    a += 1
else:
    print("Zbir unetih %d brojeva je %d" % (a,zbir))
"""

"""
#6.
#ispisivanje reci 
s = str(input("Unesi string: "))

for i in range(0,len(s)+1):
    print(s[0:i])
"""
"""
#7.
for i in range(0,len(s)+1):
    print(s[i:len(s)+1])
"""
"""
#8.
s1=""
for i in range(len(s)-1,-1,-1):
    s1+=str(s[i])
    print(s1)
"""

"""
#9.
#da li je broj armstrongov
def armstrong(n):
    sum = 0
    temp = n
    while(temp>0):
        digit = temp%10
        sum += digit ** 3
        temp //= 10
    if(n == sum):
        return 1
    else:
        return 0

n=int(input("Unesi broj: "))
if(armstrong(n)):
    print("Broj je Armstrnogov")
else:
    print("Broj nije Armstrongov")
"""

"""
#10.
s=str(input("Unesi string: "))
a=int(input("Unesi broj karaktera u grupi"))
s=s.replace(" ","")
r=""
for i in range(0, len(s),a):
    r+=s[i:i+a]
    r+=" "
print(r.upper())
"""

"""
#11
def prime(n):
    if(n==1 or n==0):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
f1 = open("test1.txt", "w")
with open("test.txt") as f:
    for line in f:
        for c in line.strip():
            if(prime(int(c))):
                print(c,file=f1)
    f1.close()
"""

"""
#12
string = str(input("Unesi string za koji se proverava da li postoji u fajlu:"))
with open("zad12.txt") as f:
    for line in f:
        if(line.find(string)==-1):
            print("ne nalazi se")
        else:
            print("nalazi se")
            break
"""
"""
#13.
string=""
with open("zad13.txt") as f:
    for line in f:
          string+=line
string = string.replace(" ", "")
string = string.replace("\n","")
print(string)
"""
"""
#14.
string = str(input("Unesi string: "))
cnt = 0
rec = ""
f1 = open("zad14.txt","w")
for i in range(0,len(string)):
    if(string[i]== " "):
        print(len(rec))
        print(rec)
        if(len(rec)>5):
            f1.write(rec+"\n")
        rec=""
    else:
        rec+=string[i]
if(len(rec)>5):
    print(len(rec))
    print(rec)
    f1.write(rec+"\n")
"""

#15.


"""
#16.
a=float(input("Unesi broj stepena u celzijusima: "))
print("Stepena u Farenhajtima %.2d"%(1.8*a+32))
"""

"""
#17.
def prime(n):
    if(n==1 or n==0):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
a=int(input("uneti donju granicu intervala: "))
b=int(input("uneti gornju granicu intervala: "))
f1= open("zad17.txt","w")
for i in range(a,b):
    if(prime(i)):
        f1.write(str(i)+" ")
"""

#18.


#19.

"""
#20.
a=int(input("Unesi broj: "))
zbir =0
proizvod = 1
while(a!=0):
    if(a%2 == 0):
        zbir+=a
    else:
        proizvod*=a
    a=int(input("unesi broj: "))
print(zbir)
print(proizvod)
"""