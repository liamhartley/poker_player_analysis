from typing import List


def count_actions(players, actions: List):
    '''
    Check the number of times a specified action appears.
    :param players: a list of players with .player_action initialised
    :param actions: the actions to check e.g. ['c', 'C', 'F', 'f']
    :return: the count of the actions specified action by the players.
    '''
    action_counter = 0
    for player in players:
        if player.player_action in actions:
            action_counter += 1
    return action_counter


def better_first(players, better_index):
    new_positions = []
    for better_finder in players:
        if better_finder.action == 'b' or 'B':
            better_index = players.index(better_index)
            new_positions.append(better_index)
            for other_players in range(better_index, len(players) - 1):
                new_positions.append(other_players)
            for other_players in range(0, better_index):
                new_positions.append(other_players)
    return new_positions


def preflop_everyone_calls_folds_and_bb_checks(table):
    call_fold_counter = count_actions(table.hand_players, ['c', 'C', 'f', 'F'])
    if call_fold_counter == len(table.hand_players) - 1 and table.hand_players[-1].player_action is 'check':
        table.round_of_betting_complete = True


def everyone_checks(table):
    check_counter = count_actions(table.hand_players, ['', ' ', 'check'])
    if check_counter == len(table.hand_players):
        table.round_of_betting_complete = True


def everyone_folds(table):
    fold_counter = count_actions(table.hand_players, ['f', 'F'])
    if fold_counter == len(table.hand_players) - 1:
        table.round_of_betting_complete = True
        table.active_hand = False


def everyone_calls_or_folds(table):
    call_fold_counter = count_actions(table.hand_players, ['f', 'F', 'c', 'C'])
    if call_fold_counter == len(table.hand_players):
        table.round_of_betting_complete = True
