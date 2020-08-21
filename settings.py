class Settings:
    '''A class to store all settings for Alien Invansion.'''

    def __init__(self):
        '''initialize the game's static  settings'''
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        #bullet setings

        self.bullet_speed_factor = 0.1
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 60

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right ; -1 represents left
        self.fleet_direction= 1

        #how quickly th game speeds up.
        self.speedup_scale = 1.1
        #how quickly the alien point values increase.
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''initialize settings that change throught the game.'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3

        self.alien_speed_factor = 1
        #fleet direction of 1 represents right,-1 represents left.
        self.fleet_direction = 1

        #scoring.
        self.alien_points = 50

    def increase_speed(self):
        '''increase speed settings and alien points values.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


