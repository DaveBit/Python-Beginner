coordinates = (1,2,3)
## there are better ways to do that, using unpacking. 
# coordinates[0] * coordinates[1] * coordinates[3] 
# you can also assign every item to a different variable. 
# x = coordinates [0] etc. 
# y = coordinates [1]
# z = coordinates [2]

x, y, z = coordinates
print(x,y,z)

coordinates2 = [1,2,3]
a,b,c = coordinates2
print(a,b,c)