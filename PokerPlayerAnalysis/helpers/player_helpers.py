def update_player_action(player, player_action, table):

    # Call
    if player_action == 'C' or player_action == 'c':
        player.calls += 1
        player.player_action = 'c'

    # Check
    elif player_action == '' or player_action == ' ':
        player.checks += 1
        player.player_action = 'check'

    # Raise
    elif player_action == 'R' or player_action == 'r':
        player.raises += 1
        player.player_action = 'r'
        table.player_raises = True
        # table.player_raises_index = index
        if table.current_state is 'pre-flop':
            player.PFR += 1

    # Bet
    elif player_action == 'B' or player_action == 'b':
        player.bets += 1
        player.player_action = 'b'
        table.player_bets = True

    # Fold
    elif player_action == 'F' or player_action == 'f':
        player.player_action = 'f'
        player.current_hand = False
        del table.hand_players[table.hand_players.index(player)]

