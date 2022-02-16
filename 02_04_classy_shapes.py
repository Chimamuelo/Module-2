# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

from cmath import pi


class Rectangle():
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width

    def __str__(self):
        return (f'A rectangle is a geometric shape that all its interior angles form right angles')

    def area_perimeter(self):
        self.result=[]
        area=self.lenght * self.width
        perimeter= 2*self.lenght+2*self.width
        self.result.append(area)
        self.result.append(perimeter)
        print(self.result)


class Circle():
    def __init__(self,radius):
        self.radius=radius
        

    def __str__(self):
        return (f'A circle is a closed curve that all the points in the curve have the same distance from the center')

    def area_circumference(self):
        self.result=[]
        area=self.radius**2 * pi
        circumference= 2*self.radius*pi
        self.result.append(area)
        self.result.append(circumference)
        print(self.result)
    
    
if __name__=='__main__':   
    circle=Circle(1)
    print(circle)
    circle.area_circumference()


    rectangle=Rectangle(4,6)
    print(rectangle)
    rectangle.area_perimeter()