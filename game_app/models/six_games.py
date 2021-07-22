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

    def game_count(self):
        how_to_game_count = HowToCountGame()
        which_point = "1:" + how_to_game_count.player1_name + "がポイントを取った\n" + "2:" + how_to_game_count.player2_name + "がポイントを取った\n1か2で入力して下さい："
        separation = "#######################################################"
        player1_count = 1
        player2_count = 1
        players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}
        player1_game_count = 0
        player2_game_count = 0

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
                player1_count = 1
                player2_count = 1

            player1_points, player1_game_count = player1_point_and_game(player1_count, player1_game_count)
            player2_points, player2_game_count = player2_point_and_game(player2_count, player2_game_count)

            player1_count = int(player1_count)
            player2_count = int(player2_count)

            if player1_count >= 5:
                player1_get_game = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + how_to_game_count.win_player1 + "\n" + separation
                print(player1_get_game)
                player1_count = 1
                player2_count = 1
            elif player2_count >= 5:
                player2_get_game = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + how_to_game_count.win_player2 + "\n" + separation
                print(player2_get_game)
                player1_count = 1
                player2_count = 1

            result_of_points = separation + "\n" + how_to_game_count.player1_name + ": " + player1_points + "\n" + how_to_game_count.player2_name + ": " + player2_points + "\n" + separation
            print(result_of_points)


class SixGame(HowToCountGame):
    def __init__(self, name="6ゲームマッチ"):
        super().__init__(name)
        self.name = name

    def six_games(self):
        about = AboutPlayers()
        how_to_count_game = HowToCountGame()
        tiebreak = SevenPointsTieBreak()
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0
        result_of_tiebreak = "still"
        separation = "#######################################################"
        while True:
            # 5-5になったら
            if (about.player1_game_count != 0 and about.player1_game_count % 5 == 0) and (about.player2_game_count != 0 and about.player2_game_count % 5 == 0):
                while True:
                    if about.player1_game_count == 6 and about.player2_game_count == 6:
                        print("\n6 game all, Tie-Break\n")
                        # player1_tiebreak_point, player2_tiebreak_point = tiebreak.seven_points_tie_break()
                        tiebreak.seven_points_tie_break()
                        result_of_tiebreak = "finish"
                        break
                    elif about.player1_game_count == 7 or about.player2_game_count == 7:
                        print(separation + "\n" + about.player1_name + ": " + str(about.player1_game_count) + "\n"
                              + about.player2_name + ": " + str(about.player2_game_count) + "\n" + separation)
                        result_of_tiebreak = "finish"
                        break
                    print(separation + "\n" + about.player1_name + ": " + str(about.player1_game_count) + "\n"
                          + about.player2_name + ": " + str(about.player2_game_count) + "\n" + separation)
                    how_to_count_game.game_count()
            if result_of_tiebreak == "finish":
                break

            game_of_two_players = about.player1_name + ": " + str(about.player1_game_count) + "\n" + about.player2_name + ": " + str(about.player2_game_count)
            # プレイヤー1とプレイヤー2の処理
            if about.player1_game_count != 0 and about.player1_game_count % 6 == 0:
                print(separation + "\n" + game_of_two_players + "\n" + separation)
                break
            elif about.player2_game_count != 0 and about.player2_game_count % 6 == 0:
                print(separation + "\n" + game_of_two_players + "\n" + separation)
                break

            print(separation + "\n" + game_of_two_players + "\n" + separation)
            about.player1_game_count, about.player2_game_count = how_to_count_game.game_count()

        # ライブレークの試合結果
        if player1_tiebreak_point > player2_tiebreak_point:
            print(separation + "\n" + about.win_player1 + "\n" + about.player1_name + ": 7" + "\n"
                  + about.player2_name + ": 6(" + str(player2_tiebreak_point) + ")\n" + separation)
        elif player2_tiebreak_point > player1_tiebreak_point:
            print(separation + "\n" + about.win_player2 + "\n" + about.player1_name + ": 6(" + str(player1_tiebreak_point) + ")\n"
                  + about.player2_name + ": 7\n" + separation)


# g = SixGame()
# g.six_games()

g = HowToCountGame()
g.game_count()