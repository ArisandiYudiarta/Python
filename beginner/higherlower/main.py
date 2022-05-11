from game_data import data
import random
from art import logo, vs
import os
clear = lambda: os.system('cls')

# function to pick random data
def generate_person():
    person = random.choice(data)
    return person

# function to compare the data
def comparison(a, b):
    if a > b:
        return "A"
    elif b > a:
        return "B"

# keep track of the score
def add_score(score):
    score += 1
    return score

# loop the game until user gets it wrong
def game():
    side_a = generate_person()
    score = 0
    end = False
    
    while not end:
        print(logo)
        side_b = generate_person()
        
        if score > 0:
            print(f"You're correct! current score : {score}")
        
        print(f"Compare A: {side_a['name']}, a {side_a['description']}, from {side_a['country']}")
        print(side_a['follower_count'])  
        print(vs)
        print(side_b['follower_count'])
        print(f"Compare B: {side_b['name']}, a {side_b['description']}, from {side_b['country']}")
        user_choice = input("Who has more follower? : Type 'A' or 'B' : ")
        
        result = comparison(side_a['follower_count'],side_b['follower_count'])
        print(result)
        if result != user_choice.upper():
            clear()
            print(logo)
            print(f"Sorry That's wrong, Final score : {score}")
            end = True
        elif result == user_choice.upper():
            score = add_score(score)
            if result == "B":
                side_a = side_b
            clear()
game()
    