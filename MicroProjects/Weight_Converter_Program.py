weight = int(input("What's your weight?"))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = round(weight * 0.45)
    print(f"You have {converted} kilos")
elif unit.upper() == "K":
    converted = round(weight / 0.45)
    print(f"You have {converted} pounds")
