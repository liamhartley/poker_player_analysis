from objects.table import TableClass as table
from scripts.action import round_of_betting


def play_hand(active_table):

    print('---- New Hand ----\n')
    active_table.active_hand = True
    if active_table.first_hand is False:
        active_table.move_dealer()
        active_table.remove_players()

    print('---- Pre-Flop ----')
    active_table.current_state = 'pre-flop'
    table.sort_players(active_table, player_index='dealer', preflop=True)
    round_of_betting(active_table)

    # active_table.calculate_VPIP() % of hands played
    if active_table.active_hand is True:
        print('---- Flop ----')
        active_table.count_players_playing()
        active_table.current_state = 'flop'
        table.sort_players(active_table, player_index='dealer')
        round_of_betting(active_table)

    if active_table.active_hand is True:
        print('---- Turn ----')
        active_table.current_state = 'turn'
        table.sort_players(active_table, player_index='dealer')
        round_of_betting(active_table)

    if active_table.active_hand is True:
        print('---- River ----')
        active_table.current_state = 'river'
        table.sort_players(active_table, player_index='dealer')
        round_of_betting(active_table)

    print('\n---- Hand Complete! ----\n')
    active_table.first_hand = False
