numbers = [1,2,2,2,3,5,4,4,5,7,8,9,10,10]

for number in numbers:
    numberCount = numbers.count(number)
    if numberCount>1:
        numbers.remove(number)
numbers.sort()
print(numbers) 

## the below is the solution proposed by the lecturer. 

numbers2 = [2,2,4,6,4,4,6,2,1,1]
uniques = []

for number in numbers2:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)

