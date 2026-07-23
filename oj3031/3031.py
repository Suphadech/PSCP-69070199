'''INK'''
import math as m
distance = []
x = 0
y = 0
time = []
PI_VALUE = 3.1416
s,n = map(int ,input().split())
for i in range(n):
    x,y = map(int ,input().split())
    distance.append(m.sqrt((x**2) + (y**2)))
for _ in range(n):
    time.append(m.ceil((PI_VALUE*((distance[_])**2))/s))
for i in time:
    print(i)
