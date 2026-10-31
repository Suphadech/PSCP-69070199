'''Amogus'''
alive = {}
dead = {}
while True:
    text = input().replace(" ","")
    if text == "Start":
        break
    player,role = text[2:-2].split(":")
    player = player.strip(' "')
    role = role.strip(' "')
    alive[player] = role

while True:
    name = input()
    if name == "End":
        break
    dead[name] = alive.pop(name)
imposter_remain = list(alive.values()).count("Impostor")
print(f"{imposter_remain} Impostor Remains")
print("***Alive***")
for i in sorted(alive):
    print(f"{i} : {alive[i]}")
print("***Dead***")
for j in sorted(dead):
    print(f"{j} : {dead[j]}")
