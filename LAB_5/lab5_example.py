# -*- coding: utf-8 -*-
"""Lab5_Example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KJ-W_3fK6TLJqcsEzkYUTRJICtIA9T5
"""

import random
import math

#Definitions
x = [random.randint(1,6) for i in range(8000)]
X = set(x)
print(x)
print(X)

#Probability distribution
P = [x.count(i)/len(x) for i in X]
print(P)

#Cumulative distribution function – CDF
FX = sum(P[:3])
print(FX)

#Expectations
EX = 0
for x in X:
  EX = EX + (x * P[x-1]);
print(EX)

#Variance
VarX = 0
for x in X:
  VarX = VarX + (x-EX)*(x-EX)*P[x-1]
print(VarX)

#Standard Deviation
SD = math.sqrt(VarX)
print(SD)