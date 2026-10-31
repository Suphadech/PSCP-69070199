'''Dupe'''
m = int(input())
n = int(input())
g1 = {input().strip() for _ in range(m)}
g2 = {input().strip() for _ in range(n)}

both = sorted(g1 & g2, key=int, reverse=True)
if both:
    for sid in both:
        print(sid)
else:
    print("Nope")
