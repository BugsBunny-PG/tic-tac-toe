import random
import sys
print("^_^welcome to tic tac toe game")
number=[0,1,2,3,4,5,6,7,8]
def tic_tac_toe():    
  print(number[0],"|",number[1],"|",number[2])
  print("-"*10)
  print(number[3],"|",number[4],"|",number[5])
  print("-"*10)
  print(number[6],"|",number[7],"|",number[8])

def ran_select():
      z=random.randint(0,8)
      if number[z]!='o' and number[z]!='x':
        number[z]='o'
        if checkwin('o')==True:
            tic_tac_toe()
            print("congratulations_O_win  ^_^")
            sys.exit()
        if if_tie()==True:
             sys.exit()
        else:    
            tic_tac_toe()
            game()    
      else:
          ran_select()  #random select number already oocupied then again select
    
              
def game():
  select=int(input("enter number to select a block"))
  if number[select]!='o' and number[select]!='x':
    number[select]='x' 
    if checkwin('x')==True:
       tic_tac_toe()
       print("congratulation_X_win ^_^")
       sys.exit()
    if if_tie()==True:
          sys.exit()
    else:
      ran_select()
  else:
    print("block is already taken")
    game()

def checking(char,block1,block2,block3):
   if number[block1]==char and number[block2]==char and number[block3]==char:
     return char    

def checkwin(char):
  if  checking(char,0,1,2):
      return True
  elif checking(char,3,4,5):
      return True
  elif checking(char,6,7,8):
    return  True
  elif checking(char,0,3,6):
    return True
  elif checking(char,1,4,7):
    return True
  elif checking(char,2,5,8):
    return True
  elif checking(char,2,4,6):
     return True
  elif checking(char,0,4,8):
     return True
def if_tie():
  count=0
  for a in range(9):
             if number[a]=='x' or number[a]=='o':
               count+=1
               if count==9:
                  print("GAME DRAW")
                  return True

tic_tac_toe()
game()



        
