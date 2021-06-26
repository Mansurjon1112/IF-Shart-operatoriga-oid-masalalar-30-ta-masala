# -*- coding: utf-8 -*-
"""
if14. Uchta son berilgan. Shu sonlarni avval kichigini keyin kattasini ekranga chiqaruvchi programma
tuzilsin.

Created on Sat Jun 26 17:01:08 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
#1-usul 
"""
if a<b:
    min=a
    max=b
else:
    min = b
    max = a

if min>c:
    min=c
if max<c:
    max=c
"""

#2-usul 
ki=min(a,b,c)
ka=max(a,b,c)

print('Kattasi:',ka,'Kichigi',ki)
    
