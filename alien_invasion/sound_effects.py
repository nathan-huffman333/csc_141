import pygame

pygame.init()
pygame.mixer.init()

class Laser():
    def __init__(self):
        self.laser_sfx = pygame.mixer.Sound("alien_invasion/alien_invasion_sprites/laser.mp3")
        self.laser_sfx.set_volume(0.5)
    

    def play_laser_sfx(self):
        self.laser_sfx.play()