# bwapi3to4
Migration scripts for converting BWAPI 3 source to BWAPI 4 source


TODO:

* "Unit *" -> "Unit "
* "UnitTypes::getType" -> "UnitType::getType"

* Position, TilePosition, and the new WalkPosition now all share the same class template: Point.
* <s>x, y members now public; x(), y() functions removed</s>

* Convert derived sets: Unitset, Playerset, Regionset, Bulletset, Forceset, e.g. "std::set<Unit*>" -> "BWAPI::Unitset"
* Interface overhead has been reduced by making some member functions with alternative parameters non-virtual
* Some function parameters re-arranged so that default parameters can be used
* getClientInfo, setClientInfo now available to all Interface classes

* Type::set (Example: UnitType::set)
* Type enumerations now available for switch case usage, accessed by Types::Enum (Example: UnitTypes::Enum::Terran_Marine)
* <s>TechType::energyUsed renamed to energyCost</s>.
* UnitTypes::getUnit, Races::getRace, etc. replaced with static Type::getType. (Example: Races::getRace doesn't exist, use Race::getType)

* canBuildHere, canMake, canResearch, and canUpgrade parameters rearranged
* getUnits_ functions now return a Unitset copy instead of a reference, and also now takes a function predicate.
* Removed getScreenBuffer, setReplayVision(use setVision for replays too), changeRace, and startGame 
* Using Special_Start_Location in canBuildHere will ignore units that are occupying the space while still checking for resource distance.
* Some functions now take an Enum type instead of an int.

* <s>groundWeaponMaxRange and airWeaponMaxRange replaced with weaponMaxRange</s>
* getTextColor now returns a char instead of an int
* Unit count functions now take a default parameter of AllUnits.
* <s>groundWeaponDamageCooldown renamed to weaponDamageCooldown</s>

* build parameters rearranged
* <s>getUpgradeLevel removed</s>
* Unit commands more strict
* <s>getResources changed</s>

* <s>isWalkable renamed to isAccessible</s>
