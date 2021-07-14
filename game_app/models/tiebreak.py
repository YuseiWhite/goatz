"""
タイブレークマッチについて

先に7ポイントを取った方が勝利
だだし、6-6になった場合は2ポイント差が着くまで永続的に続行する
"""
from match import AboutPlayers
import pdb


class HowToCountTieBreak(object):
    # タイブレークの加算方法
    def __init__(self, name="タイブレークマッチ"):
        self.name = name

    def tie_break(self):
        about = AboutPlayers()

        get_point = int(input(about.which_point))
        if get_point == 1:
            about.player1 += 1
        elif get_point == 2:
            about.player2 += 1
        return about.player1, about.player2


class SevenPointsTieBreak(HowToCountTieBreak):
    # 7ポイントのタイブレークマッチのルール
    game_name = "タイブレークマッチ"

    def __init__(self, name="7ポイントタイブレークマッチ"):
        super().__init__(name)
        self.name = name

    def seven_points_tie_break(self):
        about = AboutPlayers()
        global PLAYER1_TIEBREAK_POINT
        global PLAYER2_TIEBREAK_POINT
        while True:
            get_point = int(input(about.which_point))
            if get_point == 1:
                about.player1 += 1
            elif get_point == 2:
                about.player2 += 1

            point_of_two_players = about.player1_name + ": " + str(about.player1) + "\n" + about.player2_name + ": " + str(about.player2)
            print("#######################################################")
            print(point_of_two_players)
            print("#######################################################")

            dif = abs(about.player1 - about.player2)
            if dif == 2 and (about.player1 >= 8 or about.player2 >= 8):
                PLAYER1_TIEBREAK_POINT = about.player1
                PLAYER2_TIEBREAK_POINT = about.player2
                return PLAYER1_TIEBREAK_POINT, PLAYER2_TIEBREAK_POINT
            elif (about.player1 == 7 or about.player2 == 7) and (about.player1 < 6 or about.player2 < 6):
                PLAYER1_TIEBREAK_POINT = about.player1
                PLAYER2_TIEBREAK_POINT = about.player2
                return PLAYER1_TIEBREAK_POINT, PLAYER2_TIEBREAK_POINT


class TenPointsTieBreak(HowToCountTieBreak):
    # 10ポイントのタイブレークマッチのルール
    game_name = "タイブレークマッチ"

    def __init__(self, name="10ポイントタイブレークマッチ"):
        super().__init__(name)
        self.name = name

    def ten_points_tie_break(self):
        how_to_count_tie_break = HowToCountTieBreak()
        while True:
            dif = abs(about.player1 - about.player2)
            if dif == 2 and (about.player1 >= 11 or about.player2 >= 11):
                break
            elif (about.player1 == 10 or about.player2 == 10) and (about.player1 < 9 or about.player2 < 9):
                break
            point_of_two_players = about.player1_name + ": " + str(about.player1) + "\n" + about.player2_name + ": " + str(about.player2)
            print("#######################################################")
            print(point_of_two_players)
            print("#######################################################")
            how_to_count_tie_break.tie_break()

        if about.player1 > about.player2:
            print(about.win_player1)
        elif about.player2 > about.player1:
            print(about.win_player2)