# First attempt below !!
# ==========================================================================================

# import random
# from replit import clear
# from art import logo

# def user_hits(users_cards, users_points, coms_cards):
#     print(f"User's deck : {users_cards},  your current score is : {users_points}")
#     print(f"Computer's first card is : {coms_cards[0]}")
#     user_hit = input("Type 'y' to get another card, type 'n' to pass : ")
#     return user_hit

# def result(user_points, com_points, user_cards, com_cards):
#     User_win = False
#     Draw = False
#     if user_points == com_points: 
#         Draw = True
#     elif user_points > 21 and com_points <=21:
#         User_win = False
#     elif com_points > 21 and user_points <=21:
#         User_win = True
#     elif user_points > com_points and com_points <= 21 and user_points <= 21:
#         User_win = True
#     elif com_points > user_points and user_points <= 21 and com_points <= 21:
#         User_win = False
#     elif user_points > com_points:
#         User_win = True
    
    
#     print("===========================================================")
#     print(f"User's deck : {user_cards},  your final score is : {user_points}")
#     print(f"Computer's deck : {com_cards},  computer's score is : {com_points}")
#     if Draw == True:
#         print("Welp is a Draw!")
#     elif User_win == True:
#         print("Congratulation, you won!")
#     elif User_win == False and user_points > 21:
#         print("You went over, you lost...")
#     elif User_win == False and user_points < 21:
#         print("You Lost...")
#     print("===========================================================")

# def blackjack(start_game):
#     clear()
#     # start of the loop 
#     while start_game is True:
#         print(logo)
        
#         cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        
#         user_cards = []
#         com_cards = []
    
#         # generating two random cards for the user and the computer
#         for i in range(2):
#             user_cards.append(random.choice(cards))
#             com_cards.append(random.choice(cards))
#         if user_cards == [11,11]:
#             user_cards[0] = 1;
#         if com_cards == [11,11]:
#             com_cards[0] = 1;

#         # Calculating the points
#         user_points = 0
#         com_points = 0
#         for i in user_cards:
#             user_points += i
#         for j in com_cards:
#             com_points += j

#         # Return the function if either cards equal to 21 points
#         if user_points >= 21 or com_points >= 21:
#             result(user_points, com_points, user_cards, com_cards)
#             break
        
#         # Displaying all the user's deck while only showing the first computer's deck
        
#         print(f"User's deck : {user_cards},  your current score is : {user_points}")
#         print(f"Computer's first card is : {com_cards[0]}")
#         user_hit = input("Type 'y' to get another card, type 'n' to pass : ")

#         # If user chooses to hit
#         while user_hit == "y":
#             new_user_card = random.choice(cards)
#             user_cards.append(new_user_card)
#             user_points += new_user_card
#             if user_points >= 21:
#                 break
#             user_hit = user_hits(user_cards, user_points, com_cards)  
            
            
#         # If the user is finished the deck
#         while com_points < 17:
#             new_com_card = random.choice(cards)
#             com_cards.append(new_com_card)
#             com_points += new_com_card

#         # calculating the result
#         result(user_points, com_points, user_cards, com_cards)
#         start_game = False
#         # break
            
#     another_round = input("Do you want to play again? type 'y' to play again, type 'n' to quit: ")
#     # another_round = input("yea? ")
#     if another_round == "y":
#         blackjack(start_game = True)
#     elif another_round == "n":
#         start_game == False
#         clear()
#         print("The game has ended, thanks for playing!")
    

# # First Output
# start_game = False
# user_decision = input("Do you want to play a game of blackjack? Type 'y' or 'n' : ")
# if user_decision.lower() == "y":
#     start_game = True
#     blackjack(start_game)
# elif user_decision.lower() == "n":
#     clear()
#     print("The program ended")

# =========================================================================================
# first attempt above

    
# +=-    


# THE BETTER SOLUTION BELOW!!!
# ============================================================================================

import random
from art import logo
import os
clear = lambda: os.system('cls')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score):
    """Takes all the score, compares them then returns the winner"""
    if user_score == computer_score:
        return "Draw!.."
    elif computer_score == 0:
        return "You Lost!, the computer has a blackjack!"
    elif user_score == 0:
        return "You Won!, You just got a blackjack!"
    elif user_score > 21:
        return "You went over!, You Lost..."
    elif computer_score > 21:
        return "You Won!, the computer went over!"
    elif user_score > computer_score:
        return "You Won!"
    else:
        return "you Lost!"


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range (2): 
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    User cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            break
        else:
            user_deals_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deals_card == "y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True
    
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"    Your final deck is {user_cards}, with score of: {user_score}")
    print(f"    The computer's final deck is {computer_cards}, with score of: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n':") == "y":
    clear()
    blackjack()
    
