# -*- coding: utf-8 -*-
"""
if4. Uchta butun son berilgan. Shu sonlar orasidan nechta musbat son borligini aniqlovchi
programma tuzilsin.

Created on Sat Jun 26 11:09:09 2021

@author: Mansurjon Kamolov
"""

a=int(input('birinchi son: '))
b=int(input('ikkinchi son: '))
c=int(input('uchinchi son: '))
sanoq=0
if a>0:
    sanoq+=1
if b>0:
    sanoq+=1
if c>0:
    sanoq+=1   
if sanoq==0:
    print('Musbat son kiritilmadi')
else:
    print('Kiritilgan sonlarning',sanoq,'tasi musbat')