from scripts.play import play_hand
from objects import table

if __name__ == '__main__':
    # TODO make a pretty start-up logo
    print('Welcome to Poker Player Analysis!\n')

    # Initialise the table class
    poker_table = table.TableClass()

    # Setup players
    poker_table.initialise_players()

    # Set the dealer
    poker_table.set_dealer()

    print("\n---- Let's Play! ----\n")

    while poker_table.end_session is False:
        poker_table.print_player_stats()
        play_hand(poker_table)
        poker_table.update_players_AF()
