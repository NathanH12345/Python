import random
r = random.randint(1,3)

if r == 1:
  computer = "Rock"
elif r == 2:
  computer = "Scissors"
elif r == 3: 
  computer = "Paper"


player = str(input("Rock, Paper, Scissors? "))
print("")
print("You chose: "+player)
print("")
print("We pick: " + computer)

if player == "rock" or player == "Rock":
  value = 1
  equal = 1
elif player == "paper" or player == "Paper":
  value = 99
  equal = 3
elif player == "Scissors" or player == "scissors" or player == "Scissor" or player == "scissor":
  value  = 10
  equal = 2
else:
  print("NOT AN VALID ANSWER")


  #value_1 = rock value_2 = scissors value 3 = paper


if value == 1 and r == 2: #rock and scissor
  print("\nYOU WIN!")
elif value == 99 and r == 1: #paper and rock
  print("\nYOU WIN!")
elif value == 10 and r == 3: #scissor and paper
  print("\nYOU WIN!")
elif equal == r:
  print("\nTIE, GO AGAIN")
else:
  print("\nYOU LOSE!")
#if equal == r:
 # print("GO AGAIN!")
  
  
  
  a = 0
  b = a
  i = "h"
  while True: 
    if i == "h":
      a = a + 1 + b
      b = a +2
      c = a * b
      d = c // a
      o = a * d
      print(o)
  
