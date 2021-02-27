# Classic Snake Game

This is a Python implementation of the classic mobile game called snake, in which the user must direct a moving snake towards food without touching the tail of the snake (increases in length each time an item of food is eaten) or the edge of the screen.

## How the Application Works
1. The program uses the turtle graphics library to create a black screen on which the game is played.  
1.  Instances of 3 custom classes are created during the game: Snake, Food and Scoreboard.  
1. Event listeners are used so that the snake can be moved with the up, down, left and right arrows on the keyboard.  
1. The game ends when the distance between the head of the snake and its own tail segments or the edge of the screen cross a threshold.  
1. The game then restarts, keeping track of the users high score.  
<br>

<div style="text-align:center"><img src="/images/snake-game.png" width=50%></div>

## Trying the Game
* Simply download main.py and the other source code files in the src folder, then launch the game by running main.py.  
* No special module installs are necessary, because turtle graphics is part of the Python standard library.


## Supporting Libraries and APIs
* Turtle Graphics: https://docs.python.org/3/library/turtle.html#:~:text=The%20turtle%20module%20is%20an,up%20to%20version%20Python%202.5.

## Future Development  
I do not plan to improve this application in the future, other than bug fixes if necessary.
