# -*- coding: utf-8 -*-
"""
if17. A, B, C haqiqiy sonlari berilgan. Agar berilgan sonlar o`sish yoki kamayish tartibida berilgan
bo`lsa, sonlarni ikkilantiring, aks holda sonlarni ishorasi o’zgartirilsin. A, B, C ning qiymatlari ekranga
chiqarilsin.

Created on Sat Jun 26 17:30:39 2021

@author: Mansurjon Kamolov
"""
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

if a<b and b<c or a>b and b>c:
    a*=2
    b*=2
    c*=2
else:
    a*=-1
    b*=-1
    c*=-1

print('a=',a,'b=',b,'c=',c)