def valid_integer_rounds():
    """Asks for the user to define the number of rounds and return a valid integer. If this is not an integer, loop forever until a valid value is entered"""
    while True:
        number_of_rounds = input("How many rounds would you like to play? Type a whole number and press ENTER: ")
        try:
            number_of_rounds = int(number_of_rounds)
        except ValueError:
            print("That's not a whole number, you must enter a whole number.")
            continue
        else:
            if number_of_rounds == int(0):
                print("Zero means you can't play! Please enter a whole number greater than zero.")
                try:
                    number_of_rounds = int(number_of_rounds)
                except ValueError:
                    print("That's not a whole number, you must enter a whole number.")
                    continue
            else:
                return number_of_rounds