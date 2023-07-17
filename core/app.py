from game.objects.enemy import enemy_1
from game.objects.home import big_tower
from game.helper.const import CELLS
from game.utils.funcs import (
    draw_map,
    clear_screen
)
from game.objects.tower import (
    tower_1,
    tower_2,
    tower_3
)


def main() -> None:
    """
    Runs the main game loop for a tower defense game.

    This function starts the game loop for a tower defense game, where the player must defend three towers # noqa E501
    against enemy units that move along a path. The function updates the game state every second, moving # noqa E501
    the enemy units and firing the towers' weapons. The function ends the game when the enemy units reach # noqa E501
    the end of the path or when all towers are destroyed.

    Args:
    None.

    Returns:
    None.
    """
    running = True
    second = 0
    while running:
        clear_screen()
        print(enemy_1.health)
        if enemy_1.y < 5:
            draw_map(
                CELLS,
                big_tower,
                enemy_1(),
                tower_1(),
                tower_2(),
                tower_3()
            )
            enemy_1.move_enemy()
            second += 1
            if second == 2:
                tower_1.fire(enemy_1)
                tower_2.fire(enemy_1)
                tower_3.fire(enemy_1)
                second = 0
                print(enemy_1.health)
            if enemy_1.health <= 0:
                print('The enemy is destroyed...')
                print('\n<<< You Are Victorious! >>>')
                running = False
        else:
            print('\nGame Over')
            running = False
