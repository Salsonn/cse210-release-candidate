from game.point import Point
from game import constants

import arcade

class Projectile(arcade.Sprite):
    def __init__(self, startingX, startingY, dX, dY):
        super().__init__(constants.projectile1Image)

        self.center_x = startingX
        self.center_y = startingY
        self.change_x = dX
        self.change_y = dY
        self.bounces = 5 # add 1 for every bounce, -1 for infinite bouncing

    def reflect(self, projectiles, l, r, t, b):
        if True in {l, r}:
            self.change_x *= -1
        if True in {t, b}:
            self.change_y *= -1
        if not False in {l, r, t, b}:
            self.center_x += self.change_x
            self.center_y += self.change_y
        if self.bounces == 0:
            projectiles.remove(self)
            if constants.debug:
                print(f"Removed a projectile. There are now {len(projectiles)} on screen.")
        else: self.bounces -= 1