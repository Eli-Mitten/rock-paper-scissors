rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

seed = input("Whrite seed\n")

drawingChoices = [rock, paper, scissors]

computerChoice = random.randint(0, 2)

tie = "Tie"
lose = "Lose"
win = "win"

result = [[tie,lose,win],[win,tie,lose],[lose,win,tie]]
# Compara
playerChoice = int(input("Select your choice: rock = 0, paper = 1, scissors = 2"))

print(drawingChoices[playerChoice], drawingChoices[computerChoice], result[playerChoice][computerChoice])

"""
	0	1	2
0 t	l	w
1	w	t	l
2	l	w	t
"""
