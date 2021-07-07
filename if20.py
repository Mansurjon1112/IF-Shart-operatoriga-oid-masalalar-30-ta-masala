# -*- coding: utf-8 -*-
"""
if20. Sonlar o`qida uchta A, B, C nuqtalar berilgan. A nuqtaga eng yaqin nuqta va ular orasidagi
masofa topilsin.

Created on Sat Jun 26 18:13:10 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
ab=abs(a-b)
ac=abs(a-c)
if ab<ac:
    print('b nuqta',ab,'masofa')
elif ab>ac:
    print('c nuqta',ac,'masofa')
else: 
    print('Bir xil masofa')
