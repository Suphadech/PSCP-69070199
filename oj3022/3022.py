'''Temparature'''
temp = float(input())
unit_1 = input()
unit_2 = input()
celcius = 0

if unit_1 == "C":
    celcius = temp
elif unit_1 == "K":
    celcius = temp - 273.15
elif unit_1 == "F":
    celcius = ((temp - 32) * 5) / 9
elif unit_1 == "R":
    celcius = ((temp * 5) / 9) - 273.15

if unit_2 == "C":
    print(f"{celcius:.2f}")
elif unit_2 == "K":
    print(f"{(celcius + 273.15):.2f}")
elif unit_2 == "F":
    print(f"{(((celcius * 9) / 5) + 32):.2f}")
elif unit_2 == "R":
    print(f"{(((celcius + 273.15) * 9) / 5):.2f}")
