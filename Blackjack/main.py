# ------------ Blackjack Project ------------

# ------------ Our Blackjack House Rules ------------

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


from art import logo
import os
import random


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    # 11 is the Ace.
    return random.choice(cards)


def calculate_score(A):
    """takes a List of cards as input and returns the score. """
    S = sum(A)
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if S == 21 and 11 in A:
        return 0

    # check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    if S > 21 and 11 in A:
        A.remove(11)
        A.append(1)

    return sum(A)


def compare(User_Score, Comp_Score):
    if User_Score > 21 and Comp_Score > 21:
        print("You lose")
    if User_Score == Comp_Score:
        print("draw")
    elif Comp_Score == 0:
        print("Opponent wins with Blackjack")
    elif User_Score == 0:
        print("You win with Blackjack")

    elif User_Score > 21:
        print("You lose.")
    elif Comp_Score > 21:
        print("You win")
    else:
        if User_Score > Comp_Score:
            print("You win")
        else:
            print("You lose")


# If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
def play_game():
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            choose = input("Hit(y or n): ")
            if choose == "y":
                user_cards.append(deal_cards())

            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)


# The score will need to be rechecked with every new card drawn and the checks need to be repeated until the game ends.
# Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
# Ask the user if they want to restart the game. If they answer yes, start a new game of blackjack.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_console()
    play_game()
