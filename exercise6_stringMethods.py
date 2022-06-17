course = "Python for Beginners"
print(len(course)) #print and len do not belong to strings.
 #upper belongs to strings.
course_upper = course.upper()
print(course)
print(course_upper)
print(course.lower())
print(course.title())

print("the letter P is on the positions: ",course.find("P"))  #you can find letters, it's case sensitive. If -1, it's not there.


#You can also replace words and letters.

print(course.replace("Beginners","Absolute Beginners"))
print(course)

#Or find words in a string.
print('python' in course) #when using in, it returns a boolean, it is case sensitive.