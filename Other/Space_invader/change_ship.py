from base_menu import Base
import settings
import pygame

pygame.init()


class ChangeShip(Base):
    chosen_ship = 0  # wybór statku

    def change_ship(self):
        s = settings.Settings()

        while self.running:

            self.show_ship(ChangeShip.chosen_ship)  # wyświetla statki w menu i pokazuje miniaturki
            self.draw_back(1080, 530)  # wyświetla guzik back

            mouse = pygame.mouse.get_pos()

            if self.ship_rocket_button0.collidepoint(mouse):
                if self.click:
                    ChangeShip.chosen_ship = 0
            elif self.ship_rocket_button1.collidepoint(mouse):
                if self.click:
                    ChangeShip.chosen_ship = 1
            elif self.ship_rocket_button2.collidepoint(mouse):
                if self.click:
                    ChangeShip.chosen_ship = 2
            elif Base.button_back.collidepoint(mouse):  # back
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
