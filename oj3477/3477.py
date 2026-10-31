'''padthai'''
recipe = {"Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
          "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"}
need_taste = {"Sweet", "Sour", "Salty"}

ingredients = set()
while True:
    s = input().strip()
    if s == "Cook":
        break
    ingredients.add(s)

tastes = set()
while True:
    s = input().strip()
    if s == "End":
        break
    tastes.add(s)

if not ingredients.issubset(recipe):
    print("This is not Pad Thai!!!")
elif ingredients != recipe:
    print("This is bad!")
elif tastes != need_taste:
    print("Not Bad...")
else:
    print("Delicious!")
