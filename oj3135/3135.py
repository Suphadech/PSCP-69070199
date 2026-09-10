'''I am a king of brianrots'''
n,k,t = map(int ,input().split())
current = 1
count = 1
if current == t:
    print(count)
else:
    while True:
        current = (current - 1 + k) % n + 1
        if current == 1:
            break
        count += 1
        if current == t:
            break
    print(count)
