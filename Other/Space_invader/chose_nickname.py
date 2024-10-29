from base_menu import Base
from importing import Importing
import main_menu
import game
import pygame
import re

pygame.init()


class Nickname(Base):
    name = ""  # nazwa gracza

    def __init__(self):
        super().__init__()
        self.czyszczenie = True

    # użycie regexa
    def input_nick(self):
        g = game.Game()
        mm = main_menu.MainMenu()

        while self.running:

            if self.czyszczenie:
                Nickname.name = ""
                self.czyszczenie = False

            self.create_nickname()  # wyświetla tekst do wpisywania nazwy i przyciski
            self.draw_back(1080, 530)

            mouse = pygame.mouse.get_pos()

            nazwa = re.fullmatch(r"\w{3,12}", Nickname.name)  # regex, nazwa musi mieć między 3 a 12 znaków

            if self.button_back.collidepoint(mouse):  # back
                if self.click:
                    Nickname.name = ""
                    mm.main_menu()
            elif Base.submit_nickname_button.collidepoint(mouse):  # play
                if self.click:
                    if nazwa is not None:
                        g.main()

            self.click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if nazwa is not None:
                            g.main()
                    elif event.key == pygame.K_ESCAPE:
                        mm.main_menu()
                    elif event.key == pygame.K_BACKSPACE:
                        Nickname.name = Nickname.name[:-1]
                    elif event.key == pygame.K_SPACE:
                        pass
                    else:
                        if len(Nickname.name) < 12:
                            Nickname.name += event.unicode

            # wyświetlanie nicku gracza w ramce
            user_text = self.settings_font.render(Nickname.name, True, (255, 255, 255))
            Importing.WINDOW.blit(user_text, (Base.input_nickname_button.x + 12, Base.input_nickname_button.y - 2))

            pygame.display.update()

        quit()
