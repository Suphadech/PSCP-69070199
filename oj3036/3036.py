'''CASTLE'''
import math as m
num = int(input())
row = m.ceil(m.sqrt(num))
if row % 2:
    if num % 2:
        print(2 * (row-1))
    else:
        print((2 * (row-1)) - 1)
elif not row % 2:
    if not num % 2:
        print((2 * (row-1)))
    else:
        print(2 * (row-1) - 1)
