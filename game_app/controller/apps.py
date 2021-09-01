#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join('..', 'models'))
import json

from pywebio.input import input, TEXT, NUMBER, select, checkbox, radio, textarea, file_upload, input_group
from pywebio.output import put_text, put_buttons, put_link, put_markdown, put_table, put_image, popup, toast
from pywebio.session import hold

from game_app.models.eight_games import EightGames
from game_app.models.tiebreak import SevenPointsTieBreak, TenPointsTieBreak
from game_app.models.six_games import SixGames
from game_app.models.three_sets import ThreeSets

replace_table = str.maketrans({
    ",": "\n",
    "{": "",
    "}": "",
    '"': ''
})


class StartGame(object):
    def __init__(self):
        pass

    def input_name(self):
        start = "テニスカウントアプリケーション「Goatz」へようこそ！\nさあ、試合開始です！\nテニスを楽しみましょう！"
        put_text(start)
        player1_name = input("あなたの名前を入力して下さい：", type=TEXT, required=True)
        player2_name = input("相手の名前を入力して下さい：", type=TEXT, required=True)
        return player1_name, player2_name

    def input_whether_to_play_again(self):
        more_game = False
        play_again = "もう一度試合を行いますか？"
        input_play_again = radio(play_again, options=["はい", "いいえ"])
        if input_play_again == "はい":
            more_game = True
        return more_game

    def select_game_format(self):
        while True:
            game_format_list = {
                1: " 1： 6ゲームマッチ",
                2: "2： 8ゲームマッチ",
                3: "3： タイブレークマッチ",
                4: "4： スーパータイブレークマッチ",
                5: "5： 3セットマッチ"
            }
            str_game_format_list = json.dumps(game_format_list, ensure_ascii=False)
            put_text(str_game_format_list.translate(replace_table).replace("1:", "").replace("2:", "").replace("3:", "").replace("4:", "").replace("5:", ""))
            game_format_list_num = ["1番", "2番", "3番", "4番", "5番"]
            select_game_format = radio("試合形式を選択して下さい：", options=game_format_list_num)
            if select_game_format == "1番":
                select_game_format = 1
                toast(game_format_list[1] + "という試合形式で試合開始です！", duration=3, position='left')
            elif select_game_format == "2番":
                select_game_format = 2
                toast(game_format_list[2] + "という試合形式で試合開始です！", duration=3, position='left')
            elif select_game_format == "3番":
                select_game_format = 3
                toast(game_format_list[3] + "という試合形式で試合開始です！", duration=3, position='left')
            elif select_game_format == "4番":
                select_game_format = 4
                toast(game_format_list[4] + "という試合形式で試合開始です！", duration=3, position='left')
            elif select_game_format == "5番":
                select_game_format = 5
                toast(game_format_list[5] + "という試合形式で試合開始です！", duration=3, position='left')
            return select_game_format

    def start_game(self):
        player1_name, player2_name = self.input_name()
        game_format_num = self.select_game_format()
        if 1 <= game_format_num <= 5:
            popup("Love all.")
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
        more_game = self.input_whether_to_play_again()
        return more_game


