#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:16:03 2018

@author: milan
"""

print("Unesi broj clanova niza: ")
n = int(input())
a = []
print("Unesi brojeve niza: ")
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a[1::2])