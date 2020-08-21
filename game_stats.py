class GameStats():
    '''track statistics for alien invansion.'''

    def __init__(self,ai_settings):
        '''initialize the settings.'''
        self.ai_settings = ai_settings
        #start Alien Inavnsion game  in an inactive state.
        self.game_active = False
        self.reset_stats()
        #high score should never be reset
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        '''initializes statistics that can change during the game.'''
        self.ships_left  = self.ai_settings.ship_limit
        self.score = 0