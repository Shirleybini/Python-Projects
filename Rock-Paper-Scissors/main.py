import random

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

choose = int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
CompChoose = random.randint(0, 2)
RPS = [rock, paper, scissors]


if choose >= 3 or choose < 0:
    print("invalid number")
else:
    print("You chose", RPS[choose])
    print("Computer Chose\n", RPS[CompChoose])

    if choose == CompChoose:
        print("Draw")
    elif (choose == 0 and CompChoose == 1) or (choose == 1 and CompChoose == 2) or (choose == 2 and CompChoose == 0):
        print("You lose.")
    else:
        print("You win.")
