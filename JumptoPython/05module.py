# 모듈 테스트

import sys
print(sys.path)

import mod1
from mod1 import *

print(mod1.add(1, 2))
print(mod1.sub(55, 33))
print(mod1.pow(4, 7))

print(add(3, 4))
print(div(455, 5))

import mod2
print(mod2.PI)

a = mod2.Math(2)
print(a.solv())

print(mod2.add(mod2.PI, 4.4))
