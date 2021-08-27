#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game_app.models.tiebreak import SevenPointsTieBreak
from game_app.models.six_games import SixGames


class EightGames(SixGames):
    def __init__(self, player1_name="Aさん", player2_name="Bさん"):
        super().__init__(player1_name, player2_name)
        self.win_player1 = "Game set and match won by " + self.player1_name + "."
        self.win_player2 = "Game set and match won by " + self.player2_name + "."

    def seven_games_all_and_tiebreak_result(self, player1_game_count, player2_game_count, result_of_tiebreak):
        separation = "#" * 55
        tiebreak = SevenPointsTieBreak()
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0

        while True:
            if player1_game_count == 8 and player2_game_count == 8:
                start_tiebreak_match = "\n6 game all, Tie-Break\n"
                print(start_tiebreak_match)
                player1_tiebreak_point, player2_tiebreak_point = tiebreak.run_seven_points_tie_break()
                result_of_tiebreak = "finish"
                return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak
            # タイブレークに突入しなくてもタイブレークポイントを0で返す。
            elif player1_game_count == 9:
                result_of_set_match = separation + "\n【Games】\n" + self.player1_name + ": " + str(player1_game_count) \
                                      + "\n" + self.player2_name + ": " + str(player2_game_count) + "\n" \
                                      + self.win_player1 + "\n" + separation
                print(result_of_set_match)
                return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak
            elif player2_game_count == 9:
                result_of_set_match = separation + "\n【Games】\n" + self.player1_name + ": " + str(player1_game_count) \
                                      + "\n" + self.player2_name + ": " + str(player2_game_count) + "\n" \
                                      + self.win_player2 + "\n" + separation
                print(result_of_set_match)
                return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak

            result_of_set_match = separation + "\n【Games】\n" + self.player1_name + ": " + str(player1_game_count) + "\n" \
                                  + self.player2_name + ": " + str(player2_game_count) + "\n" + separation
            print(result_of_set_match)
            player1_game_count, player2_game_count = self.players_game_result(player1_game_count, player2_game_count)

    def which_player_won_tiebreak_match_is_output_in_case_of_eight_games(self, player1_tiebreak_point, player2_tiebreak_point):
        separation = "#" * 55
        if player1_tiebreak_point > player2_tiebreak_point:
            player1_win_tiebreak_match = separation + "\n【Tie-break】\n" + self.player1_name + ": 9" + "\n" \
                                         + self.player2_name + ": 8(" + str(player2_tiebreak_point) + ")\n" \
                                         + self.win_player1 + "\n" + separation
            print(player1_win_tiebreak_match)
        elif player1_tiebreak_point < player2_tiebreak_point:
            player2_win_tiebreak_match = separation + "\n【Tie-break】\n" + self.player1_name + ": 8(" \
                                         + str(player1_tiebreak_point) + ")\n" + self.player2_name + ": 9\n" \
                                         + self.win_player2 + "\n" + separation
            print(player2_win_tiebreak_match)

    def run_eight_games_match(self):
        separation = "#" * 55
        player1_game_count = 0
        player2_game_count = 0
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0

        while True:
            result_of_tiebreak = "still"
            if (player1_game_count != 0 and player1_game_count % 7 == 0) and (
                    player2_game_count != 0 and player2_game_count % 7 == 0):
                player1_game_count, player2_game_count, \
                player1_tiebreak_point, player2_tiebreak_point, \
                result_of_tiebreak = self.seven_games_all_and_tiebreak_result(player1_game_count,
                                                                              player2_game_count,
                                                                              result_of_tiebreak)

            if result_of_tiebreak == "finish":
                # タイブレーク結果を出力
                self.which_player_won_tiebreak_match_is_output_in_case_of_eight_games(player1_tiebreak_point,
                                                                                      player2_tiebreak_point)
                break
            elif player1_game_count == 9 or player2_game_count == 9:
                break

            if player1_game_count != 0 and player1_game_count % 8 == 0:
                player1_win_set_match = separation + "\n" + self.player1_name + ": " + str(player1_game_count) + "\n" \
                                        + self.player2_name + ": " + str(player2_game_count) + "\n" \
                                        + self.win_player1 + "\n" + separation
                print(player1_win_set_match)
                break
            elif player2_game_count != 0 and player2_game_count % 8 == 0:
                player2_win_set_match = separation + "\n" + self.player1_name + ": " + str(player1_game_count) + "\n" \
                                        + self.player2_name + ": " + str(player2_game_count) + "\n" \
                                        + self.win_player2 + "\n" + separation
                print(player2_win_set_match)
                break

            result_of_set_match = separation + "\n【Games】\n" + self.player1_name + ": " + str(player1_game_count) + "\n" \
                                  + self.player2_name + ": " + str(player2_game_count) + "\n" + separation
            print(result_of_set_match)
            player1_game_count, player2_game_count = self.players_game_result(player1_game_count, player2_game_count)