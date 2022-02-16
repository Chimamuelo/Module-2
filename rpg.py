from re import A
import char_rpg as char
import numpy as np
import time

class Game():

    def game_loop(self,hero,monsters):
        pass
        playing=True

        while playing:
            if enemies:
            
                self.movement(hero,enemies)

                print(board)

            
                
            else:
                playing=False
                print(f'{hero.name} has defeated all enemies\n The land is free!!!')


            
    def movement(self,hero,enemies):
        print('Move with the wasd keys')
        print('w:up\na:left\ns:down\nd:right')

        move=str(input('Move\n'))
        while move not in ['w','s','a','d']:
            print("Not Valid, Choose again")
            print('w:up\na:left\ns:down\nd:right')
            move=str(input('Move'))

        #Movement logic
        if move=='a':
            board[hero.start[0]][hero.start[1]]=''
            hero.start[1]-=1
            if hero.start[1]<=0:
                hero.start[1]=0

            x=self.check_board(hero,enemies)
            if x:
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'
            else:
                hero.start[1]+=1
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'
            
        elif move=='d':
            board[hero.start[0]][hero.start[1]]=''
            hero.start[1]+=1
            if hero.start[1]>=4:
                hero.start[1]=4

            x=self.check_board(hero,enemies)
            if x:
                print('w')
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'
            else:
                print('l')
                hero.start[1]-=1
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'

            
            
        elif move=='w':
            board[hero.start[0]][hero.start[1]]=''
            hero.start[0]-=1
            if hero.start[0]<=0:
                hero.start[0]=0
            x=self.check_board(hero,enemies)
            if x:
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'
            else:
                hero.start[0]+=1
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'
            
            
        elif move=='s':
            board[hero.start[0]][hero.start[1]]=''
            hero.start[0]+=1
            if hero.start[0]>=4:
                hero.start[0]=4
            x=self.check_board(hero,enemies)
            if x:
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'
            else:
                hero.start[0]-=1
                board[hero.start[0]][hero.start[1]]=f'{hero.name}'
            



    def check_board(self,hero,enemies):
        enemy=[l for l in enemies if l.start_location==hero.start]
        
        if enemy:
            print(f'{enemy[0].name} is in your way!!!')
            if hero.battle(enemy[0]):
                win=True
                enemies.remove(enemy[0])
            else:
                win=False
        else:
            win=True
            print('Free path')
        time.sleep(1)
        return win
            
                

        
                

    
            

board=np.zeros((6,6),dtype=str)

for i in range(len(board[0])):
    for j in range(len(board[1])):
        board[i][j]=''



def start_location():
    start_xlocation=np.random.randint(0,4)
    start_ylocation=np.random.randint(0,4)
    start=[start_xlocation,start_ylocation]
    return start

enemies=[
    char.Monster('Dragon',10,start_location()),
    char.Monster('Goblin',3,start_location()),
    char.Monster('Bandit',6,start_location()),
    char.Monster('King of Evil',30,start_location()),

    
    ]
hero=char.Hero('Hero',15,start_location())
board[hero.start[0]][hero.start[1]]= f'{hero.name}'
for enemy in enemies:
    if board[enemy.start_location[0]][enemy.start_location[1]]:
        new_loc=start_location()
        enemy.start_location=new_loc
        board[new_loc[0],new_loc[1]]=f'{enemy.name}'
    else:
        board[enemy.start_location[0]][enemy.start_location[1]]=f'{enemy.name}'



print(board)
game=Game()
game.game_loop(hero,enemies)





