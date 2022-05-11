from art import logo
import random

EASY_LEVEL_LIFES = 10
HARD_LEVEL_LIFES = 5

def compare_number(users_guess, the_answer, life):
    if users_guess > the_answer:
        print("too beeg")
        life -= 1
        return life
    elif users_guess < the_answer:
        print("too smol")
        life -= 1
        return life
    if users_guess == the_answer:
        print("true")

def set_difficulty():
    diff = input("Choose your difficulty, 'easy' or 'hard' : ")
    if diff == "easy":
        return EASY_LEVEL_LIFES
    elif diff == "hard":
        return HARD_LEVEL_LIFES

        
def game():
    print(logo)
    
    answer = random.randint(1,100)
    print("Number guessing game")
    life = set_difficulty()
    print(f"Answer = {answer}")
    
    guess = 0
    while guess != answer:
        print(f"You have {life} attempts remaining to guess the number")
        guess = int(input("Make a guess : "))
        life = compare_number(guess, answer, life)
        if life == 0:
            print("You ran out of life")
            return

game()
