from scripts import check_hands as check
from helpers import player_helpers


def player_action(players, table):
    actions_available = ['C', 'c', 'R', 'r', 'B', 'b', 'F', 'f', '', ' ', 'check']
    table.player_raises = False
    table.player_bets = False
    all_players_actioned = False
    action_counter = 0
    current_players = 0
    for player in players:
        if player.current_hand is True:
            current_players += 1
            table.hand_players.append(player)
        if table.player_raises is False and table.player_bets is False and player.current_hand is True:
            # If they're still playing
            # if ordered_player.current_hand is True:
            player.player_action = 'NA'
            while player.player_action not in actions_available:
                player_move = input(f'{player.name}: ')
                if player_move not in actions_available:
                    print('Invalid action! '
                          'Please enter C (call), B (bet), R (raise), F (fold) or blank for a check')
                player_helpers.update_player_action(player, player_move, table)

            action_counter += 1

    if action_counter >= len(table.hand_players):
        all_players_actioned = True
    return all_players_actioned


def round_of_betting(table, preflop=False):

    for player in table.table_players:
        player.player_action = 'NA'

    round_of_betting_complete = False

    while round_of_betting_complete is False:

        all_players_actioned = player_action(table.table_players, table)

        if all_players_actioned is False:
            # Find the better or raiser
            if table.player_bets is True or table.player_raises is True:
                bet_index = 'NA'
                raise_index = 'NA'
                for players_round_complete in table.hand_players:
                    if bet_index and raise_index == 'NA':
                        if players_round_complete.player_action == 'b' or players_round_complete.player_action == 'B':
                            bet_index = table.hand_players.index(players_round_complete)
                        elif players_round_complete.player_action == 'r' or players_round_complete.player_action == 'R':
                            raise_index = table.hand_players.index(players_round_complete)

                # Re-order the list and run again
                if bet_index is not 'NA':
                    table.hand_players = table.table_players[(bet_index+1):] + table.table_players[:bet_index]
                elif raise_index is not 'NA':
                    table.hand_players = table.table_players[(raise_index+1):] + table.table_players[:raise_index]

        elif all_players_actioned is True:
            if preflop:
                # Everyone calls or folds
                call_fold_counter = check.check_actions(table.hand_players, ['c', 'C', 'f', 'F'])
                if call_fold_counter == len(table.hand_players) - 1 and table.hand_players[-1].player_action not in ['b', 'B', 'r', 'R']:
                    round_of_betting_complete = True

            # Everyone checks
            check_counter = check.check_actions(table.hand_players, ['', ' ', 'check'])
            if check_counter == len(table.hand_players):
                round_of_betting_complete = True

            # Everyone folds
            fold_counter = 0
            for player in table.hand_players:
                if player.current_hand == False:
                    fold_counter += 1
                if fold_counter == len(table.hand_players) - 1:
                    round_of_betting_complete = True
                    table.active_hand = False

            # Everyone calls or folds
            call_fold_counter = 0
            for player in table.hand_players:
                if player.player_action in ['f', 'F', 'c', 'C']:
                    call_fold_counter += 1
                if call_fold_counter == len(table.hand_players):
                    round_of_betting_complete = True
