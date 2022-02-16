# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.


class Car():
    def __init__(self,model,year,max_speed):
        self.model=model
        self.year=year
        self.max_speed=int(max_speed)
    
    def __str__(self):
        return (f'This car is a:{self.model} year {self.year} that has a maximum speed of {self.max_speed} km/h')

    def tuning(self):
        self.max_speed+=5

    def printing(self):
        print(self.__str__())

if __name__=='__main__':

    nissan=Car('Nissan Versa',2021,200)
    print(nissan)
    nissan.tuning()
    print(nissan)
    toyota=Car('Toyota Tacoma',2021,"150")
    print(toyota)
    toyota.tuning()
    print(toyota)
    toyota.printing()