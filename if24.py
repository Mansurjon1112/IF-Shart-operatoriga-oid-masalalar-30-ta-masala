# -*- coding: utf-8 -*-
"""
if24. X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin.

Created on Sat Jun 26 19:17:46 2021

@author: Mansurjon Kamolov
"""
from math import sin

x=float(input('x='))

if x>0 :
    y=2*sin(x)
else:
    y=x-6
print(y)