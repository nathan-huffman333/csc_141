import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font("alien_invasion/alien_invasion_sprites/upheavtt.ttf", 40)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
    

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"

        self.score_image = self.render_text_with_outline(score_str, self.font, self.text_color, (0, 0, 0), 2)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    
    def show_score(self):
        """Draw scores and level to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        
        self.high_score_image = self.render_text_with_outline(high_score_str, self.font, self.text_color, (0, 0, 0), 2)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)

        self.level_image = self.render_text_with_outline(level_str, self.font, self.text_color, (0, 0, 0), 2)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def render_text_with_outline(self, text, font, text_color, outline_color, thickness):
        # Render the outline
        outline_surface = font.render(text, True, outline_color)
        outline_width = outline_surface.get_width()
        outline_height = outline_surface.get_height()

        # Create a transparent surface large enough for the outline and text
        surface = pygame.Surface((outline_width + thickness * 2, outline_height + thickness * 2), pygame.SRCALPHA)
        surface.fill((0, 0, 0, 0))  # Transparent background

        # Draw the outline by blitting the text with small offsets
        offsets = [
            (-thickness, -thickness), (-thickness, thickness),
            (thickness, -thickness), (thickness, thickness),
            (0, -thickness), (0, thickness),
            (-thickness, 0), (thickness, 0)
        ]
        for dx, dy in offsets:
            offset_text = font.render(text, True, outline_color)
            surface.blit(offset_text, (dx + thickness, dy + thickness))

        # Render the main text and blit it on top of the outline
        text_surface = font.render(text, True, text_color)
        surface.blit(text_surface, (thickness, thickness))

        return surface