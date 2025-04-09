def main():
    """Main game logic is defined in a function to ultimately allow for it to be called at the end of the program, so multiple games can be played by the user in one concurrent session."""

    from generate_equation import equation
    from rounds import valid_integer_rounds
    from max_factor import valid_max_factor
    from retry import retry_game_check
    
    #Global variables to initate score and attempt tracking
    score = 0
    attempts = 0

    print("Welcome to the equations solving game!")         
    print("You will be presented with an equation, and all you need to do is to type your answer and press ENTER to attempt to solve it.")
    
    number_of_rounds = valid_integer_rounds()
    max_factor = valid_max_factor()       

    while attempts != number_of_rounds:
        if attempts == 0:
            print("Get ready for the first equation:")
        elif attempts > 0:
            print("Get ready for the next equation:")
        else:
            break
        
        factor_one, factor_two, result = equation(max_factor)
        user_guess = None
        
        print(f"{factor_one} x 𝑥 = {result}")
        
        while user_guess != factor_two:
            user_guess = input("𝑥 = ")
            try:
                user_guess = int(user_guess)
            except ValueError:
                print("That's not a number, you must enter a number. Marking this answer as incorrect.")
            if user_guess != factor_two:
                attempts += 1
                print(f"Your answer was incorrect. The correct answer was {factor_two}.")
                break
            else:
                attempts += 1
                score += 1
                print("Your answer was correct!")
    
    print(f"Your total score was {score} out of {attempts} attempts.")
    print("Thanks for playing!")   

    retry_game = retry_game_check()
    if retry_game == True:
        print("\n")
        main()
    else:
        quit

if __name__ == "__main__":
   main()