numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)

numbers.insert(2, 3)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.clear()
print(numbers)

numbers = [5,2,1,7,4]
numbers.pop()
print(numbers)

print(numbers.index(1))

is50there = 50 in numbers
print(f"esta el numero 50 ahi", is50there)

print(f"El number de 5s es:" ,numbers.count(5))

print(f"Vamos a ordenar la lista ahora")
numbers.sort()
print(numbers)

print("La lista de mayor a menor")
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)
