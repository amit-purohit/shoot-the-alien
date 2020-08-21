import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent a single alien in the fleet.'''

    def __init__(self,ai_settings,screen):
        '''initialize the alien and set its starting position'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and its rect attribute
        self.image = pygame.image.load('images/bad_alien_ship.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        '''draw the alien at its current position.'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''MOve the alien right or left '''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x =self.x

    def check_edges(self):
        '''return true if alien is at the end of the edge.'''
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

