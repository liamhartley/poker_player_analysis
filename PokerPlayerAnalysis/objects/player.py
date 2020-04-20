class PlayerClass:
    def __init__(self, name):
        self.name = name
        self.position = ''
        self.is_active = True
        self.current_hand = True
        self.player_action = ''
        self.checks = 0
        self.raises = 0
        self.bets = 0
        self.calls = 0
        self.preflop_raises = 0
        self.preflop_bet = 0
        self.hands_played = 0
        self.AF = 'NA'
        self.VPIP = 0
        self.PFR = 0
        self.PFR_pct = 0
