"""
【1セットマッチ】

6ゲーム取ったら勝利。
1ゲームは 0 → 15 → 30 → 40 → 1ゲーム という順。

if文で
数字 % 5 == 0
数字 % 4 == 0
数字 % 3 == 0
数字 % 2 == 0
数字 % 1 == 0

gameは全て5の倍数になる
つまり、プレイヤーのカウントが6ゲームまでで5, 10, 15, 20, 25, 30...となる。
1ゲーム　＝　5
→　数字 % 5 == 0
2ゲーム　＝　10
→　数字 % 5 == 5, 数字 % 10 == 0
3ゲーム　＝　15
...
6ゲーム　＝　30


5-5なら2点差着くまで
このゲームを6つ先に取ったら勝利。

ただし、以下の場合は異なる。
・40-40となった場合
　先に2ポイント連続で取ったものが1ゲーム。40の次はAd

・5-5となった場合
　6-5で勝利ではなく、7-5となるまでやらなくてはならない。

・6-6となった場合
　タイブレーク実行で買ったものが勝利者。
　例えば、7-3のポイントで買った場合は 7-6(3) と表記する

"""
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
            get_point = int(input(which_point))
            if get_point == 1:
                player1_count += 1
            elif get_point == 2:
                player2_count += 1
            # elif get_point != 1 or get_point != 2 or get_point is not int:
            #     print("1か2で入力して下さい")

            # 40-40になった場合
            if player1_count % 4 == 0 and player2_count % 4 == 0:
                print("#######################################################")
                print(player1_name + ": " + "40\n" + player2_name + ": " + "40")
                print("#######################################################")

                while True:
                    get_point = int(input(which_point))
                    if get_point == 1:
                        player1_count += 1
                    elif get_point == 2:
                        player2_count += 1
                    # elif get_point != 1 or get_point != 2 or get_point is not int:
                    #     print("1か2で入力して下さい")

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
        how_to_count_game = HowToCountGame()
        while True:
            # player1_game_count = 5
            # player2_game_count = 5
            game_of_two_players = player1_name + ": " + str(player1_game_count) \
                                  + "\n" + player2_name + ": " + str(player2_game_count)
            # タイブレークの処理
            # if player1_game_count % 5 == 0 and player2_game_count % 5 == 0:
            #     while True:
            #         if player1_game_count % 6 == 0 and player2_game_count % 6 == 0:
            #             while True:
            #                 about = AboutPlayers()
            #                 if about.player1 > about.player2:
            #                     print("#######################################################")
            #                     print(player1_name + ": 7" + "\n" + player2_name + ": 6(" + str(about.player2) + ")")
            #                     print("#######################################################")
            #                     break
            #                 elif about.player2 > about.player1:
            #                     print("#######################################################")
            #                     print(player2_name + ": 7" + "\n" + player1_name + ": 6(" + str(about.player1) + ")")
            #                     print("#######################################################")
            #                     break
            #                 tiebreak = SevenPointsTieBreak()
            #                 tiebreak.seven_points_tie_break()
            #         elif player1_game_count == 7 or player2_game_count == 7:
            #             print("#######################################################")
            #             print(game_of_two_players)
            #             print("#######################################################")
            #             break
            #     how_to_count_game.game_count()

            # プレイヤー1とプレイヤー2の処理
            if player1_game_count != 0 and player1_game_count % 6 == 0:
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


# g = HowToCountGame()
# g.game_count()

g = SixGame()
g.six_games()