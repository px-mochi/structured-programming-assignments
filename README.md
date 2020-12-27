# structured-programming-assignments

Hi there! This repo consists of snippets of work that I have done for my school assignments (specifically, ICT133), which challenged my very beginner skill with (the not object oriented parts of) Python.

Here is a short description of what is in this repo:
## Basic text based visual calculator that adds two 3 digit numbers
- This was my first foray into understanding text and number formatting in Python
- It was also my first glimpse of the logical thinking needed to break down seemingly easy requirements into code logic

## Finding Greatest Common Denominator 
- The assignment required us to use the software Flowgorithm to generate a flowchart to illustrate the Euclid's algorithm, which is used to calculate the Greatest Common Denominator.
- Flowgorithm was then used to generate source code in [Python](Jul_2018_Structured_Programming/greatest_common_denominator.py) and in [Java](Jul_2018_Structured_Programming/greatest_common_denominator.java).
- The original flowchart and code was then [improved on](Jul_2018_Structured_Programming/greatest_common_denominator_improved.py) to
  - Add a counter in the loop, to count number of iterations used 
  - Reduce the number of iterations needed 

## A text based game of mastermind
- [What is this game?](https://en.wikipedia.org/wiki/Mastermind_(board_game))
- [Version without the use of python dictionaries](Jul_2018_Structured_Programming/mastermind_game/mastermind_game.py)
- [Version with dictionaries](Jul_2018_Structured_Programming/mastermind_game/mastermind_game_dict.py)
  - The dictionaries are used to record each player’s name, score for the current game and the number of games won thus far, as well as any other appropriate values.
- The planning of the game was done through use of top-down design.
  - [Planning](Jul_2018_Structured_Programming/mastermind_game/mastermind_game_planning.txt)
  - [Structure Chart](Jul_2018_Structured_Programming/mastermind_game/mastermind_structure_chart.png)

## (Probably outdated) Calculator for total stamp duty payable for a residential property in Singapore
- [Resources](https://propertynet.sg/what-is-stamp-duty/)
- [Code](Jul_2018_Structured_Programming/stamp_duty_calculator.py)
- Code can be improved by catering for other types of incorrect inputs (EG: Wrong date format, non-number inputs for property price)

## Text based code for booking a study room
- [Code](Jul_2018_Structured_Programming/study_room_booking.py)

## A text based guessing game
- A simple game application allows a single player to play a guessing game repeatedly.
- [Code](Jul_2018_Structured_Programming/guessing_game.py)

###### Game Rules
- The player has 50 chips at the start of the session.
- Before every new game, the player enters a positive number that is at least 4, e.g., 7.
A random sequence of whole numbers from 1 to that number is then generated, e.g., 5 2 4 1 6 7 3.
- The first number is revealed to the player, in this case, 5.
  - He makes a guess whether the next number is higher (h) or lower (l) than the number just revealed, and then places the number of chips he wishes to bet with.
  - The player may also choose to skip guessing by entering an empty string.
- Whether the player makes a guess or skips, the next number is revealed, in this case, 2.
  - If the player makes a guess and the guess is correct, he wins some chips, an amount described under the heading Bet Amount.
  - Otherwise, he loses the chips he bets with.
  - Display the number of chips the player has after computing his win or loss, or after his skip, on the console (output screen) as well as into a file, Q3Out.txt.
- The game continues with the player guessing or skipping until the third number from the end (or right) of the sequence is revealed, in this case 6. Then the game ends.


