# -*- coding: utf-8 -*-
"""
if28. Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini aniqlovchi programma
tuzilsin. Kabisa yilida 366 kun bor, kabisa bo’lmagan yilda 365 kun bor. Kabisa yil deb 4 ga karrali
yillarga aytiladi. Lekin 100 ga karrali yillar ichida faqat 400 ga karrali bo’lganlari kabisa yil
hisoblanadi. Masalan 300, 1300 va 1900 kabisa yili emas. 1200 va 2000 kabisa yili.

Created on Sat Jun 26 21:06:48 2021

@author: Mansurjon Kamolov
"""

yil = int(input('Yilni kiriting: '))
if yil % 400==0 :
    print('kabisa')
elif yil % 100 == 0:
    print('Kabisa emas')
elif yil % 4==0:
    print('kabisa')
else:
    print('Kabisa emas')