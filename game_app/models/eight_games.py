from tiebreak import SevenPointsTieBreak
from six_games import HowToCountGame


class EightGames(HowToCountGame):
    def __init__(self, name="8ゲームマッチ"):
        super().__init__(name)
        self.name = name

    def eight_games_match(self):
        how_to_count_game = HowToCountGame()
        player1_game_count = 0
        player2_game_count = 0
        separation = "#######################################################"
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0

        def seven_games_all(player1_game_count, player2_game_count, result_of_tiebreak):
            tiebreak = SevenPointsTieBreak()
            player1_tiebreak_point = 0
            player2_tiebreak_point = 0

            while True:
                if player1_game_count == 8 and player2_game_count == 8:
                    start_tiebreak_match = "\n6 game all, Tie-Break\n"
                    print(start_tiebreak_match)
                    player1_tiebreak_point, player2_tiebreak_point = tiebreak.seven_points_tie_break()
                    result_of_tiebreak = "finish"
                    return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak
                elif player1_game_count == 9 or player2_game_count == 9:
                    result_of_set_match = separation + "\n" + how_to_count_game.player1_name + ": " + str(player1_game_count) + "\n" + how_to_count_game.player2_name + ": " + str(player2_game_count) + "\n" + separation
                    print(result_of_set_match)
                    return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak

                result_of_set_match = separation + "\n" + how_to_count_game.player1_name + ": " + str(player1_game_count) + "\n" + how_to_count_game.player2_name + ": " + str(player2_game_count) + "\n" + separation
                print(result_of_set_match)
                player1_game_count, player2_game_count = how_to_count_game.game_count(player1_game_count, player2_game_count)

        def result_of_tiebreak_match(player1_tiebreak_point, player2_tiebreak_point):
            if player1_tiebreak_point > player2_tiebreak_point:
                player1_win_tiebreak_match = separation + "\n" + how_to_count_game.win_player1 + "\n" + how_to_count_game.player1_name + ": 7" + "\n" + how_to_count_game.player2_name + ": 6(" + str(player2_tiebreak_point) + ")\n" + separation
                print(player1_win_tiebreak_match)
            elif player1_tiebreak_point < player2_tiebreak_point:
                player2_win_tiebreak_match = separation + "\n" + how_to_count_game.win_player2 + "\n" + how_to_count_game.player1_name + ": 6(" + str(player1_tiebreak_point) + ")\n" + how_to_count_game.player2_name + ": 7\n" + separation
                print(player2_win_tiebreak_match)

        while True:
            result_of_tiebreak = "still"
            if (player1_game_count != 0 and player1_game_count % 7 == 0) and (player2_game_count != 0 and player2_game_count % 7 == 0):
                player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak = seven_games_all(player1_game_count, player2_game_count, result_of_tiebreak)

            if result_of_tiebreak == "finish":
                result_of_tiebreak_match(player1_tiebreak_point, player2_tiebreak_point)
                break
            elif player1_game_count == 9 or player2_game_count == 9:
                break

            result_of_set_match = separation + "\n" + how_to_count_game.player1_name + ": " + str(player1_game_count) + "\n" + how_to_count_game.player2_name + ": " + str(player2_game_count) + "\n" + separation
            if player1_game_count != 0 and player1_game_count % 8 == 0:
                print(result_of_set_match)
                break
            elif player2_game_count != 0 and player2_game_count % 8 == 0:
                print(result_of_set_match)
                break

            print(result_of_set_match)
            player1_game_count, player2_game_count = how_to_count_game.game_count(player1_game_count, player2_game_count)