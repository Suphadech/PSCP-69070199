"""Plz pass"""
import math as m
status = input()
quantity = int(input())
total = 0
dis = 1
for dis in range(quantity) :
    total += float(input())
if status == "Y" :
    dis = 0.95
elif status == "N" and total >= 500 :
    dis = 0.97
print(f"{m.ceil(total * dis * 100) / 100:.2f}")
