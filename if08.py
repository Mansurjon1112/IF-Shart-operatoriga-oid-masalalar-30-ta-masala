# -*- coding: utf-8 -*-
"""
if8. Ikkita butun son berilgan. Shu sonlarning avval kattasini keyin kichigini ekranga chiqaruvchi
programma tuzilsin.
.
Created on Sat Jun 26 12:02:17 2021

@author: Mansurjon Kamolov
"""

a=int(input('birinchi son: '))
b=int(input('ikkinchi son: '))
if a>b:
    print('Kattasi',a,'kichigi',b)
elif a<b:
    print('Kattasi',b,'kichigi',a)
else:
    print('Ular teng')