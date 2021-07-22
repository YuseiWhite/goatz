from match import AboutPlayers
from tiebreak import SevenPointsTieBreak

import pdb


class HowToCountGame(object):
    def __init__(self, name="ゲームマッチ"):
        self.name = name
        self.player1_name = "Aさん"
        self.player2_name = "Bさん"
        self.win_player1 = "Game set and match won by " + self.player1_name + "."
        self.win_player2 = "Game set and match won by " + self.player2_name + "."

    def game_count(self, player1_game_count=0, player2_game_count=0):
        how_to_game_count = HowToCountGame()
        which_point = "1:" + how_to_game_count.player1_name + "がポイントを取った\n" + "2:" + how_to_game_count.player2_name + "がポイントを取った\n1か2で入力して下さい："
        separation = "#######################################################"
        player1_count = 1
        player2_count = 1
        players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}

        def which_get_point(player1_count, player2_count):
            str_get_point = input(which_point)
            if str_get_point == "1" or str_get_point == "2":
                get_point = int(str_get_point)
                if get_point == 1:
                    player1_count += 1
                elif get_point == 2:
                    player2_count += 1
                return player1_count, player2_count

        def player1_point_and_game(player1_count, player1_game_count):
            player1_points = "0"
            if player1_count != 0 and player1_count % 5 == 0:
                player1_points = players_count[5]
                player1_game_count += 1
            elif player1_count != 0 and player1_count % 4 == 0:
                player1_points = players_count[4]
            elif player1_count != 0 and player1_count % 3 == 0:
                player1_points = players_count[3]
            elif player1_count != 0 and player1_count % 2 == 0:
                player1_points = players_count[2]
            elif player1_count != 0 and player1_count % 1 == 0:
                player1_points = players_count[1]
            return player1_points, player1_game_count

        def player2_point_and_game(player2_count, player2_game_count):
            player2_points = "0"
            if player2_count != 0 and player2_count % 5 == 0:
                player2_points = players_count[5]
                player2_game_count += 1

            elif player2_count != 0 and player2_count % 4 == 0:
                player2_points = players_count[4]
            elif player2_count != 0 and player2_count % 3 == 0:
                player2_points = players_count[3]
            elif player2_count != 0 and player2_count % 2 == 0:
                player2_points = players_count[2]
            elif player2_count != 0 and player2_count % 1 == 0:
                player2_points = players_count[1]
            return player2_points, player2_game_count

        def forty_all(player1_count, player1_game_count, player2_count, player2_game_count):
            player1_points = "0"
            player2_points = "0"

            two_players_are_fourty_all = separation + "\n" + how_to_game_count.player1_name + ": " + "40\n" + how_to_game_count.player2_name + ": " + "40\n" + separation
            print(two_players_are_fourty_all)

            while True:
                player1_count, player2_count = which_get_point(player1_count, player2_count)
                dif = abs(player1_count - player2_count)

                if dif == 2 and player1_count > player2_count:
                    player1_points = players_count[5]
                    player2_points = players_count[4]
                    player1_game_count += 1
                    player1_get_game = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + how_to_game_count.win_player1 + "\n" + separation
                    print(player1_get_game)
                    result_of_forty_all = "finish"
                    return player1_game_count, player2_game_count, result_of_forty_all
                elif dif == 2 and player1_count < player2_count:
                    player1_points = players_count[4]
                    player2_points = players_count[5]
                    player2_game_count += 1
                    player2_get_game = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + how_to_game_count.win_player2 + "\n" + separation
                    print(player2_get_game)
                    result_of_forty_all = "finish"
                    return player1_game_count, player2_game_count, result_of_forty_all

                elif player1_count == player2_count:
                    player1_points = players_count[4]
                    player2_points = players_count[4]
                elif player1_count > player2_count:
                    player1_points = "Ad"
                    player2_points = players_count[4]
                elif player2_count > player1_count:
                    player1_points = players_count[4]
                    player2_points = "Ad"

                result_of_points = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + separation
                print(result_of_points)

        while True:
            try:
                player1_count, player2_count = which_get_point(player1_count, player2_count)
            except TypeError:
                print("\n※1または2で入力して下さい\n")

            result_of_forty_all = "still"
            if player1_count % 4 == 0 and player2_count % 4 == 0:
                player1_game_count, player2_game_count, result_of_forty_all = forty_all(player1_count, player1_game_count, player2_count, player2_game_count)
            if result_of_forty_all == "finish":
                return player1_game_count, player2_game_count

            player1_points, player1_game_count = player1_point_and_game(player1_count, player1_game_count)
            player2_points, player2_game_count = player2_point_and_game(player2_count, player2_game_count)

            player1_count = int(player1_count)
            player2_count = int(player2_count)

            if player1_count >= 5:
                player1_get_game = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + how_to_game_count.win_player1 + "\n" + separation
                print(player1_get_game)
                return player1_game_count, player2_game_count
            elif player2_count >= 5:
                player2_get_game = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + how_to_game_count.win_player2 + "\n" + separation
                print(player2_get_game)
                return player1_game_count, player2_game_count

            result_of_points = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + separation
            print(result_of_points)


class SixGame(HowToCountGame):
    def __init__(self, name="6ゲームマッチ"):
        super().__init__(name)
        self.name = name

    def six_games(self):
        how_to_count_game = HowToCountGame()
        player1_game_count = 0
        player2_game_count = 0
        separation = "#######################################################"
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0

        def five_games_all(player1_game_count, player2_game_count, result_of_tiebreak):
            tiebreak = SevenPointsTieBreak()
            player1_tiebreak_point = 0
            player2_tiebreak_point = 0

            while True:
                if player1_game_count == 6 and player2_game_count == 6:
                    start_tiebreak_match = "\n6 game all, Tie-Break\n"
                    print(start_tiebreak_match)
                    player1_tiebreak_point, player2_tiebreak_point = tiebreak.seven_points_tie_break()
                    result_of_tiebreak = "finish"
                    return player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak
                elif player1_game_count == 7 or player2_game_count == 7:
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
            if (player1_game_count != 0 and player1_game_count % 5 == 0) and (player2_game_count != 0 and player2_game_count % 5 == 0):
                player1_game_count, player2_game_count, player1_tiebreak_point, player2_tiebreak_point, result_of_tiebreak = five_games_all(player1_game_count, player2_game_count, result_of_tiebreak)

            if result_of_tiebreak == "finish":
                result_of_tiebreak_match(player1_tiebreak_point, player2_tiebreak_point)
                break
            elif player1_game_count == 7 or player2_game_count == 7:
                break

            result_of_set_match = separation + "\n" + how_to_count_game.player1_name + ": " + str(player1_game_count) + "\n" + how_to_count_game.player2_name + ": " + str(player2_game_count) + "\n" + separation
            if player1_game_count != 0 and player1_game_count % 6 == 0:
                print(result_of_set_match)
                break
            elif player2_game_count != 0 and player2_game_count % 6 == 0:
                print(result_of_set_match)
                break

            print(result_of_set_match)
            player1_game_count, player2_game_count = how_to_count_game.game_count(player1_game_count, player2_game_count)