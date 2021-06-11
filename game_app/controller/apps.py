import sys
import os
sys.path.append(os.path.join('..', 'models'))

import tiebreak
from tiebreak import SevenPointsTieBreak
from tiebreak import TenPointsTieBreak

game = SevenPointsTieBreak()
game.seven_points_tie_break()
