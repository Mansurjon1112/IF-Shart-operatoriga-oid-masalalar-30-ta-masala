# -*- coding: utf-8 -*-
"""
if13. Uchta son berilgan. Shu sonlarni o`ratachasi (ya’ni katta va kichik sonlar orasidagi son) ni
aniqlovchi programma tuzilsin.

Created on Sat Jun 26 13:56:18 2021

@author: Mansurjon Kamolov
"""

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

if a>b and b>c or c>b and b>a :
    print(b)
elif a>c and c>b or b>c and c>a:
    print(c)
else:
    print(a)
