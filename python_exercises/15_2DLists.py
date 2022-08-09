matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print("Items in a row")
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

print("Iterating on the first item")
for x in matrix[0]:
    print(x)