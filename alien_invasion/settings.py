class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1200

        self.bg_color = (22, 15, 22)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_merge = 4
        self.bullet_width = 6
        self.bullet_height = 22
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 4
        self.merge_threshold = 10

        # Alien settings
        self.fleet_drop_speed = 20

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Ship settings
        self.ship_speed = 3.5

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_merge_speed = 1.5

        # Alien settings
        self.alien_speed = 2.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        #self.ship_speed *= self.speedup_scale
        #self.bullet_merge_speed *= self.speedup_scale
        #self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points +25)