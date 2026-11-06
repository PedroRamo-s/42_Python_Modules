from abc import ABC, abstractmethod
from ex0 import creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: creature.Creature) -> None:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._state = False

    @abstractmethod
    def transform(self) -> bool:
        pass

    @abstractmethod
    def revert(self) -> bool:
        pass
