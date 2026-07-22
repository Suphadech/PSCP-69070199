'''divide 10'''
num = int(input())
for num in range(num,-1,-1):
    if not num % 10:
        print(num, end = " ")
