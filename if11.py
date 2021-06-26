# -*- coding: utf-8 -*-
"""
if11. A va B butun sonlari berilgan. Agar o`zgaruvchilar o`zaro teng bo`lmasa, A va B bu sonlarning
kattasini o`zlashtirsin. Agar teng bo`lsa, 0 ni o`zlashtirsin. A va B ning qiymati ekranga chiqarilsin.

Created on Sat Jun 26 12:10:17 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
if a==b:
    a=b=0
else:
    if a>b :
        b=a
    else:
        a=b
print('a=',a,'b=',b)
