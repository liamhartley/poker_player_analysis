import unittest
from scripts import action
from objects import player
from objects import table


# TODO more
class TestActions(unittest.TestCase):
    def setUp(self):
        self.test_table = table.TableClass()
        for new_player in range(0, 3):
            self.test_table.table_players.append(player.PlayerClass(name=new_player))
        self.test_table.table_players[new_player].position = 'dealer'
        self.test_table.dealer_first()

    def preflop_all_call_and_bb_checks(self):
        self.test_table.current_state = 'pre-flop'
        self.test_table.sort_players_preflop()
        self.test_table.table_players[0].player_action = 'c'
        self.test_table.table_players[1].player_action = 'c'
        self.test_table.table_players[2].player_action = 'c'
        self.test_table.table_players[3].player_action = 'check'
        # TODO consider returning something from this function or re-structuring it
        action.round_of_betting(self.test_table, preflop=True)
        self.assertTrue(self.test_table.active_hand)


if __name__ == '__main__':
    unittest.main()
