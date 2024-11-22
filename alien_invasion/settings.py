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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_merge_speed = 1.5
        self.bullet_merge = 4
        self.bullet_width = 6
        self.bullet_height = 22
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 4
        self.merge_threshold = 10

        # Alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 20
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1