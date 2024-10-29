from base_menu import Base
from importing import Importing
import settings
import pygame

pygame.init()


class ChangeBackground(Base):
    chosen_background = 0  # wybór tła
    button_back = pygame.Rect(522.5, 630, 235, 50)  # guzik back

    @staticmethod
    def draw_back(x, y):
        pygame.draw.rect(Importing.WINDOW, Base.purple, ChangeBackground.button_back)
        Importing.WINDOW.blit(Base.button_back_text, (x, y))

    def change_background(self):
        s = settings.Settings()

        while self.running:

            self.show_background(ChangeBackground.chosen_background)  # wyświetla tła w menu i pokazuje miniaturki
            self.draw_back(602.5, 630)  # wyświetla guzik back

            mouse = pygame.mouse.get_pos()

            if self.background_button0.collidepoint(mouse):
                if self.click:
                    ChangeBackground.chosen_background = 0
            elif self.background_button1.collidepoint(mouse):
                if self.click:
                    ChangeBackground.chosen_background = 1
            elif self.background_button2.collidepoint(mouse):
                if self.click:
                    ChangeBackground.chosen_background = 2
            elif self.background_button3.collidepoint(mouse):
                if self.click:
                    ChangeBackground.chosen_background = 3
            elif self.background_button4.collidepoint(mouse):
                if self.click:
                    ChangeBackground.chosen_background = 4
            elif self.background_button5.collidepoint(mouse):
                if self.click:
                    ChangeBackground.chosen_background = 5
            elif ChangeBackground.button_back.collidepoint(mouse):
                if self.click:
                    s.settings()

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
                        if self.was_released:
                            s.settings()
                        self.was_released = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.was_released = True

        quit()
