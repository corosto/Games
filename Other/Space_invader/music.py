from importing import Importing
import pygame

pygame.init()


class Music:

    @staticmethod
    def play():
        # żeby z automatu nie byl volume na 1
        pygame.mixer.music.set_volume(0.20)
        Importing.LASER_SOUND.set_volume(0.04)
        Importing.MISSILE_SOUND.set_volume(0.05)
        # żeby muzyka grała w loopie
        pygame.mixer.music.play(-1)
