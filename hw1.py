# -*- coding: utf-8 -*-
"""hw1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1faI5ZqQRrgFY2_u5gpHFp3Olktfvdm9L
"""

def get_radius (prompt):
  r = int(input(prompt))
  return r

def get_circle_area(input_radius):
  circle = 3.14*input_r*input_r
  return circle

input_r = get_radius('넓이를 구하고자 하는 원의 반지름은?')
circle_area = get_circle_area(input_r)
print('반지름', input_r, '인 원의 넓이 = 3.14 x', input_r, 'x', input_r, '=', circle_area)