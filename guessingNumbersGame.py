import random 

number = random.randint(1,10)
chances=0

while chances < 5:
  
 Guess=input("A number has been chosen between 1 to 10,Your task is to Guess a number between (1 to 10):")
 print(Guess)   
 chances=chances+1    

 if int(Guess) == int(number):
  print("YOU WON !!! CONGRATULATIONS, YES THE CORRECT NUMBER WAS:-",number)   
  break

 elif  chances  == 5:
  print("YOU ARE A LOSER , I UNDERSTAND THE FEELING. THE NUMBER WAS:",number)
  
