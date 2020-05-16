import itertools
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
        self.first_hand = True

    # TODO move some of these methods / functions into their own modules
    def initialise_players(self):
        # TODO verify that they enter an int and check that name doesn't already exist
        number_of_players = int(input('Please enter you table size: '))
        for player_number in range(number_of_players):
            player_name = input(f'Player {player_number + 1}: ')
            self.table_players.append(player.PlayerClass(name=player_name, table_position=player_number))

    def set_dealer(self):
        print('\n' + 'Please enter the name of the player with the dealer chip')
        dealer_found = False
        while not dealer_found:
            dealers_name = input('Player name: ')
            for player in self.table_players:
                if dealers_name == player.name:
                    player.is_dealer = True
                    dealer_found = True
            if dealer_found is False:
                print('Dealer not found from players entered!')

    def move_dealer(self):
        dealer_moved = False
        player_iterator = itertools.cycle(self.table_players)
        for player in player_iterator:
            if dealer_moved is True:
                break
            if player.is_dealer is True:
                player.is_dealer = False
                next(player_iterator).is_dealer = True
                dealer_moved = True

    def print_player_stats(self):
        for active_player in self.table_players:
            print(f'{active_player.name}\n' +
                  f'VPIP: {active_player.VPIP_pct} | PFR: {active_player.PFR_pct} | AF: {active_player.AF}')
        print('\n')

    def sort_players(self, player_index: str, preflop=False):
        new_table_positions = []
        sorting_complete = False

        table_iterator = itertools.cycle(self.table_players)

        # Sort players pre and postflop
        if player_index == 'dealer':
            if preflop is False:
                for player in table_iterator:
                    if sorting_complete is True:
                        break
                    elif player.is_dealer is True:
                        for new_positions in range(0, len(self.table_players)):
                            next_player = next(table_iterator)
                            if next_player.current_hand is True:
                                new_table_positions.append(next_player)
                        sorting_complete = True
            elif preflop is True:
                for player in table_iterator:
                    if sorting_complete is True:
                        break
                    elif player.is_dealer is True:
                        next(table_iterator)
                        next(table_iterator)
                        for new_positions in range(0, len(self.table_players)):
                            next_player = next(table_iterator)
                            if next_player.current_hand is True:
                                new_table_positions.append(next_player)
                        sorting_complete = True

        # Action the better last
        elif player_index == 'better':
            for player in table_iterator:
                if sorting_complete is True:
                    break
                elif player.has_bet is True:
                    for new_positions in range(0, len(self.table_players)):
                        next_player = next(table_iterator)
                        if next_player.current_hand is True:
                            new_table_positions.append(next_player)
                    sorting_complete = True

        elif player_index == 'raiser':
            for player in table_iterator:
                if sorting_complete is True:
                    break
                elif player.has_raised is True:
                    for new_positions in range(0, len(self.table_players)):
                        next_player = next(table_iterator)
                        if next_player.current_hand is True:
                            new_table_positions.append(next_player)
                    sorting_complete = True

        else:
            print('Please enter a valid player_first argument! (dealer, better or raiser)')

        self.hand_players = new_table_positions

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

    def update__table_players_stats(self):

        # AF
        for player in self.table_players:
            if player.raises > 0 and player.bets > 0 and player.calls > 0:
                player.AF = ((player.raises + player.bets)/player.calls)
            else:
                player.AF = 'NA'

        # VPIP
        for player in self.table_players:
            if player.VPIP > 0:
                player.VPIP_pct = player.VPIP / player.hands_played

        # PFR
        for player in self.table_players:
            if player.PFR > 0:
                player.PFR_pct = player.PFR / player.hands_played

    def count_players_playing(self):
        for player in self.table_players:
            if player.current_hand is True:
                player.hands_played += 1

    def remove_players(self):
        print('Were any players knocked out?')
        response = input('(N / Y or blank): ')
        if response in ['N', 'n', ' ', '']:
            pass
        elif response in ['Y', 'y']:
            print('Please enter the players names separated by commas')
            print('e.g. "Mike, Sam, Jordan"')
            players_knocked_out = input('Knocked out: ')
            players_knocked_out.strip(',')
            for players_name in players_knocked_out:
                players_name = players_name.strip()
                for table_player in self.table_players:
                    if table_player.name == players_name:
                        if table_player.is_dealer is True:
                            self.move_dealer()
                        self.table_players.remove(table_player)
        print('\n')
