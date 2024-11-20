# For comments see alien_invasion.py

import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 2560
        self.screen_height = 1600

        self.bg_color = (22, 15, 22)

        # Ship settings
        self.ship_speed = 3

        # Bullet settings
        self.bullet_speed = 8.0
        self.bullet_merge = 1
        self.bullet_width = 6
        self.bullet_height = 20
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 4

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1