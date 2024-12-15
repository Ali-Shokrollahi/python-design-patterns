"""
Task:
    - Implement a simple system where you can build different types of houses (e.g., a wooden house, a stone house)
     using the builder design pattern.
"""

from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = None
        self.windows = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, {self.doors} doors, {self.windows} windows."


class AbstractHouseBuilder(ABC):

    def __init__(self):
        self._house = House()

    @abstractmethod
    def build_walls(self):
        ...

    @abstractmethod
    def build_roof(self):
        ...

    @abstractmethod
    def build_doors(self):
        ...

    @abstractmethod
    def build_windows(self):
        ...

    def get_house(self):
        return self._house


class WoodenHouseBuilder(AbstractHouseBuilder):
    def build_walls(self):
        self._house.walls = "wooden"

    def build_roof(self):
        self._house.roof = "wooden"

    def build_doors(self):
        self._house.doors = "wooden"

    def build_windows(self):
        self._house.windows = "glass"


class StoneHouseBuilder(AbstractHouseBuilder):
    def build_walls(self):
        self._house.walls = "stone"

    def build_roof(self):
        self._house.roof = "stone"

    def build_doors(self):
        self._house.doors = "metal"

    def build_windows(self):
        self._house.windows = "glass"


class HouseDirector:
    def __init__(self, builder: AbstractHouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_doors()
        self.builder.build_windows()
        return self.builder.get_house()


# Client Code
if __name__ == "__main__":
    # Build a wooden house
    wooden_builder = WoodenHouseBuilder()
    director = HouseDirector(wooden_builder)
    wooden_house = director.construct_house()
    print("Wooden House:", wooden_house)

    # Build a stone house
    stone_builder = StoneHouseBuilder()
    director = HouseDirector(stone_builder)
    stone_house = director.construct_house()
    print("Stone House:", stone_house)
