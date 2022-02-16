class Pokemon():
    def __init__(self,name,primary_type,max_hp,hp):
        self.name=name
        self.primary_type=primary_type
        self.max_hp=max_hp
        self.hp=hp

    def __str__(self):
        return (f'Your Pokemon: {self.name} is type {self.primary_type} and has this stats max:{self.max_hp}, current hp{self.hp}')

    def battle(self,other):
        print(f'{self.name} battle vs {other.name}')
        rival_element=other.primary_type
        this_element=self.primary_type
        
        if rival_element != this_element:
            if this_element=='fire' and rival_element=='water':
                self.hp-=25
                print(f'{other.name} has won the battle,{self.name} : {self.hp} life points left')  

            elif this_element=='grass' and rival_element=='fire':
                self.hp-=25
                print(f'{other.name} has won the battle,{self.name} : {self.hp} life points left')  
            elif this_element=='water' and rival_element=='grass':
                self.hp-=25
                print(f'{other.name} has won the battle,{self.name} : {self.hp} life points left')    
            else:
                other.hp-=25
                print(f'{self.name} has won the battle,{other.name}: {other.hp} life points left ')     
        else:
            print('Drawn')
    
    def feed(self):
        self.hp+=10
        print(f'Give food to {self.name} \n {self.name} has recover hp, Current hp: {self.hp}')
        
        
        if self.hp>=self.max_hp:
            self.hp=self.max_hp

    def stats(self):
       
        return(f'Name: {self.name}, life:{self.hp},type:{self.primary_type}')

            

    
if __name__=='__main__':
    charmander=Pokemon(str.lower('charmander'),str.lower('FIRE'),50,50)
    bulbasour=Pokemon(str.lower('bulbasour'),str.lower('grass'),50,50)
    squirtle=Pokemon(str.lower('squirtle'),str.lower('water'),50,50)

    print(squirtle.battle(squirtle))
    print(squirtle.battle(bulbasour))
    print(squirtle.battle(charmander))
    
    print(charmander.battle(squirtle))
    print(charmander.battle(bulbasour))
    print(charmander.battle(charmander))

    print(bulbasour.battle(squirtle))
    print(bulbasour.battle(bulbasour))
    print(bulbasour.battle(charmander))