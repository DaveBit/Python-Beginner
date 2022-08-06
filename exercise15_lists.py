"""
name = ['John', 'Bob', 'Mosh', 'Sarah', 'Maggie']
print(name[2])
print(name[-1])
print(name[2:4])
print(name[:])
"""
longest_string = ""
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Maggie']
longest_string = max(names, key=len)
print("The longest string is " + longest_string)

numbers = [3,6,2,8,4,10,6,22,35,2,53,13]
"""max = numbers[0]
for x in numbers:
    if x>max:
        max = x
print(f"The biggest number is {max}")"""

biggest_number = max(numbers)
print(f"The biggest number is {biggest_number}")