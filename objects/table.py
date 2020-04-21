from objects import player


class TableClass:
    def __init__(self):
        self.table_players = []
        self.hand_players = []
        self.end_session = False
        self.current_state = 'pre-flop'
        self.active_hand = True
        self.player_bets = False
        self.player_raises = False
        self.round_of_betting_complete = False

    def initialise_players(self):
        # TODO verify that they enter something and check that name doesn't already exist
        number_of_players = int(input('Please enter you table size: '))
        for player_number in range(number_of_players):
            player_name = input(f'Player {player_number + 1}: ')
            self.table_players.append(player.PlayerClass(name=player_name))

    def set_dealer(self):
        print('\n' + 'Please enter the name of the player with the dealer chip')
        dealer_found = False
        while not dealer_found:
            dealers_name = input('Player name: ')
            for player in self.table_players:
                if dealers_name == player.name:
                    player.position = 'dealer'
                    dealer_found = True
            if not dealer_found:
                print('Dealer not found from players entered!')

    def print_player_stats(self):
        for active_player in self.table_players:
            print(f'{active_player.name}\n' +
                  f'VPIP: {active_player.VPIP} | PFR: {active_player.PFR} | AF: {active_player.AF}')
        print('\n')

    def remove_inactive_players(self):
        for player in self.table_players:
            if player.is_active is False and player.position is not 'dealer':
                self.table_players.remove(player)
            elif player.is_active is False and player.position is 'dealer':
                # TODO this condition
                print('test')

    def move_dealer_first(self):
        new_positions = []
        for dealer_finder in self.table_players:
            if dealer_finder.position == 'dealer':
                dealer_index = self.table_players.index(dealer_finder)
                new_positions.append(dealer_index)
                for other_players in range(dealer_index + 1, len(self.table_players)):
                    new_positions.append(other_players)
                for other_players in range(0, dealer_index):
                    new_positions.append(other_players)

        self.table_players = [self.table_players[i] for i in new_positions]

    def dealer_first(self):
        if len(self.table_players) > 3:
            self.move_dealer_first()
            self.table_players[1].position = 'sb'
            self.table_players[2].position = 'bb'
            self.table_players[3].position = 'utg'

        # TODO make it work for <= 3 players
        # elif len(self.table_players) == 3:
        #     for player in self.table_players:
        #         if player.position is 'dealer':
        #             next(player)
        #             next(player)
        #             player.action = True
        #
        # elif len(self.table_players) == 2:
        #     for player in self.table_players:
        #         if player.position is 'dealer':
        #             next(player)
        #             player.action = True
        #
        else:
            raise Exception(f'Not enough players (requires at least four) \nPlayers: {self.table_players}')

    def sort_players_preflop(self):
        # TODO combine this with move_dealer_first
        new_positions = []
        for utg_finder in self.table_players:
            if utg_finder.position == 'utg':
                utg_index = self.table_players.index(utg_finder)
                new_positions.append(utg_index)
                for other_players in range(utg_index, len(self.table_players) - 1):
                    new_positions.append(other_players)
                for other_players in range(0, utg_index):
                    new_positions.append(other_players)

        self.table_players = [self.table_players[i] for i in new_positions]

    # TODO rename and combine with above def arrange_players(preflop=True/False):
    def sort_players_postflop(self):
        new_positions = []
        # self.hand_players = []
        # for player_in_hand in self.table_players:
        #     if player_in_hand.current_hand is not False:
        #         self.hand_players.append(player_in_hand)
        for sb_finder in self.table_players:
            if sb_finder.position == 'sb':
                sb_index = self.table_players.index(sb_finder)
                new_positions.append(sb_index)
                for other_players in range(sb_index + 1, len(self.table_players)):
                    new_positions.append(other_players)
                for other_players in range(0, sb_index):
                    new_positions.append(other_players)

        self.table_players = [self.table_players[i] for i in new_positions]

    def update_player(self, player, action):
        if action == 'C' or 'c':
            player.calls += 1
        elif action == 'R' or 'r':
            player.raises += 1
            self.player_raises = True
        elif action == 'B' or 'b':
            player.bets += 1
            self.player_bets = True
        elif action == 'F' or 'f':
            player.current_hand = False

    def update_players_AF(self):
        for player in self.table_players:
            if player.raises > 0 and player.bets > 0 and player.calls > 0:
                player.AF = ((player.raises + player.bets)/player.calls)
            else:
                player.AF = 'NA'

