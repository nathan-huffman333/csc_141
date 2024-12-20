import pygame.font
from scoreboard import Scoreboard

class Button:
    """A class to build buttons for the game."""
    
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font("alien_invasion/alien_invasion_sprites/upheavtt.ttf", 90)
    

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        
        self.msg_image = Scoreboard.render_text_with_outline(self, msg, self.font, (255,255,255), (0, 0, 0), 5) 
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw the message."""
        self.screen.blit(self.msg_image, self.msg_image_rect)
 
    
   