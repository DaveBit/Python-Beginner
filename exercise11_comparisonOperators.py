# == >= <= !=
temp = 30
if temp > 30:
    print("hot day")
else:
    print("It's not a hot day")

name = input("What's your name?")
if len(name)<3:
    print(f"{name} is too short")
elif len(name)>50:
    print("name can't be that long")
else:
    print(f"{name} looks good")