from ship import Ship
from laser import Laser
from importing import Importing
import pygame

pygame.init()


class Boss(Ship):
    boss_counter = 0

    boss_Type = {
        "boss0":
            (Importing.BOSS_ENEMY0, Importing.BOSS0_SKULL, Importing.BOSS0_BONE),
        "boss1":
            (Importing.BOSS_ENEMY1, Importing.BOSS1_BREAD, Importing.BOSS1_SAUSAGE),
        "boss2":
            (Importing.BOSS_ENEMY2, Importing.BOSS2_EGG, Importing.BOSS2_LEG)
    }

    def __init__(self, x, y, name, health, velocity_x=4, velocity_y=0.28):
        super().__init__(x, y)
        Boss.boss_counter += 1
        self.ship_img, self.laser_img0, self.laser_img1 = self.boss_Type[name]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.health = health
        self.type = "boss"
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    # poruszanie się statku
    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    # jak cooldown na strzał się skończył, to tworzy nowe lasery i w move_laser posyła je w dół
    def shoot(self):
        if self.cool_down_counter == 0:
            if self.y + 245 >= 0:
                laser0 = Laser(self.x + 70, self.y + 245, self.laser_img0)
                laser1 = Laser(self.x + 170, self.y + 245, self.laser_img1)
                self.lasers.append(laser0)
                self.lasers.append(laser1)
                self.cool_down_counter = 1

    # co loop zwiększa cool_down_counter o 1, aż do momentu końca cool_down'u i wtedy wykona się shoot,
    # jak powstały jakiś lasery dzięki metodzie shoot, to będzie go przesuwać je "dziwnie" w dół
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move_weird(vel)
            if laser.off_screen(Importing.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 1
                self.lasers.remove(laser)