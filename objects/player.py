class PlayerClass:
    def __init__(self, name: str, table_position: int):
        self.name = name
        self.table_position = table_position
        self.is_dealer = False
        self.has_bet = False
        self.has_raised = False
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
        self.VPIP_pct = 0
        self.PFR = 0
        self.PFR_pct = 0
