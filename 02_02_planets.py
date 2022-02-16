# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self,name,color,system,time_to_orbit,star):
        
        
      
        self.name=str(name)
        self.color=str(color)
        self.system=str(system)
        self.time_to_orbit=int(time_to_orbit)
        self.star=str(star)

    def __str__(self):
        return (f"Planet: {self.name} is color: {self.color},it is on the: {self.system} and needs {self.time_to_orbit} days to complete a turn around the {self.star}")

if __name__ == '__main__':
    earth=Planet('earth','blue','solar system','365','sun')
    print(earth)

    mars=Planet('mars','red','solar system','687','sun')
    print(mars)
