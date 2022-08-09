is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Get warm clothes")
else:
    print("It's a lovely day")

house_price = 1_000_000
print(house_price)

good_credit = False

if good_credit:
    down_payment = house_price*.10
else:
    down_payment = house_price*.20

#print("The down payment is: ", down_payment)
print(f"The down payment is: ${down_payment}")
