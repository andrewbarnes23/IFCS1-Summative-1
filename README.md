# Equation Solving Game Documentation

The Equation Solving Game is a Python program that asks the user to solve multiplication questions by guessing an unknown 𝑥. Useful for solving simple times tables up to a given number or otherwise solving big multiplication problems!

### Game Core Properties

- Play a defined number of rounds set by the user before game start.
- Randomly generated equations to solve x * y = z, where the largest value for both x and y is defined by the user.
- Score tracking according to both correct and incorrect answers.
- Feedback on incorrect answers, by presenting the correct answer after the user has guessed.
- Input validation pre-game in order to catch errors, such as the user entering a word when a number is expected.
- Ability to replay the game post-game when all rounds have been completed.

## User Manual

### Prerequisites

- Mandatory: A valid, up to date install of Python on the user's local machine.
- Optional: A text editor of the user's choice (such as Notepad++, Visual Studio Code, Brackets etc.) to allow for code editing.

### Installation

#### Python (if required)
Install Python 3.x by downloading and running the appropriate installer, depending on the user's operating system (Windows, Mac, Linux). 

Please visit [python.org](https://www.python.org/downloads/) where the Windows installer can be obtained, along with links to other operating systems as appropriate.

After downloading the installing executable, run it and install Python by navigating through the installer prompts. As part of this process, ensure "Add Python to PATH" is checked at the appropriate stage during installation.

#### Equations Solving Game Download

##### Download .zip

[Download the .zip file using this link](https://github.com/andrewbarnes23/IFCS1-Summative-1/archive/refs/heads/main.zip)

##### Install .zip

Extract the .zip's contents to a folder of the user's choice

##### git clone

Using git bash or otherwise, navigate to the desired project folder of the user's choice and initialise a new repository

```bash
cd folder/of/the/users/choice
```

```bash
git init
```

```bash
git clone https://github.com/andrewbarnes23/IFCS1-Summative-1.git {add optional name here}
```

### Equations Solving Game Launch

#### Operating Sytem via Python

Open the 'main.py' file with Python in the File Explorer of the user's operating system.

#### Terminal

Navigate to the installation directory and type main.py to run

### Gameplay Operation

Follow the onscreen prompts and play!

#### Number of rounds

Type the desired number of rounds and press ENTER or RETURN. Recommended rounds is 10.

#### Largest number to multiply by

Type the largest factor multiply by and press ENTER or RETURN. For example, a value of 7 will yield equations anywhere from 1 x 1 to 7 x 7. Recommended value is 12. 

#### Equation solving

Type the guess and press ENTER or RETURN. Typing anything other than a number will yield an incorrect answer. Repeat until all rounds are played.

#### Game Replay

Type either Y (indicating Yes) or N (indicating No) and press ENTER or RETURN. Typing anything other than these characters will not yield an action.

#### Quitting mid-game

Use CTRL+C or equivalent for the operating system to quit the game. Alternatively, exit the terminal or prompt.

## Technical Documentation

### Folder Structure

```
IFCS1-Summative-1-Equation/
main.py                     # Main script for game.
generate_equation.py        # Equation function to generate new random equations every round.
rounds.py                   # Function to validate user input when asked to provide desired number of rounds.
max_factor.py               # Function to validate user input when asked to provide desired maximum factor to play with.
retry.py                    # Function to validate user input when asked to provide choice to replay the game or not once the session is over.
```

#### main.py

Main game file. Contains game logic within defined `main()` function. 

`main()`:
- Imports the required functions from the other game files.
- Initiates global variables `score` and `attempts` to track the correct answers and total iterations throughout the session.
- `Print` statements at each stage from end to end game start to game conclusion.
- Initiates global variables `number_of_rounds` and `max_factor` for the session, validating each through respective individual functions.
- Validates user input as `user_guess` against variable `factor_two`, repeating until the user's `attempts` is equal to `number_of_rounds`.

#### generate_equation.py

File containing `equation(max_factor)` function.

- Using `random`, sets factor variables for the equation from a range of `(1,max_factor)`.
- Returns tuple `factor_one,factor_two,product` for assignment in `main()`.

#### rounds.py

File containing `valid_integer_rounds()` function.

- Using ` while True:` loop, takes `input()` from the user. 
- Since `input()` is a string, attempt to convert `number_of_rounds` to integer.
- First checks if the `input()` passed is a valid integer. Upon a `ValueError` (e.g a non-convertible string), `continue` restarts the loop until an integer is passed.
- Upon successful check for integer, check for `input()` of 0. 0 is a valid integer, but otherwise causes the game to immediately end with no rounds played. If 0 is passed, the loop restarts until a non-0 value is entered.
- Once all conditions are successful, return the integer for use in `main()`.

#### max_factor.py

File containing `valid_max_factor()` function. Similar logic to rounds.py.

- Using ` while True:` loop, takes `input()` from the user. 
- Since `input()` is a string, attempt to convert `max_factor` to integer.
- First checks if the `input()` passed is a valid integer. Upon a `ValueError`(e.g a non-convertible string), `continue` restarts the loop until an integer is passed.
- Upon successful check for integer, check for `input()` of 0. 0 is a valid integer, but otherwise causes the equation to generate x*0, which is always 0. If 0 is passed, the loop restarts until a non-0 value is entered.
- Once all conditions are successful, return the integer for use in `main()`.

#### retry.py

File containing `retry_game_check()` function.

- Using ` while True:` loop, takes `input()` from the user.
- Validates `input()` to be either Y or N values (as per main() print() statement) to `return True` or `return False`
- If `True`, assign to variable `retry_game` in `main()` to allow for `main()` recalled so the game starts again.

### Modules

- `random`
- `input()`

- No external modules used.

### Future Enhancements

- Refactor of all code to purify all functions.
- Use of pytest in functions to allow for test automation.