#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:42:26 2018

@author: milan
"""
"""
#a)
s = set()
str1 = input("Unesite prvi string: ")
str2 = input("Unesite drugi string: ")
str1=str1.replace(" ", "")
print(str1)
for c in str1:
    if(str2.find(c)!=-1 and c not in s):
        s.add(c)
print(s)
"""

"""
#b)
s = set()
str1 = input("Unesite prvi string: ")
str2 = input("Unesite drugi string: ")
str1=str1.replace(" ", "")
for c in str1:
    if(str2.find(c)==-1 ):
        s.add(c)
print(s)
"""
""""
#c)
str1 = input("Unesite prvi string: ")
str2 = input("Unesite drugi string: ")
str1=str1.replace(" ", "")
str2=str2.replace(" ", "")
set1 = set(str1)
set2 = set(str2)
keys = set1.intersection(set2)
dic1 = {}

for key in keys:
    if str1.count(key) == str2.count(key):
        dic1[key] = str1.count(key)
print(count)
"""
"""
#d)
str1 = input("Unesite prvi string: ")
str2 = input("Unesite drugi string: ")
str1=str1.replace(" ", "")
str2=str2.replace(" ", "")
set1 = set(str1)
set2 = set(str2)
keys = set1.union(set2)
dic1 = {}

for key in keys:
    if str1.count(key) != str2.count(key):
        dic1[key] = (str1.count(key),str2.count(key))
print(dic1)
"""