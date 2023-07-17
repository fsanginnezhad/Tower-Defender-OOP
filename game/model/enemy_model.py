from time import sleep


class Enemy:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.health = 100

    def move_enemy(self) -> tuple[int, int]:
        sleep(1)
        self.y += 1
        return self.x, self.y

    def __call__(self) -> tuple[int, int]:
        return self.x, self.y
