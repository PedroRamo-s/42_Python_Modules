#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):
    def __init__(self, valid: bool) -> None:
        self._valid = True
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(f"{creature.attack()}")

    def is_valid(self, creature: Creature) -> bool:
        return True


class AgressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if not (isinstance(creature, TransformCapability)):
            return False
        else:
            return True

    def act(self, creature: Creature) -> None:
        if self._valid is False:
            raise exception
        else:
            creature.transform()
            creature.attack()
            creature.revert()


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if not isinstance(creature, HealCapability):
            return False
        else:
            return True

    def act(self, creature: Creature) -> None:
        if self._valid is False:
            raise except
        else:
            creature.attack()
            creature.heal()