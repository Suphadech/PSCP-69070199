'''point'''
n = int(input())
total = 0
for i in range(n):
    i += 1
    symbol = input()
    if symbol == '+':
        total += 10
    else:
        total -= 5
print(total)
