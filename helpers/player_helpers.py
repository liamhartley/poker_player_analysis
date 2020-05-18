def update_player_action(player, player_action, table):

    # Call
    if player_action == 'C' or player_action == 'c':
        player.calls += 1
        player.player_action = 'c'
        if table.player_raises is True and table.current_state is 'pre-flop':
            player.VPIP += 1

    # Check
    elif player_action == '' or player_action == ' ':
        player.checks += 1
        player.player_action = 'check'

    # Raise
    elif player_action == 'R' or player_action == 'r':
        player.raises += 1
        player.player_action = 'r'
        for other_players in table.hand_players:
            other_players.has_raised = False
            other_players.has_bet = False
        player.has_raised = True
        table.player_raises = True
        if table.current_state is 'pre-flop':
            player.PFR += 1
            player.VPIP += 1

    # Bet
    elif player_action == 'B' or player_action == 'b':
        player.bets += 1
        player.player_action = 'b'
        player.has_bet = True
        table.player_bets = True
        player.VPIP += 1

    # Fold
    elif player_action == 'F' or player_action == 'f':
        player.player_action = 'f'
        player.current_hand = False
