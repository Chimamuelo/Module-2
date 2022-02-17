# Update the __add__() method of `Ingredient()` so that instead of
# instantiating the new Ingredient() object with an amount of 1,
# it'll take whichever amount of the passed ingredients is smaller
#
# Example:
# c = Ingredient("carrot", 5)
# p = Ingredient("pea", 4)
# s = c + p
# print(s)
# >>> OUTPUT: carrotpea (4)
import webbrowser


class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + other.name
        quantity=other.amount
        return Ingredient(name=new_name, amount=min(self.amount,quantity))
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

    def get_info(self):
        url="https://en.wikipedia.org/wiki/"
        webbrowser.open_new(url+self.name)


class Spice(Ingredient):
    
    def grind(self):
        print(f'you have {self.amount} of ground {self.name} ')

if __name__ == '__main__':
    c = Ingredient("carrot", 5)
    p = Ingredient("pea", 2)
    s = c + p
    print(s)
    #c.get_info()
    #s.get_info()
    spice=Spice('apple',5)
    spice.expire()