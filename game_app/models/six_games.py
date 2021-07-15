import pdb

from match import AboutPlayers
from tiebreak import SevenPointsTieBreak


player1_name = "Aさん"
player2_name = "Bさん"
which_point = "1:" + player1_name + "がポイントを取った\n" + "2:" + player2_name + "がポイントを取った\n1か2で入力して下さい："
player1_count = 1
player2_count = 1
win_player1 = "Game set and match won by " + player1_name + "."
win_player2 = "Game set and match won by " + player2_name + "."
players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}
player1_game_count = 0
player2_game_count = 0


class HowToCountGame(object):
    def __init__(self, name="ゲームマッチ"):
        self.name = name

    def game_count(self):
        while True:
            global player1_count
            global player2_count
            global which_point
            global players_count
            global player1_game_count
            global player2_game_count

            player1_points = "0"
            player2_points = "0"
            separation = "#######################################################"

            # ユーザーにどちらのプレイヤーがポイントを取ったか入力してもらう。
            str_get_point = input(which_point)
            if str_get_point == "1" or str_get_point == "2":
                get_point = int(str_get_point)
                if get_point == 1:
                    player1_count += 1
                elif get_point == 2:
                    player2_count += 1

            # 40-40になった場合
            if player1_count % 4 == 0 and player2_count % 4 == 0:
                print(separation + "\n" + player1_name + ": " + "40\n"
                      + player2_name + ": " + "40\n" + separation)
                while True:
                    str_get_point = input(which_point)
                    if str_get_point is not None:
                        get_point = int(str_get_point)
                        if get_point == 1:
                            player1_count += 1
                        elif get_point == 2:
                            player2_count += 1

                    dif = abs(player1_count - player2_count)
                    if dif == 2 and player1_count > player2_count:
                        player1_points = players_count[5]
                        player2_points = players_count[4]
                        player1_count = 1
                        player2_count = 1
                        player1_game_count += 1
                        print(separation + "\n" + player1_name + ": " + player1_points + "\n"
                              + player2_name + ": " + player2_points + "\n" + win_player1 + "\n" + separation)
                        return player1_game_count
                    elif dif == 2 and player2_count > player1_count:
                        player1_points = players_count[4]
                        player2_points = players_count[5]
                        player1_count = 1
                        player2_count = 1
                        player2_game_count += 1
                        print(separation + "\n" + player1_name + ": " + player1_points + "\n"
                              + player2_name + ": " + player2_points + "\n" + win_player2 + "\n" + separation)
                        return player2_game_count
                    elif player1_count == player2_count:
                        player1_points = players_count[4]
                        player2_points = players_count[4]
                    elif player1_count > player2_count:
                        player1_points = "Ad"
                        player2_points = players_count[4]
                    elif player2_count > player1_count:
                        player1_points = players_count[4]
                        player2_points = "Ad"

                    point_of_two_players = player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points
                    print(separation + "\n" + point_of_two_players + "\n" +separation)

            # player1のポイント
            if player1_count % 5 == 0:
                player1_points = players_count[5]
                player1_count = 1
                player2_count = 1
                player1_game_count += 1
                print(separation + "\n" + player1_name + ": " + player1_points + "\n"
                      + player2_name + ": " + player2_points + "\n" + win_player1 + "\n" + separation)
                return player1_game_count
            elif player1_count % 4 == 0:
                player1_points = players_count[4]
            elif player1_count % 3 == 0:
                player1_points = players_count[3]
            elif player1_count % 2 == 0:
                player1_points = players_count[2]
            elif player1_count % 1 == 0:
                player1_points = players_count[1]

            # player2のポイント
            if player2_count % 5 == 0:
                player2_points = players_count[5]
                player1_count = 1
                player2_count = 1
                player2_game_count += 1
                print(separation + "\n" + player1_name + ": " + player1_points + "\n"
                      + player2_name + ": " + player2_points + "\n" + win_player2 + "\n" + separation)
                return player2_game_count
            elif player2_count % 4 == 0:
                player2_points = players_count[4]
            elif player2_count % 3 == 0:
                player2_points = players_count[3]
            elif player2_count % 2 == 0:
                player2_points = players_count[2]
            elif player2_count % 1 == 0:
                player2_points = players_count[1]

            point_of_two_players = player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points
            print(separation + "\n" + point_of_two_players + "\n" + separation)


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
            game_of_two_players = player1_name + ": " + str(player1_game_count) + "\n" + player2_name + ": " + str(player2_game_count)
            # 5-5になったら
            if (player1_game_count != 0 and player1_game_count % 5 == 0) and (player2_game_count != 0 and player2_game_count % 5 == 0):
                while True:
                    if player1_game_count == 6 and player2_game_count == 6:
                        print("\n6 game all, Tie-Break\n")
                        player1_tiebreak_point, player2_tiebreak_point = tiebreak.seven_points_tie_break()
                        result_of_tiebreak = "finish"
                        break
                    elif player1_game_count == 7 or player2_game_count == 7:
                        print(separation + "\n" + player1_name + ": " + str(player1_game_count) + "\n"
                              + player2_name + ": " + str(player2_game_count) + "\n" + separation)
                        result_of_tiebreak = "finish"
                        break
                    print(separation + "\n" + player1_name + ": " + str(player1_game_count) + "\n"
                          + player2_name + ": " + str(player2_game_count) + "\n" + separation)
                    how_to_count_game.game_count()
            if result_of_tiebreak == "finish":
                break
            # プレイヤー1とプレイヤー2の処理
            if player1_game_count != 0 and player1_game_count % 6 == 0:
                print(separation + "\n" + game_of_two_players + "\n" + separation)
                break
            elif player2_game_count != 0 and player2_game_count % 6 == 0:
                print(separation + "\n" + game_of_two_players + "\n" + separation)
                break

            print(separation + "\n" + game_of_two_players + "\n" + separation)
            how_to_count_game.game_count()

        if player1_tiebreak_point > player2_tiebreak_point:
            print(separation + "\n" + about.win_player1 + "\n" + player1_name + ": 7" + "\n"
                  + player2_name + ": 6(" + str(player2_tiebreak_point) + ")\n" + separation)
        elif player2_tiebreak_point > player1_tiebreak_point:
            print(separation + "\n" + about.win_player2 + "\n" + player1_name + ": 6(" + str(player1_tiebreak_point) + ")\n"
                  + player2_name + ": 7\n" + separation)