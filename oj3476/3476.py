'''Fubuki'''
n = int(input())

cats = {}
foxes = {}

for _ in range(n):
    line = input()
    parts = line.split('"')
    for j in range(1, len(parts) - 2, 4):
        name = parts[j].strip()
        code = parts[j + 2].strip()
        num = int(code[3:])
        if code[:3].upper() == "CAT":
            cats[num] = name
        else:
            foxes[num] = name

used = list(cats.values()) + list(foxes.values())
if 1 not in cats and "Garfield" not in used:
    cats[1] = "Garfield"
if 1 not in foxes and "Fubuki" not in used:
    foxes[1] = "Fubuki"

print("Cat :", len(cats))
print("Fox :", len(foxes))

for num in sorted(cats.keys()):
    print(cats[num], " : Cat", str(num).zfill(2), sep="")
for num in sorted(foxes.keys()):
    print(foxes[num], " : Fox", str(num).zfill(2), sep="")
