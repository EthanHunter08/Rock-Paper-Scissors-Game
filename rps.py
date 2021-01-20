import random

rps = ["rock", "paper", "scissors"]
pScore = 0
aiScore = 0
rndmPick = ""
playerChoice = ""

def logic(rps, pScore, aiScore, rndmPick, playerChoice):

  rndmPick = random.choice(rps)
  playerChoice = input("Rock paper scissors. Enter r, p or s to choose\n")

  print(f"Ai chose{rndmPick}\n")

  # if player choice is rock then...
  if playerChoice == "r" and rndmPick == "rock":
    print("You Draw!")
    print(f"You:{pScore}", f"Ai:{aiScore}")
  elif playerChoice == "r" and rndmPick == "paper":
    print("You lose!")
    aiScore += 1
    print(f"You:{pScore}", f"Ai:{aiScore}")
  elif playerChoice == "r" and rndmPick == "scissors":
    print("You win!")
    pScore += 1
    print(f"You:{pScore}", f"Ai:{aiScore}")

  # if player choice is paper then...
  elif playerChoice == "p" and rndmPick == "rock":
    print("You win!")
    pScore += 1
    print(f"You:{pScore}", f"Ai:{aiScore}")
  elif playerChoice == "p" and rndmPick == "paper":
    print("You draw!")
    print(f"You:{pScore}", f"Ai:{aiScore}")
  elif playerChoice == "p" and rndmPick == "scissors":
    print("You lose!")
    aiScore += 1
    print(f"You:{pScore}", f"Ai:{aiScore}")

  #if player choice is scissors then...
  elif playerChoice == "s" and rndmPick == "rock":
    print("You lose!")
    aiScore += 1
    print(f"You:{pScore}", f"Ai:{aiScore}")
  elif playerChoice == "s" and rndmPick == "paper":
    print("You win!")
    pScore += 1
    print(f"You:{pScore}", f"Ai:{aiScore}")
  elif playerChoice == "s" and rndmPick == "scissors":
    print("You draw!")
    print(f"You:{pScore}", f"Ai:{aiScore}")
  logic(rps, pScore, aiScore, rndmPick, playerChoice)

logic(rps, pScore, aiScore, rndmPick, playerChoice)
