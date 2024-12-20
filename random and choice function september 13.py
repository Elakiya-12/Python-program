#question 1 
import random
def roll_dice():
    while True:
        user_input = input("Type 'roll' to roll the dice or 'exit' to quit: ").lower()
        if user_input == "roll":
            print(f"You rolled a {random.randint(1, 6)}!")
        elif user_input == "exit":
            print("Exiting the dice roller. Goodbye!")
            break
        else:
            print("Invalid input. Please type 'roll' or 'exit'.")
roll_dice()

#question 2
import random

def pick_restaurant():
    restaurants = ["Dominoz", "Mcdonal", "KFC", "SS Hyderabad", "Tovo", "ALsham", "Copper kitchen"]   
    while True:
        user_input = input("Type 'pick' to choose a restaurant or 'bye' to exit: ").lower()
        if user_input == "pick":
            print(f"You should go to {random.choice(restaurants)}!")
        elif user_input == "bye":
            print("Goodbye! Enjoy your meal!")
            break
        else:
            print("Invalid input. Please type 'pick' or 'bye'.")
pick_restaurant()


#question 3
def validate_username(username):
    if not username[0].isalpha():
        return False, "Must start with a letter"
    if not username.isalnum() and "_" not in username:
        return False, "Must contain only letters, numbers or underscores"
    if len(username) < 5 or len(username) > 15:
        return False, "Must be between 5 and 15 characters"
    return True, "Valid username"

def check_validity():
    username = input("Enter your username: ")
    valid, message = validate_username(username)
    print(message)
check_validity()




















