from importing import Importing
import pygame

pygame.init()


class Base:
    purple = (48, 60, 166)
    white = (255, 255, 255)
    green = (82, 87, 71)
    red_outside = (138, 29, 29)
    green_outside = (40, 143, 81)

    settings_font = pygame.font.SysFont("comicsans", 35)  # czcionka dla ustawień
    leaderboard_font = pygame.font.SysFont("comicsans", 20)  # czcionka dla leaderboard'u
    title_font = pygame.font.SysFont("comicsans", 50)  # czcionka dla tytułu
    small_font = pygame.font.SysFont("comicsans", 14)  # mała czcionka dla nickname

    button_back = pygame.Rect(1000, 530, 235, 50)  # back button
    button_back_text = settings_font.render("Back", True, white)  # back tekst

    ship_rocket_button0 = pygame.Rect(300, 300, 80, 80)  # guziki (środek) na wybieranie statku i rakiet
    ship_rocket_button1 = pygame.Rect(600, 300, 80, 80)
    ship_rocket_button2 = pygame.Rect(900, 300, 80, 80)
    out_ship_rocket_button0 = pygame.Rect(305, 305, 70, 70)  # guziki (zewnątrz) na wybieranie statku i rakiet
    out_ship_rocket_button1 = pygame.Rect(605, 305, 70, 70)
    out_ship_rocket_button2 = pygame.Rect(905, 305, 70, 70)

    background_button0 = pygame.Rect(45, 145, 330, 190)  # guziki na wybieranie tła
    background_button1 = pygame.Rect(45, 395, 330, 190)
    background_button2 = pygame.Rect(475, 145, 330, 190)
    background_button3 = pygame.Rect(475, 395, 330, 190)
    background_button4 = pygame.Rect(905, 145, 330, 190)
    background_button5 = pygame.Rect(905, 395, 330, 190)

    input_nickname_button = pygame.Rect(500, 335, 280, 50)  # guziki na wybieranie nazwy
    submit_nickname_button = pygame.Rect(790, 335, 135, 50)

    leaderboard_button0 = pygame.Rect(220, 620, 200, 50)  # włączenie gry
    leaderboard_button1 = pygame.Rect(540, 620, 200, 50)  # wejście do menu
    leaderboard_button2 = pygame.Rect(860, 620, 200, 50)  # wyjście z gry
    leaderboard_board = pygame.Rect(450, 180, 380, 400)  # leaderboard

    menu_button0 = pygame.Rect(545, 450, 200, 50)  # włączenie gry
    menu_button1 = pygame.Rect(545, 530, 200, 50)  # wejście do ustawień
    menu_button2 = pygame.Rect(545, 610, 200, 50)  # wyjście z gry

    settings_button0 = pygame.Rect(50, 100, 200, 50)  # muzyka on
    settings_button00 = pygame.Rect(50, 200, 200, 50)  # muzyka off
    settings_button1 = pygame.Rect(1020, 100, 200, 50)  # sfx on
    settings_button11 = pygame.Rect(1020, 200, 200, 50)  # sfx off
    settings_button2 = pygame.Rect(50, 330, 235, 50)  # zmiana statku
    settings_button3 = pygame.Rect(50, 530, 235, 50)  # zmiana rakiet
    settings_button4 = pygame.Rect(1000, 330, 235, 50)  # zmiana tla

    def __init__(self):
        self.running = True
        self.click = False
        self.was_released = True
        self.can_create = True

    @staticmethod
    def draw_back(x, y):  # tworzenie guzika back
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.button_back)
        Importing.WINDOW.blit(Base.button_back_text, (x, y))

    @staticmethod
    def show_background(chosen_background):  # wyświetla tła w menu i pokazuje miniaturki

        Importing.WINDOW.blit(Importing.MENU_BCK, (0, 0))
        title_label = Base.title_font.render("Chose your game background", True, Base.white)
        Importing.WINDOW.blit(title_label, (Importing.WIDTH / 2 - title_label.get_width() / 2, 50))

        if chosen_background == 0:
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.background_button0)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button1)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button2)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button3)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button4)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button5)

        elif chosen_background == 1:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button0)
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.background_button1)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button2)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button3)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button4)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button5)

        elif chosen_background == 2:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button0)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button1)
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.background_button2)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button3)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button4)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button5)

        elif chosen_background == 3:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button0)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button1)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button2)
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.background_button3)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button4)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button5)

        elif chosen_background == 4:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button0)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button1)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button2)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button3)
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.background_button4)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button5)

        elif chosen_background == 5:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button0)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button1)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button2)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button3)
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.background_button4)
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.background_button5)

        scaled = pygame.transform.scale(Importing.BACKGROUND0, (320, 180))
        Importing.WINDOW.blit(scaled, (50, 150))
        scaled = pygame.transform.scale(Importing.BACKGROUND1, (320, 180))
        Importing.WINDOW.blit(scaled, (50, 400))
        scaled = pygame.transform.scale(Importing.BACKGROUND2, (320, 180))
        Importing.WINDOW.blit(scaled, (480, 150))
        scaled = pygame.transform.scale(Importing.BACKGROUND3, (320, 180))
        Importing.WINDOW.blit(scaled, (480, 400))
        scaled = pygame.transform.scale(Importing.BACKGROUND4, (320, 180))
        Importing.WINDOW.blit(scaled, (910, 150))
        scaled = pygame.transform.scale(Importing.BACKGROUND5, (320, 180))
        Importing.WINDOW.blit(scaled, (910, 400))

    @staticmethod
    def show_ship(chosen_ship):  # wyświetla statki w menu i pokazuje miniaturki

        Importing.WINDOW.blit(Importing.MENU_BCK, (0, 0))
        title_label = Base.title_font.render("Chose your ship", True, Base.white)
        Importing.WINDOW.blit(title_label, (Importing.WIDTH / 2 - title_label.get_width() / 2, 50))

        if chosen_ship == 0:
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.ship_rocket_button0)  # zewnętrzny kwadrat
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button0)  # wewnętrzny kwadrat

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button1)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button1)

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button2)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button2)

        elif chosen_ship == 1:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button0)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button0)

            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.ship_rocket_button1)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button1)

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button2)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button2)

        elif chosen_ship == 2:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button0)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button0)

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button1)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button1)

            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.ship_rocket_button2)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button2)

        Importing.WINDOW.blit(Importing.PLAYER_SHIP0, (308, 308))
        Importing.WINDOW.blit(Importing.PLAYER_SHIP1, (608, 308))
        Importing.WINDOW.blit(Importing.PLAYER_SHIP2, (908, 308))

    @staticmethod
    def show_weapon(chosen_weapon):  # wyświetla bronie w menu i pokazuje miniaturki

        Importing.WINDOW.blit(Importing.MENU_BCK, (0, 0))
        title_label = Base.title_font.render("Chose your weapon", True, Base.white)
        Importing.WINDOW.blit(title_label, (Importing.WIDTH / 2 - title_label.get_width() / 2, 50))

        if chosen_weapon == 0:
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.ship_rocket_button0)  # zewnętrzny kwadrat
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button0)  # wewnętrzny kwadrat

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button1)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button1)

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button2)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button2)

        elif chosen_weapon == 1:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button0)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button0)

            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.ship_rocket_button1)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button1)

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button2)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button2)

        elif chosen_weapon == 2:
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button0)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button0)

            pygame.draw.rect(Importing.WINDOW, Base.red_outside, Base.ship_rocket_button1)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button1)

            pygame.draw.rect(Importing.WINDOW, Base.green_outside, Base.ship_rocket_button2)
            pygame.draw.rect(Importing.WINDOW, Base.green, Base.out_ship_rocket_button2)

        Importing.WINDOW.blit(Importing.BIGGER_PLAYER_MISSILE0, (308, 308))
        Importing.WINDOW.blit(Importing.BIGGER_PLAYER_MISSILE1, (608, 308))
        Importing.WINDOW.blit(Importing.BIGGER_PLAYER_MISSILE2, (908, 308))

    @staticmethod
    def create_nickname():  # wyświetla tekst do wpisywania nazwy i przyciski

        Importing.WINDOW.blit(Importing.MENU_BCK, (0, 0))

        input_button_text0 = Base.settings_font.render("Chose your name:", True, (255, 255, 255))
        input_button_text1 = Base.small_font.render("Between 3-12 word characters", True, (255, 255, 255))
        Importing.WINDOW.blit(input_button_text0, (500, 275))  # text nad
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.input_nickname_button, 2)  # (... ,2) robi tylko ramkę
        Importing.WINDOW.blit(input_button_text1, (540, 385))  # text pod

        submit_button_text = Base.settings_font.render("Submit", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.submit_nickname_button)
        Importing.WINDOW.blit(submit_button_text, (800, 335))

    @staticmethod
    def show_leaderboard(wyniki):  # wyświetla tabele wyników i przyciski

        Importing.WINDOW.blit(Importing.MENU_BCK, (0, 0))

        lost_label = Base.title_font.render("You Lost! Game Over", True, (255, 0, 0))
        Importing.WINDOW.blit(lost_label, (Importing.WIDTH / 2 - lost_label.get_width() / 2, 30))
        title_label = Base.title_font.render("Leaderboard", True, Base.white)
        Importing.WINDOW.blit(title_label, (Importing.WIDTH / 2 - title_label.get_width() / 2, 100))

        button0_text = Base.settings_font.render("Play", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.leaderboard_button0)
        Importing.WINDOW.blit(button0_text, (290, 617))

        button1_text = Base.settings_font.render("Menu", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.leaderboard_button1)
        Importing.WINDOW.blit(button1_text, (595, 617))

        button2_text = Base.settings_font.render("Exit", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.leaderboard_button2)
        Importing.WINDOW.blit(button2_text, (927, 617))

        pygame.draw.rect(Importing.WINDOW, (0, 0, 0), Base.leaderboard_board)
        pygame.draw.rect(Importing.WINDOW, (255, 255, 255), Base.leaderboard_board, 2)

        y_axis = 190
        for i in range(10):
            wynik = Base.leaderboard_font.render(str(i + 1) + ". " + str(wyniki[i][1]) + " - " + str(wyniki[i][0]),
                                                 True, Base.white)
            Importing.WINDOW.blit(wynik, (468, y_axis))
            y_axis += 38

    @staticmethod
    def show_menu():  # wyświetla menu

        Importing.WINDOW.blit(Importing.MENU_BCK, (0, 0))

        title_label = Base.title_font.render("Space Invader", True, Base.white)
        Importing.WINDOW.blit(title_label, (Importing.WIDTH / 2 - title_label.get_width() / 2, 50))  # tlo

        button0_text = Base.settings_font.render("Play", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.menu_button0)
        Importing.WINDOW.blit(button0_text, (615, 450))

        button1_text = Base.settings_font.render("Settings", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.menu_button1)
        Importing.WINDOW.blit(button1_text, (580, 530))

        button2_text = Base.settings_font.render("Exit", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.menu_button2)
        Importing.WINDOW.blit(button2_text, (610, 610))

    @staticmethod
    def show_settings(music, sfx, chosen_ship, chosen_weapon, chosen_background):  # wyświetla ustawienia

        Importing.WINDOW.blit(Importing.MENU_BCK, (0, 0))

        title_label = Base.title_font.render("Settings", True, Base.white)
        Importing.WINDOW.blit(title_label, (Importing.WIDTH / 2 - title_label.get_width() / 2, 50))
        additional_label = Base.settings_font.render("<Press a button to switch>", True, (255, 255, 255))
        Importing.WINDOW.blit(additional_label, (Importing.WIDTH / 2 - additional_label.get_width() / 2, 630))

        if music == 1:
            button0_frame = pygame.Rect(45, 95, 210, 60)  # muzyka on | plecy
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, button0_frame)

            button00_frame = pygame.Rect(45, 195, 210, 60)  # muzyka off | plecy
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, button00_frame)

            pygame.mixer.music.unpause()

        elif music == 0:
            button0_frame = pygame.Rect(45, 95, 210, 60)  # muzyka on | plecy
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, button0_frame)

            button00_frame = pygame.Rect(45, 195, 210, 60)  # muzyka off | plecy
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, button00_frame)

            pygame.mixer.music.pause()

        if sfx == 1:
            button1_frame = pygame.Rect(1015, 95, 210, 60)  # sfx on | plecy
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, button1_frame)

            button11_frame = pygame.Rect(1015, 195, 210, 60)  # sfx off | plecy
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, button11_frame)

            Importing.LASER_SOUND.set_volume(0.05)
            Importing.MISSILE_SOUND.set_volume(0.05)

        elif sfx == 0:
            button1_frame = pygame.Rect(1015, 95, 210, 60)  # sfx on | plecy
            pygame.draw.rect(Importing.WINDOW, Base.red_outside, button1_frame)

            button11_frame = pygame.Rect(1015, 195, 210, 60)  # sfx off | plecy
            pygame.draw.rect(Importing.WINDOW, Base.green_outside, button11_frame)

            Importing.LASER_SOUND.set_volume(0)
            Importing.MISSILE_SOUND.set_volume(0)

        button0_text = Base.settings_font.render("Music On", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.settings_button0)
        Importing.WINDOW.blit(button0_text, (75, 100))

        button00_text = Base.settings_font.render("Music Off", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.settings_button00)
        Importing.WINDOW.blit(button00_text, (68, 200))

        button1_text = Base.settings_font.render("SFX On", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.settings_button1)
        Importing.WINDOW.blit(button1_text, (1050, 100))

        button11_text = Base.settings_font.render("SFX Off", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.settings_button11)
        Importing.WINDOW.blit(button11_text, (1050, 200))

        button2_text = Base.settings_font.render("Spaceship", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.settings_button2)
        Importing.WINDOW.blit(button2_text, (85, 330))
        pygame.draw.rect(Importing.WINDOW, Base.green_outside, pygame.Rect(320, 320, 80, 80))  # zewnętrzny kwadrat
        pygame.draw.rect(Importing.WINDOW, Base.green, pygame.Rect(325, 325, 70, 70))  # wewnętrzny kwadrat

        button3_text = Base.settings_font.render("Ammo", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.settings_button3)
        Importing.WINDOW.blit(button3_text, (122, 530))
        pygame.draw.rect(Importing.WINDOW, Base.green_outside, pygame.Rect(320, 520, 80, 80))  # zewnętrzny kwadrat
        pygame.draw.rect(Importing.WINDOW, Base.green, pygame.Rect(325, 525, 70, 70))  # wewnętrzny kwadrat

        button4_text = Base.settings_font.render("Background", True, Base.white)
        pygame.draw.rect(Importing.WINDOW, Base.purple, Base.settings_button4)
        Importing.WINDOW.blit(button4_text, (1025, 330))
        pygame.draw.rect(Importing.WINDOW, Base.green_outside, pygame.Rect(637, 270, 330, 190))  # zewnętrzny kwadrat

        if chosen_ship == 0:
            Importing.WINDOW.blit(Importing.PLAYER_SHIP0, (328, 330))
        elif chosen_ship == 1:
            Importing.WINDOW.blit(Importing.PLAYER_SHIP1, (328, 330))
        elif chosen_ship == 2:
            Importing.WINDOW.blit(Importing.PLAYER_SHIP2, (328, 330))

        if chosen_weapon == 0:
            Importing.WINDOW.blit(Importing.BIGGER_PLAYER_MISSILE0, (328, 528))
        elif chosen_weapon == 1:
            Importing.WINDOW.blit(Importing.BIGGER_PLAYER_MISSILE1, (328, 528))
        elif chosen_weapon == 2:
            Importing.WINDOW.blit(Importing.BIGGER_PLAYER_MISSILE2, (328, 528))

        if chosen_background == 0:
            scaled = pygame.transform.scale(Importing.BACKGROUND0, (320, 180))
            Importing.WINDOW.blit(scaled, (642, 275))
        elif chosen_background == 1:
            scaled = pygame.transform.scale(Importing.BACKGROUND1, (320, 180))
            Importing.WINDOW.blit(scaled, (642, 275))
        elif chosen_background == 2:
            scaled = pygame.transform.scale(Importing.BACKGROUND2, (320, 180))
            Importing.WINDOW.blit(scaled, (642, 275))
        elif chosen_background == 3:
            scaled = pygame.transform.scale(Importing.BACKGROUND3, (320, 180))
            Importing.WINDOW.blit(scaled, (642, 275))
        elif chosen_background == 4:
            scaled = pygame.transform.scale(Importing.BACKGROUND4, (320, 180))
            Importing.WINDOW.blit(scaled, (642, 275))
        elif chosen_background == 5:
            scaled = pygame.transform.scale(Importing.BACKGROUND5, (320, 180))
            Importing.WINDOW.blit(scaled, (642, 275))
