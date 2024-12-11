import pygame
pygame.init()
pygame.mixer.init()


class Laser():
    """Class to manage laser sound effects."""
    def __init__(self):
        """Initialize the path to and volume of the laser sound effect."""
        self.laser_sfx = pygame.mixer.Sound("alien_invasion/alien_invasion_sprites/laser.mp3")
        self.laser_sfx.set_volume(0.5)
    

    def play_laser_sfx(self):
        """Play the laser sound effect."""
        self.laser_sfx.play()



class Explosion_sfx():
    """Class to manage explosion sound effects."""
    def __init__(self):
        """Initialize the path to and volume of the explosion sound effect."""
        self.explosion_sfx = pygame.mixer.Sound("alien_invasion/alien_invasion_sprites/explosion.mp3")
        self.explosion_sfx.set_volume(0.5)
    

    def play_explosion_sfx(self):
        """Play the explosion sound effect."""
        self.explosion_sfx.play()



class Point_sfx():
    """Class to manage the sound effect for getting points."""
    def __init__(self):
        """Initialize the path to and volume of the sound effect for getting points."""
        self.point_sfx = pygame.mixer.Sound("alien_invasion/alien_invasion_sprites/collect_point.wav")
        self.point_sfx.set_volume(0.5)
    

    def play_point_sfx(self):
        """Play the sound effect for getting points."""
        self.point_sfx.play()