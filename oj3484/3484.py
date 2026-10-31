'''หุ่นยนต์เคาะเสียงกระเบื้อง'''
n, p = input().split()
n = int(n)
p = float(p)

grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

col_tiles = [0] * n
col_dots = [0] * n
all_tiles = 0
all_dots = 0

for i in range(n):
    row_tiles = 0
    row_dots = 0
    for j in range(n):
        v = grid[i][j]
        if v > 0:
            row_tiles += 1
            col_tiles[j] += 1
        row_dots += v
        col_dots[j] += v
    print(" ".join(map(str, grid[i])), row_tiles, row_dots)
    all_tiles += row_tiles
    all_dots += row_dots

print(" ".join(map(str, col_tiles)))
print(" ".join(map(str, col_dots)))
print(all_tiles, all_dots, format(all_dots * p, ".2f"))
