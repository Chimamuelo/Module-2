# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...
import math
import numpy as np

#2D vector class

class Vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return (f'A vector ({self.x},{self.y}) has magnitude and direction')

    #Vector addition results in another vector
    def __add__(self,other):
        new_vector=[self.x+other.x,self.y+other.y]
        return Vector(*new_vector)

    def magnitude(self):
        magnitude= math.sqrt(self.x**2+self.y**2)
        return magnitude

    #Dot product between two vectors(scalar)
    def dot(self,other):
        dot_product=(self.x*other.x)+(self.y*other.y)
        return dot_product

    #Cross product result in new vector perpendicular to the input vectors
    def cross(self,other):
        cross_product=(self.x*other.y)-(self.y*other.x)
        return cross_product


if __name__=='__main__':

    A=Vector(3,4)
    B=Vector(2,6)
    C=A+B

    print(A)
    print(A.magnitude())
    #print(np.linalg.norm((A.x,A.y)))
    print(B)
    print(C.magnitude())
    print(A.dot(B))
    #print(np.dot((A.x,A.y),(B.x,B.y)))
    print(A.cross(B))
