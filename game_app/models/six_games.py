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


player1_name = "Aさん"
player2_name = "Bさん"
which_point = "1:" + player1_name + "がポイントを取った\n" + "2:" + player2_name + "がポイントを取った\n1か2で入力して下さい："
player1_num = 1
player2_num = 1
win_player1 = "Game set and match won by " + player1_name + "."
win_player2 = "Game set and match won by " + player2_name + "."
count_points = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}
player1_game_count = 0
player2_game_count = 0


class HowToCountGame(object):
    def __init__(self, name="ゲームマッチ"):
        self.name = name

    def game_count(self):
        while True:
            global player1_num
            global player2_num
            global which_point
            global count_points
            global player1_game_count
            global player2_game_count

            player1_points = "0"
            player2_points = "0"
            get_point = int(input(which_point))
            if get_point == 1:
                player1_num += 1
            elif get_point == 2:
                player2_num += 1
            elif get_point != 1 or get_point != 2 or get_point is not int:
                print("1か2で入力して下さい")

            # 40-40になった場合
            if player1_num % 4 == 0 and player2_num % 4 == 0:
                print("#######################################################")
                print(player1_name + ": " + "40\n" + player2_name + ": " + "40")
                print("#######################################################")

                while True:
                    get_point = int(input(which_point))
                    if get_point == 1:
                        player1_num += 1
                        player1_points = "Ad"
                        player2_points = count_points[4]
                    elif get_point == 2:
                        player2_num += 1
                        player1_points = count_points[4]
                        player2_points = "Ad"
                    elif get_point != 1 or get_point != 2 or get_point is not int:
                        print("1か2で入力して下さい")

                    dif = abs(player1_num - player2_num)
                    if dif == 2 and player1_num > 5:
                        player1_points = count_points[5]
                        player2_points = count_points[4]
                        player1_num = 1
                        player2_num = 1
                        player1_game_count += 1
                        print("#######################################################")
                        print(player1_name + ": " + count_points[5] + "\n" + player2_name + ": " + count_points[4])
                        print("\ngame " + player1_name)
                        print("#######################################################")
                        break
                    elif dif == 2 and player2_num > 5:
                        player1_points = count_points[4]
                        player2_points = count_points[5]
                        player1_num = 1
                        player2_num = 1
                        player2_game_count += 1
                        print("#######################################################")
                        print(player1_name + ": " + count_points[4] + "\n" + player2_name + ": " + count_points[5])
                        print("\ngame " + player2_name)
                        print("#######################################################")
                        break
                    elif player1_num == player2_num:
                        player1_points = count_points[4]
                        player2_points = count_points[4]
                    elif player1_num > player2_num:
                        player1_points = "Ad"
                        player2_points = count_points[4]
                    elif player2_num > player1_num:
                        player1_points = count_points[4]
                        player2_points = "Ad"

                    point_of_two_players = player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points
                    print("#######################################################")
                    print(point_of_two_players)
                    print("#######################################################")
            # 40-40以降でどちらかがゲームを取ったらブレークする。
            if player1_points == count_points[5] or player2_points == count_points[5]:
                break

            # player1のポイント
            if player1_num % 5 == 0:
                player1_points = count_points[5]
                player1_num = 1
                player2_num = 1
                player1_game_count += 1
                print("#######################################################")
                print(player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points)
                print("\ngame " + player1_name)
                print("#######################################################")
                break
            elif player1_num % 4 == 0:
                player1_points = count_points[4]
            elif player1_num % 3 == 0:
                player1_points = count_points[3]
            elif player1_num % 2 == 0:
                player1_points = count_points[2]
            elif player1_num % 1 == 0:
                player1_points = count_points[1]

            # player2のポイント
            if player2_num % 5 == 0:
                player2_points = count_points[5]
                player1_num = 1
                player2_num = 1
                player2_game_count += 1
                print("#######################################################")
                print(player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points)
                print("\ngame " + player2_name)
                print("#######################################################")
                break
            elif player2_num % 4 == 0:
                player2_points = count_points[4]
            elif player2_num % 3 == 0:
                player2_points = count_points[3]
            elif player2_num % 2 == 0:
                player2_points = count_points[2]
            elif player2_num % 1 == 0:
                player2_points = count_points[1]

            print("#######################################################")
            point_of_two_players = player1_name + ": " + player1_points + "\n" + player2_name + ": " + player2_points
            print(point_of_two_players)
            print("#######################################################")


game = HowToCountGame()
game.game_count()