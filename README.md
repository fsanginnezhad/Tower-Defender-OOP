# Tower Defense game project

This is a Python project that implements a tower defense game. This game involves placing towers to defend the castle against waves of enemy attacks. This project is organized into several folders and files, which are described below:

## Project structure

- `core/`:
    - `app.py`: This file contains the main logic of the game. Handles inputs to the player, calls the necessary functions from the `utils` folder, and displays the output to the user.

- `game/`':
    - `utils/`: This folder contains all the functions used in the game such as enemies, towers, and damage calculation for the game mode.

    - `models/`: This folder contains the definitions of game objects such as castles, enemies, and towers. Each object is defined by attributes such as health, damage, and cost.

    - `helper/`: This folder specifies the coordinates of the game screen. Used to map player inputs to the corresponding cell on the board.

    - `objects/`: This folder contains the implementation of game objects such as the main castle, enemy, and tower. Each object is defined by its behavior such as movement and attack.

- `run.py`: This is the main file that runs the program. Each command is sent to the desired file and the program executes the corresponding function.

## How to run the program

To run the program, follow the steps below:

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/fsanginnezhad/Tower-Defender-OOP.git
   ```

2. Go to the project directory:
   ```
   cd Tower-Defender-OOP
   ```

3. Run the program:
   ```
   python run.py
   ```


The game will continue until the castle is destroyed or all enemy waves are defeated. If the player successfully defends the castle against all enemy waves, the game is won.

## Credits

This project was created by `Farshad Sanginnezhad`. If you have any questions or feedback, please contact me.
