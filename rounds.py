def rounds():
    number_of_rounds = input("")
    try:
        number_of_rounds = int(number_of_rounds)
    except ValueError:
        print("That's not a number, you must enter a number.")
        rounds()
    else:
        return number_of_rounds