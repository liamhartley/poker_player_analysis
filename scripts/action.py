from helpers import player_helpers


def player_action_input(player, table):
    actions_available = ['C', 'c', 'R', 'r', 'B', 'b', 'F', 'f', '', ' ', 'check']
    player.player_action = 'NA'
    # TODO add more validation e.g. cannot check pre-flop unless you're big blind
    while player.player_action not in actions_available:
        player_move = input(f'{player.name}: ')
        if player_move not in actions_available:
            print('Invalid action! '
                  'Please enter C (call), B (bet), R (raise), F (fold) or blank for a check')
        else:
            player_helpers.update_player_action(player, player_move, table)


def action_all_hand_players(players, table):
    table.player_raises = False
    table.player_bets = False
    all_players_actioned = False
    action_counter = 0
    for player in players:
        if table.player_raises is False and \
                table.player_bets is False and \
                player.current_hand is True:
            if player.has_bet is True or player.has_raised is True:
                action_counter += 1
            elif table.current_state is 'pre-flop' and player.is_dealer is True:
                action_counter += 1
            else:
                # If they're still playing
                player.player_action = 'NA'
                player_action_input(player, table)
                action_counter += 1

    if action_counter == len(table.hand_players) \
            and table.player_raises is False\
            and table.player_bets is False:
        all_players_actioned = True
    return all_players_actioned


def round_of_betting(table):

    for player in table.hand_players:
        player.player_action = 'NA'
    table.round_of_betting_complete = False

    while table.round_of_betting_complete is False:
        table.round_of_betting_complete = action_all_hand_players(table.hand_players, table)

        # Someone raised or bets, so other players need to action again
        if table.player_bets is True:
            table.sort_players(player_index='better')
        elif table.player_raises is True:
            table.sort_players(player_index='raiser')

    for player in table.table_players:
        player.has_bet = False
        player.has_raised = False
