from importing import Importing
from ship import Ship
from change_ship import ChangeShip
from change_weapon import ChangeWeapon
import pygame

pygame.init()


class Player(Ship):
    def __init__(self, x, y, health=8):
        super().__init__(x, y, health)
        if ChangeShip.chosen_ship == 0:
            self.ship_img = Importing.PLAYER_SHIP0
        elif ChangeShip.chosen_ship == 1:
            self.ship_img = Importing.PLAYER_SHIP1
        elif ChangeShip.chosen_ship == 2:
            self.ship_img = Importing.PLAYER_SHIP2

        if ChangeWeapon.chosen_weapon == 0:
            self.laser_img = Importing.PLAYER_MISSILE0
        elif ChangeWeapon.chosen_weapon == 1:
            self.laser_img = Importing.PLAYER_MISSILE1
        elif ChangeWeapon.chosen_weapon == 2:
            self.laser_img = Importing.PLAYER_MISSILE2

        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.score = 0

    # co loop zwiększa cool_down_counter o 1, aż do momentu końca cool_down'u i wtedy wykona się shoot
    # jak powstał jakiś laser dzięki metodzie shoot to będzie go przesuwać w górę
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(Importing.HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        self.lasers.remove(laser)
                        obj.health -= 1  # zadaje przeciwnikom 1 dmg ze strzału
                        if obj.health <= 0:
                            objs.remove(obj)
                            if obj.type == "mob":
                                self.score += 10
                            else:
                                self.score += 100

    # tworzy pasek hp
    def health_bar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 5,
                         self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 5,
                         self.ship_img.get_width() * (1 - ((self.max_health - self.health)/self.max_health)), 10))

    # rysowanie statku i strzałów w oknie gry + dodaje pasek hp
    def draw(self, window):
        super().draw(window)
        self.health_bar(window)
