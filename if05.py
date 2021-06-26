# -*- coding: utf-8 -*-
"""
if5. Uchta butun son berilgan. Shu sonlar orasidan nechta musbat va manfiy son borligini aniqlovchi
programma tuzilsin.

Created on Sat Jun 26 11:11:52 2021

@author: Mansurjon Kamolov
"""

a=int(input('birinchi son: '))
b=int(input('ikkinchi son: '))
c=int(input('uchinchi son: '))
musbat = 0
manfiy = 0
if a>0:
    musbat+=1
elif a<0:
    manfiy+=1

if b>0:
    musbat+=1
elif b<0:
    manfiy+=1

if c>0:
    musbat+=1
elif c<0:
    manfiy+=1
    
if musbat==0 or manfiy == 0:
    print('Kiritilgan sonlarning barchasi 0 (nol)')
else:
    print('Kiritilgan sonlarning',musbat,'tasi musbat',manfiy,'tasi manfiy')