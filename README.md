# bwapi3to4
Migration scripts for converting BWAPI 3 source to BWAPI 4 source

##Usage##

Python3 is recommended. Python2 support and a Windows executable are planned, but functionality has priority over portability.

Usage: `python3 <PATH_IN> <PATH_OUT>`

Example:

```
$ python3 ../ualbertabot/ ../ualbertabot2/
```

###TODO###

**Changes in BWAPI 4.1.2**

- nothing


**Changes in BWAPI 4.1.1 Beta**

- nothing


**Changes in BWAPI 4.1.0 Beta**

- nothing


**Changes in BWAPI 4.0.1 Beta (r4453)**

- All interface pointers are now hidden. Instead of Unit* you will now just use Unit. This will require a "Replace in Files" operation to convert existing sources
- Game::setTextSize now takes a BWAPI::Text::Size::Enum parameter instead of an integer
- All instances of IsUnpowered were renamed to IsPowered


**Changes in BWAPI 4.0.0 Beta (r4350)**

- ~~x, y members now public; x(), y() functions removed~~


- Each interface class will have its own derived set with several enhancements, and brings in some functionality similar to that of BWSAL. The new sets are as follows: Unitset, Playerset, Regionset, Bulletset, Forceset
- Interface overhead has been reduced by making some member functions with alternative parameters non-virtual. Keep in mind some function parameters have been re-arranged so that default parameters can be used


- Types have also received their own set, the Type::set (Example: UnitType::set)
- ~~TechType::energyUsed renamed to energyCost~~
- UnitTypes::getUnit, Races::getRace, etc. have now been replaced with static Type::getType. (Example: Races::getRace doesn't exist, use Race::getType)


- The parameters for canBuildHere, canMake, canResearch, and canUpgrade have been rearranged
- getUnits_ functions now return a Unitset copy instead of a reference, and also now takes a function predicate
- Removed getScreenBuffer, setReplayVision(use setVision for replays too), changeRace, and startGame
- Some functions now take an Enum type instead of an int


- ~~groundWeaponMaxRange and airWeaponMaxRange have been removed. Use weaponMaxRange instead~~
- ~~Rename groundWeaponDamageCooldown to weaponDamageCooldown~~


- The parameters for build have been rearranged
- getUnits_ functions now return a Unitset copy instead of a reference, and also now takes a function predicate
- ~~Removed getUpgradeLevel~~


- ~~Renamed isWalkable to isAccessible~~


**List of all changes**
- [https://github.com/bwapi/bwapi/wiki/Changes](https://github.com/bwapi/bwapi/wiki/Changes)


<!--
* Position, TilePosition, and the new WalkPosition now all share the same class template: Point.

* Convert derived sets: Unitset, Playerset, Regionset, Bulletset, Forceset, e.g. "std::set<Unit*>" -> "BWAPI::Unitset"
* Interface overhead has been reduced by making some member functions with alternative parameters non-virtual
* Some function parameters re-arranged so that default parameters can be used

* Type::set (Example: UnitType::set)
* UnitTypes::getUnit, Races::getRace, etc. replaced with static Type::getType. (Example: Races::getRace doesn't exist, use Race::getType)

* canBuildHere, canMake, canResearch, and canUpgrade parameters rearranged
* getUnits_ functions now return a Unitset copy instead of a reference, and also now takes a function predicate.
* Removed getScreenBuffer, setReplayVision(use setVision for replays too), changeRace, and startGame 
* Some functions now take an Enum type instead of an int.

* build parameters rearranged
-->
