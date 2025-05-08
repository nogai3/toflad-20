game_name = "Test"
version = "1.0"
version_type = "release"
platforms  = [
    "windows", "osx", "linux", "arch",
    "windows-n", "osx-n", "linux-n", "arch-n"
]
platform = "windows-n"

match(version_type):
    case "snapshot":
        version_type = "/snapshot"
    case "release":
        version_type = ""
    case "dev":
        version_type = "/dev"
    case "demo":
        version_type = "DEMO"
if (platform not in platforms):
    print('[TOFLAD-20 OUTPUT]: Undefined platform.')
    exit(0)
else:
    if ("-n" in platform):
        platform = ""
    else:
        if ("osx" in platform):
            platform = " | Platform: MacOS X"
        else:
            platform = f" | Platform: {platform.capitalize()}"

