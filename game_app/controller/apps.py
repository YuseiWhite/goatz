import os
import sys
sys.path.append(os.path.join('..', 'models'))

from game_app.models.eight_games import EightGames
from game_app.models.tiebreak import SevenPointsTieBreak, TenPointsTieBreak
from game_app.models.six_games import SixGames, HowToCountGame


class StartGame(object):
    def __init__(self):
        pass

    def start_game(self):
        six_games = SixGames()
        eight_games = EightGames()
        tiebreak = SevenPointsTieBreak()
        super_tiebreak = TenPointsTieBreak()

        separation = "#######################################################"

        # 現在は名前を入力しても反映されません。
        def input_name():
            start = separation + "\n試合開始！\n" + separation
            print(start)
            player1_name = input("あなたの名前を入力して下さい：")
            player1_name = player1_name + "さん"
            player2_name = input("相手の名前を入力して下さい：")
            player2_name = player2_name + "さん"
            return player1_name, player2_name

        def select_game():
            while True:
                select_game_format = input(
                    separation +
                    "\n1：6ゲームマッチ\n"
                    "2：8ゲームマッチ\n"
                    "3：タイブレークマッチ\n"
                    "4：スーパータイブレークマッチ\n"
                    + separation +
                    "\n試合形式を選択して下さい："
                )
                if select_game_format in {"1", "2", "3", "4"}:
                    select_game_format = int(select_game_format)
                    return select_game_format

        player1_name, player2_name = input_name()
        select_game_format = select_game()

        if select_game_format == 1:
            six_games.six_games_match()
        elif select_game_format == 2:
            eight_games.eight_games_match()
        elif select_game_format == 3:
            tiebreak.seven_points_tie_break()
        elif select_game_format == 4:
            super_tiebreak.ten_points_tie_break()

