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


class LoopGame():
    
      


    def loop_game(self,players,enemies):
        life_p=self.total_player_life(players)
        life_e=self.total_enemy_life(enemies)
        
        for player in players:
            print(player.stats())
        for enemy in enemies:
            print(enemy.stats())
        
        
        while life_p>0 and life_e>0:
           

            for player in players:
                if player.life>0:
                    self.player_turn(player,enemies)
                
            for enemy in enemies:
                if enemy.life>0:
                    self.enemy_turn(players,enemy)
            print('Current State') 
            for player in players:
                print(player.stats())
            for enemy in enemies:
                print(enemy.stats())
            
            life_p=self.total_player_life(players)
            life_e=self.total_enemy_life(enemies)
        

    def player_turn(self,player,enemies):
            print(f'{player.name} turn')
            
            #Check that unit selected isn ot dead
            valid=True
            while valid:          
                print('Choose your objective:')
                for i in range(0,len(enemies)):
                    print(str(i)+':'+enemies[i].name)
                objective=int(input())
                if enemies[objective].life>0:
                        
                    valid=False
                else:
                    print('Selected enemy dead!!!, Choose again')

            print("Choose your action:1 attack the enemy, 2:Recover health")
            decision=int(input())
            print('\n')
            if decision==1:
                if enemies[objective].life<0:
                    pass

                else:
                    enemies[objective].take_damage(player)

                print(f'{player.name} attack:1{enemies[objective].name} has {enemies[objective].life} life points')
            elif decision==2:
                player.health()
                    


            

    def enemy_turn(self,players,enemy):
        print(f'{enemy.name} is going to attack!!')
        valid=True
        while valid:
            option=np.random.randint(low=0,high=len(players))
            print(option)
            if players[option].life>0:  
                
                valid=False
            else:
                print('Enemy choose other objective')
        players[option].take_damage(enemy) 

        print(f'{players[option].name} has received damage!!!, {players[option].life} life points')

    
    def total_player_life(self,players):
        self.all_life=0
        for player in players:
            self.all_life+=player.life
        return self.all_life

    def total_enemy_life(self,enemies):
        self.all_life_e=0
        for enemy in enemies:
            self.all_life_e+=enemy.life
        return self.all_life_e
        




class Player():
    def __init__(self,name,life,attack,recover):
        self.life=life
        self.name=name
        self.attack=attack
        self.recover=recover

    def __str__():
        return (f'This is your unit')

    def health(self):
        self.life+=self.recover

    def __add__(self,other):
        print('Summoning allied!!')
        new_name='Summoned Creature'
        new_life=int(self.life/2+other.life/3)
        new_attack=int(self.attack/3+other.attack/3)
        new_recover=0
        return Player(new_name,new_life,new_attack,new_recover)
    
    def take_damage(self,enemy):
        self.life-=enemy.attack
        if self.life<=0:
            print(f'{self.name} is dead')
            self.life=0

    def stats(self):
       
        return(f'Name: {self.name}, life:{self.life},attack power:{self.attack}')




class Enemy():
    def __init__(self,name,life,attack):
        self.name=name
        self.life=life
        self.attack=attack

    def __str__(self):
        return (f'This is an enemy: you have to battle it')

    def take_damage(self,player):
        self.life-=player.attack
        if self.life<=0:
            print(f'{self.name} is dead')
            self.life=0

    def stats(self):
         return(f'Name: {self.name}, life:{self.life},attack power:{self.attack}')

if __name__=='__main__':

    player=Player('Player',50,10,5)
    enemy=Enemy('Skull',25,15)
    dragon=Enemy('Dragon',30,20)
    other_player=Player('Yo',20,15,20)
    player_list=[]
    player_list.append(player)
    player_list.append(other_player)
    enemy_list=[]
    enemy_list.append(enemy)
    enemy_list.append(dragon)

    loop=LoopGame()
    loop.loop_game(player_list,enemy_list)