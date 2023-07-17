from game.model.enemy_model import Enemy


class Tower:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.damage = 20

    def fire(self, enemy: Enemy) -> int:
        enemy.health -= self.damage
        return enemy.health

    def __call__(self) -> tuple[int, int]:
        return self.x, self.y
