class AboutPlayers(object):
    # 全てのマッチで使用
    player1_name = "Aさん"
    player2_name = "Bさん"
    which_point = "1:" + player1_name + "がポイントを取った\n" + "2:" + player2_name + "がポイントを取った\n1か2で入力して下さい："
    player1 = 0
    player2 = 0
    win_player1 = "Game set and match won by " + player1_name + "."
    win_player2 = "Game set and match won by " + player2_name + "."
    # ゲームマッチで使用
    player1_count = 1
    player2_count = 1
    players_count = {1: "0", 2: "15", 3: "30", 4: "40", 5: "game"}
    player1_game_count = 0
    player2_game_count = 0
