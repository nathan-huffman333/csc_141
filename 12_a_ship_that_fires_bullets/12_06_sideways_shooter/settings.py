# For comments, see sideways_shooter.py

import pygame

class Settings:
    """A class to store all settings for Sideways Shooter."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 2560
        self.screen_height = 1600

        self.bg_color = (5, 0, 50)

        # Ship settings
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (225, 0, 0)
        self.bullets_allowed = 4