# bwapi3to4
Migration scripts for converting BWAPI 3 source to BWAPI 4 source

###TODO###

**Changes in BWAPI 4.1.1 Beta**

- nothing


**Changes in BWAPI 4.1.0 Beta**

- The video commands have been removed


**Changes in BWAPI 4.0.1 Beta (r4453)**

- All interface pointers are now hidden. Instead of Unit* you will now just use Unit. This will require a "Replace in Files" operation to convert existing sources
- Game::setTextSize now takes a BWAPI::Text::Size::Enum parameter instead of an integer
- All instances of IsUnpowered were renamed to IsPowered


**Changes in BWAPI 4.0.0 Beta (r4350)**

- ~~x, y members now public; x(), y() functions removed~~


- Each interface class will have its own derived set with several enhancements, and brings in some functionality similar to that of BWSAL. The new sets are as follows: Unitset, Playerset, Regionset, Bulletset, Forceset
- Interface overhead has been reduced by making some member functions with alternative parameters non-virtual. Keep in mind some function parameters have been re-arranged so that default parameters can be used
- getClientInfo/setClientInfo are now available to all Interface classes, and also take an optional parameter that acts as a key


- Types have also received their own set, the Type::set (Example: UnitType::set)
- All types' enumerations are now available (for switch case usage) and are accessed by Types::Enum (Example: UnitTypes::Enum::Terran_Marine)
- ~~TechType::energyUsed renamed to energyCost~~
- UnitTypes::getUnit, Races::getRace, etc. have now been replaced with static Type::getType. (Example: Races::getRace doesn't exist, use Race::getType)


- The parameters for canBuildHere, canMake, canResearch, and canUpgrade have been rearranged
- getUnits_ functions now return a Unitset copy instead of a reference, and also now takes a function predicate
- Removed getScreenBuffer, setReplayVision(use setVision for replays too), changeRace, and startGame
- Instead of using Game::printf, you may use BWAPI::Broodwar like you would std::cout, using operator <<
- Using Special_Start_Location in canBuildHere will ignore units that are occupying the space while still checking for resource distance
- Some functions now take an Enum type instead of an int


- ~~groundWeaponMaxRange and airWeaponMaxRange have been removed. Use weaponMaxRange instead~~
- getTextColor now returns a char instead of an int so that it is printed correctly when used with ostream::operator <<
- Unit count functions now take a default parameter of AllUnits
- ~~Rename groundWeaponDamageCooldown to weaponDamageCooldown~~


- The parameters for build have been rearranged
- getUnits_ functions now return a Unitset copy instead of a reference, and also now takes a function predicate
- ~~Removed getUpgradeLevel~~
- Unit commands are now more strict
- getResources now returns the last-known resource amount when the unit becomes inaccessible


- ~~Renamed isWalkable to isAccessible~~


**List of all changes**
- [http://bwapi.github.io/changes_top.html](http://bwapi.github.io/changes_top.html)


<!--
* Position, TilePosition, and the new WalkPosition now all share the same class template: Point.

* Convert derived sets: Unitset, Playerset, Regionset, Bulletset, Forceset, e.g. "std::set<Unit*>" -> "BWAPI::Unitset"
* Interface overhead has been reduced by making some member functions with alternative parameters non-virtual
* Some function parameters re-arranged so that default parameters can be used
* getClientInfo, setClientInfo now available to all Interface classes

* Type::set (Example: UnitType::set)
* Type enumerations now available for switch case usage, accessed by Types::Enum (Example: UnitTypes::Enum::Terran_Marine)
* UnitTypes::getUnit, Races::getRace, etc. replaced with static Type::getType. (Example: Races::getRace doesn't exist, use Race::getType)

* canBuildHere, canMake, canResearch, and canUpgrade parameters rearranged
* getUnits_ functions now return a Unitset copy instead of a reference, and also now takes a function predicate.
* Removed getScreenBuffer, setReplayVision(use setVision for replays too), changeRace, and startGame 
* Using Special_Start_Location in canBuildHere will ignore units that are occupying the space while still checking for resource distance.
* Some functions now take an Enum type instead of an int.

* getTextColor now returns a char instead of an int
* Unit count functions now take a default parameter of AllUnits.

* build parameters rearranged
* Unit commands more strict
-->
