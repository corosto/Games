from base_menu import Base
import main_menu
import change_ship
import change_weapon
import change_background
import pygame

pygame.init()


class Settings(Base):
    music = 1
    sfx = 1

    def settings(self):
        mm = main_menu.MainMenu()
        cs = change_ship.ChangeShip()
        cw = change_weapon.ChangeWeapon()
        cb = change_background.ChangeBackground()

        while self.running:

            mouse = pygame.mouse.get_pos()

            self.show_settings(Settings.music, Settings.sfx, cs.chosen_ship, cw.chosen_weapon, cb.chosen_background)
            self.draw_back(1080, 530)

            if Base.settings_button0.collidepoint(mouse):  # muzyka on
                if self.click:
                    Settings.music = 1
            elif Base.settings_button00.collidepoint(mouse):  # muzyka off
                if self.click:
                    Settings.music = 0
            elif Base.settings_button1.collidepoint(mouse):  # sfx on
                if self.click:
                    Settings.sfx = 1
            elif Base.settings_button11.collidepoint(mouse):  # sfx off
                if self.click:
                    Settings.sfx = 0
            elif Base.settings_button2.collidepoint(mouse):  # zmiana statku
                if self.click:
                    cs.change_ship()
            elif Base.settings_button3.collidepoint(mouse):  # zmiana rakietki
                if self.click:
                    cw.change_weapon()
            elif Base.settings_button4.collidepoint(mouse):  # zmiana tla
                if self.click:
                    cb.change_background()
            elif self.button_back.collidepoint(mouse):  # back
                if self.click:
                    mm.main_menu()

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
                            mm.main_menu()
                        self.was_released = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.was_released = True

        quit()
