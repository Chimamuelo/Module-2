import numpy as np

class Hero():
    def __init__(self,name,level,start_location):
        self.name=name
        self.level=level
        self.start=start_location

    def __str__(self):
        return(f'This is the hero of the world')

    def battle(self,other):
        hero_attack=np.random.randint(1,6)*self.level
        monster_attack=np.random.randint(1,6)*other.level

        if hero_attack>monster_attack:
            print(f'{self.name} wins the battle')
            return True
        else:
            print(f'{other.name} wins the battle \n {self.name} must retreat for now')
            return False




class Monster:
    def __init__(self,name,level,start_location):
        self.name=name
        self.level=level
        self.start_location=start_location
    
    def __str__(self):
        return (f'This is {self.name} level {self.level}')