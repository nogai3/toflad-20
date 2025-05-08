from util.gameInfo import GameInfo

matchedVersionType = ""
matchedPlatform = ""

match(GameInfo.versionType):
    case "snapshot":
        GameInfo.versionType = "/snapshot"
        matchedVersionType = GameInfo.versionType
    case "release":
        GameInfo.versionType = ""
        matchedVersionType = GameInfo.versionType
    case "dev":
        GameInfo.versionType = "/dev"
        matchedVersionType = GameInfo.versionType
    case "demo":
        GameInfo.versionType = "DEMO"
        matchedVersionType = GameInfo.versionType
if ("-n" in GameInfo.platform):
    GameInfo.platform = ""
    matchedPlatform = GameInfo.platform
else:
    match (GameInfo.platform):
        case "windows":
            GameInfo.platform = "Windows"
            matchedPlatform = GameInfo.platform
        case "osx":
            GameInfo.platform = "MacOS X"
            matchedPlatform = GameInfo.platform
        case "linux":
            GameInfo.platform = "Linux"
            matchedPlatform = GameInfo.platform
        case "arch":
            GameInfo.platform = "Arch"
            matchedPlatform = GameInfo.platform
