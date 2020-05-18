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

    # ---- Flop ----
    active_table.count_players_playing()
    active_table.current_state = 'flop'
    table.sort_players(active_table, player_index='dealer')
    if active_table.active_hand is True and len(active_table.hand_players) > 1:
        print('---- Flop ----')
        round_of_betting(active_table)

    # ---- Turn ----
    active_table.current_state = 'turn'
    table.sort_players(active_table, player_index='dealer')
    if active_table.active_hand is True and len(active_table.hand_players) > 1:
        print('---- Turn ----')
        round_of_betting(active_table)

    # ---- River ----
    active_table.current_state = 'river'
    table.sort_players(active_table, player_index='dealer')
    if active_table.active_hand is True and len(active_table.hand_players) > 1:
        print('---- River ----')
        round_of_betting(active_table)

    print('\n---- Hand Complete! ----\n')
    active_table.first_hand = False
