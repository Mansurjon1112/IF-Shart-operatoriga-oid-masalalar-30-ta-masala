# -*- coding: utf-8 -*-
"""
if23. Koordinata o`qlariga parallel ravishda to`g`ri to`rtburchakning uchta uchi berilgan, to’rtinchi uchi
koordinatasini aniqlansin.

Created on Sat Jun 26 18:22:57 2021

@author: Mansurjon Kamolov
"""

x1=float(input('x1='))
y1=float(input('y1='))

x2=float(input('x2='))
y2=float(input('y2='))

x3=float(input('x3='))
y3=float(input('y3='))

x4=y4=0

if (x1==x2):
    x4=x3
else:
    x4=x2    

    
if (y1==y2):
    y4=y3
else:
    y4=y1
    
print(x4,',',y4)
        
    