from game_app.models.tiebreak import SevenPointsTieBreak
from game_app.models.six_games import SixGames

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
            player1_game_count, player2_game_count,  player1_tiebreak_point, player2_tiebreak_point = SixGames.six_games_match()
            if player1_game_count == player2_game_count:
                if player1_tiebreak_point > player2_tiebreak_point:
                    player1_get_first_set = "win"
                elif player2_tiebreak_point > player1_tiebreak_point:
                    player2_get_first_set = "win"
            elif player1_game_count > player2_game_count:
                player1_get_first_set = "win"
                player1_get_set_call = separation + "\nGame and first set" + self.player1_name + player1_game_count + "-" + player2_game_count + "\n" + separation
            elif player2_game_count > player1_game_count:
                player2_get_first_set = "win"
                player2_get_set_call = separation + "\nGame and first set" + self.player2_name + player2_game_count + "-" + player1_game_count + "\n" + separation
            return player1_get_first_set, player2_get_first_set
