# -*- coding: utf-8 -*-
"""
if19. To`rtta butun son berilgan. Shu sonlarni uchtasi o`zaro teng, qolgan bittasini tartib raqami
aniqlansin.

Created on Sat Jun 26 17:37:18 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))

if a==b and a==c :
    print(4)
elif a==b and a==d:
    print(3)
elif a==c and a==d:
    print(2)
elif b==c and b==d:
    print(1)
else:
    print('Masala shartiga mos sonlar kiriting.')    