from generate_equation import equation
from rounds import rounds
import time

score = 0
attempts = 0
max_factor = 12

if attempts == 0:
    print("Welcome to the equations solving game!")
    #time.sleep(3)       
    print("You will be presented with an equation, and all you need to do is to type your answer and press ENTER to attempt to solve it.")
    #time.sleep(3)
    print("How many rounds would you like to play?")
    number_of_rounds = rounds()
    print("Get ready for the first equation:")
    #time.sleep(3) 
else:
    print("Get ready for the next equation:")
    #time.sleep(3)

while attempts != number_of_rounds:
    factor_one, factor_two, result = equation(max_factor)
    user_guess = None
    print(f"{factor_one} x 𝑥 = {result}")
    while user_guess != factor_two:
        user_guess = input("𝑥 =")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("That's not a number, you must enter a number.")
        if user_guess != factor_two:
            attempts += 1
            print(f"Your answer was incorrect. The correct answer was {factor_two}.")
            break
        else:
            attempts += 1
            score += 1
            print("Your answer was correct!")
print(f"Your total score was {score} out of {attempts} attempts")
print("Thanks for playing!")
