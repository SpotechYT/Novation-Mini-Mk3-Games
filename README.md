<p align="center"><img src="https://raw.githubusercontent.com/SpotechYT/Novation-Mini-Mk3-Games/main/images/Logo.jpg" height="200"></p>
<h1 align="center">Novation Mini Mk3 Games</h1>
<p align="center">Games for the Mini Mk3 Launchpad!</p>

More support for other Launchpads Comming Soon!

Bassed on [launchpad.py](https://github.com/FMMT666/launchpad.py)

## Connect 4
A recreation of the classic game "connect 4" with a scoreboard

Controls/leds:
- [0, 0] - [0, 8] shows the score (Blue/Red/Green)
- [0, 8] shows who's turn it is
- the playboard is from [0, 1] to [7, 8]
- click anywhere in a row to place a disk there
- [1, 8] resets the current board
- [8, 8] kills the programs

![Connect4](https://raw.githubusercontent.com/SpotechYT/Novation-Mini-Mk3-Games/main/Connect4/example.gif)

## Patterns
A Memorization Pattern Game thats 100x Harder then normal

Controls/leds:
- [1, 0] - [8, 7] playboard
- [8, 8] kills the programs

![Patterns](https://raw.githubusercontent.com/SpotechYT/Novation-Mini-Mk3-Games/main/Patterns/example.gif)

## Dance Floor
A LED matrix that looks like a dance floor

Controls/leds:
- [0, 0] - [8, 8] changes colors randomly
- [8, 8] kills the programs

![Dance Floor](https://raw.githubusercontent.com/SpotechYT/Novation-Mini-Mk3-Games/main/DanceFloor/example.gif)

## Installation
Install Python3

Install The Library
```
pip install launchpad_py
```
or
```
sudo pip install launchpad_py
```

You also will need the os and sys libraries installed

All games require controler.py in the same directory as the game to function properly

Be sure to move/copy controler.py to the game directory

Run The Game

## How it works
This project is bassed on the [launchpad.py](https://github.com/FMMT666/launchpad.py) and uses some code snippets from the examples to make the controler file.

Each button/light on the launchpad has an x and y value from Top-Left[0, 0] to Bottom-Right[8, 8]
![Matrix](https://raw.githubusercontent.com/SpotechYT/Novation-Mini-Mk3-Games/refs/heads/main/images/Matrix.jpg)

For more documentation, check the [launchpad.py](https://github.com/FMMT666/launchpad.py) github 

###### Created With Determination By Spotech
