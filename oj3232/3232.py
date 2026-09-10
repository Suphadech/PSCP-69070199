'''Frog'''
x,y = map(int,input().split())
distance = 0
for i in range(1,y+1):
    add_distance = x - (2 * (i-1))
    distance += add_distance
    if add_distance < 0:
        print(-1)
        break
    if distance >= y:
        print(i)
        break
