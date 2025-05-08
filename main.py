from util.window import CreateWindow
from util import Colors
from engine.gameInfo import GameInfo as ginfo
from engine.logger import Logger as log

GameTitle = ginfo.game_name + " " + ginfo.version + ginfo.version_type + ginfo.platform
CreateWindow.Start(GameTitle, 1280, 720, Colors.WHITE, 60)
