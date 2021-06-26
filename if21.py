# -*- coding: utf-8 -*-
"""
if21. Koordinatalar tekisligida butun son berilgan. Agar nuqta koordinata boshida yotsa, 0 chiqarilsin.
Agar nuqta OX yoki OY o`qlarida joylashsa mos holda 1 va 2 chiqarilsin. Agar nuqta koordinata
o`qida joylashmasa 3 chiqarilsin.

Created on Sat Jun 26 18:15:55 2021

@author: Mansurjon Kamolov
"""

x=float(input('x='))
y=float(input('y='))

if x==0 and y==0 : #Koordinata boshida
    print(0)
elif y==0: #OX o'qida joylashganligini tekshirish
    print(1)
elif x==0: #OY o'qida joylashganligini tekshirish
    print(2)
else: #Boshqa hollarda
    print(3)