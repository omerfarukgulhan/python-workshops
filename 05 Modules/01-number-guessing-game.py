import time
import random

print(
    """****************************

Welcome to number guessing game

Enter number between 1 and 40(1 and 40 included).
****************************"""
)
number_of_guesses = 7
random_number = random.randint(1, 40)

while True:
    print("**************")
    guess = int(input("Your guess:"))

    if guess == random_number:
        print("Checking....")
        time.sleep(1)
        print("Congratulations!")
        print("Number: ", random_number)
        break
    elif guess < random_number:
        print("Checking....")
        time.sleep(1)
        number_of_guesses -= 1
        print("Please enter bigger number.")
        print("Number of guesses: ", number_of_guesses)
    else:
        print("Checking....")
        time.sleep(1)
        number_of_guesses -= 1
        print("Please enter lower number.")
        print("Number of guesses: ", number_of_guesses)
    if number_of_guesses == 0:
        print("Out of guess.")
        print("Number: ", random_number)
        break
