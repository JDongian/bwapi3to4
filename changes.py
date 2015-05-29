def simple_replace(source):
    source.replace("isWalkable", "isAccessible")
    source.replace(".x()", ".x")
    source.replace(".y()", ".y")
    source.replace("groundWeaponMaxRange", "weaponMaxRange")
    source.replace("airWeaponMaxRange", "weaponMaxRange")
    source.replace("groundWeaponDamageCooldown", "weaponDamageCooldown")
    source.replace("energyUsed", "energyCost")

def warn_issues(filename):
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            # getResources now returns last-known resource amount if unit
            # becomes inaccessible.
            if "getResources" in line:
                print("{}: getResources has changed.".format(num))
            # Parameters changed from build(Unit, TilePosition) to build(

def manual_fix(filename):
    deprecated_functions = ["getScreenBuffer", "setReplayVision",
                            "changeRace", "startGame",
                            "getUpgradeLevel"]
    with open(filename) as fp:
        for num, line in enumerate(fp, 1):
            for func in deprecated_functions:
                if func in line:
                    print("{line}: {func} is deprecated.".format(line=num,
                                                                 func=func))
