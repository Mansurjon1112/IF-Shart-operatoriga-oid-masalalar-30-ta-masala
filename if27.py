# -*- coding: utf-8 -*-
"""
if27. X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin.

Created on Sat Jun 26 19:22:35 2021

@author: Mansurjon Kamolov
"""
from math import floor

x=float(input('x='))

if x<0:
    y=0
elif floor(x) % 2==0 :
    y=1
else:
    y=-1
print(y)
