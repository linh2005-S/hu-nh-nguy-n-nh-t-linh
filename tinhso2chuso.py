# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 06:44:43 2024

@author: HUYNHNGUYENNHUTLINH
"""
N = int(input("nhập số N: "))
if 9 < N < 100:
    chuc = N//10
    donvi = N%10
print("kết quả là: ", chuc + donvi)