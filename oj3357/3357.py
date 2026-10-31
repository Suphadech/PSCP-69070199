'''Giraffe'''
quantity = int(input())
lis = []
for _ in range(quantity):
    num = int(input())
    lis.append(num)
count = 0
if quantity == 1:
    count += 1
else:
    for i in range(quantity):
        if not i and lis[i] > lis[i+1]:
            count += 1
        elif i == quantity-1 and lis[i] > lis[i-1]:
            count += 1
        elif lis[i-1] < lis[i] and lis[i] > lis[i+1]:
            count += 1
print(count)
