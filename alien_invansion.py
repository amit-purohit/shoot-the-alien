import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #initialize pygame,settings and screen object
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invansion")

    #make the play button.
    play_button = Button(ai_settings,screen,"play")


    #create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #making  a ship,a group of bullet and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #set the background color

    bg_color = (233,233,233)

    #Make a alien
    alien = Alien(ai_settings,screen)

    # create the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #start the main loop for the game.

    while True:

        #watch for keyboard and mouse events.

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,
                              ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()