def simple_replace(source):
    source = source.replace("isWalkable", "isAccessible")
    source = source.replace(".x()", ".x")
    source = source.replace(".y()", ".y")
    source = source.replace("groundWeaponMaxRange", "weaponMaxRange")
    source = source.replace("airWeaponMaxRange", "weaponMaxRange")
    source = source.replace("groundWeaponDamageCooldown", "weaponDamageCooldown")
    source = source.replace("energyUsed", "energyCost")
    source = source.replace("setReplayVision", "setVision")
    return source

def warn_issues(filename):
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            # getResources now returns last-known resource amount if unit
            # becomes inaccessible.
            if "getResources" in line:
                print("{}: getResources has changed.".format(num))
            # Parameters changed from build(Unit, TilePosition) to build(

def manual_fix(filename):
    deprecated_functions = ["getScreenBuffer",
                            "changeRace", "startGame",
                            "getUpgradeLevel"]
    with open(filename) as fp:
        for num, line in enumerate(fp, 1):
            for func in deprecated_functions:
                if func in line:
                    print("{line}: {func} is deprecated.".format(line=num, func=func))
