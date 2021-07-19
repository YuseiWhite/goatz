from match import AboutPlayers
from tiebreak import SevenPointsTieBreak

import pdb


class HowToCountGame(object):
    def __init__(self, name="ゲームマッチ"):
        self.name = name

    def game_count(self):
        about = AboutPlayers()
        while True:
            player1_points = "0"
            player2_points = "0"
            separation = "#######################################################"
            # ユーザーにどちらのプレイヤーがポイントを取ったか入力してもらう。
            str_get_point = input(about.which_point)
            if str_get_point == "1" or str_get_point == "2":
                get_point = int(str_get_point)
                if get_point == 1:
                    about.player1_count += 1
                elif get_point == 2:
                    about.player2_count += 1

            # 40-40になった場合
            if about.player1_count % 4 == 0 and about.player2_count % 4 == 0:
                print(separation + "\n" + about.player1_name + ": " + "40\n"
                      + about.player2_name + ": " + "40\n" + separation)
                while True:
                    str_get_point = input(about.which_point)
                    if str_get_point is not None:
                        get_point = int(str_get_point)
                        if get_point == 1:
                            about.player1_count += 1
                        elif get_point == 2:
                            about.player2_count += 1

                    dif = abs(about.player1_count - about.player2_count)
                    if dif == 2 and about.player1_count > about.player2_count:
                        player1_points = about.players_count[5]
                        player2_points = about.players_count[4]
                        about.player1_count = 1
                        about.player2_count = 1
                        about.player1_game_count += 1
                        print(separation + "\n" + about.player1_name + ": " + player1_points + "\n"
                              + about.player2_name + ": " + player2_points + "\n" + about.win_player1 + "\n" + separation)
                        return about.player1_game_count, about.player2_game_count
                    elif dif == 2 and about.player2_count > about.player1_count:
                        player1_points = about.players_count[4]
                        player2_points = about.players_count[5]
                        about.player1_count = 1
                        about.player2_count = 1
                        about.player2_game_count += 1
                        print(separation + "\n" + about.player1_name + ": " + player1_points + "\n"
                              + about.player2_name + ": " + player2_points + "\n" + about.win_player2 + "\n" + separation)
                        return about.player1_game_count, about.player2_game_count
                    elif about.player1_count == about.player2_count:
                        player1_points = about.players_count[4]
                        player2_points = about.players_count[4]
                    elif about.player1_count > about.player2_count:
                        player1_points = "Ad"
                        player2_points = about.players_count[4]
                    elif about.player2_count > about.player1_count:
                        player1_points = about.players_count[4]
                        player2_points = "Ad"

                    point_of_two_players = about.player1_name + ": " + player1_points + "\n" + about.player2_name + ": " + player2_points
                    print(separation + "\n" + point_of_two_players + "\n" + separation)

            # player1のポイント
            if about.player1_count % 5 == 0:
                player1_points = about.players_count[5]
                about.player1_count = 1
                about.player2_count = 1
                about.player1_game_count += 1
                print(separation + "\n" + about.player1_name + ": " + player1_points + "\n"
                      + about.player2_name + ": " + player2_points + "\n" + about.win_player1 + "\n" + separation)
                return about.player1_game_count, about.player2_game_count
            elif about.player1_count % 4 == 0:
                player1_points = about.players_count[4]
            elif about.player1_count % 3 == 0:
                player1_points = about.players_count[3]
            elif about.player1_count % 2 == 0:
                player1_points = about.players_count[2]
            elif about.player1_count % 1 == 0:
                player1_points = about.players_count[1]

            # player2のポイント
            if about.player2_count % 5 == 0:
                player2_points = about.players_count[5]
                about.player1_count = 1
                about.player2_count = 1
                about.player2_game_count += 1
                print(separation + "\n" + about.player1_name + ": " + player1_points + "\n"
                      + about.player2_name + ": " + player2_points + "\n" + about.win_player2 + "\n" + separation)
                return about.player1_game_count, about.player2_game_count
            elif about.player2_count % 4 == 0:
                player2.points = about.players_count[4]
            elif about.player2_count % 3 == 0:
                player2_points = about.players_count[3]
            elif about.player2_count % 2 == 0:
                player2_points = about.players_count[2]
            elif about.player2_count % 1 == 0:
                player2_points = about.players_count[1]

            point_of_two_players = about.player1_name + ": " + player1_points + "\n" + about.player2_name + ": " + player2_points
            print(separation + "\n" + point_of_two_players + "\n" + separation)


class SixGame(HowToCountGame):
    def __init__(self, name="6ゲームマッチ"):
        super().__init__(name)
        self.name = name

    def six_games(self):
        about = AboutPlayers()
        how_to_count_game = HowToCountGame()
        player1_game_count = 0
        player2_game_count = 0
        tiebreak = SevenPointsTieBreak()
        player1_tiebreak_point = 0
        player2_tiebreak_point = 0
        result_of_tiebreak = "still"
        separation = "#######################################################"
        while True:
            # 5-5になったら
            if (player1_game_count != 0 and player1_game_count % 5 == 0) and (player2_game_count != 0 and player2_game_count % 5 == 0):
                while True:
                    if player1_game_count == 6 and player2_game_count == 6:
                        print("\n6 game all, Tie-Break\n")
                        player1_tiebreak_point, player2_tiebreak_point = tiebreak.seven_points_tie_break()
                        result_of_tiebreak = "finish"
                        break
                    elif player1_game_count == 7 or player2_game_count == 7:
                        print(separation + "\n" + about.player1_name + ": " + str(player1_game_count) + "\n"
                              + about.player2_name + ": " + str(player2_game_count) + "\n" + separation)
                        result_of_tiebreak = "finish"
                        break
                    print(separation + "\n" + about.player1_name + ": " + str(about.player1_game_count) + "\n"
                          + about.player2_name + ": " + str(about.player2_game_count) + "\n" + separation)
                    player1_game_count, player2_game_count = how_to_count_game.game_count()
            if result_of_tiebreak == "finish":
                break
            game_of_two_players = about.player1_name + ": " + str(player1_game_count) + "\n" + about.player2_name + ": " + str(player2_game_count)
            # プレイヤー1とプレイヤー2の処理
            if player1_game_count != 0 and player1_game_count % 6 == 0:
                print(separation + "\n" + game_of_two_players + "\n" + separation)
                break
            elif player2_game_count != 0 and player2_game_count % 6 == 0:
                print(separation + "\n" + game_of_two_players + "\n" + separation)
                break

            print(separation + "\n" + game_of_two_players + "\n" + separation)
            player1_game_count, player2_game_count = how_to_count_game.game_count()

        if player1_tiebreak_point > player2_tiebreak_point:
            print(separation + "\n" + about.win_player1 + "\n" + about.player1_name + ": 7" + "\n"
                  + about.player2_name + ": 6(" + str(player2_tiebreak_point) + ")\n" + separation)
        elif player2_tiebreak_point > player1_tiebreak_point:
            print(separation + "\n" + about.win_player2 + "\n" + about.player1_name + ": 6(" + str(player1_tiebreak_point) + ")\n"
                  + about.player2_name + ": 7\n" + separation)


g = SixGame()
g.six_games()