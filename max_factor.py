def valid_max_factor():
    """Asks for the user to define the maximum factor to multiply and return a valid integer. If this is not an integer, loop forever until a valid value is entered"""
    while True:
        max_factor = input("What is the largest number you would like to multiply by? Type a whole number and press ENTER: ")
        try:
            max_factor = int(max_factor)
        except ValueError:
            print("That's not a whole number, you must enter a number.")
            continue
        else:
            if max_factor == int(0):
                print("Zero is too easy! Please enter a whole number greater than zero.")
                try:
                    max_factor = int(max_factor)
                except ValueError:
                    print("That's not a whole number, you must enter a whole number.")
                    continue
            else:
                return max_factor