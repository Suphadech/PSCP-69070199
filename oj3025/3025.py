"""aaa"""
mon = int(input())
day = int(input())

if mon in (1,2,3):
    if mon == 3:
        if day >= 21:
            print("spring")
        else:
            print("winter")
    else:
        print("winter")
elif mon in (4,5,6):
    if mon == 6:
        if day >= 21:
            print("summer")
        else:
            print("spring")
    else:
        print("spring")
elif mon in (7,8,9):
    if mon == 9:
        if day >= 21:
            print("fall")
        else:
            print("summer")
    else:
        print("summer")
elif mon in (10,11,12):
    if mon == 12:
        if day >= 21:
            print("winter")
        else:
            print("fall")
    else:
        print("fall")
