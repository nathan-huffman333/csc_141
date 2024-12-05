import pygame.font
from pygame.sprite import Group
from pathlib import Path
from ship import Ship
path = Path("alien_invasion/high_score.txt")


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
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
        self.prep_ships()
    

    def prep_score(self):
        """Turn the score into a rendered image."""
        score = self.stats.score
        score_str = f"{score:,}"

        self.score_image = self.render_text_with_outline(score_str, self.font, self.text_color, (0, 0, 0), 2)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10
        
    
    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = self.stats.high_score
        high_score_str = f"{high_score:,}"
        
        self.high_score_image = self.render_text_with_outline(high_score_str, self.font, (255, 241, 87), (0, 0, 0), 2)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
        if self.stats.score > int(path.read_text()):
            with open("high_score.txt", "w") as file:
                pass
            path.write_text(str(self.stats.score))


    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)

        self.level_image = self.render_text_with_outline(level_str, self.font, self.text_color, (0, 0, 0), 2)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):   
        """Show how many ships are left with an outline around the ship texture."""
        self.ships = pygame.sprite.Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)

            # Resize the ship image
            scaled_image = pygame.transform.scale(ship.image, (65, 65))  # Adjust size as needed

            # Create an outline surface
            outline_width = 3
            # outline_color = (255, 255, 255)  # White outline
            outline_surface = pygame.Surface((scaled_image.get_width() + 2 * outline_width, scaled_image.get_height() + 2 * outline_width), pygame.SRCALPHA)

            # Fill the outline surface with transparency
            outline_surface.fill((0, 0, 0, 0))


            """
            # Create a mask of the ship texture
            mask = pygame.mask.from_surface(scaled_image)

            # Get the outline as a list of points
            outline_points = mask.outline()

            
            # Draw blocky outline by iterating over offsets
            for dx in range(-outline_width, outline_width + 1):
                for dy in range(-outline_width, outline_width + 1):
                    if dx != 0 or dy != 0:  # Skip the original pixels
                        for x, y in outline_points:
                            new_x = x + dx + outline_width
                            new_y = y + dy + outline_width
                            if 0 <= new_x < outline_surface.get_width() and 0 <= new_y < outline_surface.get_height():
                                outline_surface.set_at((new_x, new_y), outline_color)
                                """

            # Blit the original ship onto the outline surface
            outline_surface.blit(scaled_image, (outline_width, outline_width))

            # Update the ship's image to include the outlined texture
            ship.image = outline_surface

            # Position the ship icons
            ship.rect.x = 10 + ship_number * 75  # Adjust spacing
            ship.rect.y = 10
            self.ships.add(ship)


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