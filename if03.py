# -*- coding: utf-8 -*-
"""
if3. Butun son berilgan. Agar, berilgan son musbat bo`lsa, 1 ga oshiring, agar manfiy bo`lsa 2 ga
kamaytiring. Agar 0 ga teng bo`lsa, 10 ni o`zlashtirsin. Hosil bo`lgan sonni ekranga chiqaruvchi
programma tuzilsin.

Created on Sat Jun 26 11:07:36 2021

@author: Mansurjon Kamolov
"""

n = int(input('N='))
if n>0 : 
    n+=1
elif n<0:
    n-=2
else:
    n=10
print(n)