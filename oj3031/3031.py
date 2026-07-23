'''INK'''
import math as m
time = []
PI_VALUE = 3.1416
s,n = map(int ,input().split())
for i in range(n):
    i = i + 0
    x,y = map(int ,input().split())
    distance = (m.sqrt((x**2) + (y**2)))
    time.append(m.ceil((PI_VALUE*((distance)**2))/s))
print(*time, sep="\n")
