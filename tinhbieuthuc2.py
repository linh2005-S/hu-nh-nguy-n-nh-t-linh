# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:22:47 2024

@author: huynhnguyennhutlinh
"""
import math
a=float(input("nhập a: "))
b=float(input("nhập b: "))
X = (math.sqrt(a)- math.sqrt(b))/(a**(1/4)-b**(1/4))-(math.sqrt(a)+(a*b)**(1/4))/(a**(1/4))+(b**(1/4))
print("kết quả: ",X)