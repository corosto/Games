from base_menu import Base
import chose_nickname
import settings
import pygame

pygame.init()


class MainMenu(Base):

    def main_menu(self):
        s = settings.Settings()
        n = chose_nickname.Nickname()

        while self.running:

            mouse = pygame.mouse.get_pos()

            if self.can_create:  # żeby nie tworzyć tego ciągle na nowo
                Base.show_menu()
                self.can_create = False

            if Base.menu_button0.collidepoint(mouse):  # włączenie gry
                if self.click:
                    n.input_nick()
            elif Base.menu_button1.collidepoint(mouse):  # wejście do ustawień
                if self.click:
                    s.settings()
            elif Base.menu_button2.collidepoint(mouse):  # wyjście z gry
                if self.click:
                    self.running = False

            self.click = False
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
        quit()
