from base_menu import Base
import chose_nickname
import main_menu
import pygame

pygame.init()


class Leaderboard(Base):

    def leaderboard(self, wyniki):
        mm = main_menu.MainMenu()
        n = chose_nickname.Nickname()

        while self.running:

            if self.can_create:  # żeby nie tworzyć tego ciągle na nowo
                self.show_leaderboard(wyniki)
                self.can_create = False

            mouse = pygame.mouse.get_pos()

            if self.leaderboard_button0.collidepoint(mouse):  # włączenie gry
                if self.click:
                    n.input_nick()
            elif self.leaderboard_button1.collidepoint(mouse):  # wejście do ustawień
                if self.click:
                    mm.main_menu()
            elif self.leaderboard_button2.collidepoint(mouse):  # wyjście z gry
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mm.main_menu()

        quit()
