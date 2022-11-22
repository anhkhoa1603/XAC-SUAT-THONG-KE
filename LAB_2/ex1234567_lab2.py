# -*- coding: utf-8 -*-
"""ex1234567_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pr97gQMln3LbuBee8V0joanPfhtkxvkr
"""

import random
from itertools import product

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))

def simulator_dice1(n):
  count = 0
  for simulations in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 % 2 == 0 and die2 % 2 == 0:
      count += 1
  return count / n

def simulator_dice2(n):
  count = 0
  for simulations in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 % 2 == 1 and die2 % 2 == 0:
      count += 1
  return count / n

def simulator_dice3(n):
  count = 0
  for simulations in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == die2:
      count += 1
  return count / n

def simulator_dice4(n):
  count = 0
  for simulations in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 == 1 and die2 == 6:
      count += 1
  return count / n

def simulator_dice5(n):
  count = 0
  for simulations in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 >= 6:
      count += 1
  return count / n

def simulator_poker1(n):
  count = 0
  for i in range(n):
    five_card = []
    temp = 0
    for j in range(100):
      index = random.randint(0, 51)
      if temp != index:
        five_card.append(Cards[index])
        temp = index
      if len(five_card) == 5:
        break
    count_hearts = 0
    for s in five_card:
      if s[1] == '♡':
        count_hearts += 1

    if count_hearts == 5:
      count += 1
  return count / n   

# def simulator_poker2(n):
#   count = 0
#   for i in range(n):
#     four_card = []
#     for j in range(100):
#       index = random.randint(0, 51)
#       four_card.append(Cards[index])
#       four_card = list(set(four_card))
#       if len(four_card) == 4:
#         break
#     if len(four_card) == len(set(four_card)):
#       count += 1
#   print(count)
#   return count / n 
print("Cau 1:")
print(simulator_dice1(10000))
print("Cau 2:")
print(simulator_dice2(10000))
print("Cau 3:")
print(simulator_dice3(10000))
print("Cau 4:")
print(simulator_dice4(10000))
print("Cau 5:")
print(simulator_dice5(10000))
print("Cau 6:")
print(simulator_poker1(10000))