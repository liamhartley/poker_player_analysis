import unittest
from scripts import action
from scripts import check_hands
from objects import player
from objects import table


# TODO more
class TestActions(unittest.TestCase):
    def setUp(self):
        self.test_table = table.TableClass()
        for new_player in range(0, 4):
            self.test_table.table_players.append(player.PlayerClass(name=new_player))
        self.test_table.table_players[new_player].position = 'dealer'
        self.test_table.dealer_first()

    def test_preflop_all_call_and_bb_checks(self):
        self.test_table.current_state = 'pre-flop'
        self.test_table.sort_players_preflop()
        self.test_table.hand_players = self.test_table.table_players

        # Everyone called, bb checks
        self.test_table.hand_players[0].player_action = 'c'
        self.test_table.hand_players[1].player_action = 'c'
        self.test_table.hand_players[2].player_action = 'c'
        self.test_table.hand_players[3].player_action = 'check'

        check_hands.preflop_everyone_calls_folds_and_bb_checks(self.test_table)
        self.assertTrue(self.test_table.round_of_betting_complete)

        # People fold and call, bb checks
        self.test_table.hand_players[0].player_action = 'f'
        self.test_table.hand_players[1].player_action = 'f'
        self.test_table.hand_players[2].player_action = 'c'
        self.test_table.hand_players[3].player_action = 'check'

        check_hands.preflop_everyone_calls_folds_and_bb_checks(self.test_table)
        self.assertTrue(self.test_table.round_of_betting_complete)


if __name__ == '__main__':
    unittest.main()
