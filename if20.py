# -*- coding: utf-8 -*-
"""
if20. Sonlar o`qida uchta A, B, C nuqtalar berilgan. A nuqtaga eng yaqin nuqta va ular orasidagi
masofa topilsin.

Created on Sat Jun 26 18:13:10 2021

@author: Mansurjon Kamolov
"""

a=float(input('A='))
b=float(input('B='))
c=float(input('C='))

ab =abs(a-b)
ac=abs(a-c)

if ab<ac:
    print('B nuqta yaqin',ab,'masofada')
else:
    print('C nuqta yaqin',ac,'masofada')
