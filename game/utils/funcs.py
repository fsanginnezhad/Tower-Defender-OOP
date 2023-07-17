import os


def clear_screen() -> None:
    """
    Clears the console screen.

    This function uses the 'os' module to determine the current operating system and # noqa E501
    clears the console screen using the appropriate command for that system.

    Args:
    None.

    Returns:
    None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_map(
    cells: list[tuple],
    home: tuple,
    enemy: tuple,
    *towers: tuple
) -> None:
    """
    Prints a map of the game board.

    This function takes in a list of tuples representing the cells of the game board, the positions of the player's # noqa E501
    home and the enemy unit, and the positions of any towers on the board. The function prints a graphical # noqa E501
    representation of the board, with each cell represented by a vertical bar ('|') and an underscore ('_'). # noqa E501

    Args:
    cells (list[tuple]): A list of tuples representing the cells of the game board. # noqa E501
    home (tuple): A tuple representing the position of the player's home on the game board. # noqa E501
    enemy (tuple): A tuple representing the position of the enemy unit on the game board. # noqa E501
    *towers (tuple): Any number of tuples representing the positions of towers on the game board. # noqa E501

    Returns:
    None.
    """
    print(' _' * 6)
    for index, item in enumerate(cells):
        x = index % 6
        if x < 5:
            if item == home:
                print('|O', end='')
            elif item in towers:
                print('|*', end='')
            elif item == enemy:
                print('|X', end='')
            else:
                print('|_', end='')
        else:
            if item == home:
                print('|O|')
            elif item in towers:
                print('|*|')
            elif item == enemy:
                print('|X|')
            else:
                print('|_|')
