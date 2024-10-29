import pygame
import os

pygame.init()


class Importing:
    WIDTH = 1280
    HEIGHT = 720

    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    # enemies
    FIRST_ENEMY = pygame.image.load(os.path.join("additions", "alien0.png"))
    SECOND_ENEMY = pygame.image.load(os.path.join("additions", "alien1.png"))
    THIRD_ENEMY = pygame.image.load(os.path.join("additions", "alien2.png"))
    FOURTH_ENEMY = pygame.image.load(os.path.join("additions", "alien3.png"))
    FIFTH_ENEMY = pygame.image.load(os.path.join("additions", "alien4.png"))
    SIXTH_ENEMY = pygame.image.load(os.path.join("additions", "alien5.png"))

    # bosses
    BOSS_ENEMY0 = pygame.image.load(os.path.join("additions", "boss0.png"))
    BOSS_ENEMY1 = pygame.image.load(os.path.join("additions", "boss1.png"))
    BOSS_ENEMY2 = pygame.image.load(os.path.join("additions", "boss2.png"))

    # player
    PLAYER_SHIP0 = pygame.image.load(os.path.join("additions", "spaceship0.png"))
    PLAYER_SHIP1 = pygame.image.load(os.path.join("additions", "spaceship1.png"))
    PLAYER_SHIP2 = pygame.image.load(os.path.join("additions", "spaceship2.png"))

    # missile
    PLAYER_MISSILE0 = pygame.image.load(os.path.join("additions", "missile0.png"))
    PLAYER_MISSILE1 = pygame.image.load(os.path.join("additions", "missile1.png"))
    PLAYER_MISSILE2 = pygame.image.load(os.path.join("additions", "missile2.png"))

    # missile inspect
    BIGGER_PLAYER_MISSILE0 = pygame.image.load(os.path.join("additions", "bigger_missile0.png"))
    BIGGER_PLAYER_MISSILE1 = pygame.image.load(os.path.join("additions", "bigger_missile1.png"))
    BIGGER_PLAYER_MISSILE2 = pygame.image.load(os.path.join("additions", "bigger_missile2.png"))

    # enemies laser
    ENEMY_LASER_BLUE = pygame.image.load(os.path.join("additions", "laser_blue.png"))
    ENEMY_LASER_GREEN = pygame.image.load(os.path.join("additions", "laser_green.png"))
    ENEMY_LASER_PINK = pygame.image.load(os.path.join("additions", "laser_pink.png"))
    ENEMY_LASER_RED = pygame.image.load(os.path.join("additions", "laser_red.png"))
    ENEMY_LASER_WHITE = pygame.image.load(os.path.join("additions", "laser_white.png"))
    ENEMY_LASER_YELLOW = pygame.image.load(os.path.join("additions", "laser_yellow.png"))

    # boss weapon
    BOSS0_SKULL = pygame.image.load(os.path.join("additions", "skull.png"))
    BOSS0_BONE = pygame.image.load(os.path.join("additions", "bone.png"))
    BOSS1_BREAD = pygame.image.load(os.path.join("additions", "bread.png"))
    BOSS1_SAUSAGE = pygame.image.load(os.path.join("additions", "sausage.png"))
    BOSS2_EGG = pygame.image.load(os.path.join("additions", "egg.png"))
    BOSS2_LEG = pygame.image.load(os.path.join("additions", "chicken_leg.png"))

    # background
    BACKGROUND0 = pygame.transform.scale(pygame.image.load(os.path.join("additions", "bck0.jpeg")), (WIDTH, HEIGHT))
    BACKGROUND1 = pygame.transform.scale(pygame.image.load(os.path.join("additions", "bck1.jpg")), (WIDTH, HEIGHT))
    BACKGROUND2 = pygame.transform.scale(pygame.image.load(os.path.join("additions", "bck2.jpg")), (WIDTH, HEIGHT))
    BACKGROUND3 = pygame.transform.scale(pygame.image.load(os.path.join("additions", "bck3.png")), (WIDTH, HEIGHT))
    BACKGROUND4 = pygame.transform.scale(pygame.image.load(os.path.join("additions", "bck4.jpg")), (WIDTH, HEIGHT))
    BACKGROUND5 = pygame.transform.scale(pygame.image.load(os.path.join("additions", "bck5.png")), (WIDTH, HEIGHT))
    MENU_BCK = pygame.transform.scale(pygame.image.load(os.path.join("additions", "menu_bck.png")), (WIDTH, HEIGHT))

    # sound
    pygame.mixer.music.load((os.path.join("additions", "music.wav")))
    LASER_SOUND = pygame.mixer.Sound(os.path.join("additions", "laser.wav"))
    MISSILE_SOUND = pygame.mixer.Sound(os.path.join("additions", "rocket.wav"))
