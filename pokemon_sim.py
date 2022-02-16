
import pokemon
import numpy as np
class Loop():
    
    def loop_game(self,my_pokemons,enemy_pokemons):
     
        self.battle=True
    
          
        for player in my_pokemons:
            print(player.stats())
        for enemy in enemy_pokemons:
            print(enemy.stats())
        
        while self.battle:
        #while life_p>0 and life_e>0:
           

            for player in my_pokemons:
                if player.hp>0:
                    self.player_turn(player,enemy_pokemons)
                
            for enemy in enemy_pokemons:
                if enemy.hp>0:
                    self.enemy_turn(my_pokemons,enemy)
            print('Current State') 
            for player in my_pokemons:
                print(player.stats())
            for enemy in enemy_pokemons:
                print(enemy.stats())
            
            self.total_player_life(my_pokemons)
            self.total_enemy_life(enemy_pokemons)

    


    def player_turn(self,player,enemies):
        valid=True
        valid_2=True
        while valid_2:
            print(f'{player.name} turn')
            print('Choose your objective:')
            for i in range(0,len(enemies)):
                print(str(i)+':'+enemies[i].name)
            objective=int(input())  
            if objective not in range(0,len(enemies)):
                print('Not valid choice, Choose again')
                valid_2=True
            else:
                if enemies[objective].hp>0:
                    valid_2=False
                else:
                    print('Selected enemy dead!!!, Choose again')            
                #Check that unit selected isn ot dead
            
        while valid:          
              
            
            print("Choose your action \n 1 attack the enemy \n 2:Recover health \n 3:Run Away")
            decision=int(input())
            print('\n')
            if decision==1:
                valid=False
                enemies[objective].battle(player)

                
            elif decision==2:
                player.feed()
                valid=False
            elif decision==3:
                self.run_away()
                valid=False
                valid_2=False
                break
                
            
            else:
                valid=True
                print('Not valid choice, repeat your turn')


    def enemy_turn(self,players,enemy):
        print(f'{enemy.name} is going to attack!!')
        valid=True
        while valid:
            option=np.random.randint(low=0,high=len(players))
            print(option)
            if players[option].hp>0:  
                
                valid=False
            else:
                print(' choose other objective')
        print(players[option].battle(enemy))
        







    def total_player_life(self,my_pokemon):
        self.all_life=0
        for player in my_pokemon:
            self.all_life+=player.hp
        if self.all_life<=0:
            self.battle=False
             
        

    def total_enemy_life(self,enemy_pokemon):
        self.all_life_e=0
        for enemy in enemy_pokemon:
            self.all_life_e+=enemy.hp
        if self.all_life_e<=0:
            self.battle=False
            

    def run_away(self):
        print(f'Run away from this battle!!')
        self.battle=False
        



if __name__=='__main__':

    charmander=pokemon.Pokemon(str.lower('charmander'),str.lower('FIRE'),50,50)
    bulbasour=pokemon.Pokemon(str.lower('bulbasour'),str.lower('grass'),50,50)
    squirtle=pokemon.Pokemon(str.lower('squirtle'),str.lower('water'),50,50)
    fire_type=pokemon.Pokemon(str.lower('Fire'),str.lower('Fire'),50,50)

    my_pokemon=[]
    my_pokemon.append(charmander)
    my_pokemon.append(squirtle)

    enemy_pokemon=[]
    enemy_pokemon.append(bulbasour)
    enemy_pokemon.append(fire_type)

    loop_game=Loop()

    loop_game.loop_game(my_pokemon,enemy_pokemon)