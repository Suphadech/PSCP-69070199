'''Mix The Color'''
color1 = input().capitalize()
color2 = input().capitalize()
if (color1 == "Red" and color2 == "Blue") or (color2 == "Red" and color1 == "Blue"):
    print("Violet")
elif (color1 == "Red" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Red"):
    print("Orange")
elif (color1 == "Blue" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Blue"):
    print("Green")
elif color1 == "Red" and color2 == "Red":
    print("Red")
elif color1 == "Yellow" and color2 == "Yellow":
    print("Yellow")
elif color1 == "Blue" and color2 == "Blue":
    print("Blue")
else :
    print("Error")
