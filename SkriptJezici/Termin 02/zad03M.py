#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:04:39 2018

@author: milan
"""
print("Unesi string: ")
str1 = input()
str1 = str1.lower()
dict1 = {'a':0,'e':0,"i":0,"o":0,"u":0}
for c in str1:
    if(c in dict1):
        dict1[c]+=1
print(dict1)
