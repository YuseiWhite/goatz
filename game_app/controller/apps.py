import sys
import os
sys.path.append(os.path.join('..', 'models'))

import tiebreak
from tiebreak import SevenPointsTieBreak
from tiebreak import TenPointsTieBreak
import six_games
from six_games import HowToCountGame

game = SevenPointsTieBreak()
game.seven_points_tie_break()

# game = TenPointsTieBreak()
# game.ten_points_tie_break()

# game = HowToCountGame()
# game.game_count()
