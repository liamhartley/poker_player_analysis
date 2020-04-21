from typing import List


def check_actions(players, actions: List):
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
