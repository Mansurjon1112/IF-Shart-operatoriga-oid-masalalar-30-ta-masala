# -*- coding: utf-8 -*-
"""
if22. OX va OY koordinata o`qlarida yotmaydigan nuqta berilgan. Nuqta joylashgan koordinata
choragi aniqlansin.

Created on Sat Jun 26 18:19:51 2021

@author: Mansurjon Kamolov
"""

x=float(input('x='))
y=float(input('y='))

if x==0 or y == 0 :
    print('Koordinata o\'qlarida yormaydigan nuqta kiriting')
else:
    if x>0 and y>0 :
        print('1-chorak')
    elif x<0 and y>0 :
        print('2-chorak')
    elif x<0 and y<0 :
        print('3-chorak')
    else:
        print('4-chorak')
        