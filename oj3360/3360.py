'''หั่นขนมปัง'''
w,h,_,_ = map(int ,input().split())
x = list(map(int ,input().split()))
y = list(map(int ,input().split()))
x.append(w)
y.append(h)
x = sorted(x)
y = sorted(y)
first = 0
second = 0
minus_x = 0
for i in x:
    i -= minus_x
    minus_y = 0
    for j in y:
        j -= minus_y
        a = i * j
        if a > first:
            second = first
            first = a
        elif a > second:
            second = a
        minus_y += j
    minus_x += i
print(first, second)
