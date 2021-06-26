# -*- coding: utf-8 -*-
"""
if30. 1-999 oraliqdagi sonlar berilgan. Berilgan sonni “ikki xonali juft son”, “uch xonali toq son” va
x.k. ekranga yozadigan programma tuzilsin.

Created on Sat Jun 26 21:22:53 2021

@author: Mansurjon Kamolov
"""

n= int(input('N='))

if n//10==0 :
    print('Bir xonali',end=' ')
    if n%2==0:
        print('juft son')
    else:
        print('toq son')
elif n//10<=9:
    print('Ikki xonali',end=' ')
    if n%2==0:
        print('juft son')
    else:
        print('toq son')
elif n//100<=9:
    print('Uch xonali',end=' ')
    if n%2==0:
        print('juft son')
    else:
        print('toq son')
else:
    print('1 dan 999 gacha oraliqdagi son kiriting')