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

#### Python

Open the 'main.py' file with Python.

#### Terminal

Navigate to the installation directory and run main.py

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

