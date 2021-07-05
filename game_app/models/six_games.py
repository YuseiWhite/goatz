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
                print("#######################################################")
                print(player1_name + ": " + "40\n" + player2_name + ": " + "40")
                print("#######################################################")

                while True:
                    str_get_point = input(which_point)
                    if str_get_point is not None:
                        get_point = int(str_get_point)
                        if get_point == 1:
                            player1_count += 1
                        elif get_point == 2:
                            player2_count += 1

                    # player1_countとplayer2_countの差が2以上の場合、gameとなる。
                    dif = abs(player1_count - player2_count)
                    if dif == 2 and player1_count > player2_count:
                        player1_points = players_count[5]
                        player2_points = players_count[4]
                        player1_count = 1
                        player2_count = 1
                        player1_game_count += 1
                        print("#######################################################")
                        print(player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points)
                        print(win_player1)
                        print("#######################################################")
                        return player1_game_count
                    elif dif == 2 and player2_count > player1_count:
                        player1_points = players_count[4]
                        player2_points = players_count[5]
                        player1_count = 1
                        player2_count = 1
                        player2_game_count += 1
                        print("#######################################################")
                        print(player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points)
                        print(win_player2)
                        print("#######################################################")
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
                    print("#######################################################")
                    print(point_of_two_players)
                    print("#######################################################")
            # 40-40以降でどちらかがゲームを取ったらブレークする。
            # if player1_points == count_points[5] or player2_points == count_points[5]:
            #     break

            # player1のポイント
            if player1_count % 5 == 0:
                player1_points = players_count[5]
                player1_count = 1
                player2_count = 1
                player1_game_count += 1
                print("#######################################################")
                print(player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points)
                print(win_player1)
                print("#######################################################")
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
                print("#######################################################")
                print(player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points)
                print(win_player2)
                print("#######################################################")
                return player2_game_count
            elif player2_count % 4 == 0:
                player2_points = players_count[4]
            elif player2_count % 3 == 0:
                player2_points = players_count[3]
            elif player2_count % 2 == 0:
                player2_points = players_count[2]
            elif player2_count % 1 == 0:
                player2_points = players_count[1]

            print("#######################################################")
            point_of_two_players = player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points
            print(point_of_two_players)
            print("#######################################################")


class SixGame(HowToCountGame):
    def __init__(self, name="6ゲームマッチ"):
        super().__init__(name)
        self.name = name

    def six_games(self):
        about = AboutPlayers()
        how_to_count_game = HowToCountGame()
        tiebreak = SevenPointsTieBreak()
        player1_win_tiebreak = None
        player2_win_tiebreak = None
        while True:
            game_of_two_players = player1_name + ": " + str(player1_game_count) + "\n" + player2_name + ": " + str(player2_game_count)

            # 5-5になったら
            if (player1_game_count != 0 and player1_game_count % 5 == 0) and (player2_game_count != 0 and player2_game_count % 5 == 0):
                while True:
                    if player1_game_count == 6 and player2_game_count == 6:
                        return player1_game_count, player2_game_count
                    elif player1_game_count == 7 or player2_game_count == 7:
                        print("#######################################################")
                        print(player1_name + ": " + str(player1_game_count) + "\n" + player2_name + ": " + str(player2_game_count))
                        print("#######################################################")
                        break
                    print("#######################################################")
                    print(player1_name + ": " + str(player1_game_count) + "\n" + player2_name + ": " + str(player2_game_count))
                    print("#######################################################")
                    how_to_count_game.game_count()

            # プレイヤー1とプレイヤー2の処理
            elif player1_game_count != 0 and player1_game_count % 6 == 0:
                print("#######################################################")
                print(game_of_two_players)
                print("#######################################################")
                break
            elif player2_game_count != 0 and player2_game_count % 6 == 0:
                print("#######################################################")
                print(game_of_two_players)
                print("#######################################################")
                break

            print("#######################################################")
            print(game_of_two_players)
            print("#######################################################")
            how_to_count_game.game_count()

        # タイブレーク
        if player1_game_count % 6 == 0 and player2_game_count % 6 == 0:
            print("#######################################################")
            print("6 game all, Tie-Break")
            print("#######################################################")
            while True:
                tiebreak.seven_points_tie_break()
                if player1_win_tiebreak == "win":
                    print("#######################################################")
                    print(player1_name + ": 7" + "\n" + player2_name + ": 6(" + str(about.player2) + ")")
                    print("#######################################################")
                    break
                elif player2_win_tiebreak == "win":
                    print("#######################################################")
                    print(player2_name + ": 7" + "\n" + player1_name + ": 6(" + str(about.player1) + ")")
                    print("#######################################################")
                    break


g = SixGame()
g.six_games()
