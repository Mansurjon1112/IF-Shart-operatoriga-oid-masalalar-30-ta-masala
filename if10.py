# -*- coding: utf-8 -*-
"""
if10. A va B butun sonlari berilgan. Agar o`zgaruvchilar o`zaro teng bo`lmasa, A va B o`zgaruvchilari
ularning yig`indisini o`zlashtirsin. Agar teng bo`lsa, 0 ni o`zlashtirsin. A va B ning qiymati ekranga
chiqarilsin.

Created on Sat Jun 26 12:08:02 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
if a==b:
    a=b=0
else:
    a=b=a+b
print('a=',a,'b=',b)
