'''แถบดอกไม้'''
L, N = map(int, input().split())
k = 0
cumulative = 0
while True:
    s = k * L * L + L * (L + 1) // 2
    cumulative += s
    if cumulative >= N:
        print(k + 1)
        break
    k += 1
