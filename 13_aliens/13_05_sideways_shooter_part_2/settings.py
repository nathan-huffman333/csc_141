# For comments, see sideways_shooter_part_2.py

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
        self.ship_speed = 5

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_merge_speed = 1.5
        self.bullet_merge = 4
        self.bullet_width = 22
        self.bullet_height = 6
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 4
        self.merge_threshold = 10

        # Alien settings
        self.alien_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 12
        self.fleet_approach_speed = 10