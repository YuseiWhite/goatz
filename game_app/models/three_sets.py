# from game_app.models.six_games import SixGames

from six_games import SixGames

"""
six_games.pyを1stセットの変数に入れる
2セット目も
2セットとも同じプレーヤーなら終了
そうでないなら、3セットめ

six_gamesから欲しいデータは、
2人のプレーヤーのゲームカウント、タイブレークカウントの4つ

"""


class ThreeSets(object):
    def __init__(self, player1_name="Aさん", player2_name="Bさん"):
        self.player1_name = player1_name
        self.player2_name = player2_name

    def three_sets_match(self):
        six_game = SixGames()
        separation = "#######################################################"

        def first_set():
            player1_get_first_set = "lose"
            player2_get_first_set = "lose"
            player1_get_set_call = None
            player2_get_set_call = None

            player1_game_count, player2_game_count,  player1_tiebreak_point, player2_tiebreak_point = six_game.six_games_match()
            if player1_game_count == player2_game_count:
                if player1_tiebreak_point > player2_tiebreak_point:
                    player1_get_first_set = "win"
                    player1_get_set_call = separation + "\nGame and first set " + self.player1_name + " 7-" + str(player2_game_count) + "(" + str(player2_tiebreak_point) + ")\n" + separation
                elif player2_tiebreak_point > player1_tiebreak_point:
                    player2_get_first_set = "win"
                    player2_get_set_call = separation + "\nGame and first set " + self.player2_name + " 7-" + str(player1_game_count) + "(" + str(player1_tiebreak_point) + ")\n" + separation
            elif player1_game_count > player2_game_count:
                player1_get_first_set = "win"
                player1_get_set_call = separation + "\nGame and first set " + self.player1_name + " " + str(player1_game_count) + "-" + str(player2_game_count) + "\n" + separation
            elif player2_game_count > player1_game_count:
                player2_get_first_set = "win"
                player2_get_set_call = separation + "\nGame and first set " + self.player2_name + " " + str(player2_game_count) + "-" + str(player1_game_count) + "\n" + separation

            if player1_get_set_call is not None:
                print(player1_get_set_call)
            elif player2_get_set_call is not None:
                print(player2_get_set_call)

            return player1_get_first_set, player2_get_first_set

        player1_get_first_set, player2_get_first_set = first_set()

g = ThreeSets()
g.three_sets_match()

