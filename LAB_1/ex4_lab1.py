# -*- coding: utf-8 -*-
"""ex4_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UNSztflX0XVXgjQE_ZNX5tlEMCnIB4OZ
"""

def cross(A, B):
  return {a + b for a in A for b in B}

gender = cross('M', '123456') | cross('W', '123456789')

import itertools
list_gender = list(itertools.combinations(gender, 5))

for s in list_gender:
  count_M = 0
  for i in range(0,4):
    if s[i][0] == 'M':
        count_M = count_M + 1
  if count_M == 3:
    print(s)