<h1>Tetris</h1>
Project development TPJ 

<h1>Introduction</h1>
The main goal of the subject TPJ is to pick a game to develop, where we can apply the patterns we learn in class. <br>
I chose Tetris, because I had an interest in knowing how it worked since I played the game so many times when I was young

<h1>Struct Program</h1>
The program is divide into files. <br>
<ul>
  <li>piece.py - information about piece of tetris like their coordinates, tipe, and color </li> 
  <li>scoreboard.py - information about the score of the game like number of score, number of lines clear</li> 
  <li>screen_play.py where it has information about the grid used to play tetris on pygame.</li> 
  <li>commands.py possible inputs of the game</li>
  <li>game.py - main class, where program runs</li>
 </ul>
<br>

Hold piece (when we want to use current piece for later), score info, lines clear, level, next piece, falling piece and grid for playing (displaing proposes) <br>
<img src="./layout.png" width="250" height="350">  <br>
The grid has 10 rows for 20 columns <br>
The length of the piece is 4 <br>
Windows dimensions are 300x400 

<h2>Possible Pieces</h2>
Tetris has 7 possible pieces and the pieces are: (the colors in this image are similar to the program)
<img src="./pieces.png" width="250" height="250">


<h1>Commands</h1>
The possible commands that programs uses is 
<img src="./commands.png" width="250" height="150">
from https://tetris.com/play-tetris/


<h2>Validate space</h2>
The movement of the piece is restrict to the grid, so before user press the direction or rotation, a verification need to occur <br> 
To do that I create a list with free pos of the dimension of the grid containing 200 squares of possible positions.

<h2>Rotation</h2>
For rotation i adapted the code from (line 122 - 125)
https://github.com/StanislavPetrovV/Python-Tetris/blob/master/main.py

<h1>Patterns</h1>
<p>Command</p>
<p>Observer</p>
