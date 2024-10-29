from importing import Importing
from player import Player
from enemy import Enemy
from boss import Boss
from laser import Laser
from change_background import ChangeBackground
import leaderboard
import pygame
import random
import main_menu
import chose_nickname
import threading

pygame.init()


class Game:
    def __init__(self):
        pygame.display.set_caption("Space Invader")  # nazwa okienka gry

        self.settings_font = pygame.font.SysFont("comicsans", 35)  # czcionka dla ustawień
        self.title_font = pygame.font.SysFont("comicsans", 50)  # czcionka dla tytułu
        self.main_font = pygame.font.SysFont("comicsans", 20)  # czcionka dla zwykłych napisów

        self.running = True
        self.FPS = 60  # FPS, ile razy loop się wykona na sekundę
        self.level = 0  # który poziom gry
        self.lives = 10  # liczba żyć gracz

        self.lost = False  # bool, który sprawdza, czy gracz przegrał

        self.enemies = []  # lista na przeciwników
        self.wave_length = 3  # ilu przeciwników na pierwszą falę
        self.player_velocity = 8  # prędkość gracza
        self.laser_velocity = 4  # prędkość strzału gracza i przeciwników

        self.Player_ship = Player(600, 600)  # tworzenie gracza

        self.clock = pygame.time.Clock()  # tworzy obiekt, który pomaga mierzyć czas
        self.wyniki = []  # tablica na wyniki

        with open("leaderboard.txt", "r") as file:  # wpisywanie scoreboard do zmiennej wyniki
            for line in file:
                user_data = line.replace("\n", "").split(",")
                self.wyniki.append([int(user_data[0]), user_data[1]])  # ((int)wynik,nazwa)

    @staticmethod
    def drawing_background():
        if ChangeBackground.chosen_background == 0:
            Importing.WINDOW.blit(Importing.BACKGROUND0, (0, 0))
        elif ChangeBackground.chosen_background == 1:
            Importing.WINDOW.blit(Importing.BACKGROUND1, (0, 0))
        elif ChangeBackground.chosen_background == 2:
            Importing.WINDOW.blit(Importing.BACKGROUND2, (0, 0))
        elif ChangeBackground.chosen_background == 3:
            Importing.WINDOW.blit(Importing.BACKGROUND3, (0, 0))
        elif ChangeBackground.chosen_background == 4:
            Importing.WINDOW.blit(Importing.BACKGROUND4, (0, 0))
        elif ChangeBackground.chosen_background == 5:
            Importing.WINDOW.blit(Importing.BACKGROUND5, (0, 0))

    def create_enemies(self):
        self.level += 1
        if self.level % 5 == 0:  # co 5 poziom jest boss
            if Boss.boss_counter == 0:  # sprawdza ilu bossów już było
                enemy = Boss(random.randrange(300, 800), -300, "boss0", 20, velocity_x=random.choice([4, -4]))
                self.enemies.append(enemy)
            elif Boss.boss_counter == 1:
                enemy = Boss(random.randrange(300, 800), -300, "boss1", 25, velocity_x=random.choice([4, -4]))
                self.enemies.append(enemy)
            elif Boss.boss_counter == 2:
                enemy = Boss(random.randrange(300, 800), -300, "boss2", 30, velocity_x=random.choice([4, -4]))
                self.enemies.append(enemy)
            else:
                enemy = Boss(random.randrange(300, 800), -300,
                             random.choice(["boss0", "boss1", "boss2"]), 30, velocity_x=random.choice([5, -5]))
                self.enemies.append(enemy)
        else:
            self.wave_length += 1  # co poziom zwiększa fale o 1 przeciwnika
            for i in range(self.wave_length):
                enemy = Enemy(random.randrange(20, Importing.WIDTH - 100), random.randrange(-300, -100),
                              random.choice(["alien0", "alien1", "alien2", "alien3", "alien4", "alien5"]),
                              1, random.choice([1.8, -1.8]))
                self.enemies.append(enemy)

    def write_score(self):
        lb = leaderboard.Leaderboard()
        with open("leaderboard.txt", "w") as file:
            for i in range(10):
                file.write(str(self.wyniki[i][0]) + "," + self.wyniki[i][1] + "\n")
        lb.leaderboard(self.wyniki)

    def redraw_window(self):
        n = chose_nickname.Nickname()

        Game.drawing_background()  # wybór tła przez gracza

        #  etykieta żyć gracza i poziomu gry
        remaining_lives_label = self.main_font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        current_level_label = self.main_font.render(f"Level: {self.level}", True, (255, 255, 255))
        current_score_label = self.main_font.render(f"Score: {self.Player_ship.score}", True, (255, 255, 255))
        nickname_label = self.main_font.render(f"Name: {n.name}", True, (255, 255, 255))
        Importing.WINDOW.blit(remaining_lives_label, (10, 10))
        Importing.WINDOW.blit(current_score_label, (8, 40))
        Importing.WINDOW.blit(current_level_label, (1200, 10))
        Importing.WINDOW.blit(nickname_label, (Importing.WIDTH - nickname_label.get_width() - 10, 40))

        for enemy_ship in self.enemies:
            enemy_ship.draw(Importing.WINDOW)  # tworzenie modelów przeciwników

        self.Player_ship.draw(Importing.WINDOW)  # tworzenie modelu gracza

        if self.lost:
            if self.Player_ship.score >= int(self.wyniki[9][0]):
                self.wyniki.append([self.Player_ship.score, n.name])
                self.wyniki = sorted(self.wyniki, key=lambda l: l[0], reverse=True)

            threading.Thread(target=self.write_score())

        pygame.display.update()  # odświeża okno

    # tu zaczyna się loop gry
    def main(self):
        mm = main_menu.MainMenu()

        while self.running:
            self.clock.tick(self.FPS)  # ustawia 60FPS
            self.redraw_window()  # tworzy okno gry, tło, gracza, przeciwników i napis o porażce, gdy ona nastąpi

            if self.lives <= 0 or self.Player_ship.health <= 0:  # sprawdza, czy gracz nie przegrał
                self.lost = True

            if len(self.enemies) == 0:  # jak nie ma już żadnych przeciwników, to tworzy bossa lub zwykłych przeciwników
                threading.Thread(target=self.create_enemies())

            for event in pygame.event.get():  # jak gracz kliknie zamknij to wyjdzie z gry
                if event.type == pygame.QUIT:
                    quit()

            keys = pygame.key.get_pressed()  # tworzenie movementu gracza i granic okienka
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.Player_ship.x - self.player_velocity >= 0:
                self.Player_ship.x -= self.player_velocity
            if (keys[pygame.K_RIGHT] or keys[
                 pygame.K_d]) and self.Player_ship.x + self.Player_ship.get_width() < Importing.WIDTH:
                self.Player_ship.x += self.player_velocity
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.Player_ship.y > 400:
                self.Player_ship.y -= self.player_velocity
            if (keys[pygame.K_DOWN] or keys[
                 pygame.K_s]) and self.Player_ship.y + self.Player_ship.get_height() + 20 < Importing.HEIGHT:
                self.Player_ship.y += self.player_velocity
            if keys[pygame.K_SPACE]:  # strzelanie
                self.Player_ship.shoot()
            if keys[pygame.K_ESCAPE]:  # wyjście do menu po wciśnięciu ESC
                mm.main_menu()

            for enemy_ship in self.enemies[:]:  # [:] pracuje sie na wszystkich elementach
                if enemy_ship.x <= 0:  # odbijanie się przeciwników
                    enemy_ship.velocity_x = -enemy_ship.velocity_x
                elif enemy_ship.x + enemy_ship.get_width() >= Importing.WIDTH:
                    enemy_ship.velocity_x = -enemy_ship.velocity_x

                enemy_ship.move()
                enemy_ship.move_lasers(self.laser_velocity, self.Player_ship)

                if random.randrange(0, 33) == 1:  # częstotliwość strzelania przeciwników
                    enemy_ship.shoot()

                if self.level % 5 == 0:  # usuwa hp i licznik zyc w zależności czy to byl wave z bossem, czy nie
                    if Laser.collide(enemy_ship, self.Player_ship):
                        self.Player_ship.health -= 4
                        self.enemies.remove(enemy_ship)
                    elif enemy_ship.y + enemy_ship.get_height() > Importing.HEIGHT:  # jak przeciwnik wyleci poza ekran
                        self.lives -= 4
                        self.enemies.remove(enemy_ship)
                else:
                    if Laser.collide(enemy_ship, self.Player_ship):
                        self.Player_ship.health -= 1
                        self.enemies.remove(enemy_ship)
                    elif enemy_ship.y + enemy_ship.get_height() > Importing.HEIGHT:  # jak przeciwnik wyleci poza ekran
                        self.lives -= 1
                        self.enemies.remove(enemy_ship)

            self.Player_ship.move_lasers(-self.laser_velocity, self.enemies)  # strzelanie statku gracza
