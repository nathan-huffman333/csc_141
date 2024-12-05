import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from floating_score import FloatingScore
from random import choice
from threading import Timer
from sound_effects import Laser
from parallax_background import ParallaxBackground



class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1920, 1200), pygame.FULLSCREEN, pygame.HWSURFACE | pygame.DOUBLEBUF) #(1920, 1200)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics, and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.laser_fx = Laser()

        self.floating_scores = pygame.sprite.Group()
        
        
        # Initialize game states for Alien Invasion.
        self.game_active = False
        self.game_over = False
        self.waiting_for_start = True
        self.waiting_for_game_over = False

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Make the Play button.
        self.play_button = Button(self, "Enter to Play")

        # Make the Game Over screen.
        self.font = pygame.font.Font("alien_invasion/alien_invasion_sprites/upheavtt.ttf", 120)
        self.game_over_image = Scoreboard.render_text_with_outline(self, "GAME OVER", self.font, (255,255,255), (0, 0, 0), 5)
        self.game_over_image_rect = self.game_over_image.get_rect(center=self.screen.get_rect().center)

        

        self.parallax_background = ParallaxBackground(self.screen, self.settings)


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self): 
        """Start the main loop for the game."""
        while True:
            dt = self.clock.tick(60) / 1000.0
            self._check_events()

            if self.game_active:
                self.ship.update(dt)
                if self.ship.blinking:
                    self.ship.blink_after_hit()
                self._update_bullets()
                self._update_aliens()
        
 
            self.parallax_background.update(dt)
            self._update_screen()

                    
    
    def _check_events(self):
        """Respond to keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_play_button(self):
        """Start a new game when the player hits enter."""
        if self.waiting_for_start and not self.game_active and not self.game_over and not self.waiting_for_game_over:
            self.waiting_for_start = False
            self.game_active = True
            self._update_screen()

        
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_SPACE:
            # Only fire bullets when the game is active
            if self.game_active:
                self._fire_bullet()
        if event.key == pygame.K_RETURN and self.waiting_for_start and not self.game_active: #and not self.game_over and not self.game_active and not self.waiting_for_game_over:
            self._check_play_button()
        else:
            pass


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False


    def _reset_level(self):
        """Reset the level by removing aliens and bullets, then creating a new fleet and centering the ship."""

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        self.floating_scores.empty()
        # Create new fleet and return ship to starting position.
        self._create_fleet()
        self.ship.center_ship()

        self.ship.moving_up = False
        self.ship.moving_down = False
        self.ship.moving_left = False
        self.ship.moving_right = False


    def _reset_game(self):
        """Reset the entire game after a game over."""

        self._reset_level()

        # Reset the game settings.
        self.settings.initialize_dynamic_settings()
    
        # Reset the game statistics.
        self.stats.reset_stats()  # This should reset ships_left here
        self.sb.prep_score() 
        self.sb.prep_level()
        self.sb.prep_ships()  # This updates the ship count on the scoreboard
        self.sb.check_high_score()

        self.game_over = False
        self.waiting_for_game_over = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        self.parallax_background.draw()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.floating_scores.update()  # Update floating scores
        for floating_score in self.floating_scores.sprites():
            floating_score.draw()  # Draw floating scores

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if self.waiting_for_start and not self.game_over and not self.waiting_for_game_over and not self.game_active:
            self.play_button.draw_button()
        
        if self.game_over or self.waiting_for_game_over or self.game_active:
            self.waiting_for_start = False
        else:
            self.waiting_for_start = True
            
        if self.game_over:
            self._show_game_over_screen()
            
                   
        # Make the most recently drawn screen visible.
        pygame.display.flip()


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.laser_fx.play_laser_sfx()


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

         # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for bullet, aliens in collisions.items():
                for alien in aliens:
                    # Add points
                    self.stats.score += self.settings.alien_points

                    # Create a floating score at the alien's position
                    floating_score = FloatingScore(self, alien.rect.centerx, alien.rect.centery, self.settings.alien_points)
                    self.floating_scores.add(floating_score)

                # self.stats.score += self.settings.alien_points * len(aliens)

            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._update_screen()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 1:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Start blinking effect
            self.ship.blinking = True
            
            # Ship will blink for 60 frames (1 second at 60 FPS)
            self.ship.blink_timer = 60  

            # Reset level.
            self._reset_level()

        
        else: 
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.game_active = False
            self.game_over = True

            # Make the Game Over screen visible.
            self._show_game_over_screen()

            # Wait 5 seconds and then reset game.
            
            Timer(5, self._reset_game).start()
            
           
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = self.settings.screen_width/19, self.settings.screen_height/24 
        while current_y < (self.settings.screen_height/2): 
            while current_x < (self.settings.screen_width*(18/19)): 
                self._create_alien(current_x, current_y)
                current_x += (self.settings.screen_width/19)*2 
        
            # Finshed a row; reset x value, and increment y value.
            current_x = self.settings.screen_width/19 
            current_y += (self.settings.screen_height/24)*3 


    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        alien_type = choice([1, 2, 3])  # Randomly choose between three alien types
        new_alien = Alien(self, alien_type=alien_type)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
    
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
        """

        self._check_fleet_edges()
        self.aliens.update()

        # Cull aliens off-screen
        for alien in self.aliens.copy():
            if alien.rect.top >= self.settings.screen_height:
                self.aliens.remove(alien)

        # Check for ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break


    def _show_game_over_screen(self):
        """Display a Game Over screen and wait for input."""
        self.screen.blit(self.game_over_image, self.game_over_image_rect)
        self.waiting_for_game_over = True




if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game() 