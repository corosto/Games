import pygame
import random

pygame.init()


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    # tworzy obraz lasera w oknie
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    # przesuwa laser w linii prostej w dół
    def move(self, velocity):
        self.y += velocity

    # przesuwa laser w dziwny sposób w dół
    def move_weird(self, velocity_y):
        self.x += random.randrange(-10, 10)
        self.y += velocity_y

    # sprawdza, czy laser jest poza ekranem
    def off_screen(self, height):
        return not(height >= self.y >= -35)

    # sprawdza, czy obiekty się zderzyły na podstawie ich położenia
    def collide(self, object2):
        offset_x = object2.x - self.x
        offset_y = object2.y - self.y
        return self.mask.overlap(object2.mask, (offset_x, offset_y))

    # jak obiekt zderzył się z innym obiektem to zwraca true
    def collision(self, object2):
        return self.collide(object2)
