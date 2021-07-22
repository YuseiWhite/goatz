from match import AboutPlayers
from tiebreak import SevenPointsTieBreak

import pdb

# 練習用　tennis_count_appには関係ありません
# class TokutenData(object):
#     def __init__(self):
#         self.name = ''
#         self.kokugo = 0
#         self.sansuu = 0
#         self.heikin = 0.0
#
#     def heikin_cal(self):
#         self.heikin = (self.kokugo + self.sansuu) / 2
#
#
# class TaroData(object):
#     def __init__(self):
#         pass
#
#     def __taro__(self):
#         taro = TokutenData()
#         taro.name = '太郎'  # nameに'太郎'を代入
#         taro.kokugo = 50  # kokugoに50を代入
#         taro.sansuu = 45  # sansuuに45を代入
#         taro.heikin_cal()
#         print(taro.name, 'の平均点：', taro.heikin)
#
# data = TaroData()
# data.__taro__()


class HowToCountGame(object):
    def __init__(self, name="ゲームマッチ"):
        self.name = name
        self.player1_name = "Aさん"
        self.player2_name = "Bさん"
        self.player1_points = "0"
        self.player2_points = "0"
        self.player1_game_count = 0
        self.player2_game_count = 0
        self.win_player1 = "Game set and match won by " + self.player1_name + "."
        self.win_player2 = "Game set and match won by " + self.player2_name + "."

    def fourty_all(self):
        about = AboutPlayers()
        player1_points = "0"
        player2_points = "0"
        separation = "#######################################################"
        player1_count = about.player1_count
        player2_count = about.player2_count

        print(separation + "\n" + about.player1_name + ": " + "40\n"
              + about.player2_name + ": " + "40\n" + separation)
        while True:
            str_get_point = input(about.which_point)
            if str_get_point is not None:
                get_point = int(str_get_point)
                if get_point == 1:
                    player1_count += 1
                elif get_point == 2:
                    player2_count += 1

            dif = abs(player1_count - player2_count)
            if dif == 2 and player1_count > player2_count:
                player1_points = about.players_count[5]
                player2_points = about.players_count[4]
                player1_count = 1
                player2_count = 1
                about.player1_game_count += 1
                print(separation + "\n" + about.player1_name + ": " + player1_points + "\n"
                      + about.player2_name + ": " + player2_points + "\n" + about.win_player1 + "\n" + separation)
                return about.player1_game_count, about.player2_game_count
            elif dif == 2 and player1_count < player2_count:
                player1_points = about.players_count[4]
                player2_points = about.players_count[5]
                player1_count = 1
                player2_count = 1
                about.player2_game_count += 1
                print(separation + "\n" + about.player1_name + ": " + player1_points + "\n"
                      + about.player2_name + ": " + player2_points + "\n" + about.win_player2 + "\n" + separation)
                return about.player1_game_count, about.player2_game_count
            elif player1_count == player2_count:
                player1_points = about.players_count[4]
                player2_points = about.players_count[4]
            elif player1_count > player2_count:
                player1_points = "Ad"
                player2_points = about.players_count[4]
            elif player2_count > player1_count:
                player1_points = about.players_count[4]
                player2_points = "Ad"

            point_of_two_players = about.player1_name + ": " + player1_points + "\n" + about.player2_name + ": " + player2_points
            print(separation + "\n" + point_of_two_players + "\n" + separation)

    def game_count(self):
        how_to_game_count = HowToCountGame()
        which_point = "1:" + how_to_game_count.player1_name + "がポイントを取った\n" + "2:" + how_to_game_count.player2_name + "がポイントを取った\n1か2で入力して下さい："
        separation = "#######################################################"
        player1_count = 0
        player2_count = 0
        players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}

        def player1_game_count(player1_count, player1_game_count):
            if player1_count % 5 == 0:
                how_to_game_count.player1_points = players_count[5]
                how_to_game_count.player1_game_count += 1
                return how_to_game_count.player1_game_count
            elif player1_count % 4 == 0:
                how_to_game_count.player1_points = players_count[4]
            elif player1_count % 3 == 0:
                how_to_game_count.player1_points = players_count[3]
            elif player1_count % 2 == 0:
                how_to_game_count.player1_points = players_count[2]
            elif player1_count % 1 == 0:
                how_to_game_count.player1_points = players_count[1]
            return how_to_game_count.player1_points

        def player2_game_count(player2_count, player2_game_count):
            if player2_count % 5 == 0:
                how_to_game_count.player2_points = players_count[5]
                how_to_game_count.player2_game_count += 1
                return how_to_game_count.player2_game_count
            elif player2_count % 4 == 0:
                how_to_game_count.player2_points = players_count[4]
            elif player2_count % 3 == 0:
                how_to_game_count.player2_points = players_count[3]
            elif player2_count % 2 == 0:
                how_to_game_count.player2_points = players_count[2]
            elif player2_count % 1 == 0:
                how_to_game_count.player2_points = players_count[1]
            return how_to_game_count.player2_points

        while True:
            # ユーザーにどちらのプレイヤーがポイントを取ったか入力してもらう。
            str_get_point = input(which_point)
            if str_get_point == "1" or str_get_point == "2":
                get_point = int(str_get_point)
                if get_point == 1:
                    player1_count += 1
                elif get_point == 2:
                    player2_count += 1

            # if player1_count % 4 == 0 and player2_count % 4 == 0:
            #     how_to_game_count.fourty_all()

            player1_game_count(player1_count, how_to_game_count.player1_game_count)
            player2_game_count(player1_count, how_to_game_count.player2_game_count)

            player1_count = int(player1_count)
            player2_count = int(player2_count)

            print("outerの", player2_count)

            if player1_count >= 5:
                print(separation + "\n" + how_to_game_count.player1_name + ": " + how_to_game_count.player1_points + "\n"
                      + how_to_game_count.player2_name + ": " + how_to_game_count.player2_points + "\n" + how_to_game_count.win_player1 + "\n" + separation)
                player1_count = 1
            elif player2_count >= 5:
                print(separation + "\n" + how_to_game_count.player1_name + ": " + how_to_game_count.player1_points + "\n"
                      + how_to_game_count.player2_name + ": " + how_to_game_count.player2_points + "\n" + how_to_game_count.win_player2 + "\n" + separation)
                player2_count = 1

            point_of_two_players = how_to_game_count.player1_name + ": " + how_to_game_count.player1_points + "\n" + how_to_game_count.player2_name + ": " + how_to_game_count.player2_points
            print("ポイント情報\n", point_of_two_players)
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