# For comments see rain_invasion.py

import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 2560
        self.screen_height = 1600

        self.bg_color = (22, 15, 22)

        # raindrop settings
        self.raining_drop_speed = 3