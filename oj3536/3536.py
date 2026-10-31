'''Primenumber'''
number = int(input())
is_prime = True
if number == 2:
    is_prime = True
elif not number % 2:
    is_prime = False
elif number == 1:
    is_prime = False
else:
    limit = int(number**0.5)
    for i in range(3,limit+1,2):
        if not number % i:
            is_prime = False
print("YES" if is_prime else "NO")
