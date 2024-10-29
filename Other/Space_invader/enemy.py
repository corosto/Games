from ship import Ship
from laser import Laser
from importing import Importing
import pygame

pygame.init()


class Enemy(Ship):
    enemy_Type = {
        "alien0": (Importing.FIRST_ENEMY, Importing.ENEMY_LASER_RED),
        "alien1": (Importing.SECOND_ENEMY, Importing.ENEMY_LASER_PINK),
        "alien2": (Importing.THIRD_ENEMY, Importing.ENEMY_LASER_WHITE),
        "alien3": (Importing.FOURTH_ENEMY, Importing.ENEMY_LASER_BLUE),
        "alien4": (Importing.FIFTH_ENEMY, Importing.ENEMY_LASER_YELLOW),
        "alien5": (Importing.SIXTH_ENEMY, Importing.ENEMY_LASER_GREEN)
    }

    def __init__(self, x, y, name, health, velocity_x=1.8, velocity_y=0.7):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.enemy_Type[name]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.health = health
        self.type = "mob"
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    # poruszanie się przeciwnika
    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    # jak cooldown na strzał się skończył, to tworzy nowy laser i w move_laser posyła go w dół
    def shoot(self):
        if self.cool_down_counter == 0:
            if self.y >= 0:
                laser = Laser(self.x - 7, self.y + 28, self.laser_img)
                self.lasers.append(laser)
                Importing.LASER_SOUND.play()
                self.cool_down_counter = 1
