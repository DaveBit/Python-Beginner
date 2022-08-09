class Point:
    #pascal naming convention, classes have first letter in capital. 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point1 = Point(10, 20)
Point1.x = 11
print(Point1.x)