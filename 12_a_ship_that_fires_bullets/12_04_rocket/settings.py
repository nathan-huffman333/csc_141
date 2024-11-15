# For comments, see alien_invasion.py

import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 2560
        self.screen_height = 1600

        self.bg_color = (5, 0, 50)

        # Ship settings
        self.ship_speed = 2.5