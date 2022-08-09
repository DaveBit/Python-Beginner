#with dictionaries you can save key value pairs. 
#and the methos on them help you on avoiding errors.

customer = {
    "name": "John Smith", 
    "age": 30,
    "is_verified": True
}

## the line below would give an error cos there is no "Name"
#print(customer["Name"])

#using .get instead solves this. 
print(customer.get("price"))

customer["name"] = "Jack Smith"
print(customer["name"])

customer["birthdate"] = "1st of January 1989"
print(customer)
print(customer.get("birthdate"))


input("Phone\n")

numbers = {
    "1" : "one",
    "2" : "two",
    "3" : "tres",
    "4" : "cuatro",
    "5" : "cinco",
    "6" : "seis",
    "7" : "siete",
    "8" : "eight",
    "9" : "nine",
}
