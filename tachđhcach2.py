# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:14:53 2024

@author: HUYNHNGUYENHUTLINH
"""
chuoi="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
mot= chuoi.split(" , ")
hai= chuoi.replace("P. ","").replace("Q. ","").split(" , ")
print(mot)
print(hai)