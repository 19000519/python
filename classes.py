#a class is an undefined type that we want to use in our programs
class Point:
    #this is to intitialize the objects using the points aka constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def is the method defined inside a a class 
    def move(self):
        print("move")

    def draw(self):
        print("draw")


Point1 = Point(10, 20)
print(Point1.x)
Point1.draw()