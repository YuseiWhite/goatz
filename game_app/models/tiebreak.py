#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game_app.models.match import AboutPlayers


class HowToCountTieBreak(object):
    # タイブレークの加算方法
    def __init__(self, player1_name="Aさん", player2_name="Bさん"):
        self.player1_name = player1_name
        self.player2_name = player2_name

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

    def __init__(self):
        super().__init__()

    def seven_points_tie_break(self):
        about = AboutPlayers()
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
                player1_tiebreak_point = about.player1
                player2_tiebreak_point = about.player2
                return player1_tiebreak_point, player2_tiebreak_point
            elif (about.player1 == 7 or about.player2 == 7) and (about.player1 < 6 or about.player2 < 6):
                player1_tiebreak_point = about.player1
                player2_tiebreak_point = about.player2
                return player1_tiebreak_point, player2_tiebreak_point


class TenPointsTieBreak(HowToCountTieBreak):
    # 10ポイントのタイブレークマッチのルール
    game_name = "タイブレークマッチ"

    def __init__(self):
        super().__init__()

    def ten_points_tie_break(self):
        about = AboutPlayers()
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
            if dif == 2 and (about.player1 >= 11 or about.player2 >= 11):
                player1_tiebreak_point = about.player1
                player2_tiebreak_point = about.player2
                return player1_tiebreak_point, player2_tiebreak_point
            elif (about.player1 == 10 or about.player2 == 10) and (about.player1 < 9 or about.player2 < 9):
                player1_tiebreak_point = about.player1
                player2_tiebreak_point = about.player2
                return player1_tiebreak_point, player2_tiebreak_point