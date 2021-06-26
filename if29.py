# -*- coding: utf-8 -*-
"""
if29. Butun son berilgan. Berilgan sonni “musbat toq son”, “manfiy juft son”, “son nolga teng” va x.k.
ekranga yozadigan programma tuzilsin.

Created on Sat Jun 26 21:20:19 2021

@author: Mansurjon Kamolov
"""

n= int(input('N='))

if n==0 :
    print('Son nolga teng')
elif n>0:
    if n%2==0:
        print('Musbat juft son')
    else:
        print('Musbat toq son')
else:
    if n%2==0:
        print('Manfiy juft son')
    else:
        print('Manfiy toq son')
