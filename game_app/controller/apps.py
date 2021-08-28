#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join('..', 'models'))

from game_app.models.eight_games import EightGames
from game_app.models.tiebreak import SevenPointsTieBreak, TenPointsTieBreak
from game_app.models.six_games import SixGames
from game_app.models.three_sets import ThreeSets


class StartGame(object):
    def __init__(self):
        pass

    def input_name(self):
        separation = "#" * 55
        start = separation + "\n試合開始！\n" + separation
        print(start)
        player1_name = input(u"あなたの名前を入力して下さい：")
        player1_name = player1_name + "さん"
        player2_name = input(u"相手の名前を入力して下さい：")
        player2_name = player2_name + "さん"
        return player1_name, player2_name

    def select_game_format(self):
        separation = "#" * 55
        while True:
            select_game_format = input(
                separation +
                "\n1： 6ゲームマッチ\n"
                "2： 8ゲームマッチ\n"
                "3： タイブレークマッチ\n"
                "4： スーパータイブレークマッチ\n"
                "5:　3セットマッチ\n"
                + separation +
                "\n試合形式を選択して下さい："
            )
            if select_game_format in ["1", "2", "3", "4", "5"]:
                select_game_format = int(select_game_format)
                return select_game_format

    def start_game(self):
        separation = "#" * 55
        player1_name, player2_name = self.input_name()
        game_format_num = self.select_game_format()
        if 1 <= game_format_num <= 5:
            print(separation + "\nLove all.\n" + separation)
            if game_format_num == 1:
                six_games = SixGames(player1_name, player2_name)
                six_games.run_six_games_match()
            elif game_format_num == 2:
                eight_games = EightGames(player1_name, player2_name)
                eight_games.run_eight_games_match()
            elif game_format_num == 3:
                tiebreak = SevenPointsTieBreak(player1_name, player2_name)
                tiebreak.seven_points_tie_break_result()
            elif game_format_num == 4:
                super_tiebreak = TenPointsTieBreak(player1_name, player2_name)
                super_tiebreak.ten_points_tie_break_result()
            elif game_format_num == 5:
                three_sets = ThreeSets(player1_name, player2_name)
                three_sets.run_three_sets_match()


