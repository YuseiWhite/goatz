import os
import sys
sys.path.append(os.path.join('..', 'models'))

from eight_games import EightGames
from tiebreak import SevenPointsTieBreak, TenPointsTieBreak
from six_games import SixGames

"""
どういうシステムを作るか
好きな試合形式で始めることができる
"""

# game = SixGames()
# game.six_games_match()

# game = SevenPointsTieBreak()
# game.seven_points_tie_break()

# game = TenPointsTieBreak()
# game.ten_points_tie_break()

