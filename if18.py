# -*- coding: utf-8 -*-
"""
if18. Uchta butun son berilgan. Shu sonlarni ikkitasi o`zaro teng, qolgan bittasini tartib raqami
aniqlansin.

Created on Sat Jun 26 17:31:35 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

if not((a==b) and (b==c)):
    if a==b:
        print('3-si')
    elif a==c:
        print('2-si')
    elif b==c:
        print('1-si')
    else:
        print('2 ta teng son kiritilmadi')
else:
    print('3 ta son bir xil')