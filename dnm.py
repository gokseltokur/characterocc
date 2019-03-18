# -*- coding: utf-8 -*-

import re
import locale

locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

str = "aaaaşşşşşşşööööööğğğğğğğğğçççççççç"
"""
x = 97
ch = unichr(x)
sx = ch

l = len(re.findall(sx, str))

print(l)
#print(l)
"""


for i in range(592):
    ch = unichr(i)
    sx = ch
    if i == 40 or i == 41 or i == 42 or i == 43 or i == 63 or i == 91 or i == 92:
        continue
    cnt = len(re.findall(sx, str))
    if cnt > 3:
        print('Character (%s)\'s occurrance is: %d'%(sx, cnt))
