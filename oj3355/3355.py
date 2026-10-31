'''Shorten'''
num_list = []
while True:
    num = int(input())
    if num == -1:
        break
    num_list.append(num)
short_list = []
i = 0
while i < len(num_list):
    j = i
    while j + 1 < len(num_list) and num_list[j + 1] == num_list[j] + 1:
        j += 1
    if j > i:
        short_list.append(f"{num_list[i]}-{num_list[j]}")
    else:
        short_list.append(str(num_list[i]))
    i = j + 1
print(", ".join(short_list))
