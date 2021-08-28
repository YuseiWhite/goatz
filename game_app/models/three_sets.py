#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game_app.models.six_games import SixGames


class ThreeSets(object):
    def __init__(self, player1_name="Aさん", player2_name="Bさん"):
        self.player1_name = player1_name
        self.player2_name = player2_name

    def which_player_set_got_is(self, set_count):
        six_game = SixGames()
        separation = "#" * 55
        player1_get_set = "lose"
        player2_get_set = "lose"
        player1_get_set_call = None
        player2_get_set_call = None

        player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point = six_game.run_six_games_match()

        if player1_game_count == player2_game_count:
            if player1_tiebreak_point > player2_tiebreak_point:
                player1_get_set = "win"
                player1_get_set_call = separation + f"\nGame and {set_count} set " + self.player1_name + " 7-" + str(
                    player2_game_count) + "(" + str(player2_tiebreak_point) + ")\n" + separation
            elif player2_tiebreak_point > player1_tiebreak_point:
                player2_get_set = "win"
                player2_get_set_call = separation + f"\nGame and {set_count} set" + self.player2_name + " 7-" + str(
                    player1_game_count) + "(" + str(player1_tiebreak_point) + ")\n" + separation
        elif player1_game_count > player2_game_count:
            player1_get_set = "win"
            player1_get_set_call = separation + f"\nGame and {set_count} set " + self.player1_name + " " + str(
                player1_game_count) + "-" + str(player2_game_count) + "\n" + separation
        elif player2_game_count > player1_game_count:
            player2_get_set = "win"
            player2_get_set_call = separation + f"\nGame and {set_count} set " + self.player2_name + " " + str(
                player2_game_count) + "-" + str(player1_game_count) + "\n" + separation

        if player1_get_set_call is not None:
            print(player1_get_set_call)
        elif player2_get_set_call is not None:
            print(player2_get_set_call)
        return player1_get_set, player2_get_set

    def control_set_count(self):
        count_player1_set = 0
        count_player2_set = 0

        player1_get_first_set, player2_get_first_set = self.which_player_set_got_is("first")
        if player1_get_first_set == "win":
            count_player1_set += 1
        elif player2_get_first_set == "win":
            count_player2_set += 1

        player1_get_second_set, player2_get_second_set = self.which_player_set_got_is("second")
        if player1_get_second_set == "win":
            count_player1_set += 1
        elif player2_get_second_set == "win":
            count_player2_set += 1

        if count_player1_set == 1 and count_player2_set == 1:
            player1_get_third_set, player2_get_third_set = self.which_player_set_got_is("third")
            if player1_get_third_set == "win":
                count_player1_set += 1
            elif player2_get_third_set == "win":
                count_player2_set += 1
        return count_player1_set, count_player2_set

    def three_set_match_result(self):
        separation = "#" * 55
        win_three_sets_match = None
        count_player1_set, count_player2_set = self.control_set_count()
        if count_player1_set == 2 or count_player2_set == 2:
            result = "【Sets】\n" + self.player1_name + ": " + str(count_player1_set) + "\n" + self.player2_name + ": " + str(count_player2_set) + "\n" + separation
            if count_player1_set > count_player2_set:
                win_three_sets_match = separation + "\nGame and set match " + self.player1_name + ".\n"
            elif count_player1_set < count_player2_set:
                win_three_sets_match = separation + "\nGame and set match " + self.player2_name + ".\n"
            return result, win_three_sets_match

    def run_three_sets_match(self):
        result, win_three_sets_match = self.three_set_match_result()
        if win_three_sets_match is not None:
            print(win_three_sets_match + result)