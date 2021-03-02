# Treasure Island


def start():

    print("\nWelcome to my mysterious Treasure Island.")
    print("\nYour mission is to find the hidden treasure.")

    user_choice = get_user_choice(
        '\nYou\'re at a cross road. Where do you want to go? - Type "left" or "right"\n'
    )

    if user_choice == 'left':
        go_left()
    elif user_choice == 'right':
        go_right()
    else:
        wrong_choice()


def get_user_choice(question):
    choice = input(question).lower().strip()
    return choice


def wait():
    # end game
    print(
        "\nYou arrive at the island and see a house with 3 doors. One red, one blue, and the last one is purple"
    )
    user_choice = get_user_choice(
        '\nWhich color do you choose? - Type "red", "green" or "purple"\n')

    if user_choice == 'red':
        print(
            "\nThere is a red button in the middle of the room, you press it. The door shuts and locks you inside, a fire starts and you're trapped..."
        )
        print_game_over()
    elif user_choice == 'green':
        print("\nYou found the hidden treasure!")
        print(get_treasure())

    elif user_choice == 'purple':
        print(
            '\nYou open the door, and a sudden explosion occurs inside the room...'
        )
        print_game_over()
    else:
        wrong_choice()


def go_left():
    # go to lake
    user_choice = get_user_choice(
        '\nYou have come to the lake and there\'s an island in the middle do you swim or wait for a boat? - Type "swim" or "wait" \n'
    )
    if user_choice == 'swim':
        swim()
    elif user_choice == 'wait':
        wait()
    else:
        wrong_choice()


def swim():
    # game over
    print(
        "\nA white shark comes near and bites you in the stomach, you manage to reach the island but you pass out and die."
    )


def wrong_choice():
    # game over
    print("\nYou don't feel so good and die...")
    print_game_over()


def print_game_over():
    print("\nGame Over.")


def go_right():
    # dies
    print(
        "\nThere's a giant hole in front of you, you slip... and fall to death"
    )
    print_game_over()


def get_treasure():
    return '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''


def main():
    start()


if __name__ == "__main__":
    main()