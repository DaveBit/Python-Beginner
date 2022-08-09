class Point:
    #pascal naming convention, classes have first letter in capital. 
    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point1 = Point()
Point1.x = 10
print(Point1.x)
"""
Point1 = Point()
Point1.x = 10 #you can set the attributes out of the class. 
Point1.y = 20
print(Point1.x)
Point1.draw()


Point2 = Point()
print(Point2.x)
"""