def retry_game_check():
    """Asks for the user if they want to replay the game. Loop forever until Y or N (or y or n) is entered. User can also use KeyboardInterrupt to leave though."""
    while True:
        end_game_input = input("Would you like to play again? Type Y and press ENTER if you would like to play again or type N and press ENTER if you would like to quit: ")
        if end_game_input == "Y" or end_game_input == "y":            
            return True
        elif end_game_input == "N" or end_game_input == "n":
            return False
        else:
            continue