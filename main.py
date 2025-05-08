from util.window import CreateWindow
from util import Colors
from engine.gameInfo import GameInfo
from engine.gameInfo import MatchGameInfo

GameTitle = GameInfo.gameName + " " + GameInfo.version + MatchGameInfo.matchedVersionType # + " | Platform: " + MatchGameInfo.matchedPlatform
CreateWindow.Start(GameTitle, 1280, 720, Colors.WHITE, 60)
