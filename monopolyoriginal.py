import os
import random
import time

ownership=[,"-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
squares=["",0,"",1,"",2,3,"",4,5,"",6,7,8,9,10,11,12,"",13,"",14,"",15,16,17,18,19,20,21,"",22,23,"",24,25,"",26,"",27]
value=[60,60,200,100,100,120,140,150,140,160,200,180,180,200,220,220,240,200,260,260,150,280,300,300,320,200,350,400]
rent=[2,4,"r",6,6,8,10,"u",10,12,"r",14,14,16,18,18,20,"r",22,22,"u",24,26,26,28,"r",35,50]
players=["r","g","b","y"]
cash=[1500,1500,1500,1500]
player_position=[0,0,0,0]
current_player=0

def print_board():
    alist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,4):
        if alist[player_position[i]]==0:
            alist[player_position[i]] = players[i]
    print (" "," ",ownership[14]," ",ownership[15],ownership[16],ownership[17],ownership[18],ownership[19],ownership[20],ownership[21]," "," ")
    print (" ",alist[20],alist[21],alist[22],alist[23],alist[24],alist[25],alist[26],alist[27],alist[28],alist[29],alist[30]," ")
    print (ownership[13],alist[19],"                 ",alist[31],ownership[22])
    print (" ",alist[18],"                 ",alist[32]," ")
    print (ownership[12],alist[17],"                 ",alist[33],ownership[23])
    print (ownership[11],alist[16],"                 ",alist[34],ownership[24])
    print (ownership[10],alist[15],"    Monopoly     ",alist[35],ownership[25])
    print (ownership[9],alist[14],"                 ",alist[36]," ")
    print (ownership[8],alist[13],"                 ",alist[37],ownership[26])
    print (ownership[7],alist[12],"                 ",alist[38]," ")
    print (ownership[6],alist[11],"                 ",alist[39],ownership[27])
    print (" ",alist[10],alist[9],alist[8],alist[7],alist[6],alist[5],alist[4],alist[3],alist[2],alist[1],alist[0]," ")
    print (" "," ",ownership[5],ownership[4]," ",ownership[3],ownership[2]," ",ownership[1]," ",ownership[0]," "," ")
    print("r: ", cash[0])
    print("g: ", cash[1])
    print("b: ", cash[2])
    print("y: ", cash[3])

def turn():
    print_board()
    a=random.randint(1,6)
    b=random.randint(1,6)
    dice_roll=a+b
    global current_player
    global cash
    global squares
    global values
    global ownership
    player_position[current_player]=player_position[current_player]+dice_roll
    if player_position[current_player]>=40:
        cash[current_player]=cash[current_player]+200
        player_position[current_player]=player_position[current_player]-40
    if squares[player_position[current_player]]!="":
        if ownership[squares[player_position[current_player]]]=="-":
            cash[current_player]=cash[current_player]-value[squares[player_position[current_player]]]
            ownership[squares[player_position[current_player]]]=players[current_player]
        elif rent[player_position[current_player]]=="r":
            raailroads=0
            if ownership[5]==ownership[player_position[current_player]]:
                railroads=railroads+1
            if ownership[15]==ownership[player_position[current_player]]:
                railroads=railroads+1
            if ownership[25]==ownership[player_position[current_player]]:
                railroads=railroads+1
            if ownership[35]==ownership[player_position[current_player]]:
                railroads=railroads+1
            cash[current_player]=cash[current_player]-(25*(2^railroads))
            cash[ownership[player_position[current_player]]]=cash[ownership[player_position[current_player]]]+(25*railroads)  
        elif ownership[squares[player_position[current_player]]]!="-":
            cash[current_player]=cash[current_player]-rent[squares[player_position[current_player]]]
            cash[ownership[player_position[current_player]]]=cash[ownership[player_position[current_player]]]+rent[squares[player_position[current_player]]]
    current_player=current_player+1
    current_player=current_player%4
    time.sleep(1)
    os.system("cls")
    

while 1==1:
    turn()

