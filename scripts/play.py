from objects.table import TableClass as table
from scripts.action import round_of_betting


def play_hand(active_table):

    print('---- New Hand ----\n')
    active_table.active_hand = True
    table.remove_inactive_players(active_table)
    # table.move_dealer_chip
    table.dealer_first(active_table)
    # Currently don't know who is playing
    active_table.hand_players = []

    print('---- Pre-Flop ----')
    table.current_state = 'pre-flop'
    table.sort_players_preflop(active_table)
    round_of_betting(active_table, preflop=True)

    # active_table.calculate_VPIP() % of hands played
    if active_table.active_hand is True:
        print('---- Flop ----')
        active_table.hand_players = []
        table.current_state = 'flop'
        table.sort_players_postflop(active_table)
        round_of_betting(active_table)

    if active_table.active_hand is True:
        print('---- Turn ----')
        active_table.hand_players = []
        table.current_state = 'turn'
        round_of_betting(active_table)

    if active_table.active_hand is True:
        print('---- River ----')
        active_table.hand_players = []
        table.current_state = 'river'
        round_of_betting(active_table)

    print('\n---- Hand Complete! ----\n')


