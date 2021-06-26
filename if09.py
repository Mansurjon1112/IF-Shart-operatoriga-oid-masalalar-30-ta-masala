# -*- coding: utf-8 -*-
"""
if9. A va B haqiqiy sonlari beringan. Shu sonlarni shunday o’zgartirish kerakki, A son kichik B son
katta bo`lsin. A va B ning qiymati ekranga chiqarilsin.

Created on Sat Jun 26 12:03:17 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
if a>b:
    a,b=b,a
elif a==b:
    print('Ular teng')
print('a=',a,'b=',b)