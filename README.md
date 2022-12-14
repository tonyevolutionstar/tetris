<h1>Tetris</h1>
Project development TPJ 

<h1>Introduction</h1>
The main goal of the subject TPJ is to pick a game to develop, where we can apply the patterns we learn in class. <br>
I chose Tetris, because I had an interest in knowing how it worked since I played the game so many times when I was young

<h1>How tetris works</h1>
The purpose of the game is to move pieces that decends onto the playing field, until a line is clear, that means all squares of the grid are fill with color. <br>
The Current piece and the next piece are randomly selected <br>
The game ends when there is no space on grid to play. Just like the shown in the example below. <br>
<img src = "./gameover.png" width="250" height="350">

<h2>Possible Pieces</h2>
Tetris has 7 possible pieces and the pieces are: (the colors in this image are similar to the program)
<img src="./pieces.png" width="250" height="250">

<h2>Layout</h2>
Hold piece (when we want to use current piece for later), score info, lines clear, level, next piece, falling piece and grid for playing (displaying proposes) <br>
The level, hard drop (space key) and hold (c key) were not implemented.<br>
The dimension of the pygame window is 300x400.<br>
The grid used has 10 row for 20 columns.<br>

<img src="./layout.png" width="250" height="350">  <br>


<h1>Commands</h1>
The possible commands that programs uses are
<img src="./commands.png" width="250" height="150">
from https://tetris.com/play-tetris/


<h1>Validate space</h1>
The movement of the piece is restricted to the grid space so, before teh user presses the direction or rotation, a verification need to occur <br> 
To do that I create a list with free positions of the dimension of the grid containing 200 squares of possible positions.

<h1>Rotation</h1>
There are two possible rotations clock and anticlockwise for all pieces except the square (R).  
For rotation i adapted the code from (line 122 - 125)
https://github.com/StanislavPetrovV/Python-Tetris/blob/master/main.py

<h1>Score</h1>
When a piece is droping 1 value is added to the current score, if the user presses down key 1 value is added to the droping, and the velocity of droping is more faster.<br>
When a user cleans a certain number of the lines, until 4, score increases. The values are 1 line +100, 2 lines +300, 3 lines +500, 4 lines +800. 

<h1>Clear line</h1>
A line is clear when a row is full. When it's full the positions of the grid are updated to y+1 and the score is updated. 

<h1>Struct Program</h1>
The program is divided into files. <br>
<ul>
  <li>piece.py - information about piece of tetris like their coordinates, type, and color </li> 
  <li>scoreboard.py - information about the score of the game like number of score, number of lines clear</li> 
  <li>screen_play.py - information about the grid used to play tetris on pygame.</li> 
  <li>commands.py - possible inputs of the game</li>
  <li>game.py - main class, where program runs</li>
 </ul>
<br>

<h1>Patterns</h1>
- Command: Used to handle keyboard inputs. <br>
- Observer: Used to record events in game - done with log file. <br>

<h1>How to run</h1>
On a new terminal in the folder run python3 game.py <br>
Pygame needs to be install on the environment (window, ubuntu or macos) 
